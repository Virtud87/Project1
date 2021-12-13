class Reimbursement:
    def __init__(self, reimbursement_id: int, employee_id: int, date: str, amount: float, reason: str, status: str, comment: str):
        self.reimbursement_id = reimbursement_id
        self.employee_id = employee_id
        self.date = date
        self.amount = amount
        self.reason = reason
        self.status = status
        self.comment = comment

    def create_reimbursement_dictionary(self):
        return {
            "reimbursementId": self.reimbursement_id,
            "employeeId": self.employee_id,
            "date": self.date,
            "amount": self.amount,
            "reason": self.reason,
            "status": self.status,
            "comment": self.comment
        }
