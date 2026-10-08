fav_dict = {
    'book': 'A Cabana',
    'tree': 'Flamboyant',
    'song': 'Promiscuous Girl'
}

print(fav_dict['book'])

fav_thing = 'book'
print(fav_dict[fav_thing])

print(fav_dict['tree'])

fav_dict['organism'] = 'Escherichia coli'

fav_thing = 'organism'
print(fav_dict[fav_thing])

fav_thing = input("What is your favorite thing? ")
print(fav_dict[fav_thing])

fav_dict['organism'] = 'Saccharomyces cerevisiae'
print(fav_dict['organism'])
