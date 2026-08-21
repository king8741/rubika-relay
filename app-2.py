from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def health():
    """Leg 1 test: can PythonAnywhere reach THIS service at all?
    Just visit or curl this URL from PythonAnywhere's Bash console.
    """
    return jsonify({"status": "ok", "message": "Render relay is alive."})


# Put your real bot token here (from BotFather on Rubika)
RUBIKA_TOKEN = "CCDIAJ0AMVVHKIATBWWSICJLTKHTEQPGRXSCJTNRMGIHRAINFUPEJHGFGTUPALMM"

# Rubika bot API base — real servers, not api.rubika.ir (that domain doesn't exist)
RUBIKA_BASE = f"https://messengerg2b1.iranlms.ir/v3/{RUBIKA_TOKEN}"


@app.route("/rubika-test")
def rubika_test():
    """Leg 2 test: can Render reach Rubika's bot API?"""

    try:
        response = requests.post(f"{RUBIKA_BASE}/getMe", timeout=8)
        return jsonify({
            "reached_rubika": True,
            "status_code": response.status_code,
            "body": response.text,
        })
    except Exception as error:
        return jsonify({
            "reached_rubika": False,
            "error": repr(error),
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
