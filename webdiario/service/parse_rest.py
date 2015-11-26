__author__ = 'mikael'

import requests, json, re
from datetime import datetime
from urllib import parse

app_id = "uRkPJeVgTu1jbV3OSNNs5TixX33ulWPe8w8ZlewI"
rest_key = "PZqT2xZLYsabsBKevU83VhHGbNWQSHyCo2UU8HDe"
headers = {"X-Parse-Application-Id": app_id, "X-Parse-REST-API-Key": rest_key}
url_base = "https://api.parse.com/1/classes"

#logging In
# O login ainda não esta funcionando, talvez teha que criar
# uma sessão para o usuaário lá no parse.
headers["X-Parse-Revocable-Session"] = "1"
params_auth = {"username": "mkmikael", "password": "0509151607mk"}
r = requests.get(url_base + "/login", params=params_auth)
print(r.text)

# insert na base
headers["Content-Type"] = "application/json"
data = {
    'numero': '8946513',
    'content': 'asdkasjl alksjdlaksj alksdjalskdj',
    'link': 'diariobelem.com.br/diario/123872',
    'data': {
      "__type": "Date",
      "iso": datetime.now().isoformat()
    }
}

# r = requests.post(url_base + '/Diario', headers=headers, data=json.dumps(data))
# print(r.text)

# consulta a base
#where = {"content": {'$regex': 'diário'}}
def query(text):
    criteria = {'count': 1} # , 'where': json.dumps(where)
    params = parse.urlencode(criteria)
    r = requests.get(url_base + '/Diario?' + params, headers=headers)
    result = r.json()
    count = 0
    resultList = []
    for diario_page in result['results']:
        #content = re.findall(r"([^.]*?%s[^.]*[\.\?])" % text, diario_page['content'])
        if text in diario_page['content']:
            queryEntity = {}
            queryEntity['numero'] = str(diario_page['numero'])
            queryEntity['page'] = str(diario_page['page'])
            resultList.append(queryEntity)
            count += 1
    return resultList
