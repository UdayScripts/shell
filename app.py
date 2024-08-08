from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.json.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    try:
        # Run yt-dlp command
        result = subprocess.run(['yt-dlp', url], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        return jsonify({"output": result.stdout}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
