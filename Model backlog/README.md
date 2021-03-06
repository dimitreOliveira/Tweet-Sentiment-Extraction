## Model backlog (list of the developed model and metrics)
- **Train** and **validation** are the splits using the train data from the competition.
- The competition metric is **Jaccard score**.
- **Public LB** is the Public Leaderboard score.
- **Private LB** is the Private Leaderboard score.

---

## Models

|Model|Train|Validation|Public LB|Private LB|
|-----|-----|----------|---------|----------|
|1-Tweet-Train-DistilBERT|0.725|0.616| 0.624 | 0.616 |
|2-Tweet-Train-DistilBERT lower|0.761|0.638| 0.644 | 0.637 |
|3-Tweet-Train-DistilBERT BCE|0.703|0.635| 0.638 | 0.635 |
|4-Tweet-Train-DistilBERT lower softmax|0.771|0.643| 0.645 | 0.641 |
|5-Tweet-Train-DistilBERT lower softmax v2|0.771|0.643| 0.645 | 0.641 |
|6-Tweet-Train-DistilBERT lower BCE v2|0.769|0.633| 0.635 | 0.636 |
|7-Tweet-Train-DistilBERT lower lower v2|0.783|0.640| 0.645 | 0.637 |
|8-Tweet-Train-DistilBERT lower AVG_MAX|0.439|0.433| 0.437 | 0.441 |
|9-Tweet-Train-BERT base uncased|0.508|0.434| 0.443 | 0.451 |
|10-Tweet-Train-BERT base uncased BCE|0.638|0.580| 0.589 | 0.588 |
|11-Tweet-Train-BERT base uncased pb|0.363|0.338| 0.341 | 0.347 |
|12-Tweet-Train-BERT base uncased pb2|0.460|0.413| 0.418 | 0.418 |
|13-Tweet-Train-DistilBERT base uncased|0.505|0.454|0.408| 0.412 |
|14-Tweet-Train-DistilBERT base uncased lbl lower|0.737|0.631|0.524| 0.525 |
|15-Tweet-Train-DistilBERT base uncased refactor|0.705|0.645|0.645| 0.641 |
|16-Tweet-Train-DistilBERT base uncased refac BCE|0.702|0.640|0.645| 0.639 |
|17-Tweet-Train-DistilBERT base uncased BCE sigmoid|0.782|0.647|0.644| 0.641 |
|18-Tweet-Train-DistilBERT base uncased Subtract|0.048|0.050| 0.052 | 0.050 |
|19-Tweet-Train-DistilBERT base uncased Sub BCE|0.374|0.368| 0.375 | 0.374 |
|20-Tweet-Train-DistilBERT base uncased Sub|0.540|0.517| 0.521 | 0.519 |
|21-Tweet-Train-DistilBERT base SparseCat|0.485|0.484| 0.486 | 0.486 |
|22-Tweet-Train-DistilBERT base SparseCat Logit|0.705|0.644|0.645| 0.641 |
|23-Tweet-Train-DistilBERT base Lbl smoothing|0.733|0.640|0.642| 0.642 |
|24-Tweet-Train-DistilBERT base Lbl smoothing2|0.733|0.641|0.640| 0.640 |
|25-Tweet-Train-DistilBERT max_len 160|0.732|0.647|0.651| 0.651 |
|26-Tweet-Train-DistilBERT what|0.661|0.590| 0.485 | 0.482 |
|27-Tweet-Train-DistilBERT no qst|0.669|0.558| 0.571 | 0.565 |
|28-Tweet-Train-DistilBERT base Normal smoothing|0.541|0.538| 0.534 | 0.532 |
|29-Tweet-Train-DistilBERT base Norm smooth Sigmoid|0.717|0.613| 0.609 | 0.609 |
|30-Tweet-Train-DistilBERT base Norm smooth Sigmoid|0.792|0.629|0.629| 0.627 |
|31-Tweet-Train-DistilBERT base Lbl smoothing BCE|0.789|0.640|0.647| 0.638 |
|32-Tweet-Train-DistilBERT base Poisson smooth|0.701|0.597|0.601| 0.601 |
|33-Tweet-Train-DistilBERT base Poisson smooth2|0.802|0.639|0.642| 0.636 |
|34-Tweet-Train-DistilBERT 2 transformers|0.763|0.636|0.637| 0.632 |
| 35-Tweet-Train-DistilBERT public | 0.746 | 0.645 | 0.654 | 0.647 |
| 36-Tweet-Train-DistilBERT Jaccard task | 0.749 | 0.649 | 0.652 | 0.642 |
| 37-Tweet-Train-3Fold DistilBERT public | 0.735 | 0.648 | 0.668 | 0.664 |
| 38-Tweet-Train-1Fold-BERT base | 0.737 | 0.644 | 0.648 | 0.640 |
| 39-Tweet-Train-1Fold-BERT large wwm | 0.640 | 0.612 | 0.613 | 0.613 |
| 40-Tweet-Train-3Fold-BERT base | 0.700 | 0.637 | 0.660 | 0.656 |
| 41-Tweet-Train-3Fold DistilBERT Conv1D head | 0.755 | 0.651 | 0.677 | 0.671 |
| 42-Tweet-Train-3Fold-BERT Conv1D head | 0.821 | 0.658 | 0.684 | 0.676 |
| 43-Tweet-Train-3Fold DistilBERT Conv1D seq len 96 | 0.777 | 0.653 | 0.679 | 0.674 |
| 44-Tweet-Train-3Fold DistilBERT Conv1D linear | 0.455 | 0.442 | 0.490 | 0.493 |
| 45-Tweet-Train-3Fold-distilRoBERTa Conv1D head | 0.752 | 0.660 | 0.672 | 0.676 |
| 46-Tweet-Train-3Fold-roBERTa base | 0.72351 | 0.664586 | 0.685 | 0.680 |
| 47-Tweet-Train-3Fold-roBERTa base public | 0.689161 | 0.65249 | 0.671 | 0.672 |
| 48-Tweet-Train-3Fold-roBERTa base pad fix | 0.406972 | 0.391479 | 0.621 | 0.620 |
| 49-Tweet-Train-3Fold-roBERTa base tf_dataset | 0.645902 | 0.5982 | 0.679 | 0.683 |
| 50-Tweet-Train-3Fold-roBERTa base dropout | 0.608259 | 0.556035 | 0.674 | 0.672 |
| 51-Tweet-Train-3Fold-roBERTa base dropout np | 0.722102 | 0.66547 | 0.681 | 0.683 |
| 52-Tweet-Train-3Fold-roBERTa base pb | 0.73053 | 0.700871 | 0.701 | 0.703 |
| 53-Tweet-Train-3Fold-roBERTa base pb2 | 0.737609 | 0.701711 | 0.697 | 0.704 |
| 54-Tweet-Train-3Fold-roBERTa base BCE | 0.745092 | 0.700277 | 0.708 | 0.713 |
| 55-Tweet-Train-3Fold-roBERTa base SparseCat | 0.73438 | 0.704676 | 0.701 | 0.703 |
| 56-Tweet-Train-1Fold-roBERTa base Lbl smoothing | 0.743106 | 0.699319 | 0.694 | 0.705 |
| 57-Tweet-Train-3Fold-roBERTa base Jaccard task | 0.750823 | 0.698045 | 0.702 | 0.706 |
| 58-Tweet-Train-3Fold-roBERTa base pb3 | 0.74346 | 0.693244 | 0.695 | 0.705 |
| 59-Tweet-Train-1Fold-roBERTa base RAdam | 0.740513 | 0.708764 | 0.703 | 0.709 |
| 60-Tweet-Train-1Fold-roBERTa base RAdam2 | 0.727599 | 0.702031 | 0.697 | 0.706 |
| 61-Tweet-Train-1Fold-roBERTa base AdamW | 0.734198 | 0.701939 | 0.702 | 0.704 |
| 62-Tweet-Train-1Fold-roBERTa base LR schedule | 0.727328 | 0.695301 | 0.695 | 0.700 |
| 63-Tweet-Train-3Fold-roBERTa base RAdam | 0.734822 | 0.704573 | 0.705 | 0.711 |
| 64-Tweet-Train-3Fold-roBERTa base AdamW | 0.742949 | 0.698587 | 0.704 | 0.710 |
| 65-Tweet-Train-1Fold-roBERTa base Two heads | 0.738196 | 0.694098 | 0.692 | 0.699 |
| 66-Tweet-Train-1Fold-roBERTa base Avg last4 | 0.740247 | 0.700285 | 0.702 | 0.706 |
| 67-Tweet-Train-1Fold-roBERTa base dense | 0.746128 | 0.696764 | 0.695 | 0.701 |
| 68-Tweet-Train-1Fold-roBERTa base subtract | 0.744659 | 0.713293 | 0.708 | 0.711 |
| 69-Tweet-Train-1Fold-roBERTa base subtract text | 0.657457 | 0.608559 | 0.618 | 0.611 |
| 70-Tweet-Train-1Fold-roBERTa base pred sentiment | 0.668898 | 0.628801 | 0.634 | 0.627 |
| 71-Tweet-Train-5Fold-roBERTa base subtract | 0.732519 | 0.702948 | 0.703 | 0.712 |
| 72-Tweet-Train-5Fold-roBERTa base subtract dense | 0.739804 | 0.706634 | 0.706 | 0.714 |
| 73-Tweet-Train-1Fold-roBERTa base pred jaccard | 0.690943 | 0.621937 | 0.627 | 0.620 |
| 74-Tweet-Train-1Fold-roBERTa base pred sentiment2 | 0.6948 | 0.623752 | 0.629 | 0.627 |
| 75-Tweet-Train-5Fold-roBERTa base subtract AdamW | 0.736428 | 0.698001 | 0.705 | 0.710 |
| 76-Tweet-Train-3Fold-roBERTa base RAdam CNN BCE | 0.732718 | 0.707449 | 0.705 | 0.708 |
| 77-Tweet-Train-3Fold-roBERTa base RAdam CNN CCE | 0.751051 | 0.706018 | 0.708 | 0.711 |
| 78-Tweet-Train-3Fold-roBERTa base RAdam CNN Schedu | 0.737130 | 0.708520 | 0.704 | 0.711 |
| 79-Tweet-Train-3Fold-roBERTa base LRScheduler Warm | 0.741571 | 0.704275 | 0.705 | 0.712 |
| 80-Tweet-Train-3Fold-roBERTa base LRScheduler | 0.746869 | 0.704726 | 0.708 | 0.712 |
| 81-Tweet-Train-3Fold-roBERTa base Lbl smoothing 01 | 0.749219 | 0.707017 | 0.709 | 0.711 |
| 82-Tweet-Train-3Fold-roBERTa base Lbl smoothing 02 | 0.753057 | 0.708108 | 0.712 | 0.714 |
| 83-Tweet-Train-3Fold-roBERTa base pred sentiment | 0.744714 | 0.706536 | 0.710 | 0.712 |
| 84-Tweet-Train-3Fold-roBERTa base pred sent jac | 0.740921 | 0.702955 | 0.705 | 0.712 |
| 85-Tweet-Train-3Fold-roBERTa base Lbl smooth2 sent | 0.752989 | 0.706785 | 0.708 | 0.713 |
| 86-Tweet-Train-3Fold-roBERTa base exp dropout | 0.756994 | 0.709613 | 0.709 | 0.713 |
| 87-Tweet-Train-3Fold-roBERTa base smoothing 02 CNN | 0.752616 | 0.708876 | 0.710 | 0.714 |
| 88-Tweet-Train-3Fold-roBERTa base smoothing02 CNN2 | 0.756766 | 0.706790 | 0.707 | 0.713 |
| 89-Tweet-Train-3Fold-roBERTa base subtract | 0.742508 | 0.708787 | 0.709 | 0.714 |
| 90-Tweet-Train-3Fold-roBERTa base average | 0.748901 | 0.709099 | 0.711 | 0.714 |
| 91-Tweet-Train-5Fold-roBERTa base Lbl smooth02 | 0.746417 | 0.705245 | 0.714 | 0.716 |
| 92-Tweet-Train-5Fold-roBERTa base pred sentiment | 0.747240 | 0.705034 | 0.707 | 0.713 |
| 93-Tweet-Train-3Fold-roBERTa base custom loss | 0.749060 | 0.709306 | 0.709 | 0.714 |
| 94-Tweet-Train-3Fold-roBERTa base CCE BCE output | 0.737505 | 0.703423 | 0.702 | 0.711 |
| 95-Tweet-Train-3Fold-roBERTa base custom loss1 | 0.754466 | 0.708478 | 0.707 | 0.713 |
| 96-Tweet-Train-3Fold-roBERTa base custom loss025 | 0.737188 | 0.702793 | 0.707 | 0.711 |
| 97-Tweet-Train-3Fold-roBERTa base cust loss smoo02 | 0.736578 | 0.702851 | 0.706 | 0.709 |
| 98-Tweet-Train-5Fold-roBERTa base custom loss | 0.742584 | 0.704128 | 0.710 | 0.713 |
| 99-Tweet-Train-5Fold-roBERTa base Lbl smth02 AVG4 | 0.751298 | 0.708171 | 0.713 | 0.715 |
| 100-Tweet-Train-5Fold-roBERTa base Lbl smth02 sigm | 0.744290 | 0.707073 | 0.709 | 0.715 |
| 101-Tweet-Train-5Fold-roBERTa base smth02 BCE sigm | 0.743304 | 0.708947 | 0.707 | 0.714 |
| 102-Tweet-Train-5Fold-roBERTa base average | 0.748338 | 0.708052 | 0.711 | 0.713 |
| 103-Tweet-Train-5Fold-roBERTa base smoothing02 CNN | 0.742685 | 0.706157 | 0.710 | 0.712 |
| 104-Tweet-Train-2Fold-roBERTa large Lbl smooth02 | ??? | ??? | 0.690 | 0.694 |
| 105-Tweet-Train-3Fold-roBERTa base combine 4layers | 0.743229 | 0.707287 | 0.708 | 0.713 |
| 106-Tweet-Train-3Fold-roBERTa base single BN layer | 0.748189 | 0.705973 | 0.710 | 0.714 |
| 107-Tweet-Train-5Fold-roBERTa base hidden11 | 0.759228 | 0.707189	| 0.713 | 0.717 |
| 108-Tweet-Train-5Fold-roBERTa base hidden10 | 0.753675 | 0.708053 | 0.712 | 0.716 |
| 109-Tweet-Train-5Fold-roBERTa base hidden09 | 0.755624 | 0.707887	| 0.710 | 0.713 |
| 110-Tweet-Train-5Fold-roBERTa base config drop | 0.730080 | 0.706287 | 0.703 | 0.713 |
| 111-Tweet-Train-5Fold-roBERTa base 4epochs exp | 0.758400 | 0.707899 | 0.713 | 0.716 |
| 112-Tweet-Train-5Fold-roBERTa base 3epochs exp | 0.747573 | 0.707170 | 0.709 | 0.716 |
| 113-Tweet-Train-5Fold-roBERTa base 4epochs cos | 0.775953 | 0.707041 | 0.714 | 0.714 |
| 114-Tweet-Train-5Fold-roBERTa base 3epochs cos | 0.749963	| 0.706625 | 0.710 | 0.715 |
| 115-Tweet-Train-3Fold-roBERTa base tf_dataset | 0.746860 | 0.705446 | 0.711 | 0.711 |
| 116-Tweet-Train-5Fold-roBERTa base optimized loop | 0.740988 | 0.701456 | 0.706 | 0.712 |
| 117-Tweet-Train-1Fold-distilroBERTa base double decent cosine decay | 0.950197 | 0.686683 | 000 | ??? |
| 118-Tweet-Train-1Fold-distilroBERTa base double decent restart cosine decay | 0.950193 | 0.682601	| 000 | ??? |
| 119-Tweet-Train-5Fold-roBERTa base no dropout | 0.744903 | 0.702522 | 0.711 | 0.714 |
| 120-Tweet-Train-1Fold-distilroBERTa base double decent bs_128 | 0.950215 | 0.678692	| 000 | ??? |
| 121-Tweet-Train-1Fold-distilroBERTa base double decent lbl smooth 01 | 0.950181 | 0.675745 | 000 | ??? |
| 122-Tweet-Train-5Fold-roBERTa base AdamW TF | 0.745664 | 0.703401 | 0.707 | 0.714 |
| 123-Tweet-Train-5Fold-roBERTa base AdamW HF | 0.748513 | 0.701229 | 0.711 | 0.711 |
| 124-Tweet-Train-5Fold-roBERTa base bs_64 | 0.738116 | 0.704675 | 0.708 | 0.712 |
| 125-Tweet-Train-5Fold-roBERTa base bs_8 | 0.738601 | 0.693649 | 0.706 | 0.713 |
| 126-Tweet-Train-5Fold-roBERTa base poisson dist05 | 0.741765 | 0.704092 | 0.707 | 0.713 |
| 127-Tweet-Train-3Fold-roBERTa base poisson dist02 | 0.740248 | 0.705404 | 0.707 | 0.712 |
| 128-Tweet-Train-5Fold-roBERTa base balanced | 0.704530 | 0.670277 | 0.709 | 0.712 |
| 129-Tweet-Train-5Fold-roBERTa base aux mask | 0.746811 | 0.705188 | 0.712 | 0.713 |
| 130-Tweet-Train-5Fold-roBERTa base aux jaccard | 0.738686 | 0.703425 | 0.707 | 0.712 |
| 131-Tweet-Train-5Fold-roBERTa base aux word count | 0.737214 | 0.703725 | 0.705 | 0.713 |
| 132-Tweet-Train-5Fold-roBERTa base aux sentiment | 0.742824 | 0.705239 | 0.710 | 0.714 |
| 133-Tweet-Train-5Fold-roBERTa base focal loss | 0.727833 | 0.699488 | 0.706 | 0.713 |
| 134-Tweet-Train-3Fold-roBERTa base lr1e5 | 0.682733 | 0.665053 | 0.699 | 0.706 |
| 135-Tweet-Train-3Fold-roBERTa base lr1e4 | 0.711237 | 0.662831 | 0.702 | 0.707 |
| 136-Tweet-Train-5Fold-roBERTa base SGD | 0.543266 | 0.527700 | 0.696 | 0.701 |
| 137-Tweet-Train-5Fold-roBERTa base Adam | 0.747361 | 0.702654 | 0.706 | 0.713 |
| 138-Tweet-Train-5Fold-roBERTa base Conv | 0.743691 | 0.703910 | 0.708 | 0.714 |
| 139-Tweet-Train-3Fold-roBERTa base step exponential | 0.741126 | 0.705451 | 0.709 | 0.713 |
| 140-Tweet-Train-3Fold-roBERTa base AVG 4 separeted heads | 0.739654 | 0.702837 | 0.711* | 0.710 |
| 141-Tweet-Train-3Fold-roBERTa base AVG 4 separeted heads2 | 0.742636 | 0.702812 | 0.710 | 0.713 |
| 142-Tweet-Train-3Fold-roBERTa base MAX 4 separeted heads | 0.737619 | 0.703859 | 0.708 | 0.712 |
| 143-Tweet-Train-3Fold-roBERTa base MAX 4 separeted heads2 | 0.741004 | 0.707042 | 0.708 | 0.715 |
| 144-Tweet-Train-3Fold-roBERTa base sentiment head | 0.727972 | 0.694650 | 0.708 | ??? |
| 145-Tweet-Train-3Fold-roBERTa base sentiment head2 | 0.737839 | 0.708187 | 0.705 | 0.711 |
| 146-Tweet-Train-1Fold-roBERTa base subtract | 0.741861 | 0.708988 | 0.704 | 0.710 |
| 147-Tweet-Train-5Fold-roBERTa base Subtract RAdam | 0.726594 | 0.700326 | 0.706 | 0.712 |
| 148-Tweet-Train-5Fold-roBERTa base Subtract | 0.731303 | 0.702731 | 0.709 | 0.711 |
| 149-Tweet-Train-5Fold-roBERTa base Subtract smooth | 0.737801 | 0.703789 | 000 | ??? |
| 150-Tweet-Train-5Fold-roBERTa base smooth02 optmiz | 0.743141 | 0.705264 | 0.710 | 0.715 |
| 151-Tweet-Train-5Fold-roBERTa base smooth02 regula | 0.743971 | 0.703925 | 0.709 | 0.713 |
| 152-Tweet-Train-5Fold-roBERTa base MAX 4 layers | 0.728650 | 0.703601 | 000 | ??? |
| 153-Tweet-Train-5Fold-roBERTa base RMSprop | 0.739308 | 0.704772 | 000 | ??? |
| 154-Tweet-Train-3Fold-roBERTa base predict mask | 0.420923 | 0.196249 | 000 | ??? |
| 155-Tweet-Train-3Fold-roBERTa base use balanced sequential | 0.760306 | 0.728728 | 0.708 | 0.712 |
| 156-Tweet-Train-3Fold-roBERTa base use balanced sequential2 | 0.778746 | 0.706882 | 0.706 | 0.712 |
| 157-Tweet-Train-3Fold-roBERTa base use balanced sequential3 | 0.786100 | 0.703417 | 0.709 | 0.711 |
| 158-Tweet-Train-5Fold-roBERTa base 64 | 0.768491 | 0.707071 | 0.712 | 0.713 |
| 159-Tweet-Train-5Fold-roBERTa base 108 | 0.738304 | 0.699947 | 0.710 | 0.710 |
| 160-Tweet-Train-5Fold-roBERTa base 113 exp1 | 0.739509 | 0.700806 | 0.714 | 0.714 |
| 161-Tweet-Train-5Fold-roBERTa base 113 exp2 | 0.742949 | 0.702880 | 0.712 | 0.713 |
| 162-Tweet-Train-5Fold-roBERTa base 113 exp3 | 0.743299 | 0.704003 | 0.712 | 0.714 |
| 163-Tweet-Train-10Fold-roBERTa base 91 | 0.733822 | 0.705542 | 0.708 | 0.717 |
| 164-Tweet-Train-5Fold-roBERTa base 91 exp1 | 0.739160 | 0.703982 | 0.710 | 0.711 |
| 165-Tweet-Train-5Fold-roBERTa base 91 exp2 | 0.749831 | 0.704440 | 0.712 | 0.713 |
| 166-Tweet-Train-5Fold-roBERTa base 91 exp3 | 0.740047 | 0.705059 | 0.710 | 0.712 |
| 167-Tweet-Train-5Fold-roBERTa balanced finetune | 0.725405 | 0.702960 | 0.705 | 0.709 |
| 168-Tweet-Train-5Fold-roBERTa balanced finetune2 | 0.745230 | 0.707179 | 0.712 | 0.714 |
| 169-Tweet-Train-5Fold-roBERTa balanced pretrain | 0.742935 | 0.706787 | 0.711 | 0.714 |
| 170-Tweet-Train-5Fold-roBERTa base no QA sentiment head | 0.745585 | 0.689484 | 000 | ??? |
| 171-Tweet-Train-5Fold-roBERTa base no QA sentiment head step | 0.732168 | 0.691242 | 0.695 | 0.700 |
| 172-Tweet-Train-5Fold-roBERTa base no QA sentiment head2 | 0.698831 | 0.674309 | 000 | ??? |
| 173-Tweet-Train-5Fold-roBERTa noQA | 0.658314 | 0.618103 | 000 | ??? |
| 174-Tweet-Train-5Fold-roBERTa noQA lbl smoothing02 | 0.660750 | 0.619471 | 000 | ??? |
| 175-Tweet-Train-5Fold-roBERTa base no QA | 0.681384 | 0.618506 | 000 | ??? |
| 176-Tweet-Train-5Fold-roBERTa BiLSTM dense head | 0.749294 | 0.703882 | 0.710 | 0.711 |
| 177-Tweet-Train-5Fold-roBERTa single pred | 0.643046 | 0.631736 | 000 | ??? |
| 178-Tweet-Train-5Fold-roBERTa BiLSTM TD head | 0.729426 | 0.704603 | 000 | ??? |
| 179-Tweet-Train-5Fold-roBERTa LSTM TD head | 0.731912 | 0.704254 | 0.706 | 0.710 |
| 180-Tweet-Train-5Fold-roBERTa BiLSTM TD head 04dro | 0.732489 | 0.705208 | 0.704 | 0.711 |
| 181-Tweet-Train-5Fold-roBERTa BiLSTM TD head lbl02 | 0.735264 | 0.706335 | 0.708 | 0.715 |
| 182-Tweet-Train-5Fold-roBERTa CNN BiLSTM TD head | 0.735131 | 0.704615 | 000 | ??? |
| 183-Tweet-Train-5Fold-roBERTa 113 sam_weight len64 | 0.745911 | 0.704897 | 0.709 | 0.713 |
| 184-Tweet-Train-5Fold-roBERTa base no QA BiGRU | 0.734154 | 0.694102 | 000 | ??? |
| 185-Tweet-Train-5Fold-roBERTa 113 seq_len64 | 0.740471 | 0.700863 | 0.706 | 0.710 |
| 186-Tweet-Train-5Fold-roBERTa 113 seq_len64 lbl02 | 0.754793 | 0.704994 | 0.707 | 0.712 |
| 187-Tweet-Train-5Fold-roBERTa seq_len64 hidden 11 | 0.732782 | 0.705720 | 000 | ??? |
| 188-Tweet-Train-5Fold-roBERTa seq_len64 hidden 08 | 0.736657 | 0.704568 | 000 | ??? |
| 189-Tweet-Train-5Fold-roBERTa top public | 0.752028 | 0.702691 | 0.709 | 0.714 |
| 190-Tweet-Train-5Fold-roBERTa subtract | 0.736706 | 0.704861 | 0.705 | 0.714 |
| 191-Tweet-Train-5Fold-roBERTa average | 0.730423 | 0.702361 | 0.706 | 0.711 |
| 192-Tweet-Train-5Fold-roBERTa subtract2 | 0.734657 | 0.705336 | 0.709 | 0.714 |
| 193-Tweet-Train-5Fold-roBERTa average2 | 0.731477 | 0.706370 | 0.706 | 0.712 |
| 194-Tweet-Train-5Fold-roBERTa custom loss | 0.738059 | 0.707295 | 0.708 | 0.714 |
| 195-Tweet-Train-5Fold-roBERTa seq_len64 hidden 11 warmup | 0.750013 | 0.706194 | 0.709 | 0.715 |
| 196-Tweet-Train-5Fold-roBERTa seq_len64 hidden 08 warmup | 0.757281 | 0.704768 | 0.708 | 0.714 |
| 197-Tweet-Train-5Fold-roBERTa clean | 0.772706 | 0.723208 | 0.710 | 0.717 |
| 198-Tweet-Train-5Fold-roBERTa cleaner | 0.763569 | 0.723412 | 0.714 | 0.718 |
| 199-Tweet-Train-5Fold-roBERTa batch 128 | 0.762430 | 0.723863 | 0.711 | 0.716 |
| 200-Tweet-Train-5Fold-roBERTa reference | 0.766115 | 0.725589 | 0.711 | 0.715 |
| 201-Tweet-Train-5Fold-roBERTa reference2 | 0.747819 | 0.721755 | 0.710 | 0.714 |
| 202-Tweet-Train-5Fold-roBERTa label smooth01 | 0.762369 | 0.723491 | 0.710 | 0.717 |
| 203-Tweet-Train-5Fold-roBERTa reference cleaner | 0.760590 | 0.720591 | 0.714 | 0.717 |
| 204-Tweet-Train-5Fold-roBERTa 160 | 0.763995 | 0.720548 | 0.710 | 0.715 |
| 205-Tweet-Train-5Fold-roBERTa 91 | 0.768056 | 0.722643 | 0.709 | 0.716 |
| 206-Tweet-Train-5Fold-roBERTa spatial dropout | 0.759113 | 0.723198 | 0.709 | 0.715 |
| 207-Tweet-Train-5Fold-roBERTa polar pretrain | 0.783628 | 0.722201 | 0.712 | 0.715 |
| 208-Tweet-Train-5Fold-roBERTa polar fine-tune | 0.801826 | 0.721462 | 0.714 | 0.717 |
| 209-Tweet-Train-5Fold-roBERTa polar train | 0.592592 | 0.544801 | 0.711 | 0.715 |
| 210-Tweet-Train-5Fold-roBERTa polar pretrain longer | 0.780583 | 0.722432 | 0.710 | 0.715 |
| 211-Tweet-Train-5Fold-roBERTa custom loss hidden11 | 0.762375 | 0.725135 | 0.710 | 0.717 |
| 212-Tweet-Train-5Fold-roBERTa custom loss | 0.757340 | 0.725749 | 0.706 | 0.711 |
| 213-Tweet-Train-5Fold-roBERTa sample_weight_x2 | 0.761448 | 0.724150 | 0.709 | 0.716 |
| 214-Tweet-Train-5Fold-roBERTa sample_weight_x5 | 0.766376 | 0.723185 | 0.710 | 0.717 |
| 215-Tweet-Train-5Fold-roBERTa sample_weight_x10 | 0.769963 | 0.724914 | 0.714 | 0.716 |
| 216-Tweet-Train-5Fold-roBERTa double dense | 0.761275 | 0.722420 | 0.711 | 0.716 |
| 217-Tweet-Train-5Fold-roBERTa mask and span2 | 0.763933 | 0.724515 | ??? | ??? |
| 218-Tweet-Train-5Fold-roBERTa hidden_11 reference | 0.759171 | 0.723426 | 0.711 | 0.716 |
| 219-Tweet-Train-5Fold-roBERTa mask and span | 0.763956 | 0.726043 | 0.713 | 0.716 |
| 220-Tweet-Train-5Fold-roBERTa mask and span3 | 0.753132 | 0.722623 | 0.710 | 0.716 |
| 221-Tweet-Train-5Fold-roBERTa HF cosine wr long | 0.762254 | 0.724794 | 0.714 | 0.717 |
| 222-Tweet-Train-5Fold-roBERTa split | 0.756152 | 0.723301 | 000 | ??? |
| 223-Tweet-Train-5Fold-roBERTa word-level | 0.767455 | 0.715359 | 000 | ??? |
| 224-Tweet-Train-5Fold-roBERTa mask and span cleanL | 0.750229 | 0.717892 | 0.694 | 0.699 |
| 225-Tweet-Train-5Fold-roBERTa word-level2 | 0.765911 | 0.719197 | 0.697 | 0.698 |
| 226-Tweet-Train-5Fold-BERT_base word-level2 | 0.749784 | 0.682228 | 000 | ??? |
| 227-Tweet-Train-5Fold-BERT_large_squad word-level2 | 0.789670 | 0.704432 | 000 | ??? |
| 228-Tweet-Train-5Fold-roBERTa reference HF | 0.758571 | 0.723612 | 0.716 | 0.715 |
| 229-Tweet-Train-5Fold-roBERTa reference HF exp2 | 0.758997 | 0.723812 | 0.713 | 0.717 |
| 230-Tweet-Train-5Fold-roBERTa reference HF exp3 | 0.761405 | 0.725496 | 0.711 | 0.717 |
| 231-Tweet-Train-5Fold-roBERTa reference HF SpatialDropout | 0.766921 | 0.726637 | 000 | ??? |
| 232-Tweet-Train-5Fold-roBERTa reference HF hidden11 | 0.766436 | 0.726896 | 000 | ??? |
| 233-Tweet-Train-5Fold-roBERTa reference HF hidden11 | 0.757282 | 0.725199 | 000 | ??? |
| 234-Tweet-Train-5Fold-roBERTa reference HF custom loss | 0.760507 | 0.726565 | 0.714 | 0.717 |
| 235-Tweet-Train-5Fold-roBERTa ref HF clean lbl | 0.753422 | 0.723600 | 0.701 | 0.705 |
| 236-Tweet-Train-5Fold-roBERTa reference HF no bias | 0.762103 | 0.726897 | 0.711 | 0.717 |
| 237-Tweet-Train-5Fold-roBERTa HF ref label | 0.760864 | 0.722933 | 000 | ??? |
| 238-Tweet-Train-5Fold-roBERTa HF SWA cosine wr long | 0.769773 | 0.727015 | 0.715 | 0.718 |
| 239-Tweet-Train-5Fold-roBERTa HF cosine wr | 0.759788 | 0.724841 | 0.716 | 0.715 |
| 240-Tweet-Train-5Fold-roBERTa 96 HF ref label | 000 | 000 | 0.716 | 0.715 |
| 241-Tweet-Train-5Fold-roBERTa_large reference HF | 0.761508 | 0.724407 | 000 | ??? |
| 242-Tweet-Train-5Fold-roBERTa 92 ref HF | 0.748715 | 0.711352 | 0.716 | 0.717 |
| 243-Tweet-Train-5Fold-roBERTa HF AdamW TF | 0.765577 | 0.725971 | 0.714 | 0.718 |
| 244-Tweet-Train-5Fold-roBERTa HF OneCycle LR | 0.765828 | 0.726872 | 0.718 | 0.718 |
| 245-Tweet-Train-5Fold-roBERTa HF OneCycle LR | 0.757211 | 0.723926 | 0.712 | 0.714 |
| 246-Tweet-Train-5Fold-roBERTa HF OneCycle LR exp2 | 0.767726 | 0.727213 | 0.714 | 0.718 |
| 247-Tweet-Train-5Fold-roBERTa HF OneCycle LR exp3 | 0.760594 | 0.722471 | 0.712 | 0.717 |
| 248-Tweet-Train-5Fold-roBERTa OneCycle 03 lbl smoothing | 0.763896 | 0.726457 | 0.714 | 0.718 |
| 249-Tweet-Train-5Fold-roBERTa OneCycle LR Hidden11 | 0.763594 | 0.726129 | 0.714 | 0.718 |
| 250-Tweet-Train-5Fold-roBERTa OneCycle LR 025smoot | 0.763121 | 0.726307 | 0.716 | 0.719 |
| 251-Tweet-Train-5Fold-roBERTa OneCycle cosine | 0.763432 | 0.727046 | 0.714 | 0.717 |
| 252-Tweet-Train-5Fold-roBERTa 96 OneCycle LR | 0.762492 | 0.726418 | 0.716 | 0.717 |
| 253-Tweet-Train-5Fold-roBERTa 96 OneCycle LR dirty | 0.747433 | 0.709368 | 0.713 | 0.716 |
| 254-Tweet-Train-5Fold-roBERTa 96 OneCycle LR PT | 000 | 000 | 0.712 | 0.713 |
| 255-Tweet-Train-5Fold-roBERTa OneCycle hold | 0.764382 | 0.726586 | 0.713 | 0.719 |
| 256-Tweet-Train-5Fold-roBERTa OneCycle BCE | 0.757981 | 0.727300 | 0.713 | 0.714 |
| 257-Tweet-Train-5Fold-roBERTa OneCycle RAdam | 0.751558 | 0.723434 | 0.712 | 0.716 |
| 258-Tweet-Train-5Fold-roBERTa OneCycle Custom loss | 0.758095 | 0.726239 | 0.716 | 0.717 |
| 259-Tweet-Train-5Fold-roBERTa mask and span OneCycle | 0.767035 | 0.726512 | 0.715 | 0.716 |
| 260-Tweet-Train-5Fold-roBERTa mask and span OneCycle2 | 0.766930 | 0.725839 | 0.715 | 0.719 |
| 261-Tweet-Train-5Fold-roBERTa AVG last4 OneCycle | 0.773650 | 0.727990 | 0.717 | 0.717 |
| 262-Tweet-Train-5Fold-roBERTa MAX last4 OneCycle | 0.771099 | 0.728136 | 0.715 | 0.717 |
| 263-Tweet-Train-5Fold-roBERTa AVG last4 sep OneCycle | 0.770623 | 0.726052 | 0.713 | 0.718 |
| 264-Tweet-Train-5Fold-roBERTa MAX last4 sep OneCycle | 0.768826 | 0.727114 | 0.713 | 0.716 |
| 265-Tweet-Train-5Fold-roBERTa subtract residual | 0.764019 | 0.726339 | 000 | ??? |
| 266-Tweet-Train-5Fold-roBERTa subtract residual2 | 0.767326 | 0.725516 | 000 | ??? |
| 267-Tweet-Train-5Fold-roBERTa mask and custom loss one cycle | 0.763638 | 0.726076 | 0.713 | 0.716 |
| 268-Tweet-Train-5Fold-roBERTa mask and custom loss cosine wr | 0.768143 | 0.726186 | 000 | ??? |
| 269-Tweet-Train-5Fold-roBERTa Jaccard | 0.766834 | 0.726114 | 000 | ??? |
| 270-Tweet-Train-5Fold-roBERTa Jaccard cosine wr | 0.766603 | 0.726172 | 000 | ??? |
| 271-Tweet-Train-5Fold-roBERTa token count | 0.754890 | 0.723502 | 0.715 | 0.716 |
| 272-Tweet-Train-5Fold-roBERTa mask jac token cosine wr | 0.769455 | 0.726670 | 0.715 | 0.718 |
| 273-Tweet-Train-5Fold-roBERTa mask jac token oneclycle | 0.744883 | 0.715413 | 000 | ??? |
| 274-Tweet-Train-5Fold-roBERTa mask jac token cosine wr | 0.774347 | 0.726699 | 000 | ??? |
| 275-Tweet-Train-5Fold-roBERTa AVG last4 OneCy exp2 | 0.768859 | 0.726668 | 0.714 | 0.716 |
| 276-Tweet-Train-5Fold-roBERTa AVG last4 OneCy exp3 | 0.771440 | 0.724640 | 0.715 | 0.718 |
| 277-Tweet-Train-5Fold-roBERTa OneCycle Custom exp2 | 0.759392 | 0.723851 | 0.713 | 0.716 |
| 278-Tweet-Train-5Fold-roBERTa OneCycle Custom exp3 | 0.765024 | 0.727252 | 0.715 | 0.717 |
| 279-Tweet-Train-5Fold-roBERTa AVG last4 custom los | 0.764935 | 0.726904 | 0.714 | 0.718 |
| 280-Tweet-Train-5Fold-roBERTa OneCycle clean jac | 0.747617 | 0.710255 | 0.710 | 0.716 |
| 281-Tweet-Train-7Fold-roBERTa OneCycle | 0.765007 | 0.726303 | 0.717 | 0.717 |
| 282-Tweet-Train-10Fold-roBERTa OneCycle | 0.719805 | 0.683172 | 0.717 | 0.718 |
| 283-Tweet-Train-5Fold-roBERTa OneCycle label2 | 0.748561 | 0.713372 | 0.696 | 0.702 |
| 284-Tweet-Train-5Fold-roBERTa Adam L1 reg cosineWR | 0.765440 | 0.725476 | 0.716 | 0.718 |
| 285-Tweet-Train-5Fold-roBERTa Adam L1 reg | 0.758242 | 0.725879 | 0.714 | 0.717 |
| 286-Tweet-Train-5Fold-roBERTa 96 OneCycle LR exp2 | 0.761888 | 0.725264 | 0.715 | 0.717 |
| 287-Tweet-Train-5Fold-roBERTa 96 OneCycle LR exp3 | 0.766480 | 0.726240 | 0.716 | 0.719 |
| 288-Tweet-Train-5Fold-roBERTa 96 OneCycle beta1 | 0.765305 | 0.724924 | 0.714 | 0.717 |
| 289-Tweet-Train-7Fold-roBERTa 96 OneCycle LR | 0.764648 | 0.727013 | 0.714 | 0.717 |
| 290-Tweet-Train-10Fold-roBERTa 96 OneCycle LR | 0.764426 | 0.727047 | 0.713 | 0.718 |
