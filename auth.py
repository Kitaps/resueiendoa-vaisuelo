# Request para autentificar la app con la API

import requests
from auth_data import client_id, redirect_uri

# client_id se puede sacar de
# https://developer.spotify.com/dashboard/applications
payload = {client_id: client_id, response_type: "token", redirect_uri: "https://www.google.com", scope=}

r = requests.get("https://accounts.spotify.com/authorize", params=payload)

# Pagina de HTML ...
print(r.text)
