# Tweet Sentiment Extraction - Planning
 
## Working cycle:
1. Read competition information and relevant content to feel comfortable with the problem. Create a hypothesis based on the problem.
2. Initial data exploration to feel comfortable with the problem and the data.
3. Build the first implementation (baseline).
4. Loop through [Analyze -> Approach(model) -> Implement -> Evaluate].

## 1. Literature review (read some kernels and relevant content related to the competition).
- ### Relevant content:
  - [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
  - [The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning)](https://jalammar.github.io/illustrated-bert/)
  - [Ensemble BERT with Data Augmentation and Linguistic Knowledge on SQuAD 2.0](https://web.stanford.edu/class/cs224n/posters/15845024.pdf)
  - [Question Answering with a Fine-Tuned BERT](http://mccormickml.com/2020/03/10/question-answering-with-a-fine-tuned-BERT/)
  - [BERT for Question Answering on SQuAD 2.0](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/reports/default/15848021.pdf)
  - [A Bert based summarization model “BertSum”](https://medium.com/lsc-psd/a-bert-based-summarization-model-bertsum-88b1fc1b3177)
  - [Self Supervised Representation Learning in NLP](https://amitness.com/2020/05/self-supervised-learning-nlp/)
  - [A Visual Survey of Data Augmentation in NLP](https://amitness.com/2020/05/data-augmentation-for-nlp/)
  - [BERT Word Embeddings Tutorial](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/)

- ### GitHub:
  - [Huggingface transformers](https://github.com/huggingface/transformers)
  - [Hggingface tokenizers](https://github.com/huggingface/tokenizers/tree/master/bindings/python)
  - [Kashgari - production-level NLP framework](https://github.com/BrikerMan/Kashgari)
  - [bert-as-service - Interesting FAQ about serbing BERT](https://github.com/hanxiao/bert-as-service#q-why-not-the-last-hidden-layer-why-second-to-last)
  - [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://github.com/jasonwei20/eda_nlp)

- ### Papers:
  - [Frustratingly Easy Natural Question Answering](https://arxiv.org/pdf/1909.05286.pdf)
  - [EDA: Easy Data Augmentation Techniques for Boosting Performance on
Text Classification Tasks](https://arxiv.org/pdf/1901.11196v2.pdf)
  - [BERT for Question Answering on SQuAD 2.0](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/reports/default/15848021.pdf)
  - [Ensemble BERT with Data Augmentation and Linguistic Knowledge on SQuAD 2.0](https://web.stanford.edu/class/cs224n/posters/15845024.pdf)

- ### Videos:
  - [BERT for Kaggle Competitions | Yuanhae Wu | Kaggle Days](https://www.youtube.com/watch?v=jS79Y8I0DF4&t=9s)
  - [Deep Learning Formulas for NLP Applications | Chenglong Chen | Kaggle](https://www.youtube.com/watch?v=SmsAI0kLJFc&t=0s)
  - [Solving NLP Problems with BERT | Yuanhao Wu | Kaggle](https://www.youtube.com/watch?v=rQQAIJIf60s)

- ### Kernels:
  - [TensorFlow roBERTa - [0.705]](https://www.kaggle.com/cdeotte/tensorflow-roberta-0-705)
  - [Bert-base with TF2.1 mixed-precision](https://www.kaggle.com/akensert/tweet-bert-base-with-tf2-1-mixed-precision)

- ### Discussions:
  - [Ideas Which Should Improve Scores Hopefully](https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/142011)
  - [TensorFlow roBERTa Explained](https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/143281)
  - [Original dataset](https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/145363)
  - [Finetuning RoBERTa from the original Paper](https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/151684)
  - [Ideas from BERT paper](https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/151522)
 
- ### Insights:
  - #### Positive Insights
    - The metric is calculated on lowercased text, so lowercasing all texts as preprocess is viable without drawbacks
  
  - #### Negative Insights
    - Some of the labels contain only a fraction of the original text words like the bellow, thisway predict on character level may be better
      - `text`: `i'm actually starting to quite like lily allen and her music, to be honest.`
      - `selected_text`: `o quite like lily allen and her music, to be honest.`
    - Both `text` and `selected_text` can contain HTML tags
    - Train set have null label

- ### Experiments overview:
  - #### Positive experiments
    - Output head `Conv(1,1) -> Flatten -> Activation`
    - Output head `Dense(1) -> Flatten -> Activation`
    - Epoch LR scheduler (cosine and exponential)
    - Label smoothing CCE (0.1 and 0.2)
    - Removing sample with noise and with low jaccard between text and label
    - Use Keras QA [reference model](https://huggingface.co/transformers/model_doc/bert.html#tfbertforquestionanswering)
    - Use huggingface QA [reference model](https://keras.io/examples/nlp/text_extraction_with_bert/)
    - Fine-tuune model with only positive%negative samples (exp. 208)
    - Sample weight, 10 times more weight to positive%negative samples (exp. 215)
    - Predict mask and QA span (exp. 219)
    - Train longer using cosine with warm restart schedule (exp. 221)
    - Use custom loss to punish wrong predictions (exp. 93)
    - Use SWA wrapper on adam optimizer (exp. 238)
  
  - #### Neutral experiments
    - Output layers with BCE loss (exp. 54)
    - Predict Jaccard score between `text` and `selected_text` (exp. 57)
    - RAdam optimizer (exp. 59)
    - AdamW (needs fine-tunning) (exp. 61)
    - Average last 4 layers (exp. 66, 99)
    - Subtract flatten layer (before activation) of the other output flatten layer (exp. 68)
    - Predict the sentiment (exp. 83)
    - Average flatten layer (before activation) with the other output flatten layer (exp. 90)
    - Use the 11th layer (exp. 107)
    
    
  - #### Negative experiments
