@app.route("/add_Doctor", methods=['POST','GET'])
def add_Doctor():
    if not session.get('login'):
        return redirect( url_for('home') )
    qry = "SELECT * from Doctor"
    mycursor.execute(qry)
    fields = mycursor.column_names

    val = ()

    for field in fields:
        temp = request.form.get(field)
        if field not in ['Doctor_ID','Organization_ID'] and temp != '':
            temp = "\'"+temp+"\'"
        if temp == '':
            temp = 'NULL'
        val = val + (temp,)

    qry = "INSERT INTO Doctor Values (%s,%s,%s,%s)"%val
    print(qry)
    success = True
    error = False
    try:
        mycursor.execute(qry)
    except:
        print("Error : User not Inserted")
        error = True
        success = False
    mydb.commit()

    return redirect(url_for('add_page', id='Doctor', error=error,success=success))
