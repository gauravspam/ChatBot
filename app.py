from groq import Groq
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key="message_me")

def ask_groq(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",  # Free model
    )
    return chat_completion.choices[0].message.content

@app.route("/chatbot", methods=["GET"])
def chatbot_page():
    return render_template("chatbot.html")

@app.route("/get")
def get_msg():
    user_msg = request.args.get('msg')
    try:
        response = ask_groq(user_msg)
        return jsonify({"reply": response})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

