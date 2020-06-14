import numpy as np

    
# Process inputs
# Train
def preprocess(text, selected_text, question, tokenizer, max_seq_len):
    question_encoded = tokenizer.encode(question)
    question_encoded = question_encoded.ids[1:-1]
    question_size = len(question_encoded) + 2
    
    encoded = tokenizer.encode(text)
    encoded.pad(max_seq_len)
    encoded.truncate(max_seq_len)
    input_ids = encoded.ids
    offsets = encoded.offsets
    attention_mask = encoded.attention_mask
    token_type_ids = ([0] * question_size) + ([1] * (max_seq_len - question_size))
    
    # update input ids, offsets and attentions masks size
    input_ids = [101] + question_encoded + [102] + input_ids[1:-(question_size-1)]
    offsets = [(0, 0)]  * question_size + offsets[:-question_size]
    if input_ids[-1] != 0: # If sentence was truncated last token should be [102]
        input_ids[-1] = 102
        offsets[-1] = (0, 0)
    attention_mask = [1] * question_size + attention_mask[:-question_size]
    
    target_start, target_end = get_start_end(text, selected_text, offsets, max_seq_len)
    
    x = [np.asarray(input_ids, dtype=np.int32), 
         np.asarray(attention_mask, dtype=np.int32), 
         np.asarray(token_type_ids, dtype=np.int32)]
    
    y = [np.asarray(target_start, dtype=np.int32), 
         np.asarray(target_end, dtype=np.int32)]
    
    return (x, y)


def get_data(df, tokenizer, MAX_LEN, preprocess_fn=preprocess):
    x_input_ids = []
    x_attention_masks = []
    x_token_type_ids = []
    y_start = []
    y_end = []
    for row in df.itertuples(): 
        x, y = preprocess_fn(getattr(row, "text"), getattr(row, "selected_text"), getattr(row, "sentiment"), tokenizer, MAX_LEN)
        x_input_ids.append(x[0])
        x_attention_masks.append(x[1])
        x_token_type_ids.append(x[2])

        y_start.append(y[0])
        y_end.append(y[1])

    x_train = [np.asarray(x_input_ids), np.asarray(x_attention_masks), np.asarray(x_token_type_ids)]
    y_train = [np.asarray(y_start), np.asarray(y_end)]
    
    return x_train, y_train


# Test
def preprocess_test(text, question, tokenizer, max_seq_len):
    question_encoded = tokenizer.encode(question)
    question_encoded = question_encoded.ids[1:-1]
    question_size = len(question_encoded) + 2
    
    encoded = tokenizer.encode(text)
    encoded.pad(max_seq_len)
    encoded.truncate(max_seq_len)
    input_ids = encoded.ids
    attention_mask = encoded.attention_mask
    token_type_ids = ([0] * question_size) + ([1] * (max_seq_len - question_size))
    
    # update input ids and attentions masks size
    input_ids = [101] + question_encoded + [102] + input_ids[1:-(question_size-1)]
    if input_ids[-1] != 0: # If sentence was truncated last token should be [102]
        input_ids[-1] = 102
    attention_mask = [1] * question_size + attention_mask[:-question_size]
    
    x = [np.asarray(input_ids, dtype=np.int32), 
         np.asarray(attention_mask, dtype=np.int32), 
         np.asarray(token_type_ids, dtype=np.int32)]
    
    return x


def get_data_test(df, tokenizer, MAX_LEN, preprocess_fn=preprocess_test):
    x_input_ids = []
    x_attention_masks = []
    x_token_type_ids = []
    for row in df.itertuples(): 
        x = preprocess_fn(getattr(row, "text"), getattr(row, "sentiment"), tokenizer, MAX_LEN)
        x_input_ids.append(x[0])
        x_attention_masks.append(x[1])
        x_token_type_ids.append(x[2])

    x_data = [np.asarray(x_input_ids), np.asarray(x_attention_masks), np.asarray(x_token_type_ids)]
    
    return x_data


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
    offset = tokenizer.encode(text).offsets
    pred_start = pred_start - question_size
    pred_end = pred_end - question_size
    
    if pred_end >= len(offset):
        pred_end = len(offset)-2
    if pred_start >= len(offset):
        pred_start = len(offset)-2
    
    return text[offset[pred_start][0]: offset[pred_end][1]]


# NOT USING QUESTION
# Train
def preprocess_clean(text, selected_text, tokenizer, max_seq_len):
    encoded = tokenizer.encode(text)
    encoded.pad(max_seq_len)
    encoded.truncate(max_seq_len)
    input_ids = encoded.ids
    offsets = encoded.offsets
    attention_mask = encoded.attention_mask
    token_type_ids = [1] * max_seq_len
    
    target_start, target_end = get_start_end(text, selected_text, offsets, max_seq_len)
    
    x = [np.asarray(input_ids, dtype=np.int32), 
         np.asarray(attention_mask, dtype=np.int32), 
         np.asarray(token_type_ids, dtype=np.int32)]
    
    y = [np.asarray(target_start, dtype=np.int32), 
         np.asarray(target_end, dtype=np.int32)]
    
    return (x, y)


def get_data_clean(df, tokenizer, MAX_LEN):
    x_input_ids = []
    x_attention_masks = []
    x_token_type_ids = []
    y_start = []
    y_end = []
    for row in df.itertuples(): 
        x, y = preprocess_clean(getattr(row, "text"), getattr(row, "selected_text"), tokenizer, MAX_LEN)
        x_input_ids.append(x[0])
        x_attention_masks.append(x[1])
        x_token_type_ids.append(x[2])

        y_start.append(y[0])
        y_end.append(y[1])

    x_train = [np.asarray(x_input_ids), np.asarray(x_attention_masks), np.asarray(x_token_type_ids)]
    y_train = [np.asarray(y_start), np.asarray(y_end)]
    return x_train, y_train


def decode_clean(pred_start, pred_end, text, tokenizer):
    offset = tokenizer.encode(text).offsets
    
    if pred_end >= len(offset):
        pred_end = len(offset)-2
    if pred_start >= len(offset):
        pred_start = len(offset)-2
    
    return text[offset[pred_start][0]: offset[pred_end][1]]