# Metis Data Science Bootcamp | Project 4

## Investigating the Impact of Twitter Bots on the U.S. Presidential Election's Political Discourse 

For a good summary of this project, check out my blog [here](https://edubu2.medium.com/investigating-the-impact-of-twitter-bots-on-the-2020-u-s-elections-political-discourse-173638f4b95c)

![Biden vs. Trump](https://github.com/edubu2/metis-project4/blob/main/etc/biden_trump_photo.jpg)
___
## Tech Stack

* Python3 Libraries
  * Chris Doenlen's `Twitter Bot-or-Not` XGBoost Classifier model
    * provides probability of each author (Twitter user) in our document corpus with a probability of being a bot
      * More on this in the next section
  * `numpy` & `pandas`
  * `matplotlib` & `seaborn`
  * `scikit-learn`
    * Count and TF/IDF vectorizers
    * NMF, LDA, LSA clustering algorithms
  * `pickle` & `csv` (data serialization)
  * `Twint` (Twitter scraping library)
    * No limits, however the module seems to be loosely maintained and the results can be buggy.
  * `Tweepy` (Twitter's official API)
    * **NOTE**: Tweepy requires a Twitter Developer API key. There is a [request process](https://developer.twitter.com/en) that can take a couple of days.
    * Requests are limited to 300 per 15 minutes, so querying large amounts of data is also time consuming.
  * `NLTK` (natural language toolkit)
    * `tweet_tokenize`, `WordLemmatizer`, stop words, English word list

* Other tools
  * `GCP` Compute Engine (for deep learning-optimized virtual machine)
    * Debian Linux
    * `Filezilla`
  * `Tableau` Public Edition (for data visualization)
___
## Navigating This Repository

The file structure is explained as follows:

* `/code/`: contains all code used for the project. If you are planning on reproducing locally, run the below notebooks (in order). You may need to create empty directories and install any necessary libraries along the way.
  * `scrape_bot_probas.ipynb`:
    * Use this only to expand on `/data/user_stats.csv` and classify more users (In addition to the 30k already there).
    * uses `bot_predict.py`, which contains functions to be imported into notebooks to predict each user as bot (True/False)
      * Big thanks to Kris Doenlen ([@scrapfishies](https://github.com/scrapfishies)) for allowing & encouraging me to use his model in this project
      * I was cloned the original code from his [GitHub repository](https://github.com/scrapfishies/twitter-bot-detection) and modified to work for my project
  * `get_tweets.ipynb`: this notebook uses the `Twint` Python library to pull all tweets from Oct 1 - Nov 2, 2020 that contain the words `trump` and `biden`
  * `aggregate_tweets.ipynb`: combines the .csv files generated from `clean_tweets.ipynb` into one DataFrame
  * `clean_tweets.ipynb`: pre-processes tweets (stop word removal, n-grams, lemmatization)
  * `topic_modeling.ipynb`: implement TF/IDF\* and NMF\*\* algorithms in order to create 30 topic clusters 
    * \* Term Frequency * Inverse Document Frequency
    * \*\* Non-Negative Matrix Factorization
  * `topic_naming.ipynb`: analysis of our topic clusters & assigning names to each cluster
  * `bots.ipynb`: pulls user-level bot probabilities into the tweets data and analyze the results
    * data visualizations with `matplotlib` and `seaborn` here
  * `/code/custom_words/` contains three files:
    * `bigrams.py`: contains a list of tuples that combine multi-word phrases into one term
      * example: `(r"white house", "whitehouse")` will replace all occurrences of 'white house' with 'whitehouse' (all words pre-processed before this is implemented)
    * `more_words.py`: additional words (no need to repeat from `bigrams`) that should not be filtered out during pre-processing
    * `stop_words.py`: additional stop words that should be excluded during pre-processing

* `/data/` contains the raw data files generated from the various files in `code/`
* `/etc/` contains miscellaneous project resources
  * `topic_words.xls` contains the top words associated with each topic (if interested)

___
## Topics

Here are the resulting topics from NMF matrix defactorization (*k=30*)

![Tableau](https://github.com/edubu2/metis-project4/blob/main/etc/topic_viz.png)

* The empty boxes in the above figure are as follows:
  * #breakingnews, #healthcareforall, #debate, #registertovote

For more information about how these topics were generated, and some of the most relevant Tweets for each topic, check out my blog post [here](https://edubu2.medium.com/investigating-the-impact-of-twitter-bots-on-the-2020-u-s-elections-political-discourse-173638f4b95c)

