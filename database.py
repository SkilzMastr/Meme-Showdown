import mysql.connector


def checkUser(id: int):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="dankest"
    )
    mycursor = db.cursor()
    mycursor.execute(f'SELECT * FROM `users` WHERE id={id};')
    for x in mycursor:
        if x != None:
            return True
        else:
            False