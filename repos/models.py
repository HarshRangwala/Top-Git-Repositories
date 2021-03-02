# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 22:19:41 2021

@author: Anuj
"""

class GitHubRepo:
    """
    A class thats used to represent a single Github Repository
    """
    
    def __init__(self, name, language, num_stars):
        self.name = name
        self.language = language
        self.num_stars = num_stars
    
    def __str___(self):
        return f"-> {self.name} is a {self.language} repo with {self.num_stars} stars."
    
    def __repr__(self):
        return f'GithubRepo({self.name}, {self.language}, {self.num_stars})'
    