'''Validate user entry'''
import re
from werkzeug.security import generate_password_hash, check_password_hash

def validate(firstname, lastname, email, phonenumber, password, confirm_password, pwd):
    '''Validate tenant registration data'''

    if not firstname.strip():
            return jsonify({"error": "firstname cannot be empty"}), 400

    if not re.match(r"^[A-Za-z][a-zA-Z]", firstname):
        return jsonify({"error": "input valid firstname"}), 400

    if not lastname.strip():
        return jsonify({"error": "lastname cannot be empty"}), 400

    if not re.match(r"^[A-Za-z][a-zA-Z]", lastname):
        return jsonify({"error": "input valid lastname"}), 400

    if not phonenumber.strip():
        return jsonify({"error": "phonenumber cannot be empty"}), 400

    if len(phonenumber) != 10:
        return jsonify({"error": "phonenumber has 10 digits"}), 400

    if not re.match(r"^[0-9]", phonenumber):
        return jsonify({"error": "input valid phonenumber"}), 400

    if not email.strip():
        return jsonify({"error": "email cannot be empty"}), 400

    if not password.strip():
        return jsonify({"error": "password cannot be empty"}), 400

    if not re.match(r'[A-Za-z0-9@#$]{6,12}', pwd):
        return jsonify({"error": "Input a stronger password"}), 400

    if not confirm_password.strip():
        return jsonify({"error": "confirm password cannot be empty"}), 400

    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        return jsonify({"error": "input valid email"}), 400

    if not check_password_hash(password, confirm_password):
        return jsonify({"error": "passwords did not match"}), 400