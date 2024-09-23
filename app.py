import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, redirect, url_for, session, render_template
import requests

load_dotenv()

HTTP_API = os.getenv("API_URL")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form.get('url')

    data = {
        "url":url
    }
    print(HTTP_API)
    response = requests.post(url=HTTP_API + "download",json=data)    
    response_data = response.json()
    return redirect(response_data.get('aws_url'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000', debug=True)