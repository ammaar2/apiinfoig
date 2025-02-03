from flask import Flask, request, jsonify
import requests
from user_agent import generate_user_agent as abo
import uuid
import string
import random

app = Flask(__name__)

class S1:
    def __init__(self):
        self.tok = ''
        self.id = ''
        self.g = 0
        self.gb = 0
        self.b = 0

    def rest(self, email):
        y = "".join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32))
        url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'
        h = {
            'Content-Length': '328',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Host': 'i.instagram.com',
            'Connection': 'Keep-Alive',
            'User-Agent': 'Instagram 6.12.1 Android (30/11; 320dpi; 720x1339; realme; RMX3269; RED8F6; RMX3265; ar_IQ)',
            'Cookie': 'mid=Z0ZQoQABAAFHk8B-qvDkQ4bq_XLc; csrftoken=wf5gPNZiHZptDbscGF9l1QX2YYNgi1oK',
            'Cookie2': '$Version=1',
            'Accept-Language': 'ar-IQ, en-US',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': 'AQ==',
            'Accept-Encoding': 'gzip',
        }
        d = {
            'user_email': email,
            'device_id': str(uuid.uuid4()),
            'guid': str(uuid.uuid4()),
            '_csrftoken': y
        }
        re = requests.post(url, headers=h, data=d).json()
        try:
            hj = re["obfuscated_email"]
            return hj
        except:
            return ''

    def date_sc(self, Id):
        try:
            if int(Id) > 1 and int(Id) < 1279000:
                return 2010
            elif int(Id) > 1279001 and int(Id) < 17750000:
                return 2011
            elif int(Id) > 17750001 and int(Id) < 279760000:
                return 2012
            elif int(Id) > 279760001 and int(Id) < 900990000:
                return 2013
            elif int(Id) > 900990001 and int(Id) < 1629010000:
                return 2014
            elif int(Id) > 1900000000 and int(Id) < 2500000000:
                return 2015
            elif int(Id) > 2500000000 and int(Id) < 3713668786:
                return 2016
            elif int(Id) > 3713668786 and int(Id) < 5699785217:
                return 2017
            elif int(Id) > 5699785217 and int(Id) < 8507940634:
                return 2018
            elif int(Id) > 8507940634 and int(Id) < 21254029834:
                return 2019
            else:
                return "2020-2023"
        except:
            return ''

    def inf(self, email):
        user = email.split('@')[0]

        cookies = {
            'datr': 'lhI2Z-qsh_SE2tBAm-z9sT8c',
            'ig_did': 'FBBFF354-5D64-40BE-82A6-F40D4C80FC4E',
            'mid': 'ZzYSlgABAAFR3pvSs-MtncGVPir1',
            'ig_nrcb': '1',
            'ps_l': '1',
            'ps_n': '1',
            'dpr': '2.1988937854766846',
            'ds_user_id': '277613183',
            'csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
            'wd': '891x1654',
            'rur': '"LLA\\054277613183\\0541764135205:01f7191faf0392a232a09e8551689df778531b54d6147fb6b0ee28550084ef623409d5ce"',
        }

        headers = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'referer': 'https://www.instagram.com/dd/',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Linux"',
            'sec-ch-ua-platform-version': '""',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': str(abo()),
            'x-asbd-id': '129477',
            'x-csrftoken': 'S1tFXRCsflUJCBKWav6rP8d0DsnfiEMP',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR07T_Q0xaDQfazO_ogFm4DlAfLnCNNeQ0b0skK1F4sWzJzO',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'username': user,
        }

        res = requests.get(
            'https://www.instagram.com/api/v1/users/web_profile_info/',
            params=params,
            cookies=cookies,
            headers=headers,
        )

        pp = res.json()

        try:
            b = pp["data"]["user"]["biography"]
        except:
            b = None

        try:
            fol = pp["data"]["user"]["edge_followed_by"]["count"]
        except:
            fol = None

        try:
            fog = pp["data"]["user"]["edge_follow"]["count"]
        except:
            fog = None

        try:
            Id = pp["data"]["user"]["id"]
            aj = self.date_sc(Id)
        except:
            Id = None

        try:
            pr = pp["data"]["user"]["is_private"]
        except:
            pr = None

        try:
            us = pp["data"]["user"]["username"]
        except:
            us = None

        try:
            pos = pp["data"]["user"]["edge_owner_to_timeline_media"]["count"]
        except:
            pos = None

        try:
            na = pp["data"]["user"]["full_name"]
        except:
            na = None

        ret = self.rest('mariahwilliamsfans@gmail.com')

        info = {
            "name": na,
            "username": us,
            "gmail": f"{us}@gmail.com",
            "rest": ret,
            "following": fog,
            "followers": fol,
            "id": Id,
            "private": pr,
            "posts": pos,
            "date_created": aj,
            "bio": b
            "by":"@jokerpython3"
        }

        return info

@app.route('/infoIg', methods=['GET'])
def get_info():
    user = request.args.get('user')
    if not user:
        return jsonify({"error": "يجب تقديم اسم المستخدم (user) في الرابط."}), 400

    email = f"{user}@gmail.com"
    s1 = S1()
    result = s1.inf(email)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
