# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:35:24 2021

@author: Anuj
"""

from flask import Flask, render_template, request

from repos.exceptions import GithubApiException
from repos.api import repos_with_most_stars

app = Flask(__name__)

available_languages = ["Python", "JavaScript", "Ruby", "Java"]

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        selected_languages = available_languages
    elif request.method == 'POST':
        selected_language = request.form.getlist("languages")
    
    if request.method == 'GET':
        # Use the list of all languages
        selected_languages = available_languages
    elif request.method == 'POST':
        # Use the languages we selected in the request form
        selected_languages = request.form.getlist("languages")
    
    results = repos_with_most_stars(selected_languages)

    return render_template(
        'index.html',
        selected_languages=selected_languages,
        available_languages=available_languages,
        results=results)

@app.errorhandler(GithubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)
