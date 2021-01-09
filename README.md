# MLmodelDeployment_Backend

This is hobby repository created to explore Flask framework as API creation tool for model deployment

## **About**

I was curious about deployment of ML model as api with automated model training and predicting

This project is aimed to predict if email is spam/not spam. For predicting purposes the system uses `SVM` model with `Porter stemmer` and tokenizer at the core. Prediction pipeline is entirely wrapped into `API` providing opportunity to interact.

### Tech stack

* Python3.8.5
* Docker
* flask_restful
* numpy, pandas, scikit-learn, nltk


## **Architecture**

![Architecture](diagrams/ProjectDiagrams.png)

## **Goal**

, where model will be wrapped into Flask and can be utilized using `POST` method.

## **Deployment guideline**

* Start from installing [prerequisites](https://github.com/AtmosOne/FlaskExploration/blob/main/docs/Prerequisites.md)
* Then go to [backend deployment](https://github.com/AtmosOne/FlaskExploration/blob/main/docs/Backend_deploy.md)
* Usage:
  * And Lastly checkout [API documentation](https://github.com/AtmosOne/FlaskExploration/blob/main/docs/API.md) & [Jupyter Example](https://github.com/AtmosOne/FlaskExploration/blob/main/Example/Example.ipynb)
  * *Optional*: you can deploy [frontend](https://github.com/AtmosOne/MLmodelDeployment_Backend) container of this project
