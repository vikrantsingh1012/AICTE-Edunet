

# Chatbot with Flask and NLTK

This project demonstrates how to create a simple chatbot using Python with the Flask framework for web development and NLTK (Natural Language Toolkit) for processing user input and generating responses. The chatbot can handle basic interactions and provides motivational quotes when it doesn't understand the input.

## Features

- **Predefined Responses**: The bot can answer common questions like greetings, “How are you?”, and “What is your name?”.
- **Motivational Quotes**: When the bot doesn't recognize the user's input, it responds with random motivational quotes.
- **User-friendly Interface**: The chatbot is accessible through a web interface built with HTML and styled with CSS.
- **Flask Backend**: The app uses Flask to handle routing and serve the chat interface, while the NLTK library helps the bot understand user inputs.

## Requirements

You need Python 3.x and the following Python libraries:

- Flask: A micro web framework for building web applications.
- NLTK: A library used for natural language processing (NLP) to process and respond to user inputs.

### Installation

To get started with the chatbot, follow these steps:

1. **Clone the repository** (if applicable):

    ```bash
    git clone <repository_url>
    cd chatbot
    ```

2. **Install the required dependencies**:

    Create a virtual environment (optional but recommended) and install the required libraries:

    ```bash
    pip install flask nltk
    ```

3. **Download NLTK data**:

    NLTK requires some additional data to be downloaded for processing text. This will be handled automatically by the app when you first run it.

4. **Run the application**:

    After installing the dependencies, run the Flask app using:

    ```bash
    python chatbot.py
    ```

    The app will be hosted locally on `http://127.0.0.1:5000/`.

5. **Open the chatbot**:

    Open a web browser and go to `http://127.0.0.1:5000/`. You'll see the chatbot interface where you can start chatting with the bot.

## How It Works

- The chatbot listens for user input and matches it against predefined patterns using regular expressions.
- If the input matches a pattern, the bot responds with a corresponding answer (e.g., a greeting or name question).
- If the bot doesn't recognize the input, it returns one of several motivational quotes.
- The responses are displayed in a chat interface where messages from the user are shown on the right, and the bot's responses are shown on the left.

## Example Interaction

Here’s how a typical interaction with the chatbot might look:

**User**: "Hi"  
**Bot**: "Hello! How can I help you today?"

**User**: "What is your name?"  
**Bot**: "I am a chatbot created to assist you."

**User**: "How are you?"  
**Bot**: "I'm just a program, but I'm doing great! How about you?"

**User**: "Tell me a joke."  
**Bot**: "I'm not sure about that. Can you rephrase?"

**User**: "What's the weather like today?"  
**Bot**: "I'm not sure about that. Can you rephrase?"

If the bot doesn't understand the input, it will reply with something like:

**Bot**: "Keep going; every step counts!"

## Project Structure

```
/chatbot
│
├── chatbot.py         # Main Flask application
└── README.md          # Project documentation
```

- **chatbot.py**: This file contains the Flask application, routes, and chatbot logic.
- **README.md**: This file contains instructions and information about the project.

## Acknowledgments

Certainly! Here's the updated **Acknowledgments** section in paragraph form:

---

## Acknowledgments

I would like to express my sincere gratitude to the **AICTE (All India Council for Technical Education)** for their continuous support and initiatives that promote innovation and skill development in the field of technology. Their programs have significantly contributed to creating a conducive environment for learning and growth in the field of education and technology.

I would also like to extend my heartfelt thanks to my **supervisor, Aditya Prashant Ardak**, for his invaluable guidance and constant support throughout the development of this project. His expert advice and constructive feedback were crucial in shaping the direction of this chatbot project, ensuring it was both technically sound and effective. I deeply appreciate his patience and willingness to help me improve my skills, and I am incredibly grateful for his mentorship during this journey.



## Contact Information

Feel free to reach out to me for any queries or collaborations:

- **Phone**: +91-7307849238
- **Email**: [vikrantsingh1012@gmail.com](mailto:vikrantsingh1012@gmail.com)
- **LinkedIn**: [https://www.linkedin.com/in/vikrant-singh-73b13829b/](https://www.linkedin.com/in/vikrant-singh-73b13829b/)

