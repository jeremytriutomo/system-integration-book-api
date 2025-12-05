from flask import Flask, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity, get_jwt
import datetime

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "this_is_a_super_secret_key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=1)
jwt = JWTManager(app)

USERS = {
    "alice": {"password": "password123", "roles": ["user"]},
    "bob": {"password": "password456", "roles": ["admin", "user"]}
}


@app.route('/login', methods=['POST'])
def login():

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username not in USERS or USERS[username]["password"] != password:
        return jsonify({"msg": "Bad username or password"}), 401

    # 3. Create extra claims for the token
    user_roles = USERS[username]["roles"]
    additional_claims = {"roles": user_roles}

    # 4. Create the access token
    access_token = create_access_token(
        identity=username, additional_claims=additional_claims)

    return jsonify(access_token=access_token), 200


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected_user_route():
    current_user = get_jwt_identity()
    return jsonify(
        logged_in_as=current_user,
        message=f"Hello, {current_user}"), 200


@app.route('/protected_admin', methods=['GET'])
@jwt_required()
def protected_admin_route():
    current_user = get_jwt_identity()
    return jsonify(
        logged_in_as=current_user,
        message=f"ACCESS GRANTED: {current_user} is an admin accessed the restricted route"), 200


if __name__ == "__main__":
    app.run(debug=True, ssl_context='adhoc')
