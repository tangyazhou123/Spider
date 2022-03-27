from winreg import REG_QWORD
import requests
from fake_useragent import UserAgent
import random
import urllib.parse
import time

class GoogleFanyi():
    def __init__(self, query):
        form_data = f'[[["MkEWBc","[[\"{query}\",\"zh-CN\",\"en\",true],[null]]",null,"generic"]]]'
        data = urllib.parse.quote(form_data)
        self.data = {
            'f.req': data
        }
        self.url = 'https://translate.google.cn/_/TranslateWebserverUi/data/batchexecute'
        self.headers = {
            'referer': 'https://translate.google.cn/',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'User-Agent': UserAgent(verify_ssl=False).random,
            'x-goog-batchexecute-bgr': self.get_bgr()
        }
        self.cookies = {
            'NID': '511=lyOn7qI4W5kBQwkk31nmdANG9Wi68u8QyLid8cc4Wav_8Eh4plU5uDn-bbZB97rpU_cLzd6TF61CFf--PsoQ4eiu0xKNmXqOZQ9rdPsnvWuHA5Qz5QXEPjkTGbWXLCT-FVSrvQb1swRpFx8cujCOoQD6iQAuQZcSWu7Hd5lNVFc',
            'ga': 'GA1.3.1609092802.1648347034',
            'gid': 'GA1.3.1355829628.1648347034',
            'OTZ': '6434051_24_24__24_'
        }

    def make_params(self):
        params = {
            'rpcids': 'MkEWBc',
            'source-path': '/',
            'f.sid': '8460628132913231713',
            'bl': self.get_bl(),
            'hl': 'zh-CN',
            'soc-app': '1',
            'soc-platform': '1',
            'soc-device': '1',
            '_reqid': self.make_reqid(),
            'rt': 'c'
        }
        return params
    def get_bl(self):
        date = time.strftime('%Y%M/%D')
        bl = 'boq_translate-webserver_' + date + '.06_p0'
        return bl


    def make_reqid(self):
       _reqid = str(random.randint(1, 20)) + '67742'
       return _reqid
    
    def get_bgr(self):
        pass

    def get_contents(self):
        response = requests.post(
            url=self.url, 
            params=self.make_params(),
            data=self.data,
            headers=self.headers,
            cookies=self.cookies
            ).text
        print(response)


if __name__=='__main__':
    fanyi = GoogleFanyi('金融')
    fanyi.get_contents()
