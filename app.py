import os, json, re, time
from time import strftime
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('gMDQJch7y6DV/xjii15ZEFFU6QAB8VjdYyfXSk7iOa2Kf0/aRe9GdX0RIZ1RL6sPpeDwnsi3A5HAGGu+l32g/HLBngA9ggD36uLHHX8J2sT7fJv+06VmmXuI2OufP6+iEYQ1mOqZITsQuE5Ff5eOvwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2e4768d8bc7eab05157afac571717500')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


#@handler.add(MessageEvent, message=TextMessage)
#def handle_message(event):
    #line_bot_api.reply_message(
        #event.reply_token,
        #TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text

    if text == '!profile':
        if isinstance(event.source, SourceGroup):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='用戶名稱: \n' + profile.display_name + '\nUser id: \n' + profile.user_id))
        elif isinstance(event.source, SourceRoom):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='用戶名稱: \n' + profile.display_name + '\nUser id: \n' + profile.user_id))
        else:
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='用戶名稱: \n' + profile.display_name + '\nUser id: \n' + profile.user_id + '\n用戶照片: \n' + profile.picture_url))

    elif text == '!id':
        if isinstance(event.source, SourceGroup):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=profile.user_id))
        elif isinstance(event.source, SourceRoom):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=profile.user_id))
        else:
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=profile.user_id))

    elif text == '!name':
        if isinstance(event.source, SourceGroup):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=profile.display_name))
        elif isinstance(event.source, SourceRoom):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=profile.display_name))
        else:
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=profile.display_name))

    elif text == '!bye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='大家掰掰～'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='大家掰掰～'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="好,掰掰~\n\n\n騙你的啦～私人聊天沒有辦法退出..."))

    elif text.lower() == "!time":
        now = strftime('%Y-%m-%d %I:%M:%S %p')
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=now))

    elif text in ['作者','Creator','creator','Author','author']:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='darkkingtw.cf 協助製作'))
    elif text in ['安','安安','ㄤㄤ','ㄤ']:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='安呦～'))
    elif text == "μ'sic♪":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="μ'sic♪萬歲"))
    elif text == "信μ'sic♪得永生":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生\n信μ'sic♪得永生"))
    elif text in ['白痴','87']:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='不要自我介紹#'))
    elif text == "μ'sic♪萬歲":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="一日μ'sic♪\n終日μ'sic♪\n生為μ'sic♪人\n死為μ'sic♪鬼\n\nμ'sic♪forever♪"))
    elif text in ['嗨嗨','嗨','hi','hihi']:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你好'))
    elif text in ['自我介紹','自介']:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="你好，我是μ'sic♪機器人\n蕾米莉亞·斯卡雷特\n想知道作者是誰，請輸入「作者」"))
    elif text in ['再見','88','8','bye bye','bye']:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='再見~'))
    elif text == '早安':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='早安~'))
    elif text == '晚安':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='晚安啊~'))
    elif text == '午安':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='午安~'))
    elif text == "μ'sic♪官方":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='https://line.me/R/ti/p/%40eks7289f'))
    elif text == '頭香':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='二香'))
    elif text == "/洗版":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪ ∪･ω･∪'))
    elif text == "∪･ω･∪":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='信∪･ω･∪得永生'))
    elif text == "恭喜":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發財'))
    elif text == '東方萬歲':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='今生無悔入東方 來世願生幻想鄉\n紅魔地靈夜神雪 永夜風神星蓮船\n非想天則文花帖 萃夢神靈緋想天\n冥界地獄異變起 櫻下華胥主謀現\n凈罪無改渡黃泉 華鳥風月是非辨\n境界顛覆入迷途 幻想花開嘯風弄\n二色花蝶雙生緣 前緣未盡今生還\n星屑灑落雨霖鈴 虹彩慧光銀塵耀\n無壽迷蝶彼岸歸 幻真如畫妖如月\n永劫夜宵哀傷起 幼社靈中幻似夢\n追憶往昔巫女緣 許彌之間冥夢\n人榀華誕井中天 歌雅風頌心無念\n不求間隙一紫妹 但求回眸望幽香\n生死夢寄永遠亭 孤魂永伴迷途林\n白玉樓前西行櫻 花開無緣彼岸川\n何處覓得妖怪山 千年神戀絕不厭\n此生唯一是紅白 黑白魔女串門來\n\n喜歡東方\n只因為我希望生在美麗，神聖的[幻想鄉]，\n那是，與世隔絕的世外桃源，\n那是，沒有煩惱，無憂無慮的一方淨土。'))
    elif text == '東方無限好':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='只因為我希望生在美麗，神聖的[幻想鄉]，\n那是，與世隔絕的世外桃源，\n那是，沒有煩惱，無憂無慮的一方淨土。'))
    elif text == "大家好":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你好'))
    elif text in ['姐姐大人','姊姊大人']:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='才不是笨蛋呢！'))
    elif text == '明夫':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='很可愛'))
    elif text == '030':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='030'))
    elif text == '0.0':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='0.0'))
    elif text == '哞':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='咲夜！這裏有一隻牛'))
    elif text == '呱':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='咲夜！這裏有一隻鴨'))
    elif text == '1':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='2'))
    elif text == '唧':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='咲夜！這裏有一隻蟬'))
    elif text == '嘶':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='咲夜！這裏有一條蛇'))
    elif text == '卡卡西':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='萬歲'))
    elif text == '儀式開始':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='開始啊*^O^*'))
    elif text == '儀式完畢':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='謝謝觀賞*^O^*'))
    elif text == '(｀・ω・´)':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='(｀・ω・´)'))
    elif text == 'WTF':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='Welcome to Facebook'))
    elif text == '幹':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='嘛'))
    elif text == '幹你娘':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='我沒有娘'))
    elif text == '智障':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='我不是智障啦OAQ'))
    elif text == '乾':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='乾的話去喝水吧'))
    elif text == '好無聊':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='睡毛起來嗨〓'))
    elif text == '企鵝':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='[ 企鵝さんの共有 ]\n\nline://home/post?userMid=udc1cda40c2a20aa90081e481ca4f2249&postId=1146843819404033946'))
    elif text == '(´・ω・｀)':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='(´・ω・｀)'))
    elif text == 'UR':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你抽不到'))
    elif text == '晨曦':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='吸塵器'))
    elif text == '茵':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='偽娘一枚'))
    elif text == 'explosion':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='炸毛啊！？'))
    elif text == "μ'sic♪pv":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="μ'sic♪pv\n\nhttps://youtu.be/5luWaePm09w"))
    elif text == '7+1':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='你就是很丑还要问什么7+1'))
    elif text == '千代':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='絕緣人'))
    elif text == '流星':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='可愛小弟'))
    elif text == '科科':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='草泥馬'))
    elif text == '月漪':
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='超級大帥哥'))


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
