from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import statistics

app = Flask(__name__)
app.run(
    host="0.0.0.0",
    port=5000
)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'True'

db = SQLAlchemy(app)

class Formdata(db.Model):
    __tablename__ = 'formdata'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    firstname = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)

    def __init__(self, firstname, email, age, q1, q2, q3, q4, q5, q6, q7, q8):
        self.firstname = firstname
        self.email = email
        self.age = age
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6
        self.q7 = q7
        self.q8 = q8

db.create_all()


@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route("/form")
def show_form():
    return render_template('form.html')

@app.route("/raw")
def show_raw():
    fd = db.session.query(Formdata).all()
    return render_template('raw.html', formdata=fd)


@app.route("/result")
def show_result():
    fd_list = db.session.query(Formdata).all()

    # Some simple statistics for sample questions
    q1 = []
    q2 = []
    q3 = []
    q4 = []
    q5 = []
    q6 = []
    q7 = []
    q8 = []
    for el in fd_list:
        q1.append(int(el.q1))
        q2.append(int(el.q2))
        q3.append(int(el.q3))
        q4.append(int(el.q4))
        q5.append(int(el.q5))
        q6.append(int(el.q6))
        q7.append(int(el.q7))
        q8.append(int(el.q8))

    q1_answ_1=0
    q1_answ_2=0
    q1_answ_3=0
    q1_answ_4=0
    q1_answ_5=0
    for q1_wsk in q1:
        if q1_wsk == 1:
            q1_answ_1=q1_answ_1+1
        if q1_wsk == 2:
            q1_answ_2=q1_answ_2+1
        if q1_wsk == 3:
            q1_answ_3=q1_answ_3+1
        if q1_wsk == 4:
            q1_answ_4=q1_answ_4+1
        if q1_wsk == 5:
            q1_answ_5=q1_answ_5+1

    q2_answ_1=0
    q2_answ_2=0
    q2_answ_3=0
    q2_answ_4=0
    q2_answ_5=0
    q2_answ_6=0
    for q2_wsk in q2:
        if q2_wsk == 1:
            q2_answ_1=q2_answ_1+1
        if q2_wsk == 2:
            q2_answ_2=q2_answ_2+1
        if q2_wsk == 3:
            q2_answ_3=q2_answ_3+1
        if q2_wsk == 4:
            q2_answ_4=q2_answ_4+1
        if q2_wsk == 5:
            q2_answ_5=q2_answ_5+1
        if q2_wsk == 6:
            q2_answ_6=q2_answ_6+1

    q3_answ_1=0
    q3_answ_2=0
    q3_answ_3=0
    q3_answ_4=0
    q3_answ_5=0
    q3_answ_6=0
    for q3_wsk in q3:
        if q3_wsk == 1:
            q3_answ_1=q3_answ_1+1
        if q3_wsk == 2:
            q3_answ_2=q3_answ_2+1
        if q3_wsk == 3:
            q3_answ_3=q3_answ_3+1
        if q3_wsk == 4:
            q3_answ_4=q3_answ_4+1
        if q3_wsk == 5:
            q3_answ_5=q3_answ_5+1
        if q3_wsk == 6:
            q3_answ_6=q3_answ_6+1

    q4_answ_1=0
    q4_answ_2=0
    q4_answ_3=0
    q4_answ_4=0
    for q4_wsk in q4:
        if q4_wsk == 1:
            q4_answ_1=q4_answ_1+1
        if q4_wsk == 2:
            q4_answ_2=q4_answ_2+1
        if q4_wsk == 3:
            q4_answ_3=q4_answ_3+1
        if q4_wsk == 4:
            q4_answ_4=q4_answ_4+1

    q5_answ_1=0
    q5_answ_2=0
    q5_answ_3=0
    q5_answ_4=0
    for q5_wsk in q5:
        if q5_wsk == 1:
            q5_answ_1=q5_answ_1+1
        if q5_wsk == 2:
            q5_answ_2=q5_answ_2+1
        if q5_wsk == 3:
            q5_answ_3=q5_answ_3+1
        if q5_wsk == 4:
            q5_answ_4=q5_answ_4+1

    q6_answ_1=0
    q6_answ_2=0
    q6_answ_3=0
    q6_answ_4=0
    for q6_wsk in q6:
        if q6_wsk == 1:
            q6_answ_1=q6_answ_1+1
        if q6_wsk == 2:
            q6_answ_2=q6_answ_2+1
        if q6_wsk == 3:
            q6_answ_3=q6_answ_3+1
        if q6_wsk == 4:
            q6_answ_4=q6_answ_4+1

    q7_answ_1=0
    q7_answ_2=0
    q7_answ_3=0
    q7_answ_4=0
    q7_answ_5=0
    for q7_wsk in q7:
        if q7_wsk == 1:
            q7_answ_1=q7_answ_1+1
        if q7_wsk == 2:
            q7_answ_2=q7_answ_2+1
        if q7_wsk == 3:
            q7_answ_3=q7_answ_3+1
        if q7_wsk == 4:
            q7_answ_4=q7_answ_4+1
        if q7_wsk == 5:
            q7_answ_5=q7_answ_5+1

    q8_answ_1=0
    q8_answ_2=0
    q8_answ_3=0
    for q8_wsk in q8:
        if q8_wsk == 1:
            q8_answ_1=q8_answ_1+1
        if q8_wsk == 2:
            q8_answ_2=q8_answ_2+1
        if q8_wsk == 3:
            q8_answ_3=q8_answ_3+1

        
    # Prepare data for google charts
    data1 = [['Codziennie', q1_answ_1], ['2-3 razy w tygodniu', q1_answ_2], ['Raz w tygodniu', q1_answ_3], ['Okazjonalnie', q1_answ_4], ['Nie uprawiam sportu', q1_answ_5]]
    data2 = [['Słuchanie muzyki/Czytanie książek', q2_answ_1], ['Oglądanie telewizji', q2_answ_2], ['Uprawianie sportu', q2_answ_3], ['Spacery/wycieczki', q2_answ_4], ['Spotkania z przyjaciółmi', q2_answ_5], ['Inne', q2_answ_6]]
    data3 = [['Kilka razy dziennie', q3_answ_1], ['Codziennie', q3_answ_2], ['Kilka razy w tygodniu', q3_answ_3], ['Raz w tygodniu', q3_answ_4], ['Okazjonalnie ', q3_answ_5], ['Nie uprawiam sportu ', q3_answ_6]]
    data4 = [['Więcej niż 5 posiłków', q4_answ_1], ['5 posiłków', q4_answ_2], ['3-4 posiłki', q4_answ_3], ['Mniej niż 3 posiłki', q4_answ_4]]
    data5 = [['1 szklankę', q5_answ_1], ['2-3 szklanki', q5_answ_2], ['4-5 szklanek', q5_answ_3], ['Więcej', q5_answ_4]]
    data6 = [['Wiecej niż 8h', q6_answ_1], ['6-8h', q6_answ_2], ['4-6h', q6_answ_3], ['Mniej niż 4h', q6_answ_4]]
    data7 = [['Codziennie', q7_answ_1], ['2-3 razy w tygodniu', q7_answ_2], ['Raz w tygodniu', q7_answ_3], ['Okazjonalnie', q7_answ_4], ['Nie piję alkoholu', q7_answ_5]]
    data8 = [['Tak', q8_answ_1], ['Nie', q8_answ_2], ['Okazjonalnie', q8_answ_3]]
    return render_template('result.html', data1=data1, data2=data2, data3=data3, data4=data4, data5=data5, data6=data6, data7=data7, data8=data8)


@app.route("/save", methods=['POST'])
def save():
    q8=0
    # Get data from FORM
    firstname = request.form['firstname']
    email = request.form['email']
    age = request.form['age']
    q1 = request.form['q1']
    q2 = request.form['q2']
    q3 = request.form['q3']
    q4 = request.form['q4']
    q5 = request.form['q5']
    q6 = request.form['q6']
    q7 = request.form['q7']
    q8 = request.form['q8']

    #if q8 < 1 or q8 > 5:
    #    q8=0

    # Save the data
    fd = Formdata(firstname, email, age, q1, q2, q3, q4, q5, q6, q7, q8)
    db.session.add(fd)
    db.session.commit()

    return redirect('/')


if __name__ == "__main__":
    app.debug = True
    app.run()
