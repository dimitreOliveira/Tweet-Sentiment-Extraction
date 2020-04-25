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

- ### GitHub:
  - [Huggingface transformers](https://github.com/huggingface/transformers)
  - [Hggingface tokenizers](https://github.com/huggingface/tokenizers/tree/master/bindings/python)

- ### Papers:
  - [Frustratingly Easy Natural Question Answering](https://arxiv.org/pdf/1909.05286.pdf)

- ### Videos:
  - [BERT for Kaggle Competitions | Yuanhae Wu | Kaggle Days](https://www.youtube.com/watch?v=jS79Y8I0DF4&t=9s)
  - [Deep Learning Formulas for NLP Applications | Chenglong Chen | Kaggle](https://www.youtube.com/watch?v=SmsAI0kLJFc&t=0s)
  - [Solving NLP Problems with BERT | Yuanhao Wu | Kaggle](https://www.youtube.com/watch?v=rQQAIJIf60s)

- ### Kernels:
  - [kernel 1]()

- ### Discussions:
  - [Ideas Which Should Improve Scores Hopefully](https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/142011)
  - [TensorFlow roBERTa Explained](https://www.kaggle.com/c/tweet-sentiment-extraction/discussion/143281)
 
- ### Insights:
  - #### Positive Insights
    - The metric is calculated on lowercased text, so lowercasing all texts as preprocess is viable without drawbacks
  
  - #### Negative Insights
    - Some of the labels contain only a fraction of the original text words like the bellow, thisway predict on character level may be better
      - `text`: `i'm actually starting to quite like lily allen and her music, to be honest.`
      - `selected_text`: `o quite like lily allen and her music, to be honest.`
    - Both `text` and `selected_text` can contain HTML tags
    - Train set have null label
