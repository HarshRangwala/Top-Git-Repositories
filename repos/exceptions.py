# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:35:57 2021

@author: Anuj
"""

class GithubApiException(Exception):
    
    def __init__ (self, status_code):
        
        if status_code == 403:
            message = "Rate limit reached."
        else:
            message = f"Status code was: {status_code}"
        
        super().__init__(message)
             