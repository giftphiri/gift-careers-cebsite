from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Network Engineer II',
  'location': 'London, UK',
  'salary': '£50,000'
}, {
  'id': 2,
  'title': 'Sr. Data Anylyst',
  'location': 'Dublin, Ireland',
  'salary': '€70,000'
}, {
  'id': 3,
  'title': 'IT Support Engineer II',
  'location': 'Seattle, WA',
  'salary': '$65,000'
}, {
  'id': 4,
  'title': 'Full Stack Developer',
  'location': 'Remote',
  'salary': '€120,000'
}, {
  'id': 5,
  'title': 'Front-End Developer',
  'location': 'Remote'
}]


@app.route("/")
def hellow_world():
  return render_template('home.html', jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run('0.0.0.0', debug=True)
