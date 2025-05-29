from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/api/voice', methods=['POST'])
def voice():
    data = request.get_json()
    transcript = data.get('transcript', '').strip()
    if transcript:
        print(f"[ash-voice-relay] Received transcript: {transcript}")
        try:
            response = subprocess.check_output(['ashctl', transcript], text=True).strip()
            return jsonify({ "reply": response })
        except Exception as e:
            print(f"[ash-voice-relay] ashctl error: {e}")
            return jsonify({ "reply": "An error occurred processing your voice command." }), 500
    return jsonify({ "reply": "No transcript received." }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

