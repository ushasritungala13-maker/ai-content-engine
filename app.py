from flask import Flask, render_template, request
from prompt_engine import build_prompt
from content_processor import process_content

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    content_type = request.form.get("content_type")
    tone = request.form.get("tone")
    audience = request.form.get("audience")
    length = request.form.get("length")
    keywords = request.form.get("keywords")

    # Build prompt (for architecture purpose)
    prompt = build_prompt(content_type, tone, audience, length, keywords)

    # Paragraph generation based on length
    if length == "Short":
        body_text = f"This {content_type} is written in a {tone.lower()} tone for {audience}. It highlights {keywords} effectively."

    elif length == "Medium":
        body_text = f"This {content_type} is crafted in a {tone.lower()} tone specifically for {audience}. It naturally incorporates keywords such as {keywords}. The content is structured to engage readers while maintaining clarity and impact."

    else:  # Long
        body_text = f"""
This {content_type} is carefully developed in a {tone.lower()} tone for {audience}. 
It integrates important keywords such as {keywords} in a natural and engaging way. 
The objective is to provide meaningful insights, build credibility, and connect effectively with the target audience. 
By focusing on structure, clarity, and engagement, this content ensures maximum impact and professional presentation.
"""

    ai_output = {
        "headline": f"{tone} {content_type} for {audience}",
        "two_lines": "Create powerful content instantly.\nBoost engagement with AI-driven precision.",
        "cta": "Take Action Today!",
        "body": body_text
    }

    final_content = process_content(content_type, ai_output)

    return render_template("index.html", generated_content=final_content)


if __name__ == "__main__":
    app.run(debug=True)