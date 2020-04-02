# Tweet Sentiment Extraction - Planning
 
## Working cycle:
1. Read competition information and relevant content to feel comfortable with the problem. Create a hypothesis based on the problem.
2. Initial data exploration to feel comfortable with the problem and the data.
3. Build the first implementation (baseline).
4. Loop through [Analyze -> Approach(model) -> Implement -> Evaluate].

## 1. Literature review (read some kernels and relevant content related to the competition).
- ### Relevant content:
  - [content 1]()

- ### GitHub:
  - [Huggingface transformers](https://github.com/huggingface/transformers)
  - [Hggingface tokenizers](https://github.com/huggingface/tokenizers/tree/master/bindings/python)

- ### Papers:
  - [paper 1]()

- ### Videos:
  - [video 1]()

- ### Kernels:
  - [kernel 1]()

- ### Discussions:
  - [discussion 1]()
 
- ### Insights:
  - #### Positive Insights
    - The metric is calculated on lowercased text, so lowercasing all texts as preprocess is viable without drawbacks
  
  - #### Negative Insights
    - Some of the labels contain only a fraction of the original text words like the bellow, thisway predict on character level may be better
      - `text`: `i'm actually starting to quite like lily allen and her music, to be honest.`
      - `selected_text`: `o quite like lily allen and her music, to be honest.`
    - Both `text` and `selected_text` can contain HTML tags
    - Train set have null label
