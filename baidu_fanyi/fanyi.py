import requests
from fake_useragent import UserAgent
import execjs


class BaiduFanyi():
    def __init__(self, query):
        self.url = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        self.query = query
        self.headers = {
            'User-Agent': UserAgent(verify_ssl=False).random
        }
        self.cookies = {
            'BAIDUID_BFESS': '9254CAD7BD9966315CDDC6D2931CD05A:FG=1',
            'BAIDUID': '9254CAD7BD996631B92D894CD3A63CDF:FG=1',
            'RT': '"z=1&dm=baidu.com&si=uktj2p1d5o&ss=l10s06iu&sl=4&tt=2zx&bcn=https://fclog.baidu.com/log/weirwood?type=perf&ld=c6t&cl=awu&ul=7hjv&hd=7hlz"',
            'REALTIME_TRANS_SWITCH': '1',
            'FANYI_WORD_SWITCH': '1',
            'HISTORY_SWITCH': '1',
            'SOUND_SPD_SWITCH': '1',
            'SOUND_PREFER_SWITCH': '1',
            'APPGUIDE_10_0_2': '1',
            'Hm_lvt_64ecd82404c51e03dc91cb9e8c025574': '1648218223,1648262246',
            'Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574': '1648278724',
            'ab_sr': '1.0.1_MDY5OWNlNmNmNjllNGIyNmEyN2MyYWQ4MDUyOGNhMjY1ZThkNzEyMWZjNWZiNjA3YWNhMjRhMjUwYmYwYmMwYjE0ZGI5OTY5Yjc3ODNhZDFkOTY3ODBiNGJlN2NiN2EyZjIyZGVjZGU5ZjgyMWI1ZDRjZmIwZDZmMDM2MDBjMjJiNjNiNWY4ZTFkNjg5ZTE1NWQ4ZWFkOTc3ZWU1YjhiZQ=='}
    
    def get_proxy(self):
        response = requests.get('http://localhost:5555/random')
        proxy = {
            'http': 'http://' + response.text,
        }
        return proxy

    def make_data(self):
        data = {
            'from': 'zh',
            'to': 'en',
            'query': self.query,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': self.make_sign(),
            'token': '96d82a9f5a76b7954d06761f3f115609',
            'domain': 'common'
        }
        return data
            
    def make_sign(self):
        with open('D:/baidu_fanyi/fanyi.js', 'r', encoding='utf-8') as f:
            sign = execjs.compile(f.read()).call('e', self.query)
            return sign

    def get_content(self):
        response = requests.post(url=self.url, data=self.make_data(), headers=self.headers, cookies=self.cookies).json()
        translate = response['trans_result']['data'][0]['dst']
        print('translate:' + translate)

if '__name__'=='main':
    fanyi = BaiduFanyi('金融')
    fanyi.get_content()


