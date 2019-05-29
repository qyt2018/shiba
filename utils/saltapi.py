import requests
import json
import logging
import websockets
import asyncio

logger = logging.getLogger(__name__)


def request_error(func):
    def decorator(self, url, data):
        request = func(self, url, data)
        if request.status_code == 401:
            logger.error("认证失败，请检查用户名密码")
            result = False
        else:
            result = json.loads(request.text)
        return result

    return decorator


class SaltApi(object):

    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.username = username
        self.password = password

    def get_token(self):
        data = {
            "username": self.username,
            "password": self.password,
            "eauth": "pam"
        }
        token = self.post_data("/login", data)
        if token:
            return token['return'][0]['token']
        else:
            raise Exception

    @request_error
    def get_data(self, url, params):
        url = self.base_url + url
        request = requests.get(url, params)
        return request

    @request_error
    def post_data(self, url, data):
        url = self.base_url + url
        request = requests.post(url, data)
        return request

    def run(self):
        pass

    async def ws(self):
        while True:
            try:
                # 格式化websocket url
                base_url = self.base_url.replace('http://', 'ws://')
                url = f"{base_url}/ws/{self.get_token()}"

                async with websockets.connect(url) as ws:
                    await ws.send('websocket client ready')
                    logger.info("开始处理消息")
                    while True:
                        result = await ws.recv()
                        print(f"< {result}")
            except Exception as e:
                logger.error(f"salt ws连接失败，等待5秒重新连接{e}")
                await asyncio.sleep(5)


if __name__ == '__main__':
    api = SaltApi("http://172.16.8.248:8200", "saltapi", "saltapi")
    asyncio.get_event_loop().run_until_complete(api.ws())
