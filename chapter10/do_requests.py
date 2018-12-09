import requests
from lxml import etree

class Login:
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
            'Host': 'github.com',
        }

        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        # print(response.text)
        token = selector.xpath('//form/input/@value')
        return token

    def do(self):
        data = self.token()
        print(data)
        post_data = {
            'commit': 'Sign in',
            'utf8':'✓',
            'authenticity_token':  data[1],
            'login': '1026037967@qq.com',
            'password': 'wen1998...',
        }

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)

        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    def dynamics(self, html):
        selector = etree.HTML(html)
        dynamics = selector.xpath('//div[contains(@class, "push")]')
        print(html)
        print(dynamics)

        for item in dynamics:
            dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
            print(dynamic)

    def profile(self, html):
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profit_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profit_email"]/option[@value!=""]/text()')
        print(name,email)


if __name__ == '__main__':
    login = Login()
    print(login.do())