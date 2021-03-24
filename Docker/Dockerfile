FROM python:3.8.5

# Dependencies
COPY ./Requirements.txt ./
RUN /usr/local/bin/python -m pip install --upgrade pip && pip3 install -r Requirements.txt && rm Requirements.txt