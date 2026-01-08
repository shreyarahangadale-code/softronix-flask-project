from flask import Flask , render_template,request,jsonify

from flask_mysqldb import MySQL


app=Flask(__name__)

#con=mysql.connector.connect(user="root",password="root",host="localhost",database="product")

app.config["MYSQL_USER"]='root'
app.config["MYSQL_PASSWORD"]='root'
app.config["MYSQL_HOST"]='localhost'
app.config["MYSQL_PORT"]=3306
app.config["MYSQL_DB"]='employ'

mysql=MySQL(app)

#mysql=MySQL(app)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")


    





@app.route("/savedata",methods=['GET','POST'])
def saveSave():
    if request.method=='POST':
        eid=request.form['eid']
        ename=request.form['ename']
        esal=request.form['esal']
        eaddrr=request.form['eaddrr']

        cursor=mysql.connection.cursor()
        cursor.execute("insert into employei(eid,ename,esal,eaddrr) values(%s,%s,%s,%s)",(eid,ename,esal,eaddrr))
        mysql.connection.commit()

        return jsonify({"Message":"DataSend Successfully"})

@app.route("/data")
def sendData():
    cursor=mysql.connection.cursor()
    cursor.execute("select * from employei")
    e=cursor.fetchall()
    print(e)
    mysql.connection.commit()
    
    return render_template("data.html",e=e)

   

if __name__ == '__main__':
    app.run(debug=True)