from flask import Blueprint, request, jsonify
from models import db, Like
import requests

like_bp = Blueprint('like_bp', __name__)

@like_bp.route('/messages/<int:message_id>/like', methods=['POST'])
def like_message(message_id):
    data = request.get_json()
    user_id = data['user_id']
    # Verify user exists
    user_response = requests.get(f'http://localhost:5001/users/{user_id}')
    if user_response.status_code != 200:
        return jsonify({"error": "User not found"}), 404
    # Verify message exists
    message_response = requests.get(f'http://localhost:5002/messages/{message_id}')
    if message_response.status_code != 200:
        return jsonify({"error": "Message not found"}), 404
    new_like = Like(user_id=user_id, message_id=message_id)
    db.session.add(new_like)
    db.session.commit()
    return jsonify({"status": "success"}), 201