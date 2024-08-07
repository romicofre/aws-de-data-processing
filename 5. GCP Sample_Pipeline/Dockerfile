# build this Docker image with:
# docker build .

# set base image (host OS)
FROM python:3.8-slim-buster

# set the working directory in the container
WORKDIR /pubsub

# copy the content of the local src directory to the working directory
COPY pubsub-suscriber/ .

# install dependencies
RUN pip install -r requirements.txt

# set environment variables
ENV GOOGLE_APPLICATION_CREDENTIALS=creds.json
ENV TIMEOUT=10

# command to run on container start
CMD [ "python", "./main.py" ]