import requests
from bs4 import BeautifulSoup
import json

from card import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Accept-Language": "ko",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
}


def uni_reply(response):
    json_hakgwa = open('hakgwa.json', 'r', encoding="utf-8").read()
    data = json.loads(json_hakgwa)
    for i in data['ipsi']:
        uni = i['id']
        reply = make_reply(uni, uni + "에 대해 알려주세요")
        response = insert_replies(response, reply) 
    return response

def hakgwa_data(content):
    json_hakgwa = open('hakgwa.json', 'r', encoding="utf-8").read()
    data = json.loads(json_hakgwa)
    for a in data['ipsi']:
        if a['id'] == content:
            response = insert_card("",a['text'])
            response = insert_button_url(response, "대학 상세보기", a['url'])
            response = plus_carousel_card(response)
            for b in a['hakgwa']:
                response = insert_carousel_card(response,b['id'],"",b['image_url'])
                response = insert_carousel_button_url(response,"학과홈페이지 바로가기",b['url'])
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply) 
    return response