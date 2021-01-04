import time
import pickle
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, roc_auc_score
from EmailPreprocessor import EmailPreprocessor


def predict(model, email_content, vocabulary) -> int:
    """
        Note model requires list<list(int)>

        Arguments:
            * model (scikit-learn.GridSearch): model
            * email_content (str): email string
            * vocabulary (pd.DataFrame): vocabulary

        Returns:
            * list<int>: 0 - IS NOT SPAM, 1 - IS SPAM
            example: [0, 0, .. 1]
    """
    email_prep = EmailPreprocessor(vocabulary, email_content)
    X = [email_prep.preprocess_email()]
    return model.predict(X)


def fit(TRAIN_DATA: str, TEST_DATA: str, MODEL: str, REPORT: str):
    """
        Classical fit function with next steps:
            1. Reading Train & Test matrix
            2. GRID search of SVC
            3. Report construction
            4. Model & report save

        Args:
            * TRAIN_DATA (str): path to train matrix (env var)
            * TEST_DATA (str): path to train matrix (env var)
            * MODEL (str): path to model need to be exported (env var)
            * REPORT (str): path to .csv model report file

        Outputs:
            * None
    """
    # 1. Reading Train & Test matrix
    def read_and_split_X_y(path):
        df = pd.read_csv(path)
        y = df.loc[:, ['y']].copy()
        cols = list(set(df.columns) - set(y))
        X = df.loc[:, cols].copy()
        del df
        return X, y

    X_train, y_train = read_and_split_X_y(TRAIN_DATA)
    X_test, y_test = read_and_split_X_y(TEST_DATA)

    # 2. GRID search of SVC
    parameter_candidates = [
        {'C': [10, 100, 1000], 'kernel': ['linear']},
        {'C': [10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
    ]
    start = time.time()
    roc_auc_scorer = make_scorer(roc_auc_score, greater_is_better=True,
                                 needs_threshold=True)
    model = GridSearchCV(estimator=svm.SVC(),
                         param_grid=parameter_candidates,
                         n_jobs=-1,
                         scoring=roc_auc_scorer)
    model.fit(X_train.values, np.ravel(y_train.values))
    end = time.time()

    # 3. Report construction
    report = pd.DataFrame({
        'model': 'SVC',
        'best_score': model.best_score_,
        'C': model.best_estimator_.C,
        'kernel': model.best_estimator_.kernel,
        'gamma': model.best_estimator_.gamma,
        'AUC': model.score(X_test.values, np.ravel(y_test.values)),
        'time_elapsed': end - start
    }, index=[0])

    # 4. Model & report save
    pickle.dump(model, open(MODEL, 'wb'))
    report.to_csv(REPORT, index=False)