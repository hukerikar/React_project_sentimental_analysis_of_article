import nltk
import re
import newspaper
import requests

from newspaper import Article
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy
from textstat.textstat import textstatistics
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
def analyze_keywords(url):
    article_name = Article(url, language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    keywords = article_name.keywords
    print("Keywords:", keywords) 
    return keywords

def analyze_summary(url):
    article_name = Article(url, language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    summary = article_name.summary
    clean_summary = summary.replace('\n', ' ')

    return clean_summary


def load_and_preprocess_article(url):
    article_name = Article(url, language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    article = article_name.text
    text_tokens = word_tokenize(article)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    final_article = " ".join(tokens_without_sw)
    return final_article

def pos_score(final_article):
    score = SentimentIntensityAnalyzer().polarity_scores(final_article)
    return score['pos']

def negative_score(final_article):
    score = SentimentIntensityAnalyzer().polarity_scores(final_article)
    return score['neg']

def getSubjectivity(final_article):
   return TextBlob(final_article).sentiment.subjectivity

def getPolarity(final_article):
   return TextBlob(final_article).sentiment.polarity

def word_count(final_article):
    sentences = break_sentences(final_article)
    words = 0
    for sentence in sentences:
        words += len([token for token in sentence])
    return words
 
def sentence_count(final_article):
    sentences = break_sentences(final_article)
    return len(sentences)

def syllables_count(word):
    return textstatistics().syllable_count(word)

def break_sentences(final_article):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(final_article)
    return list(doc.sents)

def avg_sentence_length(final_article):
    words = word_count(final_article)
    sentences = sentence_count(final_article)
    average_sentence_length = float(words / sentences)
    return average_sentence_length

def complex_words(final_article):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(final_article)
    words = []
    sentences = break_sentences(final_article)
    for sentence in sentences:
        words += [str(token) for token in sentence]
    complex_words_set = set()
    for word in words:
        syllable_count = syllables_count(word)
        if word not in nlp.Defaults.stop_words and syllable_count >= 2:
            complex_words_set.add(word)
    return len(complex_words_set)

def Avg_num_of_words_per_sentence(final_article):
    words = final_article.split()
    sentences = sentence_count(final_article)
    average_words = len(words) / sentences
    return average_words

def Avg_word_length(final_article):
    words = final_article.split()
    res = sum(map(len, words)) / len(final_article)
    return res

def percentage_complex_word(final_article):
    per_diff_words = (complex_words(final_article) / word_count(final_article) * 100)
    return per_diff_words

def fog_index(final_article):
    grade = 0.4 * (avg_sentence_length(final_article) + percentage_complex_word(final_article))
    return grade

def personal_pronous(final_article):
    pronounRegex = re.compile(r'I|we|my|ours|us', re.I)
    pronouns = pronounRegex.findall(final_article)
    result = len(pronouns)
    return result

def syllable_count_per_word(final_article):
    res = syllables_count(final_article) / word_count(final_article)
    return res

def analyze_Description(final_article):
    result = {
        "positive_score": pos_score(final_article),
        "negative_score": negative_score(final_article),
        "polarity_score": getPolarity(final_article),
        "subjectivity_score": getSubjectivity(final_article),
        "average_sentence_length": avg_sentence_length(final_article),
        "percentage_of_complex_words": percentage_complex_word(final_article),
        "fog_index": fog_index(final_article),
        "average_word_count_per_sentence": Avg_num_of_words_per_sentence(final_article),
        "complex_word_count": complex_words(final_article),
        "word_count": word_count(final_article),
        "syllable_count_per_word": syllable_count_per_word(final_article),
        "count_of_personal_pronouns": personal_pronous(final_article),
        "average_word_length": Avg_word_length(final_article),
    }
    return result



def analyze_sentiment(final_article):
    pos_score_val = pos_score(final_article)
    neg_score_val = negative_score(final_article)
    
    sentiment = 'positive' if pos_score_val > neg_score_val else 'negative'
    
    result = {
        'sentiment': sentiment,
        'positive_score': pos_score_val,
        'negative_score': neg_score_val,
    }
    
    return result
