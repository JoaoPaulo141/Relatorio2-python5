import sys

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

fav_thing = sys.argv[1]
new_value = sys.argv[2]

fav_dict[fav_thing] = new_value

print(fav_dict[fav_thing])

for key, value in fav_dict.items():
    print(key, value)
