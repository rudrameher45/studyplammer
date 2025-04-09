from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Placeholder data - replace with actual data later
    name = "Rudra" 
    subjects_covered = 10
    total_subjects = 20
    hours_this_week = 8
    tasks_done_today = 5
    total_tasks_today = 6
    return render_template('dashboard.html', 
                           name=name,
                           subjects_covered=subjects_covered,
                           total_subjects=total_subjects,
                           hours_this_week=hours_this_week,
                           tasks_done_today=tasks_done_today,
                           total_tasks_today=total_tasks_today)

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/skill-planner')
def skill_planner():
    return render_template('skill_planner.html')

@app.route('/linkedin-share')
def linkedin_share():
    # Placeholder data
    tasks_completed_today = 4
    return render_template('linkedin_share.html', tasks_completed_today=tasks_completed_today)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/motivation')
def motivation():
    # Placeholder data
    streak = 5 # Example streak
    return render_template('motivation.html', streak=streak)


if __name__ == '__main__':
    app.run(debug=True)