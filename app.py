# app.py
from flask import Flask, render_template, request, jsonify
# Import our optimized chatbot class
from chatbot_engine import RuleBot

app = Flask(__name__)  # Create a Flask app instance

# Create an instance of our chatbot
chatbot = RuleBot()


# Define the route for the homepage
@app.route('/')
def home():
    # This renders the 'index.html' template
    return render_template('index.html')


# Define the route to handle chat messages (API endpoint)
@app.route('/get_response', methods=['POST'])
def get_bot_response():
    try:
        # Get the 'message' data sent from the JavaScript via POST request
        user_message = request.form['message']

        # Get the bot's response by calling our core function
        bot_response = chatbot.match_reply(user_message)

        # Return the response as JSON so JavaScript can easily use it
        return jsonify({'status': 'success', 'response': bot_response})

    except Exception as e:
        # In case something goes wrong, return an error message
        return jsonify({'status': 'error', 'response': str(e)})


# Run the app if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)  # debug=True helps with development