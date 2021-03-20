import re
import pandas as pd
from nltk.stem import PorterStemmer
from sklearn.base import BaseEstimator, TransformerMixin


class EmailContentPreprocessor(BaseEstimator, TransformerMixin):
    """
        Class required to perform data preprocessing
        NLP prediction model
    """
    def __init__(self, vocabulary: pd.DataFrame):
        """
            Args:
                * vocabulary (pd.DataFrame): Model's corpus text
                                             need to be converted
        """
        self.vocabulary = vocabulary

    def __base_preprocessing(self, email_content: str) -> str:
        """
            * Converts to lower case
            * symbols -> missing empty char
            * [0-9]+  -> Number
            * URLS -> httpaddr
            * email -> emailaddr
            * $ sign -> dollar
            * Remove non-character

            Args:
                * email_content (str): Raw email content
            Returns:
                * email_content (str): Preprocessed email content
        """
        email_content = email_content.lower()
        email_content = re.sub(r'<[^<>]+>', ' ', email_content)
        email_content = re.sub(r'[0-9]+', 'number', email_content)
        email_content = re.sub(r'(http|https)://[^\s]*',
                               'httpaddr', email_content)
        email_content = re.sub(r'[^\s]+@[^\s]+', 'emailaddr', email_content)
        email_content = re.sub(r'[$]+', 'dollar', email_content)
        email_content = re.sub('[^0-9a-zA-Z ]+', '', email_content)
        return email_content

    def __preprocess_Porter_stemmer(self, email_content: str) -> str:
        """
            Performs Porter stemming over entire email content
            and stores email contenat as list<str>.

            Args:
                * email_content (str): Raw email content
            Returns:
                * email_content (str): Preprocessed email content
        """
        email_content = email_content.split(' ')
        email_content = list(map(lambda func, x: func(x),
                                 [PorterStemmer().stem]*len(email_content),
                                 email_content))
        return email_content

    def __tokenize(self, email_content: str) -> list:
        """
            stores into word_vec presence in vocabulary
            Example:
                [0, 1...1] where amount == lenght of vocabulary

            Args:
                * email_content (str): Raw email content
            Returns:
                * list<int>: Vector of word presence in vocabulary
        """
        vocab = self.vocabulary
        vocab['is_present'] = 0
        vocab.loc[vocab.word.isin(email_content),
                  'is_present'] = 1
        return list(vocab.T.values[1])

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        """
            Main function aggregating all preprocessing stages:
                1. Base preprocessing
                    * Converts to lower case
                    * symbols -> missing empty char
                    * [0-9]+  -> Number
                    * URLS -> httpaddr
                    * email -> emailaddr
                    * $ sign -> dollar
                    * Remove non-character
                2. Porter stemming
                3. Tokenization according model's vocabulary

            Args:
                * X (str): Email content

            Returns:
                * self.tokens (list<int>): vector of word
                                           presence in vocabulary
        """
        # 1. Preprocessing
        X = self.__base_preprocessing(X)
        X = self.__preprocess_Porter_stemmer(X)
        X = self.__tokenize(X)

        # 2. Wrap into list to make email content
        #    as single observation used for prediction
        X = [X]
        return X
