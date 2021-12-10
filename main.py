import logging
from flask import Flask, request, jsonify

from custom_exceptions.custom_exceptions import NonNumericAmount, NegativeDollarAmount, UsernameOrPasswordIncorrect
from dao_layer.implemented_classes.employee_postgres_dao import EmployeePostgresDAO
from entities.credentials import Credentials
from entities.submission import Submission
from service_layer.implemented_classes.employee_postgres_service import EmployeePostgresService

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)

employee_dao = EmployeePostgresDAO()
employee_service = EmployeePostgresService(employee_dao)


# EMPLOYEES
@app.route('/login', methods=['POST'])
def login():
    try:
        credentials = request.get_json()
        login_data = Credentials(
            credentials["username"],
            credentials["password"])
        logged_in = employee_service.service_login(login_data)
        return f"Logged in as {logged_in}."
    except UsernameOrPasswordIncorrect as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.post("/submission")
def submit_new_request():
    try:
        submission_data = request.get_json()
        new_submission = Submission(
            submission_data["reimbursementId"],
            submission_data["employeeId"],
            submission_data["date"],
            submission_data["amount"],
            submission_data["reason"])
        submission = employee_service.service_submit_new_request(new_submission)
        return f"{submission} successful!"
    except NonNumericAmount as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)
    except NegativeDollarAmount as e:
        exception_dictionary = {"message": str(e)}
        return jsonify(exception_dictionary)


@app.get("/reimbursements/<employee_id>")
def view_reimbursements_by_employee_id(employee_id: str):
    reimbursements = employee_service.service_view_reimbursements_by_employee_id(int(employee_id))
    reimbursement_list = []
    for reimbursement in reimbursements:
        reimbursements_as_dict = reimbursement.create_reimbursement_dictionary()
        reimbursement_list.append(reimbursements_as_dict)
    return jsonify(reimbursement_list)




app.run()
