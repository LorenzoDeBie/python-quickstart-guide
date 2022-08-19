from flask import Flask, request
from sub_controller import sub_page

app = Flask(__name__)
app.register_blueprint(sub_page)


@app.route("/")
def home():
    print(request.headers)
    return "Hello Flask!"
