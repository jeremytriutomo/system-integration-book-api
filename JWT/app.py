from flask import Flask, g, jsonify
from flask_httpauth import HTTPBasicAuth
from passlib.hash import pbkdf2_sha256 as hasher

app = Flask(__name__)
auth = HTTPBasicAuth()

USERS = {
    "apiuser": hasher.hash("securepwd"),
    "admin": hasher.hash("adminpwd")
}


@auth.verify_password
def verify_password(username, password):
    if username in USERS:
        hashed_password = USERS[username]

        if hasher.verify(password, hashed_password):
            g.user = username
            return True
    return False


@auth.error_handler
def auth_error(status):
    return jsonify({"error": "Unauthorized access"}), status


@app.route('/api/status', methods=['GET'])
@auth.login_required
def status_check():
    return jsonify(
        status="OK",
        message=f"Welcome back, {g.user}. Your request was authenticated."
    ), 200


if __name__ == "__main__":
    app.run(debug=True)
