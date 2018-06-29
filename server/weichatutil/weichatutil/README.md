# wechat

进行微信消息通知

## 使用步骤

### 前期准备

具体方式为:

1. 在阿里云后台，打开对应的端口 port
2. 修改 `WeChatListen.py`, 修改对应的 port.
3. 修改 `WeChatListen.py` 和 `WeChatLogSender.py` 使 `Token` 保持统一

### 服务器端部署

1. 在服务器部署, `WeChatListen.py` 用于监听微信消息
2. 使用 `Supervisor` 管理
3. 在 `Supervisor` 的 `conf.d` 添加 `python WeChatListen.py --port=8889`
4. `supervisor` update status

### 使用

客户端使用 `WeChatLogSender.py` 进行微信消息发送
