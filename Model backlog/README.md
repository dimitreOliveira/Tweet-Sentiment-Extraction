## Model backlog (list of the developed model and it's score)
- **Train** and **validation** are the splits using the train data from the competition.
- The competition metric is **Jaccard score**.
- **Pb Leaderboard** is the Public Leaderboard score.
- **Pv Leaderboard** is the Private Leaderboard score.

---

## Models

|Model|Train|Validation|Pb Leaderboard|Pv Leaderboard|
|-----|-----|----------|--------------|--------------|
|1-Tweet-Train-DistilBERT|0.725|0.616|000|000|
|2-Tweet-Train-DistilBERT lower|0.761|0.638|000|000|
|3-Tweet-Train-DistilBERT BCE|0.703|0.635|000|000|
|4-Tweet-Train-DistilBERT lower softmax|0.771|0.643|000|000|
|5-Tweet-Train-DistilBERT lower softmax v2|0.771|0.643|000|000|
|6-Tweet-Train-DistilBERT lower BCE v2|0.769|0.633|000|000|
|7-Tweet-Train-DistilBERT lower lower v2|0.783|0.640|000|000|
|8-Tweet-Train-DistilBERT lower AVG_MAX|0.439|0.433|000|000|
|9-Tweet-Train-BERT base uncased|0.508|0.434|000|000|
|10-Tweet-Train-BERT base uncased BCE|0.638|0.580|000|000|
|11-Tweet-Train-BERT base uncased pb|0.363|0.338|000|000|
|12-Tweet-Train-BERT base uncased pb2|0.460|0.413|000|000|
|13-Tweet-Train-DistilBERT base uncased|0.505|0.454|0.408|000|
|14-Tweet-Train-DistilBERT base uncased lbl lower|0.737|0.631|0.524|000|
|15-Tweet-Train-DistilBERT base uncased refactor|0.705|0.645|0.645|000|
|16-Tweet-Train-DistilBERT base uncased refac BCE|0.702|0.640|0.645|000|
|17-Tweet-Train-DistilBERT base uncased BCE sigmoid|0.782|0.647|0.644|000|
|18-Tweet-Train-DistilBERT base uncased Subtract|0.048|0.050|000|000|
|19-Tweet-Train-DistilBERT base uncased Sub BCE|0.374|0.368|000|000|
|20-Tweet-Train-DistilBERT base uncased Sub|0.540|0.517|000|000|
|21-Tweet-Train-DistilBERT base SparseCat|0.485|0.484|000|000|
|22-Tweet-Train-DistilBERT base SparseCat Logit|0.705|0.644|0.645|000|
|23-Tweet-Train-DistilBERT base Lbl smoothing|0.733|0.640|0.642|000|
|24-Tweet-Train-DistilBERT base Lbl smoothing2|0.733|0.641|0.640|000|
|25-Tweet-Train-DistilBERT max_len 160|0.732|0.647|0.651|000|
|26-Tweet-Train-DistilBERT what|0.661|0.590|000|000|
|27-Tweet-Train-DistilBERT no qst|0.669|0.558|000|000|
|28-Tweet-Train-DistilBERT base Normal smoothing|0.541|0.538|000|000|
|29-Tweet-Train-DistilBERT base Norm smooth Sigmoid|0.717|0.613|000|000|
|30-Tweet-Train-DistilBERT base Norm smooth Sigmoid|0.792|0.629|0.629|000|
|31-Tweet-Train-DistilBERT base Lbl smoothing BCE|0.789|0.640|0.647|000|
|32-Tweet-Train-DistilBERT base Poisson smooth|0.701|0.597|0.601|000|
|33-Tweet-Train-DistilBERT base Poisson smooth2|0.802|0.639|0.642|000|
|34-Tweet-Train-DistilBERT 2 transformers|0.763|0.636|0.637|000|
