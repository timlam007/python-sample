'''
Created on 04-Sep-2019

@author: bkadambi
'''

# -*- coding: UTF-8 -*-
"""
hello_flask: First Python-Flask webapp
"""
from flask import Flask  # From module flask import class Flask
app = Flask(__name__)    # Construct an instance of Flask class for our webapp

@app.route('/')   # URL '/' to be handled by main() route handler
def main():
    """Say hello"""
    return 'Hello Timothy Lam !'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
