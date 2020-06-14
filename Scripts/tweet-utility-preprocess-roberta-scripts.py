import numpy as np


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
    
    return target_start, target_end

def decode(pred_start, pred_end, text, question_size, tokenizer):
    enc_text = tokenizer.encode(' ' + text).ids
    enc_text = enc_text[pred_start-question_size:pred_end-(question_size-1)]
    decoded_text = tokenizer.decode(enc_text)[1:]
    
    return decoded_text


# Train
def preprocess_roberta(text, selected_text, question, tokenizer, max_seq_len):
    question_encoded = tokenizer.encode(question)
    question_encoded = question_encoded.ids
    question_size = len(question_encoded) + 3
    
    encoded = tokenizer.encode(text)
    input_ids = encoded.ids
    offsets = encoded.offsets
    attention_mask = encoded.attention_mask
    
    # Add question
    input_ids = [0] + question_encoded + [2] + [2] + input_ids + [2]
    offsets = [(0, 0)]  * question_size + offsets + [(0, 0)]
    attention_mask = [1] * question_size + attention_mask + [1]
    
    # Truncate
    input_ids = input_ids[:max_seq_len]
    offsets = offsets[:max_seq_len]
    attention_mask = attention_mask[:max_seq_len]
    
    # Pad
    input_ids = input_ids + [1] * (max_seq_len - len(input_ids))
    offsets = offsets + [(0, 0)] * (max_seq_len - len(offsets))
    attention_mask = attention_mask + [0] * (max_seq_len - len(attention_mask))
    
    target_start, target_end = get_start_end(text, selected_text, offsets, max_seq_len)
    
    x = [np.asarray(input_ids, dtype=np.int32), 
         np.asarray(attention_mask, dtype=np.int32)]
    
    y = [np.asarray(target_start, dtype=np.int32), 
         np.asarray(target_end, dtype=np.int32)]
    
    return (x, y)

def get_data(df, tokenizer, MAX_LEN, preprocess_fn=preprocess_roberta):
    x_input_ids = []
    x_attention_masks = []
    y_start = []
    y_end = []
    for row in df.itertuples(): 
        x, y = preprocess_fn(' ' + getattr(row, "text"), getattr(row, "selected_text"), ' ' + getattr(row, "sentiment"), tokenizer, MAX_LEN)
        x_input_ids.append(x[0])
        x_attention_masks.append(x[1])

        y_start.append(y[0])
        y_end.append(y[1])

    x_train = [np.asarray(x_input_ids), np.asarray(x_attention_masks)]
    y_train = [np.asarray(y_start), np.asarray(y_end)]
    
    return x_train, y_train


# Test
def preprocess_roberta_test(text, question, tokenizer, max_seq_len):
    question_encoded = tokenizer.encode(question)
    question_encoded = question_encoded.ids
    question_size = len(question_encoded) + 3
    
    encoded = tokenizer.encode(text)
    input_ids = encoded.ids
    attention_mask = encoded.attention_mask
    
    # Add question
    input_ids = [0] + question_encoded + [2] + [2] + input_ids + [2]
    attention_mask = [1] * question_size + attention_mask + [1]
    
    # Truncate
    input_ids = input_ids[:max_seq_len]
    attention_mask = attention_mask[:max_seq_len]
    
    # Pad
    input_ids = input_ids + [1] * (max_seq_len - len(input_ids))
    attention_mask = attention_mask + [0] * (max_seq_len - len(attention_mask))
    
    x = [np.asarray(input_ids, dtype=np.int32), 
         np.asarray(attention_mask, dtype=np.int32)]
    
    return x

def get_data_test(df, tokenizer, MAX_LEN, preprocess_fn=preprocess_roberta_test):
    x_input_ids = []
    x_attention_masks = []
    for row in df.itertuples(): 
        x = preprocess_fn(' ' + getattr(row, "text"), ' ' + getattr(row, "sentiment"), tokenizer, MAX_LEN)
        x_input_ids.append(x[0])
        x_attention_masks.append(x[1])

    x_data = [np.asarray(x_input_ids), np.asarray(x_attention_masks)]
    
    return x_data