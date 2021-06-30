# External Module
from flask import Flask, request, jsonify
import json

# Internal Module
from card import *  # 카카오톡 데이터 전송 양식
from ipsi import *

app = Flask(__name__)

# Route urls
# app.route는 flask의 기능으로, '/hello'와 같은 url로 요청이 들어오면 해당 함수만 호출한다.

#uni
@app.route("/swlee", methods=['POST'])
#@app.route("/uni", methods=['POST'])
def uni():
    response = insert_text("대구대학교 대학 학과에 대해 알려드릴게요!\n아래 버튼에서 원하는 대학을 찾아보세요😃")
    response = uni_reply(response)
    return response

#hakgwa
@app.route("/uni", methods=['POST'])
#@app.route("/hakgwa", methods=['POST'])
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
