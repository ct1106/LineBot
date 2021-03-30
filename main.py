# 这是一个示例 Python 脚本。
from flask import Flask, request, abort
from urllib.request import urlopen

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError, LineBotApiError
)

### Script start ###

from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(
    '0h39bUasfmcqQb2UcwfvKdTbCmT/isTtLNelVjVT7jKmDYapOOeEe/qqgBxFLBViWyAetuY9en2OX7Kw85br68WtMyInqpIoQMxRtplhobfZDUN2yh05sOsrl4cAEd+oMDs/Ne6kq/+F9EFB2G566QdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('3d840ca12c208b906927f8cb212467cb')


# 監聽所有來自 / 的 Post Request
@app.route("/", methods=['POST'])
def callback():
    # get X_Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app.run()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
