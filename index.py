from flask import Flask, request
from mock import mock_db
app = Flask(__name__)

@app.route('/get_user_info', methods=['POST'])
def get_user_info():
    key_word = request.json.get('key_word','')
    user_info = mock_db(key_word)
    if user_info:
        return 'POST :%s Response: :%s' % (key_word, user_info)
    else:
        return 'cannot find %s' % key_word

@app.route('/')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run()