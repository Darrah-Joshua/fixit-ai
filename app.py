# from flask import Flask, render_template, request
# import openai
# import os
# from dotenv import load_dotenv 

# load_dotenv()

# app = Flask(__name__)
# openai.api_key = os.getenv("OPENAI_API_KEY")

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route("/code", methods=["GET", "POST"])
# def fix_code():
#     fixed_code = ""
#     if request.method == "POST":
#         user_code = request.form["code"]
#         response = openai.ChatCompletion.create(
#             model = "gpt-4",
#             messages = [
#                 {"role": "system", "content": "You are an expert software developer."},
#                 {"role": "user", "content": f"Fix this code and explain the fix:\n{user_code}"} 
#             ]
#         )
#         fixed_code = response.choices[0].message.content
#     return render_template("code.html", fixed_code = fixed_code)

# @app.route("/grammar", methods=["GET", "POST"])
# def fix_grammar():
#     corrected = ""
#     if request.method == "POST":
#         user_text = request.form["text"]
#         response = openai.ChatCompletion.create(
#             model="gpt-4",
#             messages=[
#                 {"role": "system", "content": "You are a writing assistant that corrects grammar."},
#                 {"role": "user", "content": f"Correct the grammar and explain:\n{user_text}"}
#             ]
#         )
#         corrected = response.choices[0].message.content
#     return render_template("grammar.html", corrected=corrected)


# if __name__ == "__main__":
#     app.run(debug=True)






# from flask import Flask, render_template, request
# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route("/code", methods=["GET", "POST"])
# def fix_code():
#     fixed_code = ""
#     if request.method == "POST":
#         user_code = request.form["code"]
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are an expert software developer."},
#                 {"role": "user", "content": f"Fix this code and explain the fix:\n{user_code}"}
#             ]
#         )
#         fixed_code = response.choices[0].message.content
#     return render_template("code.html", fixed_code=fixed_code)

# @app.route("/grammar", methods=["GET", "POST"])
# def fix_grammar():
#     corrected = ""
#     if request.method == "POST":
#         user_text = request.form["text"]
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": "You are a writing assistant that corrects grammar."},
#                 {"role": "user", "content": f"Correct the grammar and explain:\n{user_text}"}
#             ]
#         )
#         corrected = response.choices[0].message.content
#     return render_template("grammar.html", corrected=corrected)

# if __name__ == "__main__":
#     app.run(debug=True)






# from flask import Flask, render_template, request
# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# app = Flask(__name__)

# # DeepSeek API configuration
# DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
# DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"  # Correct endpoint

# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route("/code", methods=["GET", "POST"])
# def fix_code():
#     fixed_code = ""
#     if request.method == "POST":
#         user_code = request.form["code"]
        
#         headers = {
#             "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#             "Content-Type": "application/json"
#         }
        
#         payload = {
#             "model": "deepseek-chat",  # Make sure this is a valid model name from DeepSeek
#             "messages": [
#                 {"role": "system", "content": "You are an expert software developer."},
#                 {"role": "user", "content": f"Fix this code and explain the fix:\n{user_code}"}
#             ]
#         }
        
#         response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
#         response_data = response.json()
        
#         if response.status_code == 200:
#             fixed_code = response_data["choices"][0]["message"]["content"]
#         else:
#             error_message = response_data.get("error", {}).get("message") or response_data.get("error") or response.text
#             fixed_code = f"❌ Error: {error_message}"
    
#     return render_template("code.html", fixed_code=fixed_code)

# @app.route("/grammar", methods=["GET", "POST"])
# def fix_grammar():
#     corrected = ""
#     if request.method == "POST":
#         user_text = request.form["text"]
        
#         headers = {
#             "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
#             "Content-Type": "application/json"
#         }
        
#         payload = {
#             "model": "deepseek-chat",  # Ensure model name is correct
#             "messages": [
#                 {"role": "system", "content": "You are a writing assistant that corrects grammar."},
#                 {"role": "user", "content": f"Correct the grammar and explain:\n{user_text}"}
#             ]
#         }
        
#         response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
#         response_data = response.json()
        
#         if response.status_code == 200:
#             corrected = response_data["choices"][0]["message"]["content"]
#         else:
#             error_message = response_data.get("error", {}).get("message") or response_data.get("error") or response.text
#             corrected = f"❌ Error: {error_message}"
    
#     return render_template("grammar.html", corrected=corrected)

# if __name__ == "__main__":
#     app.run(debug=True)







from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = "https://api.openai.com/v1"
MODEL_NAME = "gpt-3.5-turbo"

client = OpenAI(
    base_url=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/code", methods=["GET", "POST"])
def fix_code():
    fixed_code = ""
    if request.method == "POST":
        user_code = request.form["code"]
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are an expert software developer."},
                    {"role": "user", "content": f"Fix this code and explain the fix:\n{user_code}"}
                ]
            )
            fixed_code = response.choices[0].message.content
        except Exception as e:
            fixed_code = f"❌ Error: {str(e)}"
    return render_template("code.html", fixed_code=fixed_code)

@app.route("/grammar", methods=["GET", "POST"])
def fix_grammar():
    corrected = ""
    if request.method == "POST":
        user_text = request.form["text"]
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful writing assistant that fixes grammar and explains the changes."},
                    {"role": "user", "content": f"{user_text}"}
                ]
            )
            corrected = response.choices[0].message.content
        except Exception as e:
            corrected = f"❌ Error: {str(e)}"
    return render_template("grammar.html", corrected=corrected)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_API_BASE = "https://api.openai.com/v1"
MODEL_NAME = "gpt-3.5-turbo"

client = OpenAI(
    base_url=OPENAI_API_BASE,
    api_key=OPENAI_API_KEY
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/code", methods=["GET", "POST"])
def fix_code():
    fixed_code = ""
    if request.method == "POST":
        user_code = request.form["code"]
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are an expert software developer."},
                    {"role": "user", "content": f"Fix this code and explain the fix:\n{user_code}"}
                ]
            )
            fixed_code = response.choices[0].message.content
        except Exception as e:
            fixed_code = f"❌ Error: {str(e)}"
    return render_template("code.html", fixed_code=fixed_code)

@app.route("/grammar", methods=["GET", "POST"])
def fix_grammar():
    corrected = ""
    if request.method == "POST":
        user_text = request.form["text"]
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[
                    {"role": "system", "content": "You are a helpful writing assistant that fixes grammar and explains the changes."},
                    {"role": "user", "content": f"{user_text}"}
                ]
            )
            corrected = response.choices[0].message.content
        except Exception as e:
            corrected = f"❌ Error: {str(e)}"
    return render_template("grammar.html", corrected=corrected)

if __name__ == "__main__":
    app.run(debug=True)
