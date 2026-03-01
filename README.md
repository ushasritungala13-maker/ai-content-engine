# 🚀 AI Content Generation Engine

An intelligent AI-powered content generation system built using Flask.  
This project enables dynamic generation of multiple content types such as LinkedIn posts, professional emails, and advertisements using structured prompt engineering techniques.

---

## 📌 Project Overview

The AI Content Generation Engine is designed to create personalized, structured, and high-quality content based on user-defined parameters such as:

- Tone (Professional, Casual, Persuasive, Friendly)
- Target Audience
- Content Length (Short, Medium, Long)
- Keyword Inclusion
- Content Type Selection (LinkedIn Post, Email, Advertisement)

The system dynamically constructs prompts based on user input and generates formatted output specific to the selected content type.

---

## 🏗️ System Architecture

The project follows a **modular backend architecture** for scalability and maintainability.

### Backend Modules:

- `app.py` → Handles routing and request processing
- `prompt_engine.py` → Builds dynamic prompts based on input parameters
- `content_processor.py` → Applies content-specific formatting
- `templates/index.html` → Frontend user interface
- `static/style.css` → UI styling

This separation ensures clean code structure and easier future enhancements.

---

## ⚙️ Features

- Advanced Input Parameter System
- Multi-Content Type Generation Engine
- Dynamic Prompt Engineering
- Content-Specific Post-Processing
- Structured Output (Headline, Two Lines, CTA, Body)
- Clean and Professional UI
- Git Version Control Integration

---

## 🛠️ Tech Stack

- Python
- Flask
- HTML5
- CSS3
- Git & GitHub

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ai-content-engine.git
cd ai-content-engineend design
2️⃣ Install Dependencies
pip install flask
3️⃣ Run the Application
python app.py
4️⃣ Open in Browser
http://127.0.0.1:5000
🧠 How It Works

User selects input parameters from the form.

Flask captures the data using POST request.

The prompt engine constructs a dynamic prompt.

The content processor formats output based on content type.

Structured content is rendered back to the frontend.

🔮 Future Enhancements

Integration with OpenAI API for real AI-generated content

User authentication system

Export generated content as PDF

Store generated history in database

Deploy application online
