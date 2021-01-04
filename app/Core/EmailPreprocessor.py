import re
from nltk.stem import PorterStemmer


class EmailPreprocessor:

    def __init__(self, vocabulary, email_content):
        """
            Args:
            * vocabulary (pd.DataFrame): List of words
        """
        self.vocabulary = vocabulary
        self.email_content = email_content

    def preprocess_content(self):
        """
            * Converts to lower case
            * symbols -> missing empty char
            * [0-9]+  -> Number
            * URLS -> httpaddr
            * email -> emailaddr
            * $ sign -> dollar
            * Remove non-character
        """
        email_content = self.email_content
        email_content = email_content.lower()
        email_content = re.sub(r'<[^<>]+>', ' ', email_content)
        email_content = re.sub(r'[0-9]+', 'number', email_content)
        email_content = re.sub(r'(http|https)://[^\s]*',
                               'httpaddr', email_content)
        email_content = re.sub(r'[^\s]+@[^\s]+', 'emailaddr', email_content)
        email_content = re.sub(r'[$]+', 'dollar', email_content)
        email_content = re.sub('[^0-9a-zA-Z ]+', '', email_content)
        self.email_content = email_content

    def preprocess_Porter_stemmer(self):
        """
            Performs Porter stemming over entire email content
            and stores email contenat as list<str>.
        """
        email_content = self.email_content
        email_content = email_content.split(' ')
        email_content = list(map(lambda func, x: func(x),
                                 [PorterStemmer().stem]*len(email_content),
                                 email_content))
        self.email_content = email_content

    def tokenize(self):
        """
            stores into word_vec presence in vocabulary
            Example:
                [0, 1...1] where amount == lenght of vocabulary
        """
        email_content = self.email_content
        vocab = self.vocabulary.copy()
        vocab['is_present'] = 0
        vocab.loc[vocab.word.isin(email_content),
                  'is_present'] = 1
        self.tokens = vocab.T.values[1]

    def preprocess_email(self):
        self.preprocess_content()
        self.preprocess_Porter_stemmer()
        self.tokenize()
        return self.tokens
