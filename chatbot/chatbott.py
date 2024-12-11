# Install the required dependencies before running the code
# pip install flask
# pip install nltk

from flask import Flask, request, jsonify
import nltk
from nltk.chat.util import Chat, reflections
import random

# Ensure NLTK data is downloaded
nltk.download("punkt")

app = Flask(__name__)

# Define chatbot pairs (predefined questions and responses)
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! How can I assist?"]],
    [r"what is your name\??", ["I am a chatbot created to assist you."]],
    [r"how are you\??", ["I'm just a program, but I'm doing great! How about you?"]],
    [r"bye|exit|quit", ["Goodbye! Have a nice day!", "See you soon!"]],
    [r"(.*)", [
        "I'm not sure about that. Can you rephrase?", 
        "Stay positive and keep pushing forward!", 
        "Believe in yourself—you can achieve great things!",
        "Every challenge is an opportunity to grow."]], 
]

# Initialize the chatbot
def chatbot_response(user_input):
    chatbot = Chat(pairs, reflections)
    response = chatbot.respond(user_input)
    # Add motivational quotes randomly
    if response in ["I'm not sure about that. Can you rephrase?"]:
        motivational_quotes = [
            "Keep going; every step counts!",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Believe in your infinite potential. Your only limitations are those you set upon yourself.",
            "Dream big and dare to fail.",
        ]
        response = random.choice(motivational_quotes)
    return response

# Define the home route with embedded HTML
@app.route('/')
def index():
    return '''
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
        }
        .chatbox {
            width: 90%;
            max-width: 500px;
            border: 1px solid #ccc;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
            background: linear-gradient(to bottom right, #ffffff, #f3f3f3);
            color: #333;
            display: flex;
            flex-direction: column;
        }
        .messages {
            height: 300px;
            overflow-y: auto;
            border: 1px solid #ddd;
            margin-bottom: 15px;
            padding: 10px;
            border-radius: 10px;
            background: linear-gradient(to bottom, #f9f9f9, #e6e6e6);
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }
        .messages div {
            margin: 10px 0; /* Added spacing between messages */
            padding: 10px;
            border-radius: 5px;
            max-width: 70%;
            word-wrap: break-word;
        }
        .user {
            text-align: right;
            color: #007bff;
            background-color: #cce5ff;
            display: inline-block;
            padding: 5px 10px;
            border-radius: 5px;
            margin-left: auto; /* Align the user's messages to the right */
        }
        .bot {
            text-align: left;
            color: #28a745;
            background-color: #d4edda;
            display: inline-block;
            padding: 5px 10px;
            border-radius: 5px;
            margin-right: auto; /* Align the bot's messages to the left */
        }
        input {
            flex-grow: 1;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            font-size: 16px;
            margin-right: 10px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: #fff;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.2s;
        }
        button:hover {
            background-color: #0056b3;
            transform: scale(1.05);
        }
        .chat-input {
            display: flex;
            align-items: center;
        }
    </style>
</head>
<body>
    <div class="chatbox">
        <div class="messages" id="chatMessages"></div>
        <div class="chat-input">
            <input type="text" id="userInput" placeholder="Type your message here...">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>

    <script>
        const messagesDiv = document.getElementById('chatMessages');

        function appendMessage(content, className) {
            const message = document.createElement('div');
            message.textContent = content;
            message.className = className;
            messagesDiv.appendChild(message);
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }

        async function sendMessage() {
            const userInput = document.getElementById('userInput');
            const message = userInput.value.trim();

            if (!message) return;

            appendMessage(message, 'user'); // User's message on the right
            userInput.value = '';

            const response = await fetch('/get_response', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message }),
            });

            const data = await response.json();
            appendMessage(data.response, 'bot'); // Bot's response on the left
        }
    </script>
</body>
</html>

    '''

# API endpoint for chatbot communication
@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get("message")
    response = chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
