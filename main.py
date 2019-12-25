import requests



# En el pauload se pone el diccionario con los parametros
payload = dict()

# Se hace el request
r = requests.get('https://api.github.com/events')

# print(r.url)
print(r.raw)
