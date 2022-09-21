from textwrap import shorten

name = input("Who's your favourite CC on Twitter? ")
print(f"{shorten(f'My fav CC on Twitter is {name}', width=30)}")
# >>> My fav CC on Twitter is [...]
