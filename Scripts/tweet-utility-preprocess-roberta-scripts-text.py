import numpy as np


sentiment_map = {'negative': 0, 
                 'neutral': 1,
                 'positive': 2}

sentiment_ohe_map = {'negative': [1, 0, 0], 
                     'neutral':  [0, 1, 0],
                     'positive': [0, 0, 1]}

# Auxiliar functions
def get_start_end(text, selected_text, offsets, max_seq_len):
    # find the intersection between text and selected text
    idx_start, idx_end = None, None
    for index in (i for i, c in enumerate(text) if c == selected_text[0]):
        if text[index:index + len(selected_text)] == selected_text:
            idx_start = index
            idx_end = index + len(selected_text)
            break
    
    intersection = [0] * len(text)
    if idx_start != None and idx_end != None:
        for char_idx in range(idx_start, idx_end):
            intersection[char_idx] = 1
            
            
    targets = np.zeros(len(offsets))
    for i, (o1, o2) in enumerate(offsets):
        if sum(intersection[o1:o2]) > 0:
            targets[i] = 1
            
    # OHE targets
    target_start = np.zeros(len(offsets))
    target_end = np.zeros(len(offsets))
    targets_nonzero = np.nonzero(targets)[0]
    if len(targets_nonzero) > 0: 
        target_start[targets_nonzero[0]] = 1
        target_end[targets_nonzero[-1]] = 1
    
    return target_start, target_end, targets

def decode(pred_start, pred_end, text, tokenizer):
    enc_text = tokenizer.encode(' ' + text).ids
    enc_text = enc_text[pred_start:pred_end+1]
    decoded_text = tokenizer.decode(enc_text)[1:]
    
    return decoded_text


# Train
def preprocess_roberta(text, selected_text, tokenizer, max_seq_len):
    encoded = tokenizer.encode(text)
    
    # Truncate
    input_ids = encoded.ids[:max_seq_len]
    offsets = encoded.offsets[:max_seq_len]
    attention_mask = encoded.attention_mask[:max_seq_len]
    
    # Pad
    input_ids = input_ids + [1] * (max_seq_len - len(input_ids))
    offsets = offsets + [(0, 0)] * (max_seq_len - len(offsets))
    attention_mask = attention_mask + [0] * (max_seq_len - len(attention_mask))
    
    target_start, target_end, targets = get_start_end(text, selected_text, offsets, max_seq_len)
    
    x = [np.asarray(input_ids, dtype=np.int32), 
         np.asarray(attention_mask, dtype=np.int32)]
    
    y = [np.asarray(target_start, dtype=np.int32), 
         np.asarray(target_end, dtype=np.int32), 
         np.asarray(targets, dtype=np.int32)]
    
    return (x, y)

def get_data(df, tokenizer, MAX_LEN, preprocess_fn=preprocess_roberta):
    x_input_ids = []
    x_attention_masks = []
    x_sentiment = []
    x_sentiment_ohe = []
    
    y_start = []
    y_end = []
    y_mask = []
    y_jaccard = []
    y_wordCnt = []
    y_tokenCnt = []
    
    for row in df.itertuples(): 
        x, y = preprocess_fn(' ' + getattr(row, "text"), getattr(row, "selected_text"), tokenizer, MAX_LEN)
        x_input_ids.append(x[0])
        x_attention_masks.append(x[1])
        x_sentiment.append(sentiment_map[getattr(row, "sentiment")])
        x_sentiment_ohe.append(sentiment_ohe_map[getattr(row, "sentiment")])

        y_start.append(y[0])
        y_end.append(y[1])
        y_mask.append(y[2])
        y_jaccard.append(getattr(row, "jaccard"))
        y_wordCnt.append(getattr(row, "selected_text_wordCnt"))
        y_tokenCnt.append(getattr(row, "selected_text_tokenCnt"))

    x_data = [np.array(x_input_ids, dtype=np.int32), 
               np.array(x_attention_masks, dtype=np.int32)]
    
    x_data_aux = np.array(x_sentiment, dtype=np.int32), 
    
    x_data_aux_2 = np.array(x_sentiment_ohe, dtype=np.int32)
    
    y_data = [np.array(y_start, dtype=np.int32), 
               np.array(y_end, dtype=np.int32)]
    
    y_data_mask = np.array(y_mask, dtype=np.int32)
    
    y_data_aux = [np.array(y_jaccard, dtype=np.float32),
                  np.array(y_wordCnt, dtype=np.int32),
                  np.array(y_tokenCnt, dtype=np.int32)]
    
    return x_data, x_data_aux, x_data_aux_2, y_data, y_data_mask, y_data_aux


# Test
def preprocess_roberta_test(text, tokenizer, max_seq_len):
    encoded = tokenizer.encode(text)
    
    # Truncate
    input_ids = encoded.ids[:max_seq_len]
    attention_mask = encoded.attention_mask[:max_seq_len]
    
    # Pad
    input_ids = input_ids + [1] * (max_seq_len - len(input_ids))
    attention_mask = attention_mask + [0] * (max_seq_len - len(attention_mask))
    
    x = [np.asarray(input_ids, dtype=np.int32), 
         np.asarray(attention_mask, dtype=np.int32)]
    
    return x

def get_data_test(df, tokenizer, MAX_LEN, preprocess_fn=preprocess_roberta_test):
    x_input_ids = []
    x_attention_masks = []
    x_sentiment = []
    x_sentiment_ohe = []
    
    for row in df.itertuples(): 
        x = preprocess_fn(' ' + getattr(row, "text"), tokenizer, MAX_LEN)
        x_input_ids.append(x[0])
        x_attention_masks.append(x[1])
        x_sentiment.append(sentiment_map[getattr(row, "sentiment")])
        x_sentiment_ohe.append(sentiment_ohe_map[getattr(row, "sentiment")])

    x_data = [np.asarray(x_input_ids, dtype=np.int32), 
              np.asarray(x_attention_masks, dtype=np.int32)]
    
    x_data_aux = np.array(x_sentiment, dtype=np.int32)
    
    x_data_aux2 = np.asarray(x_sentiment_ohe, dtype=np.int32)
    
    return x_data, x_data_aux, x_data_aux2