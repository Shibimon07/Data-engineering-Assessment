from flask import Flask, request, jsonify
from service.database import app, db
from service.model import User, EmploymentInfo, UserBankInfo

# creating new user with employment and bank info
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json

    existing_user = User.query.filter_by(email=data["email"]).first()
    if existing_user:
        return jsonify({
            "error": f"User's email '{data['email']}' already exists"
        }), 400

    new_user = User(
        first_name = data["first_name"],
        last_name = data["last_name"],
        email = data["email"],
        phone = data["phone"],
        address_line1 = data["address_line1"],
        city = data["city"],
        state = data["state"],
        pincode = data["pincode"]
    )
    db.session.add(new_user)
    db.session.commit()

    emp = EmploymentInfo(
        user_id = new_user.id,
        company_name = data["employment"]["company_name"],
        designation = data["employment"]["designation"],
        is_current = data["employment"]["is_current"]
    )
    db.session.add(emp)

    bank = UserBankInfo(
        user_id = new_user.id,
        bank_name = data["bank"]["bank_name"],
        account_number = data["bank"]["account_number"],
        ifsc = data["bank"]["ifsc"],
        account_type = data["bank"]["account_type"]
    )
    db.session.add(bank)
    db.session.commit()

    return jsonify({"message": "user created successfully", "user_id": new_user.id}), 201


#all users
@app.route("/users", methods=["GET"])
def get_users():
    all_users = User.query.all()
    output = []

    for u in all_users:
        output.append({
            "id": u.id,
            "name": f"{u.first_name} {u.last_name}",
            "email": u.email,
            "city": u.city,
            "pincode": u.pincode
        })

    return jsonify(output)


# getting user by id
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    emp_data = []
    for e in user.employment:
        emp_data.append({
            "company_name": e.company_name,
            "designation": e.designation,
            "is_current": e.is_current
        })

    bank_data = []
    for b in user.bank:
        bank_data.append({
            "bank_name": b.bank_name,
            "account_number": b.account_number,
            "ifsc": b.ifsc,
            "account_type": b.account_type
        })

    result = {
        "id": user.id,
        "name": f"{user.first_name} {user.last_name}",
        "email": user.email,
        "city": user.city,
        "state": user.state,
        "pincode": user.pincode,
        "employment": emp_data,
        "bank": bank_data
    }
    return jsonify(result)


# updating user info
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    updated_fields = []  

    user_fields = ["first_name", "last_name", "email", "phone", "address_line1", "city", "state", "pincode"]
    for field in user_fields:
        if field in data:
            old_value = getattr(user, field)
            new_value = data[field]
            if old_value != new_value:  
                setattr(user, field, new_value)
                updated_fields.append(f"{field.replace('_', ' ')} updated successfully")

    if "employment" in data:
        emp = EmploymentInfo.query.filter_by(user_id=user.id).first()
        if not emp:
            emp = EmploymentInfo(user_id=user.id)
            db.session.add(emp)

        for field in ["company_name", "designation", "is_current"]:
            if field in data["employment"]:
                old_value = getattr(emp, field)
                new_value = data["employment"][field]
                if old_value != new_value:
                    setattr(emp, field, new_value)
                    updated_fields.append(f"{field.replace('_', ' ')} updated successfully")

    if "bank" in data:
        bank = UserBankInfo.query.filter_by(user_id=user.id).first()
        if not bank:
            bank = UserBankInfo(user_id=user.id)
            db.session.add(bank)

        for field in ["bank_name", "account_number", "ifsc", "account_type"]:
            if field in data["bank"]:
                old_value = getattr(bank, field)
                new_value = data["bank"][field]
                if old_value != new_value:
                    setattr(bank, field, new_value)
                    updated_fields.append(f"{field.replace('_', ' ')} updated successfully")

    db.session.commit()

    if not updated_fields:
        return jsonify({"message": "No changes detected"}), 200

    return jsonify({
        "message": f" User {user.id} updated successfully",
        "updated_fields": updated_fields
    }), 200



# deleting user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": f"user {user_id} deleted"})


# adding new employment
@app.route("/users/<int:user_id>/employment", methods=["POST"])
def add_employment(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    data = request.json
    emp = EmploymentInfo(
        user_id = user.id,
        company_name = data.get("company_name"),
        designation = data.get("designation"),
        start_date = data.get("start_date"),
        end_date = data.get("end_date"),
        is_current = data.get("is_current", True)
    )

    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "employment added", "employment_id": emp.id}), 201

#adding bank
@app.route("/users/<int:user_id>/bank", methods=["POST"])
def add_bank(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404

    data = request.json
    bank = UserBankInfo(
        user_id = user.id,
        bank_name = data.get("bank_name"),
        account_number = data.get("account_number"),
        ifsc = data.get("ifsc"),
        account_type = data.get("account_type")
    )

    db.session.add(bank)
    db.session.commit()
    return jsonify({"message": "bank record added", "bank_id": bank.id}), 201


@app.route("/users/<int:user_id>/bank/<int:bank_id>", methods=["DELETE"])

def delete_bank(user_id,bank_id):
    user= User.query.get(user.id)
    if not user:
        return jsonify ({"error": f"user {user_id} is not found"}),404
    bank = UserBankInfo.query.filter_by(id=bank_id,user_id=user_id).first(),404
    if not bank:
        return jsonify ({"error":f"bank is {bank_id} not found for {user_id}user "}),404
    
    db.session.delete(bank)
    db.session.commit()

    return jsonify ({
        "message": f"{bank_id} bank account deleted successfully for {user_id}"
    }),200


