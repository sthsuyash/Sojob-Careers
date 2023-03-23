from flask import Flask, render_template, jsonify

app = Flask(__name__)

# database variables
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Kathmandu, Nepal',
        'salary': 'Rs. 1,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Pokhara, Nepal',
        'salary': 'Rs. 2,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Developer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Backend Developer',
        'location': 'LA, USA',
        'salary': '$1,20,000'
    },

]


@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    return render_template('index.html', jobs=JOBS, company_name="Sojob")

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)

@app.route('/jobs/<int:id>')
def get_job(id):
    job = [job for job in JOBS if job['id'] == id]
    if len(job) == 0:
        return jsonify({'message': 'Job not found!'})
    return jsonify(job[0])


if __name__ == '__main__':
    app.run(port=8000, debug=True)
