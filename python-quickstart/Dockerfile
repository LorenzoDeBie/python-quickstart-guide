# pull official base image
FROM python:3.9.5-slim-buster

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
# RUN apt-get update && apt-get install -y --no-install-recommends netcat

# copy project
COPY . $APP_HOME

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

WORKDIR $APP_HOME/src