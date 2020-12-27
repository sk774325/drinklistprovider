import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message, send_button_message, send_image_message

load_dotenv()


machine = TocMachine(
    states=[
            "gin", "gin_tonic", 'martini','nagroni',
            "vodka","screwdriver","vodka_lime",'moscow_mule','vodka_martini',
            "rum",'mojito','cuba_libre','blue_hawaii',
            "tequila",'margarita','tequila_sunrise','diablo',
            "brandy",'brandy_alexander','between_the_sheets','vieux_carre','horse_neck',
            "whisky",'godfather','highball','manhattan','whisky_sour'
            ],
    transitions=[
        {"trigger": "advance", "source": "user", "dest": "gin", "conditions": "is_going_to_gin",},
        {"trigger": "advance", "source": "gin", "dest": "gin_tonic", "conditions": "is_going_to_gin_tonic",},
        {"trigger": "advance", "source": "gin", "dest": "martini", "conditions": "is_going_to_martini",},
        {"trigger": "advance", "source": "gin", "dest": "nagroni", "conditions": "is_going_to_nagroni",},
        {"trigger": "advance", "source": "user", "dest": "vodka", "conditions": "is_going_to_vodka",},
        {"trigger": "advance", "source": "vodka", "dest": "screwdriver", "conditions": "is_going_to_screwdriver",},
        {"trigger": "advance", "source": "vodka", "dest": "vodka_lime", "conditions": "is_going_to_vodka_lime",},
        {"trigger": "advance", "source": "vodka", "dest": "moscow_mule", "conditions": "is_going_to_moscow_mule",},
        {"trigger": "advance", "source": "vodka", "dest": "vodka_martini", "conditions": "is_going_to_vodka_martini",},
        {"trigger": "advance", "source": "user", "dest": "rum", "conditions": "is_going_to_rum",},
        {"trigger": "advance", "source": "rum", "dest": "mojito", "conditions": "is_going_to_mojito",},
        {"trigger": "advance", "source": "rum", "dest": "cuba_libre", "conditions": "is_going_to_cuba_libre",},
        {"trigger": "advance", "source": "rum", "dest": "blue_hawaii", "conditions": "is_going_to_blue_hawaii",},
        {"trigger": "advance", "source": "user", "dest": "tequila", "conditions": "is_going_to_tequila",},
        {"trigger": "advance", "source": "tequila", "dest": "margarita", "conditions": "is_going_to_margarita",},
        {"trigger": "advance", "source": "tequila", "dest": "tequila_sunrise", "conditions": "is_going_to_tequila_sunrise",},
        {"trigger": "advance", "source": "tequila", "dest": "diablo", "conditions": "is_going_to_diablo",},
        {"trigger": "advance", "source": "user", "dest": "brandy", "conditions": "is_going_to_brandy",},
        {"trigger": "advance", "source": "brandy", "dest": "brandy_alexander", "conditions": "is_going_to_brandy_alexander",},
        {"trigger": "advance", "source": "brandy", "dest": "between_the_sheets", "conditions": "is_going_to_between_the_sheets",},
        {"trigger": "advance", "source": "brandy", "dest": "vieux_carre", "conditions": "is_going_to_vieux_carre",},
        {"trigger": "advance", "source": "brandy", "dest": "horse_neck", "conditions": "is_going_to_horse_neck",},
        {"trigger": "advance", "source": "user", "dest": "whisky", "conditions": "is_going_to_whisky",},
        {"trigger": "advance", "source": "whisky", "dest": "godfather", "conditions": "is_going_to_godfather",},
        {"trigger": "advance", "source": "whisky", "dest": "highball", "conditions": "is_going_to_highball",},
        {"trigger": "advance", "source": "whisky", "dest": "manhattan", "conditions": "is_going_to_manhattan",},
        {"trigger": "advance", "source": "whisky", "dest": "whisky_sour", "conditions": "is_going_to_whisky_sour",},
        {
            "trigger": "go_back", 
            "source": [
                    "gin_tonic", 'martini','nagroni',
                    "screwdriver","vodka_lime",'moscow_mule','vodka_martini', 
                    'mojito','cuba_libre','blue_hawaii', 
                    'margarita','tequila_sunrise','diablo', 
                    'brandy_alexander','between_the_sheets','vieux_carre','horse_neck',
                    'godfather','highball','manhattan','whisky_sour'
                    ], 
            "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")

        response = machine.advance(event)

        if response == False:
            if event.message.text.lower() == 'fsm':
                send_image_message(event.reply_token, 'https://i.imgur.com/JsP8Ogj.png')
            else:
                send_text_message(event.reply_token, "請輸入想要的基酒名稱：")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
