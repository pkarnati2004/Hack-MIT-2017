from flask import Flask, render_template, request, redirect, url_for, jsonify

import time
import threading
import requests


app = Flask(__name__)

@app.route('/')
def default_route():

    return render_template('index.html')

@app.route('/suggest', methods=['GET']) 
def get_songs():
    my_data = ["GabeMaddona"]
    x = ["beyonce lemonade"]
    return jsonify(result=x)

# TODO 
def search_for_songs(query="Beyonce"):
    request = requests.get("https://api.spotify.com/v1/search?q=%s%20bowra&type=artist" %(query))
    suggestions = []
    artists = request["artists"]["items"]
    for a in artists:
        suggestions.append(artists["name"])
    return suggestions


if __name__ == '__main__':
    app.run()


#import cgi
#form = cgi.FieldStorage()
#searchterm =  form.getvalue('searchbox')
#print(searchterm)