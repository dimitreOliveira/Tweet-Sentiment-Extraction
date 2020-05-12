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
| 63-Tweet-Train-3Fold-roBERTa base RAdam | 0.734822 | 0.704573 | 0.705 | ??? |
| 64-Tweet-Train-3Fold-roBERTa base AdamW | 0.742949 | 0.698587 | 0.704 | ??? |
| 65-Tweet-Train-1Fold-roBERTa base Two heads | 0.738196 | 0.694098 | 0.692 | ??? |
| 66-Tweet-Train-1Fold-roBERTa base Avg last4 | 0.740247 | 0.700285 | 0.702 | ??? |
| 67-Tweet-Train-1Fold-roBERTa base dense | 0.746128 | 0.696764 | 0.695 | ??? |
| 68-Tweet-Train-1Fold-roBERTa base subtract | 0.744659 | 0.713293 | 0.708 | ??? |
| 69-Tweet-Train-1Fold-roBERTa base subtract text | 0.657457 | 0.608559 | 0.618 | ??? |
| 70-Tweet-Train-1Fold-roBERTa base pred sentiment | 0.668898 | 0.628801 | 0.634 | ??? |
| 71-Tweet-Train-5Fold-roBERTa base subtract | 0.732519 | 0.702948 | 0.703 | ??? |
| 72-Tweet-Train-5Fold-roBERTa base subtract dense | 0.739804 | 0.706634 | 0.706 | ??? |
| 73-Tweet-Train-1Fold-roBERTa base pred jaccard | 0.690943 | 0.621937 | 0.627 | ??? |
| 74-Tweet-Train-1Fold-roBERTa base pred sentiment2 | 0.6948 | 0.623752 | 0.629 | ??? |
| 75-Tweet-Train-5Fold-roBERTa base subtract AdamW | 0.736428 | 0.698001 | 0.705 | ??? |
| 76-Tweet-Train-3Fold-roBERTa base RAdam CNN BCE | 0.732718 | 0.707449 | 0.705 | ??? |
| 77-Tweet-Train-3Fold-roBERTa base RAdam CNN CCE | 0.751051 | 0.706018 | 0.708 | ??? |
| 78-Tweet-Train-3Fold-roBERTa base RAdam CNN Schedu | 0.737130 | 0.708520 | 0.704 | ??? |
| 79-Tweet-Train-3Fold-roBERTa base LRScheduler Warm | 0.741571 | 0.704275 | 0.705 | ??? |
| 80-Tweet-Train-3Fold-roBERTa base LRScheduler | 0.746869 | 0.704726 | 0.708 | ??? |
| 81-Tweet-Train-3Fold-roBERTa base Lbl smoothing 01 | 0.749219 | 0.707017 | 0.709 | ??? |
| 82-Tweet-Train-3Fold-roBERTa base Lbl smoothing 02 | 0.753057 | 0.708108 | 0.712 | ??? |
| 83-Tweet-Train-3Fold-roBERTa base pred sentiment | 0.744714 | 0.706536 | 0.710 | ??? |
| 84-Tweet-Train-3Fold-roBERTa base pred sent jac | 0.740921 | 0.702955 | 0.705 | ??? |
| 85-Tweet-Train-3Fold-roBERTa base Lbl smooth2 sent | 0.752989 | 0.706785 | 0.708 | ??? |
| 86-Tweet-Train-3Fold-roBERTa base exp dropout | 0.756994 | 0.709613 | 0.709 | ??? |
| 87-Tweet-Train-3Fold-roBERTa base smoothing 02 CNN | 0.752616 | 0.708876 | 0.710 | ??? |
| 88-Tweet-Train-3Fold-roBERTa base smoothing02 CNN2 | 0.756766 | 0.706790 | 0.707 | ??? |
| 89-Tweet-Train-3Fold-roBERTa base subtract | 0.742508 | 0.708787 | 0.709 | ??? |
| 90-Tweet-Train-3Fold-roBERTa base average | 0.748901 | 0.709099 | 0.711 | ??? |
| 91-Tweet-Train-5Fold-roBERTa base Lbl smooth02 | 0.746417 | 0.705245 | 0.714 | ??? |
| 92-Tweet-Train-5Fold-roBERTa base pred sentiment | 0.747240 | 0.705034 | 0.707 | ??? |
| 93-Tweet-Train-3Fold-roBERTa base custom loss | 0.749060 | 0.709306 | 0.709 | ??? |
| 94-Tweet-Train-3Fold-roBERTa base CCE BCE output | 0.737505 | 0.703423 | 0.702 | ??? |
| 95-Tweet-Train-3Fold-roBERTa base custom loss1 | 0.754466 | 0.708478 | 0.707 | ??? |
| 96-Tweet-Train-3Fold-roBERTa base custom loss025 | 0.737188 | 0.702793 | 0.707 | ??? |
| 97-Tweet-Train-3Fold-roBERTa base cust loss smoo02 | 0.736578 | 0.702851 | 0.706 | ??? |
| 98-Tweet-Train-5Fold-roBERTa base custom loss | 0.742584 | 0.704128 | 0.710 | ??? |
| 99-Tweet-Train-5Fold-roBERTa base Lbl smth02 AVG4 | 0.751298 | 0.708171 | 0.713 | ??? |
| 100-Tweet-Train-5Fold-roBERTa base Lbl smth02 sigm | 0.744290 | 0.707073 | 0.709 | ??? |
| 101-Tweet-Train-5Fold-roBERTa base smth02 BCE sigm | 0.743304 | 0.708947 | 0.707 | ??? |
| 102-Tweet-Train-5Fold-roBERTa base average | 0.748338 | 0.708052 | 0.711 | ??? |
| 103-Tweet-Train-5Fold-roBERTa base smoothing02 CNN | 0.742685 | 0.706157 | 0.710 | ??? |
| 104-Tweet-Train-2Fold-roBERTa large Lbl smooth02 | ??? | ??? | 0.690 | ??? |
| 105-Tweet-Train-3Fold-roBERTa base combine 4layers | 0.743229 | 0.707287 | 0.708 | ??? |
| 106-Tweet-Train-3Fold-roBERTa base single BN layer | 0.748189 | 0.705973 | 0.710 | ??? |
| 107-Tweet-Train-5Fold-roBERTa base hidden11 | 0.759228 | 0.707189	| 0.713 | ??? |
| 108-Tweet-Train-5Fold-roBERTa base hidden10 | 0.753675 | 0.708053 | 0.712 | ??? |
| 109-Tweet-Train-5Fold-roBERTa base hidden09 | 0.755624 | 0.707887	| 0.710 | ??? |
| 110-Tweet-Train-5Fold-roBERTa base config drop | 0.730080 | 0.706287 | 0.703 | ??? |
| 111-Tweet-Train-5Fold-roBERTa base 4epochs exp | 0.758400 | 0.707899 | 0.713 | ??? |
| 112-Tweet-Train-5Fold-roBERTa base 3epochs exp | 0.747573 | 0.707170 | 0.709 | ??? |
| 113-Tweet-Train-5Fold-roBERTa base 4epochs cos | 0.775953 | 0.707041 | 0.714 | ??? |
| 114-Tweet-Train-5Fold-roBERTa base 3epochs cos | 0.749963	| 0.706625 | 0.710 | ??? |
| 115-Tweet-Train-3Fold-roBERTa base tf_dataset | 0.746860 | 0.705446 | 0.711 | ??? |
| 116-Tweet-Train-5Fold-roBERTa base optimized loop | 0.740988 | 0.701456 | 0.706 | ??? |
| 117-Tweet-Train-1Fold-distilroBERTa base double decent cosine decay | 0.950197 | 0.686683 | 000 | ??? |
| 118-Tweet-Train-1Fold-distilroBERTa base double decent restart cosine decay | 0.950193 | 0.682601	| 000 | ??? |
| 119-Tweet-Train-5Fold-roBERTa base no dropout | 0.744903 | 0.702522 | 0.711 | ??? |
| 120-Tweet-Train-1Fold-distilroBERTa base double decent bs_128 | 0.950215 | 0.678692	| 000 | ??? |
| 121-Tweet-Train-1Fold-distilroBERTa base double decent lbl smooth 01 | 0.950181 | 0.675745 | 000 | ??? |
