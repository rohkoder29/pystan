# from itertools import product

# max_x = [3, 7, 1]
# max_y = list(range(1, 5, 2))


# # for x in range(len(max_x)):
# #   for y in range(len(max_y)):
# #     print(f'{x} -> {y}')

# # reemplazar el de arriba con el de abajo

# for x, y in product(range(len(max_x)), range(len(max_y))):
#   print(f'{x} -> {y}')

##############
# import math

# x = 17
# y = 7
# # Dans ce code il va retourner -1, car 17+1=18 qui est un multiple de 6. Donc il te retourne l'écart entre x et le multiple de y le plus proche de x.
# m = math.remainder(x, y)
# print(m)

######################
# import requests

# url = 'https://v2.jokeapi.dev/joke/Any?lang=fr'
# rsp = requests.get(url).json()

# if rsp['type'] == 'single':
#   print(rsp['joke'])
# else:
#   print(rsp['setup'], rsp['delivery'])
######################
# import requests


# url = 'https://api.jokes.one/jod?category=knock-knock'
# api_token = "YOUR API KEY HERE"
# headers = {'content-type': 'application/json',
#            'X-JokesOne-Api-Secret': format(api_token)}

# response = requests.get(url, headers=headers)
# #print(response)
# # print(response.text)
# jokes = response.json()['contents']['jokes'][0]['joke']['text']
# print(jokes)
#############################

TEMP = print("yay") if 2 > 1 else -1
