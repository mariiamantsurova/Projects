from flask  import Flask , session
import mysql.connector
from main.home import home_route
from main.inventory_update import inventory_update_route
from main.registration_and_login import register_and_login
from main.error import error_route
from flask_session import Session

# Setting up SQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="online_store_15"
)
cursor = mydb.cursor()

cursor.execute("SELECT IFNULL(MAX(order_num), 1000) FROM online_store_15.transactions")
order_num = cursor.fetchone()[0] 
app = Flask(__name__, template_folder='templates')


# session config
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"]= "filesystem" 
Session(app)

# Import routes from other files
home_route(app, cursor,mydb, order_num)
inventory_update_route(app, cursor,mydb)
register_and_login(app, cursor,mydb)
error_route(app)



if __name__ == "__main__":
    app.run(debug=True)

cursor.close()
mydb.close()
