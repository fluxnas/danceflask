from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/projet')
def projet():
  return render_template('projet.html')

@app.route('/cours')
def cours():
  return render_template('cours.html')

@app.route('/prix')
def prix():
  return render_template('prix.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')



app.run(host='0.0.0.0', port=81) 