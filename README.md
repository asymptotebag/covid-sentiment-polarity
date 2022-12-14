# Extracting Sentiment-Polarizing Tokens from COVID-19 Topic Tweets

*MIT 6.864 Fall 2022 Final Project: Alice Chen, Keenly Chuang, Emily Jiang, Filip Ryzner*

Our research investigates the polarization of public sentiment surrounding the COVID-19 pandemic and related public health guidelines. In particular, we develop a method to isolate polarizing terms, or words that are important in influencing both the positive and negative sentiment of a text. We use the well-studied, lightweight transformer model DistilBERT to train a multiclass sentiment classifier on a dataset of pandemic-related tweets. We then design and implement a novel method of interpreting self-attention weights to quantify relative polarization between terms. For each word, we analyze the self-attention weights for each tweet it appears in, using KL-divergence to isolate the most informative self-attention head per layer. We compute the variance in self-attention scores across tweets to compare the polarity of different words. Overall, our self-attention interpretation method isolates many pandemic-related terms as most polarizing, with words relating to quarantine, vaccines, and historically controversial COVID-19 drugs showing significant contribution toward determining a tweet's sentiment in both positive and negative directions.


**Contents of the code repository:**
  - `data` - folder containing all required data to run the code
  - `preprocess_data.ipynb` - notebook containing the code for data preparation
  - `baseline.ipynb` - code to obtain the baseline results
  - `transformer.ipynb` - main code section, transformer training and results generation
  - `data_visualization.ipynb` - code used for visual data analysis
  - `report.pdf` - our final research report

**Order of execution to replicate the results:**
  1. Run `preprocess_data.ipynb` to pre-process and save the tweet data used for our analysis. This part of the code performs general data cleaning, including hashtag removal, account references (mentions) removal, and lemmatization.
  2. Run `baseline.ipynb` to obtain the baseline results with the pre-processed data.
  3. Run sections 0, 1, 3, 4 of `transformer.ipynb` to replicate our results using the transformer. Section 2 of this notebook contains the training of a binary classifier, which we did not use in our final results.
  4. Optional: Visualize datasets using `data_visualization.ipynb`.

Should you have any questions about the code, please reach out to one of the authors:
  - ayjchen@mit.edu
  - kschuang@mit.edu
  - emji@mit.edu
  - ryznerf@mit.edu
