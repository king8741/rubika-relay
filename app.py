from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def health():
    """Leg 1 test: can PythonAnywhere reach THIS service at all?
    Just visit or curl this URL from PythonAnywhere's Bash console.
    """
    return jsonify({"status": "ok", "message": "Render relay is alive."})


@app.route("/rubika-test")
def rubika_test():
    """Leg 2 test: can Render reach Rubika's API?"""

    try:
        response = requests.get("https://api.rubika.ir", timeout=8)
        return jsonify({
            "reached_rubika": True,
            "status_code": response.status_code,
        })
    except Exception as error:
        return jsonify({
            "reached_rubika": False,
            "error": repr(error),
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
