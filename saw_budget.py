import functions
api_key = '18a3429d8ccfefc2bd0202ad5dec5cba'
print('Бюджет фильма "Пила" :{} $ '.format(functions.make_tmdb_api_request('/movie/215', api_key)['budget']) )
