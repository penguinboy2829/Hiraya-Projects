from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(minutes = 5)

# database creation
# mysql://username:password@localhost/db_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:LRMA02132389*@localhost/Sched2'
# secret key
app.config['SECRET_KEY'] = "1234"
# database initialization
db = SQLAlchemy(app)

class Sched2(db.Model):
    id = db.Column("id",db.Integer, unique=True, primary_key=True)
    nm = db.Column(db.String(80))
    tm = db.Column(db.String(120))
    dm = db.Column(db.String(120))
    pm = db.Column(db.String(120))

    def __init__(self, nm, tm, dm, pm):
        self.nm = nm
        self.tm = tm
        self.dm = dm
        self.pm = pm

# Home Page
@app.route("/")
def home():
    return render_template("index.html", values = Sched2.query.order_by(Sched2.dm.asc()).order_by(Sched2.pm.asc()).all())


#Create Data Page
@app.route("/create", methods = ['POST','GET'])
def create():
    if request.method == 'POST':
        nm = request.form['nm']
        tm = request.form['tm']
        dm = request.form['dm']
        pm = request.form['pm']
        sched = Sched2(nm=nm, tm=tm, dm=dm, pm=pm)
        
        #add data to table
        db.session.add(sched)
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template("edit.html")

#delete table
@app.route("/delete/<int:id>")
def delete(id):
    # retrieve the record to delete
    sched = Sched2.query.get(id)
    
    # delete the record from the table
    db.session.delete(sched)
    #db.session.execute(text('UPDATE sched2 SET id = id - 1 WHERE id > :id'), {'id': id})
    db.session.commit()
    
    # redirect to home page
    return redirect(url_for('home'))

@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    # retrieve the record to edit
    sched = Sched2.query.get(id)
    if request.method == 'POST':
        # update the record with the new values
        sched.nm = request.form['nm']
        sched.tm = request.form['tm']
        sched.dm = request.form['dm']
        sched.pm = request.form['pm']

        db.session.commit()
        # redirect to home page
        return redirect(url_for('home'))

    # render the update form
    return render_template("update.html", sched=sched)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug = True)