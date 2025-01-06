from flask import Flask, render_template, request, redirect
import mysql.connector
import os

app = Flask(__name__, template_folder='templates')

# Setting up SQL connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="online_store"
)
cursor = mydb.cursor()

@app.route('/')
def homepage():
    return render_template("home_page.html")

@app.route('/inventory_update/<email>')
def inventory_update(email):
    # checking if the user is admin
    cursor.execute("SELECT email FROM online_store.managers")
    admins = [admin[0] for admin in cursor.fetchall()]
    # if he is an admin we'll redirect him to the update page
    if email in admins:
        return render_template("inventory_update.html")
    else:
        return redirect('/')
@app.route('/update_table', methods=['POST'])
def update_table():
    # if the manager pressed the update button:
    if request.method == 'POST':
        # Get data from the form
        table_name = 'online_store.clothes'
        cloth_id = request.form['cloth_id']
        quantity_to_update = int(request.form['quantity_to_update'])
        query = f"UPDATE {table_name} SET available_amount = available_amount + %s WHERE cloth_id = %s"
        values = (quantity_to_update, cloth_id)
        # Execute the query
        cursor.execute(query, values)
        mydb.commit()
        return render_template("inventory_update.html", message="Record updated successfully!")


    # If the request method is not POST, redirect back to the inventory update page
    return redirect(f'/inventory_update/{request.form.get("manager_email")}')


if __name__ == "__main__":
    app.run(debug=True)
