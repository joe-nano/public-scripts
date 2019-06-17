import flask
import requests


def alert_api(request):
    """
    Sample call: https://asia-east2-viet-grade.cloudfunctions.net/Alert-API?message=ABC
    """
    msg = request.args.get('message')
    __send_message(msg)
    return flask.jsonify({"status": "done"})


def __send_message(msg):
    '''
    Send message via telegram bot
    :param msg:
    :return:
    '''

    TELEGRAM_TOKEN = 'TELEGRAM_TOKEN_ID'
    TELEGRAM_CHAT_ID = 'TELEGRAM_CHANNEL_ID'

    # For payload params refer: https://core.telegram.org/bots/api#sendmessage
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': msg,
        'parse_mode': 'HTML'
    }
    return requests.post('https://api.telegram.org/bot{token}/sendMessage'.format(token=TELEGRAM_TOKEN),
                         data=payload).content