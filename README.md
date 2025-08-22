# Visual Understanding Chat Assistant

## 🚀 Project Overview

A lightweight Flask-based assistant that:

- Accepts video uploads
- Extracts frames and generates summaries using Google Gemini API
- Allows conversational Q&A about the video content

Designed for hackathons, research, or early-stage projects involving **video understanding + conversational AI**.

---

## 🧠 High-Level Architecture Diagram

```text
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌──────────────────┐
│             │    │             │    │             │    │                  │
│   User      │───▶│   Flask     │───▶│   Frame     │───▶│   Google Gemini  │
│  (Browser)  │    │   Server    │    │ Extraction  │    │      API         │
│             │◀───│             │◀───│ (OpenCV)    │◀───│                  │
└─────────────┘    └─────────────┘    └─────────────┘    └──────────────────┘
       ▲                  ▲                     │                  │
       │                  │                     │                  │
       └──────────────────┘                     └──────────────────┘
                 Chat Interaction                      Video Analysis
```

---

## 🛠️ Tech Stack & Justifications

| Component           | Technology Used       | Justification                                                                 |
|---------------------|-----------------------|-------------------------------------------------------------------------------|
| Backend Framework   | Flask (Python)        | Lightweight, excellent for rapid prototyping and building simple REST APIs    |
| Video Processing    | OpenCV                | Industry standard for computer vision tasks with reliable frame extraction    |
| AI Model            | Google Gemini API     | Free tier available, excellent multimodal capabilities for video understanding|
| Storage             | Local filesystem      | Simplest solution for prototypes with no external dependencies                 |
| Frontend            | HTML + Jinja2         | Minimal frontend requirements met with server-side rendering                  |

---

## ⚙️ Installation

### ✅ Prerequisites

- Python 3.8+
- Google Cloud account (for Gemini API key)

### 📦 Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/visual-chat-assistant.git
   cd visual-chat-assistant
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

---

## 🧪 Usage

1. **Run the application:**
   ```bash
   flask run
   ```

2. **Access the web interface:**  
   Open your browser at `http://localhost:5000`

3. **Workflow:**
   - Upload a video file (MP4, MOV, AVI supported)
   - Wait for frame extraction and summary generation
   - View the summary
   - Chat with the assistant about the video

---

## 📁 Folder Structure

```text
visual-chat-assistant/
├── app.py                # Main application logic
├── requirements.txt      # Python dependencies
├── README.md             # This documentation
├── .env.example          # Environment variables template
├── .gitignore
├── uploads/              # Temporary video storage
├── templates/
│   └── index.html        # Frontend interface
└── venv/                 # Virtual environment (ignored)
```

---

## ⚠️ Limitations

- Only stores the **last uploaded** video summary in memory
- No user authentication or sessions
- Minimal error handling

---

## 🌱 Future Enhancements

- Persistent storage for video summaries and chat history
- Support for longer videos (chunked summarization)
- User accounts and multi-session support
- Audio transcription + scene detection

---


