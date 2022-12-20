import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

#Ex https://theriturajps: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@github.com/theriturajps/File-Sharing
os.system("git clone https://theriturajps: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@github.com/theriturajps/File-Sharing ok && cd ok && pip3 install -U -r requirements.txt && nohup python3 main.py &")
