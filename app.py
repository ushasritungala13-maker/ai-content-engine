from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    tone = request.form['tone']
    audience = request.form['audience']
    length = request.form['length']
    keywords = request.form['keywords']
    content_type = request.form['content_type']

    # Temporary Demo Output (Replace with LLM later)
    generated_content = f"""
    Generated {content_type} for {audience}
    Tone: {tone}
    Length: {length}
    Keywords: {keywords}
    """

    return render_template("index.html", generated_content=generated_content)

if __name__ == '__main__':
    app.run(debug=True)