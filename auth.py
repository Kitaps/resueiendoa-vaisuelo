# Request para autentificar la app con la API

import requests
from auth_data import client_id, response_type, redirect_uri

payload = {client_id: client_id, response_type: response_type, redirect_uri: redirect_uri}

r = requests.get("https://accounts.spotify.com/authorize", params=payload)

print(r)
