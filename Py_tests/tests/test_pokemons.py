import requests
import pytest

token = 'здесь_должен_быть_токен'
t_id = 1609
host = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id': t_id})
    assert response.status_code == 200 # проверяем, что статус ответа 200
    

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id': t_id})
    assert response.json()['trainer_name'] == 'Тестер_2000' # проверяем, что в ответе имя тренера "Тестер_2000"

'''
@pytest.mark.parametrize('key, value',[('city','Tokyo'),
                                       ('trainer_id',f'{trainers_id}'),
                                       ('attack',1.0)])

def tests_parts_of_answer(key, value):
    response = requests.get(f'{host}/pokemons', params = {'trainer_id':trainers_id})
    assert response.json()[0][key] == value
'''