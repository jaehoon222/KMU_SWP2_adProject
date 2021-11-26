import urllib.request
import json
from Locale import Locale

key = '67d90b1825b1d3a10533ab9bcf46e307'
site = 'https://dapi.kakao.com/v2/local/search/keyword.json'
auth_key = "KakaoAK " + key
auth_header = "Authorization"
category_group_code = "FD6"


def SearchLocale(query, food):
    query = urllib.parse.quote(query)
    query_str = site + "?" + "query=" + query
    request = urllib.request.Request(query_str)
    request.add_header(auth_header, auth_key)
    response = urllib.request.urlopen(request)  # 웹 서버에 요청
    rescode = response.getcode()

    if (rescode == 200):
        res = response.read().decode('utf-8')
        jres = json.loads(res)
        if jres == None:
            return []
        locales = []
        x = jres['documents'][0]['x']
        y = jres['documents'][0]['y']
        jres['documents'][0]['place_name'] = '나의 거주지'
        locales.append(Locale.MakeLocale(jres['documents'][0]))

    query = urllib.parse.quote(food)
    query_str = site + "?y=" + str(y) + "&x=" + str(x) + "&category_group_code=" + category_group_code+"&radius=1000&query=" + query
    request = urllib.request.Request(query_str)
    request.add_header(auth_header, auth_key)
    response = urllib.request.urlopen(request)  # 웹 서버에 요청
    rescode = response.getcode()

    if (rescode == 200):
        res = response.read().decode('utf-8')
        jres = json.loads(res)
        if jres == None:
            return []
        for jloc in jres['documents']:
            locale = Locale.MakeLocale(jloc)
            if (locale != None):
                locales.append(locale)
        return x, y, locales
    else:
        return []