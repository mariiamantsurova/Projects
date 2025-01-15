from flask import Flask
import mysql.connector
# from python.home import 
from python.inventory_update import inventory_update_route


# Setting up SQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPassword",
    database="online_store"
)
cursor = mydb.cursor()



app = Flask(__name__, template_folder='templates')

# Import routes from other files
# home_routes(app)
inventory_update_route(app, cursor,mydb)

if __name__ == "__main__":
    app.run(debug=True)

cursor.close()
mydb.close()
