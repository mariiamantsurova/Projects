from flask  import Flask , session
import mysql.connector
from python.home import home_route
from python.inventory_update import inventory_update_route
from python.registration_and_login import register_and_login
from python.clear_session import clear_session_route
from python.error import error_route
from flask_session import Session

# Setting up SQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="online_store"
)
cursor = mydb.cursor()



app = Flask(__name__, template_folder='templates')
# session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"]= "filesystem" 
Session(app)

# Import routes from other files
home_route(app, cursor,mydb)
inventory_update_route(app, cursor,mydb)
register_and_login(app, cursor,mydb)
error_route(app)
clear_session_route(app)



if __name__ == "__main__":
    app.run(debug=True)

cursor.close()
mydb.close()
