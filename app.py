from flask import Flask, render_template, request, jsonify
import os
import cv2
import base64
import numpy as np
from werkzeug.utils import secure_filename
import google.generativeai as genai

# ------------------ CONFIG ------------------ #
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configure Gemini
genai.configure(api_key="AIzaSyADTeHFIcsrGWYMF7ywduAvN12MGvgOXyM")
model = genai.GenerativeModel("gemini-1.5-flash")

# Memory for frames
video_frames_base64 = []

# ------------------ FRAME EXTRACTION ------------------ #
def extract_frames(video_path, frame_rate=1):
    """Extract frames at a fixed rate (default: 1 frame/sec)."""
    frames = []
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = max(1, int(fps / frame_rate))
    frame_count = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        if frame_count % frame_interval == 0:
            _, buffer = cv2.imencode('.jpg', frame)
            frames.append(base64.b64encode(buffer).decode('utf-8'))
        frame_count += 1

    cap.release()
    return frames

# ------------------ GEMINI ANALYSIS ------------------ #
def analyze_video(video_path):
    global video_frames_base64
    video_frames_base64 = extract_frames(video_path, frame_rate=1)  # More frames for better answers
    return "Video processed successfully. You can now ask specific questions about it."

# ------------------ CHATBOT ------------------ #
@app.route('/chat', methods=['POST'])
def chat():
    global video_frames_base64
    data = request.json
    question = data.get("question", "")

    if not video_frames_base64:
        return jsonify({"answer": "No video analyzed yet. Please upload a video first."})

    try:
        # Send the question + frames to Gemini
        contents = [
            f"Answer the following question based only on the provided video frames:\n{question}",
        ]
        # Add frames as image parts
        for frame_b64 in video_frames_base64[:10]:  # Limit to avoid token overflow
            contents.append({"mime_type": "image/jpeg", "data": base64.b64decode(frame_b64)})

        response = model.generate_content(contents)
        answer = response.text.strip() if response.text else "I couldn't determine the answer."

        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"answer": f"Error generating answer: {str(e)}"})

# ------------------ FLASK ROUTES ------------------ #
@app.route('/', methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST' and 'video' in request.files:
        file = request.files['video']
        if file.filename:
            filename = secure_filename(file.filename)
            video_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(video_path)
            message = analyze_video(video_path)
            try:
                os.remove(video_path)
            except:
                pass
    return render_template('index.html', summary=message)

if __name__ == '__main__':
    app.run(debug=True)

