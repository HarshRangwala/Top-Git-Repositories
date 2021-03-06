# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:23:51 2021

@author: Anuj
"""

from repos.exceptions import GithubApiException
from repos.models import GitHubRepo
import requests

GITHUB_API_URL = "https://api.github.com/search/repositories"

def create_query(languages, min_stars):
    """
    Create the query string for the GitHub search API,
    based on the minimum amount of stars for a project, and
    the provided programming languages.
    """
    
    query = " ".join(f"language:{language.strip()}" for language in languages)
    query = query + f" stars:>{min_stars}"
    return query

def repos_with_most_stars(languages, min_stars=40000, sort="stars", order="desc"):
    query = create_query(languages, min_stars)
    parameters = {"q": query, "sort": sort, "order": order}
    print(parameters)
    response = requests.get(GITHUB_API_URL, params=parameters)

    if response.status_code != 200:
        raise GithubApiException(response.status_code)

    response_json = response.json()
    items = response_json["items"]
    return [GitHubRepo(item["name"], item["language"], item["stargazers_count"]) for item in items]
