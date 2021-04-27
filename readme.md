# Tw33t

A simple Flask + Vue app that communicates with Twitter API when user input a Twitter handle and logs info about each search.

## Get Twitter API

Make sure to get Twitter API before start, and add it into file ~/app/tw33t/views/settings.py

TOKEN = ''

TOKEN_SECRET = ''

CONSUMER_KEY = ''

CONSUMER_SECRET = ''

## How to run

Build the docker image and start server:

```
docker build -t cubicasa-developer-test .
docker-compose up web
```
## UI

1. Start Screen

![Start Screen](https://i.imgur.com/tsIXUKc.png)

2. Get some latest tweets from @CasaCubi

![Result Screen](https://i.imgur.com/CAytfyk.png)
