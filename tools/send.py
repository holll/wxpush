import json

import requests


def send_msg(token, uid, content, url, cache, wxpusherId=None, wxpusherToken=None):
    def backup_send(wxpusherId, wxpusherToken, msg):
        wxpusher_api = 'http://wxpusher.zjiecode.com/api/send/message'
        data = {
            'appToken': wxpusherToken,
            'content': msg,
            'contentType': 1,
            'uids': [wxpusherId]
        }
        requests.post(wxpusher_api, headers={'Content-Type': 'application/json'}, data=json.dumps(data))

    if wxpusherId is not None:
        backup_send(wxpusherId, wxpusherToken, content)
        return
    if uid is None or content is None:
        return {'code': 400, 'msg': '关键参数缺失'}
    api = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + token
    if url is not None:
        content = '%s\n<a href=\"%s\">点击查看原文链接</a>' % (content, url)
    values = {
        'touser': uid,
        'msgtype': 'text',
        'agentid': '1000005',
        'text': {'content': content},
        'enable_duplicate_check': int(cache),
        'duplicate_check_interval': 900
    }
    rep = requests.post(api, json=values).json()
    if rep['errcode'] != 0:
        msg = '企业微信消息发送失败: ' + str(rep)
        backup_send(wxpusherId, wxpusherToken, msg + '\n' + content)
        return {'code': 501, 'msg': msg}
    else:
        return {'code': 200, 'msg': '发送成功'}


def get_token(corpid: str, corpsecret: str, wxpusherId, wxpusherToken):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
    values = {
        'corpid': corpid,
        'corpsecret': corpsecret,
    }
    req = requests.get(url, params=values)
    data = json.loads(req.text)
    if data["errcode"] == 0:
        new_token = data["access_token"]
        return new_token
    else:
        msg = "企业微信access_token获取失败: " + str(data)
        send_msg(uid='YangYiFan', content=msg, wxpusherId=wxpusherId, wxpusherToken=wxpusherToken, cache='0', token='',
                 url=None)
        return
