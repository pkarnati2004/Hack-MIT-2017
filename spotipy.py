# import spotipy
# sp = spotipy.Spotify()

# results = sp.search(q='weezer', limit=20)
# for i, t in enumerate(results['tracks']['items']):
#     print (' ', i, t['name'])
# import requests
# import json

# request = requests.get("https://api.spotify.com/v1/search?q=" + "Beyonce" + "%20bowra&type=artist")
# suggestions = []
# print(request.json())
# artists = request.json()["artists"]["items"]
# for a in artists:
#     suggestions.append(artists["name"])

# print(suggestions)

import spotipy
import spotipy.util as util
#import cgi
#form = cgi.FieldStorage()
#searchterm =  form.getvalue('searchbox')
#print(searchterm)

def search(query):
    scope = 'user-library-read'
    token = util.prompt_for_user_token('22qi37dpunsbh7fixly35rrvi', scope, client_id='fb70f5c9b1214cd9a91d9aac589ea5f2', client_secret='9f9ab38600834e6584196b682ac5154e', redirect_uri='http://localhost:8888/callback')
    spotify = spotipy.Spotify(auth=token)
    name = query
    results = spotify.search(q=name, limit=10, type='track')

    suggestions = [] 
    for i in range(10):
        album = results['tracks']['items'][i]['album']['name']
        artist = ((results['tracks']['items'][i]['artists'][0]['name']))
        track = (results['tracks']['items'][i]['name'])
        suggestion = {'Song': track, 'Artist': artist, 'Album': album}
        suggestions.append(suggestion)
    return suggestions
    print(suggestions)
    
#print(search('Justin Timberlake'))

search("Beyonce")