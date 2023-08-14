import json
from random import choice


def get_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel
    }

    return person


def key_json():
    key_num = ''

    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(key_num) != 10:
        key_num += choice(nums)

    return key_num


def write_json(key_j, person_dict):
    try:
        data = json.load(open('person.json'))

    except FileNotFoundError:
        data = dict()

    data[key_j] = person_dict
    with open('person.json', 'w') as fw:
        json.dump(data, fw, indent=2)


for i in range(5):
    write_json(key_json(), get_person())


with open('person.json', 'r') as f:
    data1 = json.load(f)

for key, value in data1.items():
    print(key, '-', value)

