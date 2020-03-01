#import configparser
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
#config = configparser.ConfigParser()
#config.read("config.ini")
# Channel Access Token
line_bot_api = LineBotApi('gMDQJch7y6DV/xjii15ZEFFU6QAB8VjdYyfXSk7iOa2Kf0/aRe9GdX0RIZ1RL6sPpeDwnsi3A5HAGGu+l32g/HLBngA9ggD36uLHHX8J2sT7fJv+06VmmXuI2OufP6+iEYQ1mOqZITsQuE5Ff5eOvwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2e4768d8bc7eab05157afac571717500')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        StickerSendMessage(
            package_id=event.message.package_id,
            sticker_id=event.message.sticker_id)
    )


@handler.add(FollowEvent)
def handle_follow(event):
    print("Follow event:" + event.source.user_id)
    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text='歡迎使用A型~\nCreator by:烈火\nhttps://github.com/YiJhu'))


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    print("Unfollow event:" + event.source.user_id)


@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='歡迎使用A型~\nCreator by:烈火\nhttps://github.com/YiJhu'))


@handler.add(LeaveEvent)
def handle_leave():
    print("leave event")
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='有人失去了夢想\n掰掰~'))

if __name__ == "__main__":
    app.run()
