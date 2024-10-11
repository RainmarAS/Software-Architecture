from flask import Blueprint, request, jsonify
from models import db, Message
import requests

message_bp = Blueprint('message_bp', __name__)

@message_bp.route('/messages', methods=['POST'])
def post_message():
    data = request.get_json()
    user_id = data['user_id']
    content = data['content']
    if len(content) > 400:
        return jsonify({"error": "Message exceeds 400 characters"}), 400
    # Verify user exists
    user_response = requests.get(f'http://localhost:5001/users/{user_id}')
    if user_response.status_code != 200:
        return jsonify({"error": "User not found"}), 404
    new_message = Message(user_id=user_id, content=content)
    db.session.add(new_message)
    db.session.commit()
    return jsonify({"message_id": new_message.id}), 201

@message_bp.route('/feed', methods=['GET'])
def get_feed():
    messages = Message.query.order_by(Message.timestamp.desc()).limit(10).all()
    feed = []
    for message in messages:
        user_response = requests.get(f'http://localhost:5001/users/{message.user_id}')
        user_data = user_response.json()
        feed.append({
            "message_id": message.id,
            "username": user_data['username'],
            "content": message.content,
            "timestamp": message.timestamp
        })
    return jsonify(feed), 200

@message_bp.route('/messages/<int:message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.query.get(message_id)
    if not message:
        return jsonify({"error": "Message not found"}), 404
    return jsonify({
        "message_id": message.id,
        "user_id": message.user_id,
        "content": message.content,
        "timestamp": message.timestamp
    }), 200