from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)

# Configure the Gemini API
genai.configure(api_key="AIzaSyB2UMm-eoesafVu6dJFRGoSGLQKkP-HSc8")
model = genai.GenerativeModel("gemini-pro")

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle the form submission via POST request
@app.route('/generate', methods=['POST'])
def generate_text():
    prompt = request.form['prompt']  # Get the prompt from the form
    response = model.generate_content(prompt)  # Generate text using Gemini model
    return jsonify({'response': response.text})  # Return the generated text as JSON

if __name__ == '__main__':
    app.run(debug=True)


# import google.generativeai as genai

# # Configure the Gemini API
# genai.configure(api_key="AIzaSyB2UMm-eoesafVu6dJFRGoSGLQKkP-HSc8")

# # Choose the Gemini model you want to use
# model = genai.GenerativeModel("gemini-pro")  

# # Prompt for user input
# while True:
#     prompt = input("Enter your prompt: ")
#     # Generate text using the Gemini model
#     response = model.generate_content(prompt)
#     print(response.text)
#     print("\n")


