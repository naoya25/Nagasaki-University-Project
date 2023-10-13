from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
import os
from model import create_image

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('SECRET'))

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text
    # if create_image(text):
    messages = ImageSendMessage(
        original_content_url='./image.png',
        preview_image_url='./image.png'
    )
    line_bot_api.reply_message(
        event.reply_token, messages
    )
    # else:
    #     line_bot_api.reply_message(
    #         event.reply_token, TextSendMessage(text='画像生成に失敗しました')
    #     )

if __name__ == '__main__':
    app.run()
