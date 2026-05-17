from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Goal(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    employee_name = db.Column(
        db.String(100),
        nullable=False
    )

    title = db.Column(
        db.String(200),
        nullable=False
    )

    description = db.Column(
        db.String(500)
    )

    target = db.Column(
        db.String(100),
        nullable=False
    )

    weightage = db.Column(
        db.Integer,
        nullable=False
    )

    status = db.Column(
        db.String(50),
        default="Pending"
    )

    def __repr__(self):
        return f"<Goal {self.title}>"