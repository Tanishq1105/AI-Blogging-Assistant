# 🚀 AI Blogging Assistant 

An advanced AI-powered blog generation app built with **Streamlit** and **Google Gemini API**.
Generate high-quality, SEO-optimized blogs with multiple writing styles, streaming output, and export options.

---

## ✨ Features

* ⚡ **Streaming Output** (real-time typing effect)
* 🔍 **SEO Enhancement** (AI improves blog quality)
* 🎯 **Title Generator**
* 🎨 Multiple Writing Styles:

  * SEO-Optimized
  * Casual
  * Technical
  * Storytelling
* 🔁 **Retry Logic** (handles API failures)
* 💾 **Session History** (view previous blogs)
* 📄 **Export Options**:

  * Download as TXT
  * Download as PDF
* 📊 Token Estimation (cost awareness)
* 🔐 Secure API key handling using `.env`

---

## 🧱 Project Structure

```
project/
│── app.py
│── config.py
│── llm_client.py
│── prompt_builder.py
│── seo.py
│── utils.py
│── pdf_export.py
│── .env
│── .gitignore
│── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-blog-generator.git
cd ai-blog-generator
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```
GOOGLE_API_KEY=your-api-key
MODEL_NAME=models/gemini-flash-latest
APP_ENV=development
MAX_RETRIES=3
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. User enters blog details (title, keywords, style)
2. Prompt is generated dynamically
3. AI generates blog content (streamed or full)
4. Optional SEO enhancement is applied
5. Blog is displayed, stored, and available for download

---

## 🔐 Security

* API keys are stored in `.env`
* `.env` is excluded via `.gitignore`
* No secrets are hardcoded

---

## 📦 Dependencies

* streamlit
* google-generativeai / google-genai
* python-dotenv
* reportlab

---

## 🚀 Future Improvements

* 🔐 User authentication
* ☁️ Cloud deployment
* 💰 API usage tracking
* 📊 Analytics dashboard
* 🧾 Export to DOCX

---

## 🤝 Contributing

Pull requests are welcome!
For major changes, open an issue first.

---

## 📄 License

This project is open-source and available under the MIT License.

---

## 💡 Author

Built as an advanced AI project for learning and real-world usage.
