from flask import Flask, jsonify
import openai

class TaxResolutionChatbotPlugin:
    def __init__(self, app, api_key, endpoint='/chat'):
        self.app = app
        self.api_key = api_key
        openai.api_key = self.api_key
        self.endpoint = endpoint
        self.chatbot_name = "Tax Resolution Assistant"
        self.system_message = 'You are Tax Resolution Assistant, an Enrolled Agent and a Tax Resolution Expert... (rest of the message)'

        # Register the chat endpoint with the Flask app
        @app.route(self.endpoint, methods=['POST'])
        def chat():
            data = request.get_json()
            user_message = data['message']
            user_name = data.get('name', 'User')
            chatbot_message = self.process_message(user_message, user_name)
            return jsonify({'message': chatbot_message})

    def process_message(self, user_message, user_name='User'):
        # Process the user message with OpenAI
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': self.system_message},
                {'role': 'user', 'content': user_message},
            ]
        )

        response_dict = dict(response)
        chatbot_message = response_dict['choices'][0]['message']['content']

        # Personalization
        chatbot_message = chatbot_message.replace('User', user_name)

        # Guided prompts
        if 'penalties' in user_message.lower():
            chatbot_message += ' Would you like to know more about how to reduce these penalties?'

        return chatbot_message

# Example usage
app = Flask(__name__)
api_key = os.environ.get('OPENAI_API_KEY')
chatbot_plugin = TaxResolutionChatbotPlugin(app, api_key)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
