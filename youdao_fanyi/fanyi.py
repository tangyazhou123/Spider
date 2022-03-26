import random
import time
from fake_useragent import UserAgent
import requests
from hashlib import md5

timestamp = str(int(time.time() * 1e+3))

class YoudaoFanyi():
    def __init__(self, query):
        self.url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.query = query
        self.headers = {
        'User-Agent': UserAgent(verify_ssl=False).random
    }
        self.cookies = {
            'OUTFOX_SEARCH_USER_ID': '1929728460@10.110.96.158',
            'JSESSIONID': 'aaa2JSwJmV6HYbpRxng-x',
            'OUTFOX_SEARCH_USER_ID_NCOO': '1576115038.7939863',
            '___rl__test__cookies': timestamp
        }

    def make_sign(self):
        e = self.query
        i = timestamp + str(random.randint(0,9))
        param = "fanyideskweb" + e + i + "Ygy_4c=r#e#4EX^NUGUc5"
        md5().update(param.encode())
        sign = md5().hexdigest()
        return sign

    def make_data(self):
        data = {
            'i': self.query,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': timestamp + str(random.randint(0,9)),
            'sign': self.make_sign(),
            'lts': timestamp,
            'bv': '440755c54fd4a0fa5a4519a85e0abbd4',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        return data
    
    def get_content(self):
        response = requests.post(url=self.url, data=self.make_data(), headers=self.headers, cookies=self.cookies).json()
        translate = response['translateResult'][0][0]['tgt']
        print('translate:' + translate)    

if __name__=='__main__':
    fanyi = YoudaoFanyi('金融')
    fanyi.get_content()

