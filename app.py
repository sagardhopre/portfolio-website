from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Portfolio data
portfolio_data = {
    "name": "Sagar Dhopre",
    "email": "sagardhopare7297@gmail.com",
    "title": "Python Developer | Software Developer",
    "bio": "Passionate Python Developer and Problem Solver. Fresher looking for opportunities in Python Development and Software Engineering.",
    "social_links": {
        "linkedin": "https://linkedin.com/in/sagar-dhopre-522346279",
        "leetcode": "https://assets.leetcode.com/users/sagardhopare/",
        "github": "https://github.com/account"
    },
    "skills": [
        "Python",
        "Flask",
        "Django",
        "Data Structures",
        "Algorithms",
        "REST APIs",
        "Databases (SQL)",
        "Git & GitHub",
        "Problem Solving",
        "Web Development",
        "Object-Oriented Programming",
        "MySQL"
    ],
    "projects": [
        {
            "name": "Project 1",
            "description": "Coming soon...",
            "link": "#"
        },
        {
            "name": "Project 2",
            "description": "Coming soon...",
            "link": "#"
        },
        {
            "name": "Project 3",
            "description": "Coming soon...",
            "link": "#"
        }
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=portfolio_data)

@app.route('/api/portfolio')
def api_portfolio():
    return jsonify(portfolio_data)

@app.route('/api/skills')
def get_skills():
    return jsonify({"skills": portfolio_data["skills"]})

if __name__ == '__main__':
    app.run(debug=True)