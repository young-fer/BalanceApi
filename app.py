from flask import Flask
from flask import request
import BalanceModifier

app = Flask(__name__)


@app.route('/')
def hello_balance():
    return 'Hello Balance!'


@app.route('/WeChat', methods=['POST'])
def wechat_balance():
    balance = None
    if request.method == 'POST':
        print(request.form)
        balance = request.form['balance']
        BalanceModifier.cover_up_balance()
        BalanceModifier.we_chat_balance_change(balance)
        return {
            "base64": BalanceModifier.screenshot_base64()
        }

    return 'error'


if __name__ == '__main__':
    app.run()
