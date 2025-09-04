from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField
from wtforms import HiddenField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thequickbrownfrog'

import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thequickbrownfrog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Jpf24506@localhost/rainfall'


db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

def month_to_int(mystring):
    my_months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    for myrange in range(12):
        if(my_months[myrange] == mystring):
            return myrange

class SearchButton_Form(FlaskForm):
    submit = SubmitField('Go To Search')

class NameForm(FlaskForm):
    name1 = StringField('Enter Year', validators=[DataRequired()])
    name3 = SelectField('Limit Search Results By', choices=[('1', '1'), ('5', '5'), ('10', '10'),('50', '50')])
    submit = SubmitField('Submit')
class NameForm2(FlaskForm):
    name4 = StringField('Enter Month', validators=[DataRequired()])
    name1 = StringField('Enter Year', validators=[DataRequired()])
    name3 = SelectField('Limit Search Results By', choices=[('1', '1'), ('5', '5'), ('10', '10'),('50', '50')])
    submit = SubmitField('Submit')
class NameForm3(FlaskForm):
    name1 = StringField('Enter Month', validators=[DataRequired()])
    name3 = SelectField('Limit Search Results By', choices=[('1', '1'), ('5', '5'), ('10', '10'), ('50', '50'), ('100', '100'), ('500', '500')])
    submit = SubmitField('Submit')
class NameForm4(FlaskForm):
    name1 = StringField('Enter Range Start Month', validators=[DataRequired()])
    name2 = StringField('Enter Range Start Year', validators=[DataRequired()])
    name3 = StringField('Enter Range End Month', validators=[DataRequired()])
    name4 = StringField('Enter Range End Year', validators=[DataRequired()])
    name5 = SelectField('Limit Search Results By', choices=[('1', '1'), ('5', '5'), ('10', '10'), ('50', '50'), ('100', '100'), ('500', '500')])
    submit = SubmitField('Submit')

class Data(db.Model):
    __tablename__ = "rainfall_table"
    year = db.Column(db.String(15),
                        primary_key=True,
                        index=False,
                        nullable=False)
    january = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    february = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    march = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    april = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    may = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    june = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    july = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    august = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    september = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    october = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    november = db.Column(db.String(15),
                        index=False,
                        nullable=False)
    december = db.Column(db.String(15),
                        index=False,
                        nullable=False)

    def __init__(self, year, january, february, march, april, may, june, july, august, september, october, november, december):
        self.year = year
        self.january = january
        self.february = february
        self.march = march
        self.april = april
        self.may = may
        self.june = june
        self.july = july
        self.august = august
        self.september = september
        self.october = october
        self.novemer = november
        self.december = december

    def __repr__(self):
        return f"<year {self.year}>"

class Data2(db.Model):
    __tablename__ = "rainfall_month"
    year = db.Column(db.String(15),
                        primary_key=True,
                        index=False,
                        nullable=False)
    month = db.Column(db.String(15),
                        primary_key=True,
                        index=False,
                        nullable=False)
    rainfall = db.Column(db.String(15),
                        primary_key=True,
                        index=False,
                        nullable=False)


    def __init__(self, year, month, rainfall):
        self.year = year
        self.month = month
        self.rainfall = rainfall

    def __repr__(self):
        return f"<year {self.year}>"


@app.route("/", methods =['GET','POST'])
def index():
    form2 = SearchButton_Form()
    if request.method == 'POST':
        return redirect('/search')
    return render_template("index.html", form2=form2)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route("/results", methods = ['GET', 'POST'])
def presults():
    name1 = session.get('name1')
    name3 = session.get('name3')
    form3 = SearchButton_Form()

    searchterm = "%{}%".format(name1)
    displayorder = eval('Data.{}'.format('january'))
    displayorder2 = eval('Data2.{}'.format('year'))


    presults = Data.query.filter(Data.year.like(searchterm)).order_by(displayorder).limit(name3).all()
    presults2 = Data2.query.filter(Data2.year.like(searchterm)).order_by(displayorder2).limit(name3).all()

    labels = [row.month + "-" + row.year for row in presults2]
    values = [row.rainfall for row in presults2]

    if request.method == 'POST':
        return redirect('/search')

    return render_template('pres_results.html', presults=presults,\
     name1=name1,name3=name3,labels=labels,values=values,form3=form3)

@app.route("/results2", methods = ['GET', 'POST'])
def presults2():
    name1 = session.get('name1')
    name3 = session.get('name3')
    name4 = session.get('name4')
    form3 = SearchButton_Form()

    searchterm = "%{}%".format(name1)
    month = "%{}%".format(name4)
    displayorder = eval('Data2.{}'.format('year'))

    presults = Data2.query.filter(and_(Data2.year == name1, Data2.month == name4)).order_by(displayorder).limit(name3).all()
    presults2 = Data2.query.filter(Data2.year.like(searchterm)).order_by(displayorder).limit(name3).all()
    labels = [row.month + "-" + row.year for row in presults2]
    values = [row.rainfall for row in presults2]

    if request.method == 'POST':
        return redirect('/search2')

    return render_template('pres_results2.html', presults=presults,\
     name1=name1,name3=name3,name4=name4,labels=labels,values=values,form3=form3)

@app.route("/results3", methods = ['GET', 'POST'])
def presults3():
    name1 = session.get('name1')
    name3 = session.get('name3')
    form3 = SearchButton_Form()

    searchterm = "%{}%".format(name1)
    displayorder = eval('Data2.{}'.format('year'))


    presults = Data2.query.filter(Data2.month.like(searchterm)).order_by(displayorder).limit(name3).all()

    labels = [row.month + "-" + row.year for row in presults]
    values = [row.rainfall for row in presults]


    if request.method == 'POST':
        return redirect('/search3')

    return render_template('pres_results3.html', presults=presults,\
     name1=name1,name3=name3,labels=labels,values=values,form3=form3)

@app.route("/results4", methods = ['GET', 'POST'])
def presults4():
    name1 = session.get('name1')
    name2 = session.get('name2')
    name3 = session.get('name3')
    name4 = session.get('name4')
    name5 = session.get('name5')
    form3 = SearchButton_Form()

    searchterm = "%{}%".format(name4)
    displayorder = eval('Data2.{}'.format('year'))

    presults = Data2.query.filter(and_(Data2.year >= name2, Data2.year <= name4, Data2.rainfall < 2)).order_by(displayorder).limit(name5).all()
    count=0
    mylen=len(presults)
    for item in range(mylen):
        if ((month_to_int(presults[count].month) <= month_to_int(name1) and presults[count].year == name2) or (month_to_int(presults[count].month) >= month_to_int(name3) and presults[count].year == name4)):
            presults.pop(count)
            count-=1
        count+=1
    labels = [row.month + "-" + row.year for row in presults]
    values = [row.rainfall for row in presults]


    if request.method == 'POST':
        return redirect('/search4')

    return render_template('pres_results4.html', presults=presults,\
     name1=name1,name3=name3,labels=labels,values=values,form3=form3)

@app.route('/search', methods=['GET', 'POST'])
def search():
    name1 = None
    name3 = None
    form = NameForm()

    if form.validate_on_submit():
        if request.method == 'POST':
           session['name1']  = form.name1.data
           session['name3']  = form.name3.data

           return redirect('/results')

        form.name1.data = ''
        form.name3.data = ''
    return render_template('search.html', form=form)

@app.route('/search2', methods=['GET', 'POST'])
def search2():
    name1 = None
    name3 = None
    name4 = None
    form = NameForm2()

    if form.validate_on_submit():
        if request.method == 'POST':
           session['name1']  = form.name1.data
           session['name3']  = form.name3.data
           session['name4']  = form.name4.data

           return redirect('/results2')

        form.name1.data = ''
        form.name3.data = ''
        form.name4.data = ''
    return render_template('search.html', form=form)

@app.route('/search3', methods=['GET', 'POST'])
def search3():
    name1 = None
    name3 = None
    form = NameForm3()

    if form.validate_on_submit():
        if request.method == 'POST':
           session['name1']  = form.name1.data
           session['name3']  = form.name3.data

           return redirect('/results3')

        form.name1.data = ''
        form.name3.data = ''
    return render_template('search.html', form=form)

@app.route('/search4', methods=['GET', 'POST'])
def search4():
    name1 = None
    name2 = None
    name3 = None
    name4 = None
    name5 = None
    form = NameForm4()

    if form.validate_on_submit():
        if request.method == 'POST':
           session['name1']  = form.name1.data
           session['name2']  = form.name2.data
           session['name3']  = form.name3.data
           session['name4']  = form.name4.data
           session['name5']  = form.name5.data

           return redirect('/results4')

        form.name1.data = ''
        form.name2.data = ''
        form.name3.data = ''
        form.name4.data = ''
        form.name5.data = ''
    return render_template('search.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
