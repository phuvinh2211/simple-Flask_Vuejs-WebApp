from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from twitter import *
from operator import itemgetter
from tw33t.views.settings import TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET
from tw33t.views.utils import logsearch
from tw33t.views.data import DemoData
import json, requests, datetime, sys, os, uuid, re, time

'''
Twitter API Settings
'''

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


'''
Introduce a "Get tweets" route for the client and log relevant info from each search into a file.

'''
@app.route('/get_tweets/<user_screen>/', methods=['GET'])
def get_tweets(user_screen):
    if request.method == 'GET':
        # Already validate in the client side, but make sure user_screen is not null
        if user_screen.strip() == '':
            return redirect(url_for('index'))
        else:
            t = Twitter(auth=OAuth(TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

            # Just get three lastest tweets from user name, use try/except in case
            # not found any match screen_name in Twitter API (user is not exist)
            try:
                query = t.statuses.user_timeline(screen_name=user_screen, count=3)
            except:
                return jsonify([{'creation_date': '-/-/-', 'content': 'Oop!!! This user is not exist on Twitter'}])

            result = []
            for q in query:
                # Return time creation date format: Wed Mar 09 04:03:35 +0000 2011
                # We need to extract it to get needed information, split it and get index from list
                creation_date = list(itemgetter(2, 1, 5)(q['created_at'].split(' ')))
                creation_date = '/'.join(creation_date)

                content = q['text']
                result.append({'content': content, 'creation_date': creation_date})

            # Just logging for successful result
            logsearch(user_screen, result)

            return jsonify(result)

    return redirect(url_for('index'))
