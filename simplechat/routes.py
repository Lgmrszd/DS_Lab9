from simplechat import app
from flask import render_template, jsonify, request, abort
from simplechat.messaging import Message


@app.route('/')
def index():
    return render_template("index.html", title="Main page")


@app.route('/api/messages', methods=['GET'])
def api_get_messages():
    messages = Message.get_messages()
    return jsonify(messages)


@app.route('/api/messages', methods=['POST'])
def api_post_message():
    if not request.json or "name" not in request.json or "text" not in request.json:
        abort(400)
    name = request.json["name"]
    text = request.json["text"]
    if len(name) == 0 or len(text) == 0:
        abort(400)
    Message.send_message(name, text)
    return "Ok"
