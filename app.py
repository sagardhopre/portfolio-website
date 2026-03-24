from flask import Flask, render_template, jsonify
from flask_caching import Cache

app = Flask(__name__)
app.config['CACHE_TYPE'] = 'simple'
cache = Cache(app)

# Portfolio data (cached)
@cache.memoize(timeout=300)  # 5min cache for speed
def get_portfolio_data():
    return {
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
            "Python", "Flask", "Django", "Data Structures", "Algorithms",
            "REST APIs", "Databases (SQL)", "Git & GitHub", "Problem Solving",
            "Web Development", "OOP", "MySQL"
        ],
        "projects": [
            {"name": "Project 1", "description": "Coming soon...", "link": "#"},
            {"name": "Project 2", "description": "Coming soon...", "link": "#"},
            {"name": "Project 3", "description": "Coming soon...", "link": "#"}
        ]
    }

@app.route('/')
def home():
    return render_template('index.html', data=get_portfolio_data())

@app.route('/api/portfolio')
@cache.cached(timeout=60)
def api_portfolio():
    return jsonify(get_portfolio_data())

@app.route('/api/skills')
@cache.cached(timeout=60)
def get_skills():
    return jsonify({"skills": get_portfolio_data()["skills"]})

if __name__ == '__main__':
    app.run(debug=True, port=5000, threaded=True)
