class Admission:
    
    def __init__(self, student, subject, date, status=True):
        self.student = student
        self.subject = subject
        self.date = date
        self.status = status

    def __repr__(self):
        return f"Admision: {self.student}, {self.subject}, {self.date}, {self.status}"