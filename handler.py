import tornado.web
import tornado.web

from tools import *


class SendmsgHandler(tornado.web.RequestHandler):

    def post(self, *args, **kwargs):
        corpid = self.get_argument('corpid', default=None, strip=True)
        corpsecret = self.get_argument('corpsecret', default=None, strip=True)
        wxpusherId = self.get_argument('wxpusherId', default=None, strip=True)
        wxpusherToken = self.get_argument('wxpusherToken', default=None, strip=True)
        uid = self.get_argument('uid', default=None, strip=True)
        content = self.get_argument('content', default=None, strip=True)
        url = self.get_argument('url', default=None, strip=True)
        cache = self.get_argument('cache', default='1', strip=True)
        token = send.get_token(corpid, corpsecret, wxpusherId, wxpusherToken)
        if token is not None:
            rep = send.send_msg(token, uid, content, url, cache)
        else:
            rep = {'code': 501, 'msg': 'token获取失败'}
        self.write(rep)

    def get(self, *args, **kwargs):
        self.post(self, *args, **kwargs)
