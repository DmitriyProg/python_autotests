import requests

token = 'здесь_должен_быть_токен'
host = 'https://api.pokemonbattle.me:9104'

'''respons = requests.post(f'{host}/trainers/reg', json = {
    "trainer_token": token,
    "email": "почта",
    "password": "пароль"
}, headers = {
    'Content-Type': 'application/json'
}) # запрос на регитсрацию тренера

print(respons.status_code) # ответ в виде кода

if respons.status_code == 200:
    print('Ok!')
else:
    print('Not OK!') '''

'''response_activation = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token
}, headers = {
    'Content-Type': 'application/json'
}) # запрос на активацию тренера '''

# ====================== НАЧАЛО ЗАДАНИЯ 13.1 =====================

response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Sun",
    "photo": "https://dolnikov.ru/pokemons/albums/080.png"
}, headers = {'Content-Type' : 'application/json',
    'trainer_token' : token }) # запрос на создание покемона

print(response_add_pokemon.text) # напечатать результат запроса

'''response_change_name_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "6127",
    "name": "MegaFox",
    "photo": "https://dolnikov.ru/pokemons/albums/027.png"
}, headers = {'Content-Type' : 'application/json',
    'trainer_token' : token }) # запрос на изменение имени покемона (заодно поменял и каринку тоже)

print(response_change_name_pokemon.text) # напечатать результат запроса'''

'''response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {    
    "pokemon_id": "6127"
}, headers = {'Content-Type' : 'application/json',
    'trainer_token' : token }) # запрос на добавление покемона в покебол

print(response_add_pokeball.text) # напечатать результат запроса'''