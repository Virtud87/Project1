import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from custom_exceptions.custom_exceptions import NonNumericAmount, NegativeDollarAmount, UsernameOrPasswordIncorrect
from dao_layer.implemented_classes.employee_postgres_dao import EmployeePostgresDAO
from dao_layer.implemented_classes.manager_postgres_dao import ManagerPostgresDAO
from service_layer.implemented_classes.employee_postgres_service import EmployeePostgresService
from service_layer.implemented_classes.manager_postgres_service import ManagerPostgresService

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresService(employee_dao)

manager_dao = ManagerPostgresDAO()
manager_service = ManagerPostgresService(manager_dao)


# --------------------------------------------- EMPLOYEES ------------------------------
@app.post("/employee/login")
def employee_login():
    try:
        body = request.get_json()
        employee_id = employee_service.service_employee_login(body["username"], body["password"])
        employee_id_as_dict = {"employee_id": employee_id}
        return jsonify(employee_id_as_dict)
    except UsernameOrPasswordIncorrect as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary), 400


@app.post("/submission")
def submit_new_request():
    try:
        submission_data = request.get_json()
        employee_id = submission_data["employeeId"]
        date = submission_data["date"]
        amount = float(submission_data["amount"])
        reason = submission_data["reason"]
        return jsonify(employee_service.service_submit_new_request(employee_id, date, amount, reason))
    except NonNumericAmount as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)
    except NegativeDollarAmount as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/reimbursements/<employee_id>")
def view_reimbursements_by_employee_id(employee_id):
    reimbursements = employee_service.service_view_reimbursements_by_employee_id(int(employee_id))
    reimbursement_list = []
    for reimbursement in reimbursements:
        reimbursements_as_dict = reimbursement.create_reimbursement_dictionary()
        reimbursement_list.append(reimbursements_as_dict)
    return jsonify(reimbursement_list)


# ------------------------------- Managers -----------------------------------------
@app.post("/manager/login")
def manager_login():
    try:
        body = request.get_json()
        manager_id = manager_service.service_manager_login(body["username"], body["password"])
        manager_id_as_dict = {"manager_id": manager_id}
        return jsonify(manager_id_as_dict)
    except UsernameOrPasswordIncorrect as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary), 400


@app.patch("/approve/<reimbursement_id>")
def approve_reimbursement_by_id(reimbursement_id: str):
    return manager_service.service_approve_reimbursement_by_id(int(reimbursement_id))


@app.patch("/deny/<reimbursement_id>")
def deny_reimbursement_by_id(reimbursement_id: str):
    comment_dict = request.get_json()
    comment = comment_dict["comment"]
    return manager_service.service_deny_reimbursement_by_id(int(reimbursement_id), comment)


@app.get("/pending")
def view_pending_requests():
    pending_requests = manager_service.service_view_pending_requests()
    pending_list = []
    for reimbursement in pending_requests:
        pending_as_dict = reimbursement.create_reimbursement_dictionary()
        pending_list.append(pending_as_dict)
    return jsonify(pending_list)


@app.get("/past")
def view_past_requests():
    past_requests = manager_service.service_view_past_requests()
    past_list = []
    for reimbursement in past_requests:
        past_as_dict = reimbursement.create_reimbursement_dictionary()
        past_list.append(past_as_dict)
    return jsonify(past_list)


@app.get("/amount")
def view_total_amount_approved():
    amounts = manager_service.service_view_total_amount_approved()
    amounts_list = []
    for total_amount_approved in amounts:
        amount_as_dict = total_amount_approved.create_tap_dictionary()
        amounts_list.append(amount_as_dict)
    return jsonify(amounts_list)


@app.get("/approved/number")
def view_total_number_approved_requests():
    number_approved = manager_service.service_view_total_number_approved_requests()
    number_approved_list = []
    for total_number_approved_requests in number_approved:
        number_approved_as_dict = total_number_approved_requests.create_tnar_dictionary()
        number_approved_list.append(number_approved_as_dict)
    return jsonify(number_approved_list)


@app.get("/denied/number")
def view_total_number_denied_requests():
    number_denied = manager_service.service_view_total_number_denied_requests()
    number_denied_list = []
    for total_number_denied_requests in number_denied:
        number_denied_as_dict = total_number_denied_requests.create_tndr_dictionary()
        number_denied_list.append(number_denied_as_dict)
    return jsonify(number_denied_list)


@app.get("/foodDrink")
def view_total_number_approved_food_drink():
    approved_food_drink = manager_service.service_view_total_number_approved_food_drink()
    approved_food_drink_list = []
    for total_number_approved_food_drink in approved_food_drink:
        approved_food_drink_as_dict = total_number_approved_food_drink.create_tnafd_dictionary()
        approved_food_drink_list.append(approved_food_drink_as_dict)
    return jsonify(approved_food_drink_list)


@app.get("/transportation")
def view_total_number_approved_transportation():
    approved_transportation = manager_service.service_view_total_number_approved_transportation()
    approved_transportation_list = []
    for total_number_approved_transportation in approved_transportation:
        approved_transportation_as_dict = total_number_approved_transportation.create_tnat_dictionary()
        approved_transportation_list.append(approved_transportation_as_dict)
    return jsonify(approved_transportation_list)


app.run()
