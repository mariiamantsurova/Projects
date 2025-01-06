from flask import Flask, render_template, request, redirect
import mysql.connector
app = Flask(__name__)
#setting up sql connection
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "online_store"
)
cursor = mydb.cursor()
cursor.execute("SELECT email FROM online_store.managers")
admins = cursor.fetchall()
print(admins)
# after connecting with the login page we can check if the user is an admin or not
# (if he is an admin we'll redirect him to the relvent page)
# if email in admins:
#     return render_template("inventory_update.html")
# else:
#     return render_template("home_page.html")
