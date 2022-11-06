# wxpush

为了应对企业微信推送ip白名单机制建立的一个api转发服务

# 安装步骤

```commandline
git clone https://github.com/holll/wxpush.git
cd wxpush
pip3 install -r requirements.txt
服务器开放8888端口
在企业微信ip白名单中添加你服务器的ip
```

# 使用步骤

1. `python3 service.py`
2. 向http://127.0.0.1:8888/send接口发送post请求（其中127.0.0.1:8888换成你服务器的ip或域名）

# post参数解释

```commandline
corpid 跳过
corpsecret 跳过
wxpusherId 微信公众号 WxPusher消息推送平台 的uid 非必填
wxpusherToken 微信公众号 WxPusher消息推送平台 的token 非必填
uid 企业微信推送uid
content 推送消息的内容 目前仅支持纯文本
url 原文链接 非必填
cache 是否检测重复消息 非必填 默认检测15分钟内重复消息 不检测请填0
```

# 保活教程

1. 在/etc/systemd/system目录下新建一个wxpush.service，内容如下（替换路径时连带{}一起替换）

```
[Unit]
Description=webapi
After=network.target
 
[Service]
Type=simple
WorkingDirectory={文件夹路径}
ExecStart=/usr/bin/python3 {service.py的绝对路径}
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

然后就可以使用`systemctl start wxpush`来启动程序，其余systemctl使用方法请自行百度
