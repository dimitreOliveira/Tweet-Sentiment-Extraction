## Model backlog (list of the developed model and metrics)
- **Train** and **validation** are the splits using the train data from the competition.
- The competition metric is **Jaccard score**.
- **Public LB** is the Public Leaderboard score.
- **Private LB** is the Private Leaderboard score.

---

## Models

|Model|Train|Validation|Public LB|Private LB|
|-----|-----|----------|---------|----------|
|1-Tweet-Train-DistilBERT|0.725|0.616| ??? | ??? |
|2-Tweet-Train-DistilBERT lower|0.761|0.638| ??? | ??? |
|3-Tweet-Train-DistilBERT BCE|0.703|0.635| ??? | ??? |
|4-Tweet-Train-DistilBERT lower softmax|0.771|0.643| ??? | ??? |
|5-Tweet-Train-DistilBERT lower softmax v2|0.771|0.643| ??? | ??? |
|6-Tweet-Train-DistilBERT lower BCE v2|0.769|0.633| ??? | ??? |
|7-Tweet-Train-DistilBERT lower lower v2|0.783|0.640| ??? | ??? |
|8-Tweet-Train-DistilBERT lower AVG_MAX|0.439|0.433| ??? | ??? |
|9-Tweet-Train-BERT base uncased|0.508|0.434| ??? | ??? |
|10-Tweet-Train-BERT base uncased BCE|0.638|0.580| ??? | ??? |
|11-Tweet-Train-BERT base uncased pb|0.363|0.338| ??? | ??? |
|12-Tweet-Train-BERT base uncased pb2|0.460|0.413| 0.418 | ??? |
|13-Tweet-Train-DistilBERT base uncased|0.505|0.454|0.408| ??? |
|14-Tweet-Train-DistilBERT base uncased lbl lower|0.737|0.631|0.524| ??? |
|15-Tweet-Train-DistilBERT base uncased refactor|0.705|0.645|0.645| ??? |
|16-Tweet-Train-DistilBERT base uncased refac BCE|0.702|0.640|0.645| ??? |
|17-Tweet-Train-DistilBERT base uncased BCE sigmoid|0.782|0.647|0.644| ??? |
|18-Tweet-Train-DistilBERT base uncased Subtract|0.048|0.050| 0.052 | ??? |
|19-Tweet-Train-DistilBERT base uncased Sub BCE|0.374|0.368| 0.375 | ??? |
|20-Tweet-Train-DistilBERT base uncased Sub|0.540|0.517| 0.521 | ??? |
|21-Tweet-Train-DistilBERT base SparseCat|0.485|0.484| 0.486 | ??? |
|22-Tweet-Train-DistilBERT base SparseCat Logit|0.705|0.644|0.645| ??? |
|23-Tweet-Train-DistilBERT base Lbl smoothing|0.733|0.640|0.642| ??? |
|24-Tweet-Train-DistilBERT base Lbl smoothing2|0.733|0.641|0.640| ??? |
|25-Tweet-Train-DistilBERT max_len 160|0.732|0.647|0.651| ??? |
|26-Tweet-Train-DistilBERT what|0.661|0.590| 0.485 | ??? |
|27-Tweet-Train-DistilBERT no qst|0.669|0.558| 0.571 | ??? |
|28-Tweet-Train-DistilBERT base Normal smoothing|0.541|0.538| 0.534 | ??? |
|29-Tweet-Train-DistilBERT base Norm smooth Sigmoid|0.717|0.613| 0.609 | ??? |
|30-Tweet-Train-DistilBERT base Norm smooth Sigmoid|0.792|0.629|0.629| ??? |
|31-Tweet-Train-DistilBERT base Lbl smoothing BCE|0.789|0.640|0.647| ??? |
|32-Tweet-Train-DistilBERT base Poisson smooth|0.701|0.597|0.601| ??? |
|33-Tweet-Train-DistilBERT base Poisson smooth2|0.802|0.639|0.642| ??? |
|34-Tweet-Train-DistilBERT 2 transformers|0.763|0.636|0.637| ??? |
| 35-Tweet-Train-DistilBERT public | 0.746 | 0.645 | 0.654 | ??? |
| 36-Tweet-Train-DistilBERT Jaccard task | 0.749 | 0.649 | 0.652 | ??? |
| 37-Tweet-Train-3Fold DistilBERT public | 0.735 | 0.648 | 0.668 | ??? |
| 38-Tweet-Train-1Fold-BERT base | 0.737 | 0.644 | 0.648 | ??? |
| 39-Tweet-Train-1Fold-BERT large wwm | 0.640 | 0.612 | 0.613 | ??? |
| 40-Tweet-Train-3Fold-BERT base | 0.700 | 0.637 | 0.660 | ??? |
| 41-Tweet-Train-3Fold DistilBERT Conv1D head | 0.755 | 0.651 | 0.677 | ??? |
| 42-Tweet-Train-3Fold-BERT Conv1D head | 0.821 | 0.658 | 0.684 | ??? |
| 43-Tweet-Train-3Fold DistilBERT Conv1D seq len 96 | 0.777 | 0.653 | 0.679 | ??? |
| 44-Tweet-Train-3Fold DistilBERT Conv1D linear | 0.455 | 0.442 | 0.490 | ??? |
| 45-Tweet-Train-3Fold-distilRoBERTa Conv1D head | 0.752 | 0.660 | 0.672 | ??? |
| 46-Tweet-Train-3Fold-roBERTa base | 0.72351 | 0.664586 | 0.685 | ??? |
| 47-Tweet-Train-3Fold-roBERTa base public | 0.689161 | 0.65249 | 0.671 | ??? |
| 48-Tweet-Train-3Fold-roBERTa base pad fix | 0.406972 | 0.391479 | 0.621 | ??? |
| 49-Tweet-Train-3Fold-roBERTa base tf_dataset | 0.645902 | 0.5982 | 0.679 | ??? |
| 50-Tweet-Train-3Fold-roBERTa base dropout | 0.608259 | 0.556035 | 0.674 | ??? |
| 51-Tweet-Train-3Fold-roBERTa base dropout np | 0.722102 | 0.66547 | 0.681 | ??? |
| 52-Tweet-Train-3Fold-roBERTa base pb | 0.73053 | 0.700871 | 0.701 | ??? |
| 53-Tweet-Train-3Fold-roBERTa base pb2 | 0.737609 | 0.701711 | 0.697 | ??? |
| 54-Tweet-Train-3Fold-roBERTa base BCE | 0.745092 | 0.700277 | 0.708 | ??? |
| 55-Tweet-Train-3Fold-roBERTa base SparseCat | 0.73438 | 0.704676 | 0.701 | ??? |
| 56-Tweet-Train-1Fold-roBERTa base Lbl smoothing | 0.743106 | 0.699319 | 0.694 | ??? |
| 57-Tweet-Train-3Fold-roBERTa base Jaccard task | 0.750823 | 0.698045 | 0.702 | ??? |
| 58-Tweet-Train-3Fold-roBERTa base pb3 | 0.74346 | 0.693244 | 0.695 | ??? |
| 59-Tweet-Train-1Fold-roBERTa base RAdam | 0.740513 | 0.708764 | 0.703 | ??? |
| 60-Tweet-Train-1Fold-roBERTa base RAdam2 | 0.727599 | 0.702031 | 0.697 | ??? |
| 61-Tweet-Train-1Fold-roBERTa base AdamW | 0.734198 | 0.701939 | 0.702 | ??? |
| 62-Tweet-Train-1Fold-roBERTa base LR schedule | 0.727328 | 0.695301 | 0.695 | ??? |
