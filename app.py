from flask import Flask, render_template, request, redirect
from models import db, Goal

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///goals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize DB
db.init_app(app)

# Create Database Tables
with app.app_context():
    db.create_all()

# Home Page
@app.route('/')
def home():

    goals = Goal.query.all()

    return render_template(
        'index.html',
        goals=goals
    )

# Create Goal
@app.route('/create', methods=['GET', 'POST'])
def create_goal():

    if request.method == 'POST':

        employee_name = request.form['employee_name']
        title = request.form['title']
        description = request.form['description']
        target = request.form['target']
        weightage = int(request.form['weightage'])

        # Minimum Weightage Validation
        if weightage < 10:
            return "Minimum weightage is 10%"

        # Maximum 8 Goals Validation
        goal_count = Goal.query.filter_by(
            employee_name=employee_name
        ).count()

        if goal_count >= 8:
            return "Maximum 8 goals allowed"

        # Total Weightage Validation
        existing_goals = Goal.query.filter_by(
            employee_name=employee_name
        ).all()

        total_weight = sum(
            goal.weightage for goal in existing_goals
        )

        if total_weight + weightage > 100:
            return "Total weightage cannot exceed 100"

        # Save Goal
        goal = Goal(
            employee_name=employee_name,
            title=title,
            description=description,
            target=target,
            weightage=weightage
        )

        db.session.add(goal)
        db.session.commit()

        return redirect('/')

    return render_template('create_goal.html')

# Approve Goal
@app.route('/approve/<int:id>')
def approve_goal(id):

    goal = Goal.query.get(id)

    goal.status = "Approved"

    db.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)