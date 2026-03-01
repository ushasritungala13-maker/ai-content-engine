from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate-multi-content", methods=["POST"])
def generate_multi_content():
    data = request.json
    content_type = data.get("type", "linkedin")
    tone = data.get("tone", "professional")
    audience = data.get("audience", "")
    length = data.get("length", "medium")
    keywords = data.get("keywords", "")

    # Build dynamic prompt
    prompt = f"Write a {length} {content_type} in {tone} tone for {audience}."
    if keywords:
        prompt += f" Include keywords: {keywords}."

    # Call AI engine (placeholder)
    content = call_ai_engine(prompt)

    # Content-type-specific formatting
    if content_type == "linkedin":
        content = process_linkedin(content)
    elif content_type == "email":
        content = process_email(content)
    elif content_type == "ad":
        content = process_ad(content)

    return jsonify({"content": content})

def call_ai_engine(prompt):
    # Replace with your OpenAI / AI engine call
    return f"[Generated content based on prompt: {prompt}]"

# LinkedIn post: add hashtags
def process_linkedin(text):
    return text + "\n\n#Innovation #AI #Tech"

# Email: structured with subject and body
def process_email(text):
    return {"subject": "Your Subject Here", "body": text}

# Ad copy: add CTA
def process_ad(text):
    return text + "\nCall us today!"

if __name__ == "__main__":
    app.run(debug=True)