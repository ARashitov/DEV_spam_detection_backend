FROM python:3.8.5

LABEL MAINTAINER="Adil Rashitov adil.rashitov.98@gmail.com"
WORKDIR /application

# 1. Update packages
RUN apt-get update

# 2. Passing application inside
COPY app ./app
COPY data ./data
COPY models ./models
COPY tests ./tests

RUN ls app
ENV MODEL=/application/models/svm_v_0_0_2.pkl
ENV VOCABULARY_PATH=/application/data/vocabulary.csv

# 3. Install requirements
COPY Docker/Requirements.txt ./
RUN pip3 install --upgrade pip \
    && pip3 install wheel \
    && pip3 install -r Requirements.txt \
    && rm Requirements.txt

# 4. Passing entry-point
COPY Docker/docker-entrypoint.sh ./
ENTRYPOINT /bin/bash /application/docker-entrypoint.sh

EXPOSE 8000/tcp