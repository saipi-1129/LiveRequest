from flask import Flask, request, render_template
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html',code = None)

@app.route('/submit', methods=['POST'])
def submit():
    url = "https://www.mirrativ.com/api/user/post_live_request"

    headers = {
}

    user_id = request.form.get('user_id')
    count = request.form.get('count')

    data = {
        'user_id': user_id,
        'count': count,
        'where': 'profile'
    }

    response = requests.post(url, headers=headers, data=data)
    ut = time.time()
    code = response.status_code


    return render_template("result.html",code=code) 
    #sonify({"timestamp": ut, "response": response.text})
    
@app.route("/change",methods=['POST'])
def change():
    url = 'https://www.mirrativ.com/api/user/profile_edit'
    
    user_name = request.form.get('user_name')

    # フォームデータ
    data = {
        'user_id': '',
        'name': user_name,
        'description': '',
        'links': '[{"url":""}]',
        'include_urge_users': '0',
        'dynamic_link': '',
        'birthday': '0101',
        'is_visible_birthday': '0',
        'is_vip_public': '1'
    }

    encoder = MultipartEncoder(fields=data, boundary='')

    headers = {
}

    response = requests.post(url, headers=headers, data=encoder)
    # print(response.text)
    code = response.status_code

    return render_template("form.html",code=code,name = user_name) 

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
