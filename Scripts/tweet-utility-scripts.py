import os, time
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt

    
# Auxiliary functions
def seed_everything(seed=0):
    np.random.seed(seed)
    tf.random.set_seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
    
def color_map(val):
    if type(val) == float:
        if val <= 0.4:
            color = 'red'
        elif val <= 0.5:
            color = 'orange'
        elif val >= 0.9:
            color = 'green'
        else:
            color = 'black'
    else:
        color = 'black'
    return 'color: %s' % color
    
def plot_metrics(history):
    metric_list = list(history.keys())
    size = len(metric_list)//2
    fig, axes = plt.subplots(size, 1, sharex='col', figsize=(20, size * 5))
    axes = axes.flatten()
    
    for index in range(len(metric_list)//2):
        metric_name = metric_list[index]
        val_metric_name = metric_list[index+size]
        axes[index].plot(history[metric_name], label='Train %s' % metric_name)
        axes[index].plot(history[val_metric_name], label='Validation %s' % metric_name)
        axes[index].legend(loc='best', fontsize=16)
        axes[index].set_title(metric_name)

    plt.xlabel('Epochs', fontsize=16)
    sns.despine()
    plt.show()
    

# Model evaluation
def jaccard(str1, str2): 
    a = set(str1.lower().split()) 
    b = set(str2.lower().split())
    c = a.intersection(b)
    return float(len(c)) / (len(a) + len(b) - len(c))

def evaluate_model(train_set, validation_set):
    rows = []
    sentiment_cols = np.sort(train_set['sentiment'].unique())
    train_set['jaccard'] = train_set.apply(lambda x: jaccard(x['selected_text'], x['prediction']), axis=1)
    validation_set['jaccard'] = validation_set.apply(lambda x: jaccard(x['selected_text'], x['prediction']), axis=1)
    rows.append(['Overall', train_set['jaccard'].mean(), validation_set['jaccard'].mean(), len(train_set), len(validation_set)])

    for sentiment in sentiment_cols:
        train_subset = train_set[train_set['sentiment'] == sentiment]
        validation_subset = validation_set[validation_set['sentiment'] == sentiment]
        rows.append(['Sentiment %s' % sentiment, train_subset['jaccard'].mean(), 
                     validation_subset['jaccard'].mean(), len(train_subset), len(validation_subset)])
        
    lower_bound = [0, 3, 15, 30, 45]
    upper_bound = [3, 15, 30, 45, 120]
    for idx, lower in enumerate(lower_bound):
        upper = upper_bound[idx]
        train_subset = train_set[(train_set['text_tokenCnt'] >= lower) & (train_set['text_tokenCnt'] < upper)]
        validation_subset = validation_set[(validation_set['text_tokenCnt'] >= lower) & (validation_set['text_tokenCnt'] < upper)]
        rows.append(['%d <= text tokens < %d' % (lower, upper), train_subset['jaccard'].mean(), 
                     validation_subset['jaccard'].mean(), len(train_subset), len(validation_subset)])

    for idx, lower in enumerate(lower_bound):
        upper = upper_bound[idx]
        train_subset = train_set[(train_set['selected_text_tokenCnt'] >= lower) & (train_set['selected_text_tokenCnt'] < upper)]
        validation_subset = validation_set[(validation_set['selected_text_tokenCnt'] >= lower) & (validation_set['selected_text_tokenCnt'] < upper)]
        rows.append(['%d <= selected text tokens < %d ' % (lower, upper), train_subset['jaccard'].mean(), 
                     validation_subset['jaccard'].mean(), len(train_subset), len(validation_subset)])
        
    metrics_df = pd.DataFrame(rows, columns=['Metric/Jaccard', 'Train', 'Validation', 'Train samples', 'Validation samples']).set_index('Metric/Jaccard')
        
    return metrics_df

def evaluate_model_kfold(k_fold, n_folds):
    metrics_df = pd.DataFrame([], columns=['Metric/Jaccard', 'Train', 'Valid', 'Var'])
        
    lower_bound = [0, 3, 15, 30, 45]
    upper_bound = [3, 15, 30, 45, 120]
    sentiment_cols = np.sort(k_fold['sentiment'].unique())
    labels = (['Overall'] + ['Sentiment %s' % s for s in sentiment_cols] + 
              ['%d <= text tokens < %d' % (lower_bound[idx], upper_bound[idx]) for idx in range(len(lower_bound))] + 
              ['%d <= selected text tokens < %d' % (lower_bound[idx], upper_bound[idx]) for idx in range(len(lower_bound))])
    metrics_df['Metric/Jaccard'] = labels
    for n_fold in range(n_folds):
        rows = []
        train_set = k_fold[k_fold['fold_%d' % (n_fold+1)] == 'train']
        validation_set = k_fold[k_fold['fold_%d' % (n_fold+1)] == 'validation']        
        
        train_set['jaccard'] = train_set.apply(lambda x: jaccard(x['selected_text'], x['prediction_fold_%d' % (n_fold+1)]), axis=1)
        validation_set['jaccard'] = validation_set.apply(lambda x: jaccard(x['selected_text'], x['prediction_fold_%d' % (n_fold+1)]), axis=1)
        rows.append([train_set['jaccard'].mean(), validation_set['jaccard'].mean()])

        for sentiment in sentiment_cols:
            train_subset = train_set[train_set['sentiment'] == sentiment]
            validation_subset = validation_set[validation_set['sentiment'] == sentiment]
            rows.append([train_subset['jaccard'].mean(), validation_subset['jaccard'].mean()])

        for idx, lower in enumerate(lower_bound):
            upper = upper_bound[idx]
            train_subset = train_set[(train_set['text_tokenCnt'] >= lower) & 
                                     (train_set['text_tokenCnt'] < upper)]
            validation_subset = validation_set[(validation_set['text_tokenCnt'] >= lower) & 
                                               (validation_set['text_tokenCnt'] < upper)]
            rows.append([train_subset['jaccard'].mean(), validation_subset['jaccard'].mean()])

        for idx, lower in enumerate(lower_bound):
            upper = upper_bound[idx]
            train_subset = train_set[(train_set['selected_text_tokenCnt'] >= lower) & 
                                     (train_set['selected_text_tokenCnt'] < upper)]
            validation_subset = validation_set[(validation_set['selected_text_tokenCnt'] >= lower) & 
                                               (validation_set['selected_text_tokenCnt'] < upper)]
            rows.append([train_subset['jaccard'].mean(), validation_subset['jaccard'].mean()])

        metrics_df = pd.concat([metrics_df, pd.DataFrame(rows, columns=['Train_fold_%d' % (n_fold+1), 
                                                                        'Valid_fold_%d' % (n_fold+1)])], axis=1)
    
    metrics_df['Train'] = metrics_df[[c for c in metrics_df.columns if c.startswith('Train_fold')]].mean(axis=1)
    metrics_df['Valid'] = metrics_df[[c for c in metrics_df.columns if c.startswith('Valid_fold')]].mean(axis=1)
    metrics_df['Var'] = metrics_df['Train'] - metrics_df['Valid']
    
    return metrics_df.set_index('Metric/Jaccard')

def predict_eval_df(df, model, x_train, x_valid, dataset_fn, decode_fn, n_fold, tokenizer, config, question_size=None):
    fold_col = f'fold_{n_fold}'
    end_col = f'end_fold_{n_fold}'
    start_col = f'start_fold_{n_fold}'
    pred_col = f'prediction_fold_{n_fold}'
    jaccard_col = f'jaccard_fold_{n_fold}'
    
    train_preds = model.predict(dataset_fn(x_train, config['BATCH_SIZE']))
    valid_preds = model.predict(dataset_fn(x_valid, config['BATCH_SIZE']))
    
    df.loc[df[fold_col] == 'train', start_col] = train_preds[0].argmax(axis=-1)
    df.loc[df[fold_col] == 'train', end_col] = train_preds[1].argmax(axis=-1)
    df.loc[df[fold_col] == 'validation', start_col] = valid_preds[0].argmax(axis=-1)
    df.loc[df[fold_col] == 'validation', end_col] = valid_preds[1].argmax(axis=-1)
    
    df[end_col] = df[end_col].astype(int)
    df[start_col] = df[start_col].astype(int)
#     df[end_col].clip(0, df['text_len'], inplace=True)
#     df[start_col].clip(0, df[start_col], inplace=True)
    if question_size is None:
        df[pred_col] = df.apply(lambda x: decode_fn(x[start_col], x[end_col], x['text'], tokenizer), axis=1)
    else:
        df[pred_col] = df.apply(lambda x: decode_fn(x[start_col], x[end_col], x['text'], config['question_size'], tokenizer), axis=1)
        
    df[pred_col] = df.apply(lambda x: ' '.join([word for word in x[pred_col].split() if word in x['text'].split()]), axis=1)
    df[pred_col] = df.apply(lambda x: x['text'] if (x[pred_col] == '') else x[pred_col], axis=1)
    df[pred_col].fillna(df['text'], inplace=True)
    df[jaccard_col] = df.apply(lambda x: jaccard(x['selected_text'], x[pred_col]), axis=1)

# Datasets
def get_training_dataset(x_train, y_train, batch_size, buffer_size, seed=0):
    dataset = tf.data.Dataset.from_tensor_slices(({'input_ids': x_train[0],'attention_mask': x_train[1]}, 
                                                  {'y_start': y_train[0],'y_end': y_train[1]}))
    dataset = dataset.repeat()
    dataset = dataset.shuffle(2048, seed=seed)
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.prefetch(buffer_size)
    return dataset

def get_validation_dataset(x_valid, y_valid, batch_size, buffer_size, repeated=False, seed=0):
    dataset = tf.data.Dataset.from_tensor_slices(({'input_ids': x_valid[0],'attention_mask': x_valid[1]}, 
                                                  {'y_start': y_valid[0],'y_end': y_valid[1]}))
    if repeated:
        dataset = dataset.repeat()
        dataset = dataset.shuffle(2048, seed=seed)
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.cache()
    dataset = dataset.prefetch(buffer_size)
    return dataset

def get_test_dataset(x_test, batch_size):
    dataset = tf.data.Dataset.from_tensor_slices({'input_ids': x_test[0],'attention_mask': x_test[1]})
    dataset = dataset.batch(batch_size)
    return dataset


# Training
def custom_fit(model, metrics_dict, train_step_fn, valid_step_fn, train, validation, 
               train_step_size, validation_step_size, batch_size, epochs, patience=None, 
               model_path='model.h5', save_last=False, checkpoint_freq=None):
        
    # ==================== Setup training loop ====================
    step = 0
    epoch = 0
    epoch_steps = 0
    epoch_start_time = time.time()
    patience_cnt = 0
    best_val = float("inf")
    
    history = {}
    for metric in metrics_dict.keys():
        history[metric] = []

    print(f'Train for {train_step_size} steps, validate for {validation_step_size} steps')
    # ==================== Train model ====================
    while True:
        train_step_fn(train)
        epoch_steps += train_step_size
        step += train_step_size

        # validation run at the end of each epoch
        if (step // train_step_size) > epoch:
            # validation run
            valid_epoch_steps = 0
            valid_step_fn(validation)
            valid_epoch_steps += validation_step_size
            
            # compute metrics
            for metric in metrics_dict.keys():
                if 'loss' in metric:
                    if 'val_' in metric: # loss from validation
                        history[metric].append(metrics_dict[metric].result().numpy() / (batch_size * valid_epoch_steps))
                    else: # loss from training
                        history[metric].append(metrics_dict[metric].result().numpy() / (batch_size * epoch_steps))
                else: # any other metric
                    history[metric].append(metrics_dict[metric].result().numpy())

            # report metrics
            epoch_time = time.time() - epoch_start_time
            print('\nEPOCH {:d}/{:d}'.format(epoch+1, epochs))
            report = f"time: {epoch_time:0.1f}s"
            for metric in metrics_dict.keys():
                report += f" {metric}: {history[metric][-1]:0.4f}"
            print(report)

            # set up next epoch
            epoch = step // train_step_size
            epoch_steps = 0
            epoch_start_time = time.time()
            for metric in metrics_dict.values():
                metric.reset_states()
                
            # Model checkpoint
            if checkpoint_freq is not None:
                if epoch % checkpoint_freq == 0:
                    model_path_chk = 'ep_%d_%d' % (epoch, model_path)
                    model.save_weights(model_path_chk)
                    print('Checkpointing model weights at "%s"' % model_path_chk)

            if epoch <= epochs:
                if patience is not None:
                    # Early stopping monitor
                    if history['val_loss'][-1] <= best_val:
                        best_val = history['val_loss'][-1]
                        model.save_weights(model_path)
                        print('Saved model weights at "%s"' % model_path)
                    else:
                        patience_cnt += 1
                    if patience_cnt >= patience:
                        print('Epoch %05d: early stopping' % epoch)
                        if epoch < epochs:
                            return history
            if epoch >= epochs:
                if save_last:
                    model_path_last = 'last_' + model_path
                    model.save_weights(model_path_last)
                    print('Training finished saved model weights at "%s"' % model_path_last)
                else:
                    print('Training finished')
                    
                return history