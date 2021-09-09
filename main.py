# External Module
from flask import Flask, request, jsonify
import json

# Internal Module
from card import *  # 카카오톡 데이터 전송 양식
from ipsi import *

app = Flask(__name__)

# Route urls
# app.route는 flask의 기능으로, '/hello'와 같은 url로 요청이 들어오면 해당 함수만 호출한다.

# 메인 시작 화면
@app.route("/index", methods=['POST'])
def index():
    response = ipsi_index()
    return response

# 재외국인 전형 화면
@app.route("/foreigner", methods=['POST'])
def foreigner():
    response = ipsi_foreigner()
    return response

# 신입학
@app.route("/new", methods=['POST'])
def new():
    response = ipsi_new()
    return response

# 전형일정
@app.route("/schedule", methods=['POST'])
def schedule():
    response = ipsi_schedule()
    return response

# 전형일정_수시
@app.route("/susi", methods=['POST'])
def susi():
    response = ipsi_susi()
    return response

# 전형일정_정시
@app.route("/jungsi", methods=['POST'])
def jungsi():
    response = ipsi_jungsi()
    return response

# 전년도 입시결과
@app.route("/result", methods=['POST'])
def result():
    response = ipsi_result()
    return response

# 교과반영기준
@app.route("/subject", methods=['POST'])
def subject():
    response = ipsi_subject()
    return response

# 성적산출
@app.route("/score", methods=['POST'])
def score():
    response = ipsi_score()
    return response

# 경쟁률
@app.route("/ratio", methods=['POST'])
def ratio():
    response = ipsi_ratio()
    return response

# 진로선택과목
@app.route("/course", methods=['POST'])
def course():
    response = ipsi_course()
    return response

# 복수지원
@app.route("/multiple", methods=['POST'])
def multiple():
    response = ipsi_multiple()
    return response

# 대학 소개 화면
@app.route("/uni", methods=['POST'])
def uni():
    response = insert_text("대구대학교 대학 학과에 대해 알려드릴게요!\n아래 버튼에서 원하는 대학을 찾아보세요😃")
    response = uni_reply(response)
    return response

# 대학, 학과 소개 화면
@app.route("/hakgwa", methods=['POST'])
def hakgwa():
    content = request.get_json()
    content = content['action']['detailParams']['uni']["value"]
    content = ''.join(str(e) for e in content)
    content = content.replace(" ", "")
    response = hakgwa_data(content)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="1818", debug=False)
    # app.run()
