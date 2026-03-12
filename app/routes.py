from flask import request, jsonify, render_template
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.chatbot import Chatbot
from app.cache import faq_cache
from app.analytics import analytics
import uuid

MAX_MESSAGE_LENGTH = 500

bot = Chatbot()
sessions = {}


def register_routes(app):

    limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day"])

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/chat", methods=["POST"])
    @limiter.limit("10 per minute")
    def chat():

        data = request.json
        message = data.get("message")
        session_id = data.get("session_id")

        if not message:
            return jsonify({"error": "Message required"}), 400

        if len(message) > MAX_MESSAGE_LENGTH:
            return jsonify({"error": "Message too long"}), 400

        message_lower = message.lower().strip()

        if not session_id or session_id not in sessions:
            session_id = str(uuid.uuid4())
            sessions[session_id] = []

        user_messages = sessions[session_id]

        # Cache check
        if message_lower in faq_cache:
            analytics["cache_hits"] += 1
            analytics["total_messages"] += 1

            return jsonify({
                "reply": faq_cache[message_lower],
                "session_id": session_id,
                "cached": True,
                "status": "success"
            })

        try:
            reply = bot.chat(message, user_messages)

            faq_cache[message_lower] = reply

            analytics["llm_calls"] += 1
            analytics["total_messages"] += 1

            return jsonify({
                "reply": reply,
                "session_id": session_id,
                "cached": False,
                "status": "success"
            })

        except Exception:
            return jsonify({
                "status": "error",
                "message": "AI service temporarily unavailable."
            }), 503

    @app.route("/analytics")
    def analytics_dashboard():
        return jsonify(analytics)