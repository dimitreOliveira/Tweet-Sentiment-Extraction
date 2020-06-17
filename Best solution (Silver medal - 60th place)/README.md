## Quick summary
- Model: 5-Fold `RoBERTa base`. [training notebook here](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/blob/master/Model%20backlog/Train/260-Tweet-Train-5Fold-roBERTa%20mask%20and%20span%20OneCycle2.ipynb)
- Tasks: Predicted start/end indexes and mask span `(details below)`
- Dataset: Removed about 30 noisy samples, and samples with Jaccard score between `text` and `selected_text` == 0, found that they were very noisy. [dataset creation here](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/blob/master/Datasets/tweet-dataset-5fold-roberta-64-clean.ipynb)
- Post-process: Removed words that were not present in `text` field. `(details below)` [inference notebook here](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/blob/master/Model%20backlog/Inference/260-tweet-inference-5fold-roberta-mask-and-span-on.ipynb)
- Framework: `Tensorflow` only GPUs

#### This is a metrics table that I used to compare my models (this one is from the 0.720 model).
![](https://github.com/dimitreOliveira/Tweet-Sentiment-Extraction/blob/master/Assets/260_metrics.png)

## Detailed summary
### Model &amp; training
- 5-Fold `RoBERTa base`
- Public leaderboard: `0.715`
- Private leaderboard: `0.720`
- Sequence length: `64`
- Batch size: `32`
- Epochs: `2`
- Learning rate: `1e-4`
- Training schedule: One cycle (from 0 to 1e-4 then to 1e-6)
- Target: Start/end indexes and masked span (token level)
- Used the pooled `11th layer`
- Dense layer without `bias`

I got pretty good results using one cycle schedule for training, the first time I tried one cycle got me 0.718 on the public leaderboard. My model had 3 outputs, 1 for each span index (start and end) and an extra output for the masked span, this means if we had a sequence of size 6, the start span is index 2 and end span is index 4, the masked span would be `0 0 1 1 1 0`, makes sense? I thought this would give the model a more general feeling about the target.

### Dataset
- Nothing fancy here dropped `null` samples, removed about 30 samples that I thought were very noisy, and after some study, I found that samples with very low Jaccard score between `text` and `selected_text` were noisier, so I removed them.
- I would like to say here that at the beginning I made a lot of mistakes with the tokenizers, so for every dataset that I created I have added some tests, check it out!
- 5-Fold split using `sklearn StratifiedKFold` and `sentiment` as the target, like many others.
- To save time for each dataset I was creating a bunch of outputs.
- I have used `ByteLevelBPETokenizer` as the tokenizer for RoBERTa
- Lowercased text

### Inference
- Summed all 5 model's logits and then used `argmax` to get start/end indexes.
- The post-process was very trivial, I just removed words that were not present in the `text` field, this helped to remove word-pieces that the tokenizer created and got predicted.
- Empty predictions got filled the whole `text` field.

**This is how my model looked like:**
```
input_ids = layers.Input(shape=(MAX_LEN,), dtype=tf.int32, name='input_ids')
attention_mask = layers.Input(shape=(MAX_LEN,), dtype=tf.int32, name='attention_mask')
    
base_model = TFRobertaModel.from_pretrained(config['base_model_path'], config=module_config, name='base_model')
_, _, hidden_states = base_model({'input_ids': input_ids, 'attention_mask': attention_mask})
    
h11 = hidden_states[-2]
    
logits = layers.Dense(3, use_bias=False, name='qa_outputs')(h11)
    
start_logits, end_logits, mask_logits = tf.split(logits, 3, axis=-1)
start_logits = tf.squeeze(start_logits, axis=-1, name='y_start')
end_logits = tf.squeeze(end_logits, axis=-1, name='y_end')
mask_logits = tf.squeeze(mask_logits, axis=-1, name='y_mask')
    
model = Model(inputs=[input_ids, attention_mask], outputs=[start_logits, end_logits, mask_logits])
```
