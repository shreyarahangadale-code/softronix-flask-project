from flask import Flask , render_template,request,jsonify,redirect,url_for

from flask_mysqldb import MySQL


app=Flask(__name__)

#con=mysql.connector.connect(user="root",password="root",host="localhost",database="product")

app.config["MYSQL_USER"]='root'
app.config["MYSQL_PASSWORD"]='root'
app.config["MYSQL_HOST"]='localhost'
app.config["MYSQL_PORT"]=3306
app.config["MYSQL_DB"]='product'

mysql=MySQL(app)

#mysql=MySQL(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/savedata",methods=['GET','POST'])
def dataSave():
    if request.method=='POST':
        pid=request.form['pid']
        pname=request.form['pname']
        pcost=request.form['pcost']

        cursor=mysql.connection.cursor()
        cursor.execute("insert into ptable(pid,pname,pcost) values(%s,%s,%s)",(pid,pname,pcost))
        mysql.connection.commit()

        return jsonify({"Message":"DataSend Successfully"})

    
@app.route("/show")
def sendData():
    cursor=mysql.connection.cursor()
    cursor.execute("select * from ptable")
    p=cursor.fetchall()
    print(p)
    mysql.connection.commit()
    
    return render_template("show.html",p=p)

@app.route("/delete/<int:pid>") #/delete/101
def deleteData(pid):
    cursor=mysql.connection.cursor()
    cursor.execute("delete from ptable where pid=%s",(pid,))
    return redirect (url_for("senData"))


@app.route("/edit/<int:pid>") #/delete/101
def editData(pid):
    cursor=mysql.connection.cursor()
    cursor.execute("select * from ptable where pid=%s",(pid,))
    p=cursor.fetchone()
    return render_template ("edit.html",p=p)

@app.route("/update",methods=['GET','POST'])
def updateSave():
    if request.method=='POST':
        pid=request.form['pid']
        pname=request.form['pname']
        pcost=request.form['pcost']

        cursor=mysql.connection.cursor()
        cursor.execute("update ptable set pname=%s,pcost=%swherem pid=%s",(pid,pname,pcost))
        mysql.connection.commit()
        return redirect(url_for("sendData"))




@app.route("/savedata",methods=['GET','POST'])
def saveSave():
    if request.method=='POST':
        eid=request.form['eid']
        ename=request.form['ename']
        esal=request.form['esal']
        eadder=request.form['eadder']

        cursor=mysql.connection.cursor()
        cursor.execute("insert into ptable(eid,ename,esal,eadder) values(%s,%s,%s,%s)",(eid,ename,esal,eadder))
        mysql.connection.commit()

        return jsonify({"Message":"DataSend Successfully"})


   

if __name__ == '__main__':
    app.run(debug=True)