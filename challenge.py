import requests, json


def step_one(token):
    payload = {'token': token, 'github': 'https://github.com/tosmith97/Code2040'}
    r = requests.post('http://challenge.code2040.org/api/register', data=payload)
    print r.text


def step_two(token):
    url = 'http://challenge.code2040.org/api/reverse'
    payload = {'token': token}
    r = requests.post(url, data=payload)
    str_to_reverse = r.text
    reversed = str_to_reverse[::-1]
    url2 = 'http://challenge.code2040.org/api/reverse/validate'
    payload2 = {'token': token, 'string': reversed}
    r = requests.post(url2, data=payload2)
    print r.text


def step_three(token):
    url = 'http://challenge.code2040.org/api/haystack'
    payload = {'token': token}
    r = requests.post(url, data=payload)
    dict = r.json()
    needle = dict['needle']

    idx = -1
    for i in range(0, len(dict['haystack'])):
        if dict['haystack'][i] == needle:
            idx = i
            break

    payload2 = {'token': token, 'needle': idx}
    r = requests.post('http://challenge.code2040.org/api/haystack/validate', data=payload2)
    print r.text


def step_four(token):
    url = 'http://challenge.code2040.org/api/prefix'
    payload = {'token': token}
    r = requests.post(url, data=payload)
    dict = r.json()
    prefix = dict['prefix']
    no_prefix = []

    for word in dict['array']:
        if not word.startswith(prefix):
            no_prefix.append(word)
    print dict
    print no_prefix

    payload2 = {'token': token, 'array': no_prefix}
    r = requests.post('http://challenge.code2040.org/api/prefix/validate', data=payload2)
    print r.text


token = 'a21f0f545e01aa117d5472938d1de09e'

step_four(token)