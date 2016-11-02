import requests, datetime
import dateutil.parser as dp


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

    payload2 = {'token': token, 'array': no_prefix}
    r = requests.post('http://challenge.code2040.org/api/prefix/validate', json=payload2)

    print r.text


def step_five(token):
    url = 'http://challenge.code2040.org/api/dating'
    payload = {'token': token}
    r = requests.post(url, data=payload)
    dict = r.json()
    datestamp = dict['datestamp']
    interval = dict['interval']

    d = dp.parse(datestamp)
    new_datetime = d + datetime.timedelta(0, interval)
    new_datestamp = new_datetime.isoformat()

    # not the best in terms of robustness, but got the job done
    new_datestamp = new_datestamp.replace('+00:00', 'Z')

    payload2 = {'token': token, 'datestamp': new_datestamp}
    r = requests.post('http://challenge.code2040.org/api/dating/validate', data=payload2)
    print r.text

token = 'a21f0f545e01aa117d5472938d1de09e'

step_four(token)
