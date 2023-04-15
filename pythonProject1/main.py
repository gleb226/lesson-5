import requests
import json
from colorama import Fore, Back, Style

try:
    r = requests.get('https://randomuser.me/api')

    person = json.loads(r.text)
except Exception as e:
    print(e)
class Person:
    def __init__(self, name, surname, age, gender, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.isMan = gender == 'male'
        self.email = email
try:
    api_name = person['results'][0]['name']['first']
    api_surname = person['results'][0]['name']['last']
    api_age = person['results'][0]['dob']['age']
    api_gender = person['results'][0]['gender']
    api_email = person['results'][0]['email']

    random_person = Person(api_name, api_surname, api_age, api_gender, api_email)

    if random_person.isMan:
        print(Fore.BLUE + random_person.name, random_person.surname, random_person.age, random_person.email)
    else:
        print(Fore.MAGENTA + random_person.name, random_person.surname, random_person.age, random_person.email)
except Exception as e:
    print(e)
