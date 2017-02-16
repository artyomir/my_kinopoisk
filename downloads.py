import functions

api_key = '18a3429d8ccfefc2bd0202ad5dec5cba'
movies_list = []
temp, mov_id = 0, 1

while temp < 1000:
    try:
        movies_list.append(functions.make_tmdb_api_request('/movie/{}'.format(mov_id), api_key))
        movies_list[temp]["keyw"] = functions.make_tmdb_api_request('/movie/{}/keywords'.format(mov_id), api_key)
        movies_list[temp]["credits"] = functions.make_tmdb_api_request('/movie/{}/credits'.format(mov_id), api_key)
        temp += 1
        print ("{} Loaded!".format(mov_id))
        mov_id += 1
    except:
        print("{} Not available :(".format(mov_id))
        mov_id += 1
print("Download complete!")
mov = open('movies_data.json', 'w')
functions.json.dump(movies_list, mov)

