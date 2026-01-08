from flask import Flask,render_template,request,redirect,url_for


from flask_mysqldb import MySQL


app = Flask(__name__)

# ---------------- MySQL Configuration ----------------
app.config['MYSQL_DB'] = 'studentdb'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306   # must be integer

mysql = MySQL(app)

# ---------------- Index Page ----------------
@app.route("/")
def index():
    return render_template("index.html")

# ---------------- Registration Page ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        rollno = request.form["rollno"]
        name = request.form["name"]
        course = request.form["course"]
        duration = request.form["duration"]

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO student (rollno, name, course, duration) VALUES (%s, %s, %s, %s)",
            (rollno, name, course, duration)
        )
        mysql.connection.commit()
        cur.close()

        return redirect(url_for("view_student"))

    return render_template("register.html")

# ---------------- View Students ----------------
@app.route("/view")
def view_student():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    data = cur.fetchall()
    cur.close()

    return render_template("view.html", student=data)

# ---------------- Delete Student ----------------
@app.route("/delete/<int:rollno>")
def delete_student(rollno):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student WHERE rollno=%s", (rollno,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("view_student"))

# ---------------- Edit Student ----------------
@app.route("/edit/<int:rollno>")
def edit_student(rollno):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student WHERE rollno=%s", (rollno,))
    student = cur.fetchone()
    cur.close()

    return render_template("edit.html", student=student)

# ---------------- Update Student ----------------
@app.route("/update/<int:rollno>", methods=["POST"])
def update_student(rollno):
    name = request.form['name']
    course = request.form['course']
    duration = request.form['duration']

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE student SET name=%s, course=%s, duration=%s WHERE rollno=%s",
        (name, course, duration, rollno)
    )
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("view_student"))

# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(debug=True )



'''student = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET","POST" ])
def index():
    return render_template("index.html")

#MySQL Connection with Flask

app.config['MYSQL_DB']='studentdb'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='root'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']='3306'

mysql=MySQL(app)


#Display index page

def index():
    return render_template('index.html')


#Display Registration Page


#Save the data  Registration Page


#Display all User data to frontEnd


#Delete User data


#edit User data


#update User Data




app = Flask(__name__)

# ---------------- MySQL Configuration ----------------
app.config['MYSQL_DB'] = 'studentdb'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_PORT'] = 3306   # must be integer

mysql = MySQL(app)

# ---------------- Index Page ----------------
@app.route("/")
def index():
    return render_template("index.html")

# ---------------- Registration Page ----------------
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        roll = request.form['roll']
        name = request.form['name']
        course = request.form['course']
        duration = request.form['duration']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO students (roll, name, course, duration) VALUES (%s,%s,%s,%s)",
            (roll, name, course, duration)
        )
        mysql.connection.commit()
        cur.close()

        return redirect(url_for("index"))

    return render_template("register.html")

# ---------------- View Students ----------------
@app.route("/view")
def view_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students")
    data = cur.fetchall()
    cur.close()

    return render_template("view.html", students=data)

# ---------------- Delete Student ----------------
@app.route("/delete/<int:roll>")
def delete_student(roll):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE roll=%s", (roll,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("view_students"))

# ---------------- Edit Student ----------------
@app.route("/edit/<int:roll>")
def edit_student(roll):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM students WHERE roll=%s", (roll,))
    student = cur.fetchone()
    cur.close()

    return render_template("register.html", student=student)

# ---------------- Update Student ----------------
@app.route("/update/<int:roll>", methods=["POST"])
def update_student(roll):
    name = request.form['name']
    course = request.form['course']
    duration = request.form['duration']

    cur = mysql.connection.cursor()
    cur.execute(
        "UPDATE students SET name=%s, course=%s, duration=%s WHERE roll=%s",
        (name, course, duration, roll)
    )
    mysql.connection.commit()
    cur.close()

    return redirect(url_for("view_students"))

# ---------------- Run App ----------------
if __name__ == '__main__':
    app.run(debug=True, port=6000)'''

