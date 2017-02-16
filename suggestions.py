import functions

movies = functions.json.load(open("movies_data.json", "r"))
print('Введите название фильма:', end=' ')
f = False
while f == False:
    search = input()
    for i in movies:
        if search.lower() == i['title'].lower() or search.lower() == i['original_title'].lower():
            genres = functions.func_genres(i)
            keywords = functions.func_keywords(i)
            director = functions.find_director(i)
            col = functions.get_collect(i)
            f = True
            break
    if f == False:
        print("Фильм не найден, введите точное название!")

suit = []
suit_dir = []
collect = []

for i in movies:
    if col != None and functions.get_collect(i) == col:
        collect.append(i['title'])
    elif functions.find_director(i) == director:
        suit_dir.append(i['title'])
    elif len(functions.func_keywords(i) & keywords) >= 2 and len(functions.func_genres(i) & genres) >= len(genres) - 5:
        suit.append((i['title'], len(functions.func_genres(i) & genres) / 5 + len(functions.func_keywords(i) & keywords)))

if len(collect) + len(suit_dir) < 10 and len(suit) > 0:
    suit = sorted(suit, key = lambda x: -x[1])
    print(*collect, *suit_dir, sep = '\n')
    for i in range((len(suit))):
        print(suit[i][0])
        if i + 1 + len(collect) + len(suit_dir) >= 10:
            break
else:
    print(*collect, *suit, *suit_dir,sep = '\n')
