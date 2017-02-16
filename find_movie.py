import json

movies = json.load(open("movies_data.json", "r"))
print('Введите название фильма:', end = ' ')
search = input()
found = set()
for i in movies:
    if search.lower() in i['title'].lower():
        found.add(i['title'])
    elif search.lower() in i['original_title'].lower():
        found.add(i['original_title'])
if (len(found) > 0):
    print("Результаты поиска:", sep = '\n', *found)
else:
    print("Ничего не найдено.")

