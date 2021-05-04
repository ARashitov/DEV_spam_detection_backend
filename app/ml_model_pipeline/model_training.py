"""
NOTE: This fit function is not used on app.
      In real world we produce model from experiments,
      Not from predetrmined function
"""
import time
import pickle
import numpy as np
import pandas as pd
from sklearn import svm
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, roc_auc_score


def fit(TRAIN_DATA: str, TEST_DATA: str, MODEL: str, REPORT: str) -> None:
    """
        NOTE: This function is not used in backed
            it is required only model export purposes

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
    model = GridSearchCV(estimator=svm.SVC(probability=True),
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


if __name__ == '__main__':
    TRAIN_DATA = '/home/atmos/Hobby/SPAM_DETECTION_BACKEND/data/TrainMatrix.csv'
    TEST_DATA = '/home/atmos/Hobby/SPAM_DETECTION_BACKEND/data/TestMatrix.csv'
    MODEL = '/home/atmos/Hobby/SPAM_DETECTION_BACKEND/models/svm_v_0_0_2.pkl'
    REPORT = '/home/atmos/Hobby/SPAM_DETECTION_BACKEND/models/svm_v_0_0_2_report.csv'
    fit(TRAIN_DATA, TEST_DATA, MODEL, REPORT)
