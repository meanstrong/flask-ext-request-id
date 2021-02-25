# flask-request-id - 一个Flask每次接收请求时生成request_id的模块

## About
一个Flask每次接收请求时生成request_id的模块。  

## Requirements
- Python3

## Install
通过pip命令安装：
```shell
pip install flask-ext-request-id
```

## Usage
```python
from flask import Flask
from flask_ext_request_id import RequestId

app = Flask(__name__)
request_id = RequestId(app)

@app.route("/hello")
def hello():
    return request_id.current_id
```

## Author
- <a href="mailto:pmq2008@gmail.com">Rocky Peng</a>
