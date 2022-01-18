class Submission:
    def __init__(self, reimbursement_id, employee_id: int, date: str, amount, reason: str):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self. date = date
        self.amount = amount
        self. reason = reason

    def create_submission_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "employeeId": self.employee_id,
            "date": self.date,
            "amount": self.amount,
            "reason": self.reason
        }

