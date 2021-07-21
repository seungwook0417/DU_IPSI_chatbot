from flask.wrappers import Response
import requests
from bs4 import BeautifulSoup
import json

from card import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Accept-Language": "ko",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
}

# 메인 시작 화면
def ipsi_index():
    response = insert_text("안녕하세요 대구대학교 입학처입니다.🙂\n입학과 관련하여 어떤 정보가 궁금하신가요?")
    response = plus_card(response,"버튼을 누르면 관련 페이지로 이동합니다.","")
    response = insert_button_text(response, "신입학", "신입학 알려주세요")
    response = insert_button_text(response, "재외국인", "재외국인 알려주세요")
    response = insert_button_url(response, "입학처 홈페이지", "https://ipsi.daegu.ac.kr/")
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response

# 재외국인 선택화면
def ipsi_foreigner():
    response = insert_text("안녕하세요 대구대학교 입학처입니다.🙂\n외국인의 입학은 국제교류지원부에서 담당하고 있습니다.\n아래 전화로 문의 부탁드리겠습니다.")
    response = plus_carousel_card(response)
    response = insert_carousel_card(response, "외국인 특별전형", "","https://i.esdrop.com/d/hlogPZr3wi/QpW6QuUqNU.png")
    response = insert_carousel_button_phone(response,"담당 부서로 연결하기","053-850-5685")
    response = insert_carousel_card(response, "외국인 입학", "", "https://i.esdrop.com/d/hlogPZr3wi/oN5J0XPm5k.png")
    response = insert_carousel_button_phone(response, "담당 부서로 연결하기", "053-850-5687")
    response = insert_carousel_card(response, "한국어교육센터, TOPIK", "", "https://i.esdrop.com/d/hlogPZr3wi/y8mOoz4d68.png")
    response = insert_carousel_button_phone(response, "담당 부서로 연결하기", "053-850-5692")
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가주세요")
    response = insert_replies(response, reply)
    return response

# 신입학 시작 화면
def ipsi_new():
    response = insert_text("신입학과 관련하여 어떤 정보가 궁금하신가요?🙂")
    response = plus_carousel_card(response)
    response = insert_carousel_card(response, "", "", "https://i.esdrop.com/d/hlogPZr3wi/Wjt7Kpo3GN.png")
    response = insert_carousel_button(response, "전형일정", "전형일정 알려주세요")
    response = insert_carousel_button(response, "전년도 입시결과", "전년도 입시결과 알려주세요")
    response = insert_carousel_button(response, "수시 교과반영기준", "교과반영기준 알려주세요")
    response = insert_carousel_card(response, "", "", "https://i.esdrop.com/d/hlogPZr3wi/teCKmSeBhY.png")
    response = insert_carousel_button(response, "수시 진로선택과목", "진로 선택과목 알려주세요")
    response = insert_carousel_button(response, "수시 복수지원", "복수지원 알려주세요")
    response = insert_carousel_button(response, "대학 학과별 소개", "학과별 소개 알려주세요")
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response

# 전형일정
def ipsi_schedule():
    response = insert_text("주요 일정을 안내해줄게요😀\n원서접수부터 등록까지 전형일정 꼼꼼하게 확인하기 잊지말아요!\n"
                           "💡전형 일정이 변경될 경우에는 입학안내 홈페이지에 공고 됩니다.")
    response = plus_card(response," ","")
    response = insert_button_text(response, "수시모집 일정", "수시모집 일정 알려주세요")
    response = insert_button_text(response, "정시모집 일정", "정시모집 일정 알려주세요")
    response = insert_button_url(response, "전형일정 공지사항", "https://ipsi.daegu.ac.kr/_prog/_board/?code=notice&site_dvs_cd=kr&menu_dvs_cd=0601")
    reply = make_reply("이전으로 돌아가기", "신입학 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response

# 수시일정
def ipsi_susi():
    response = insert_card("", "수시 모집 주요 일정을 안내해줄게요😀\n원서접수부터 등록까지 전형일정 꼼꼼하게 확인하기 잊지말아요!\n💡전형 일정이 변경될 경우에는 입학안내 홈페이지에 공고 됩니다.")
    response = insert_button_url(response, "수시전형 전형일정 전체보기", "https://ipsi.daegu.ac.kr/html/kr/sub1/sub1_0101.html")
    response = plus_carousel_itemcard(response)
    response = insert_carousel_itemcard(response, "🔸원서접수 기한 및 도착확인",
                                    "🔹입학원서 접수(인터넷)\n"
                                    "2021. 9. 10.(금) ∼ 9. 14.(화) 18:00\n"
                                    "🔹서류제출 기한(해당자)\n"
                                    "2021. 9. 10.(금) ~ 9. 17.(금) 17:00\n",
                                    "https://i.esdrop.com/d/hlogPZr3wi/GzfhZBETUF.png")
    response = insert_carousel_itemcard(response, "🔸면접고사 일정",
                                    "🔹학생부종합(서류면접전형)\n"
                                    "2021. 11. 5.(금)\n"
                                    "🔹학생부종합(장애인 등 대상자 전형)\n"
                                    "2021. 11. 5.(금) 13:00 ~ 17:00\n",
                                    "https://i.esdrop.com/d/hlogPZr3wi/Nh0QR4JrMa.png")
    response = insert_carousel_itemcard(response, "🔸실기고사(체능계)",
                                    "2021. 10. 1.(금) ~ 2.(토)\n"
                                    "스포츠레저학과\n"
                                    "체육학과",
                                    "https://i.esdrop.com/d/hlogPZr3wi/6b841hnn4q.png")
    response = insert_carousel_itemcard(response, "🔸실기고사(조형예술대학)",
                                        "2021. 10. 9.(토) 10:00\n"
                                        "아트앤디자인전공\n"
                                        "영상애니메이션디자인학\n"
                                        "생활조형디자인학전공\n"
                                        "시각디자인전공\n"
                                        "서비스디자인전공\n"
                                        "산업디자인학과\n"
                                        "패션디자인학과\n"
                                        "실내건축디자인학과",
                                        "https://i.esdrop.com/d/hlogPZr3wi/g5G827iLrx.png")
    response = insert_carousel_itemcard(response, "🔸실기고사(문화예술학부)",
                                        "2021. 10. 15.(금)\n"
                                        "문화예술학부",
                                        "https://i.esdrop.com/d/hlogPZr3wi/4ZTAqOXe6R.png")
    response = insert_carousel_itemcard(response, "🔸합격자 발표",
                                        "🔹수능최저학력 기준 미적용\n"
                                        "2021. 11. 12.(금) 21:00\n"
                                        "🔹수능최저학력 기준 적용\n"
                                        "2021. 12. 16.(목) 21:00",
                                        "https://i.esdrop.com/d/hlogPZr3wi/BD2idISgCh.png")
    reply = make_reply("이전으로 돌아가기", "전형일정 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    reply = make_reply("신입학", "신입학 알려주세요")
    response = insert_replies(response, reply)
    return response

# 정시일정
def ipsi_jungsi():
    response = insert_card("","❗정시일정은 아직 작성중에 있어요😰")
    response = insert_button_url(response, "정시전형 전형일정 전체보기", "https://ipsi.daegu.ac.kr/html/kr/sub2/sub2_0201.html?site_dvs_cd=kr&menu_dvs_cd=0201")
    reply = make_reply("이전으로 돌아가기", "전형일정 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    reply = make_reply("신입학", "신입학 알려주세요")
    response = insert_replies(response, reply)
    return response

# 전년도 입시 결과
def ipsi_result():
    response = insert_text("대구대학교의 전년도 입시결과를 안내해줄게요!😘")
    response = plus_card(response,"👇아래 버튼을 눌러 2021학년도 입시결과를 확인해보세요!\n", "")
    response = insert_button_url(response, "수시모집 입시결과", "https://ipsi.daegu.ac.kr/_prog/_board/?mode=V&no=22766&code=data&site_dvs_cd=kr&menu_dvs_cd=0102&skey=&sval=&stype=&gubun02=susi&GotoPage=")
    response = insert_button_url(response, "정시모집 입시결과", "https://ipsi.daegu.ac.kr/_prog/_board/?mode=V&no=22776&code=data&site_dvs_cd=kr&menu_dvs_cd=0202&skey=&sval=&stype=&gubun02=jungsi&GotoPage=")
    reply = make_reply("이전으로 돌아가기", "신입학 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response

# 교과반영기준
def ipsi_subject():
    response = insert_text("2022학년도 대구대학교 수시모집 학생교과반영기준을 안내해줄게요!😘")
    response = puls_text(response,"학생부교과전형은 인문사회/자연과학/공학 계열과 관계없이\n국어/영어/수학 교과 중 상위 2개 교과의 전 과목과\n사회/과학 교과 중 상위 1개 교과의 전 과목을 반영합니다.")
    response = puls_text(response,"학생부종합전형은 별도의 교과반영기준은 없습니다.😀\n학교생활기록부의 전반적인 내용을 종합적으로 평가하게 됩니다.\n따라서 이수과목, 학생수, 이수단위, 교과등급, 세부능력 및 특기사항 등 기재된 모든 내용을 통해 평가를 진행합니다.")
    reply = make_reply("이전으로 돌아가기", "신입학 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response

# 진로선택과목
def ipsi_course():
    response = insert_text("2022학년도 대구대학교 수시모집에서는 진로선택과목을 아래과 같이 반영해요!😘")
    response = puls_text(response,"학생부교과전형의 경우 상위 3개 과목까지 반영하며, 성취도 기준 A(2점), B(1.5점), C(1점)으로 최대 6점, 최소 3점 가산점을 부여합니다.")
    response = puls_text(response,"학생부종합전형의 경우 이수한 과목의 학생수, 단위수, 성취도, 세부능력 및 특기사항 등을 종합적으로 평가하게 됩니다.")
    reply = make_reply("이전으로 돌아가기", "신입학 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response

# 복수선택
def ipsi_multiple():
    response = insert_text("2022학년도 수시모집에서는 총 6회 복수지원이 가능합니다.")
    response = puls_text(response,"단, 복수지원 시 세부전형의 중복은 불가합니다.\n예를 들어 학생부교과(일반전형)-국어교육과, 학생부교과(일반전형)-영어교육과 이런식으로 세부전형 안에서 중복하여 지원하실 수는 없습니다.")
    response = puls_text(response,"다만 전형이 다른 경우 얼마든지 중복가능한 점 참고바랍니다\n(학생부교과(일반전형)-국어교육과, 학생부교과(지역인재전형)-국어교육과)")
    reply = make_reply("이전으로 돌아가기", "신입학 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response

# 학과별 소개 화면
# 학과 소개 답글
def uni_reply(response):
    json_hakgwa = open('hakgwa.json', 'r', encoding="utf-8").read()
    data = json.loads(json_hakgwa)
    for i in data['ipsi']:
        uni = i['id']
        reply = make_reply(uni, uni + "에 대해 알려주세요")
        response = insert_replies(response, reply)
    return response

# 대학 학과 소개 화면
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
    reply = make_reply("이전으로 돌아가기", "신입학 알려주세요")
    response = insert_replies(response, reply)
    reply = make_reply("처음으로 돌아가기", "처음으로 돌아가기")
    response = insert_replies(response, reply)
    return response