from flask import g, Markup
from flask import (Blueprint, render_template, make_response, redirect, url_for, abort, request, Response)
from tw33t import app
from functools import wraps
from flask import jsonify
from twitter import *
from tw33t.views.data import DemoData
import json, requests, datetime, sys, os, uuid, re, time

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

        return jsonify(DemoData)

    return redirect(url_for('index'))
