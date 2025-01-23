from flask import Flask, render_template, request, redirect
from datetime import datetime

def inventory_update_route(app,cursor,mydb):
    @app.route('/inventory_update/<email>')
    def inventory_update(email):
        # checking if the user is admin
        cursor.execute("SELECT u.is_admin FROM online_store.users u WHERE u.email = %s", (email,))     

        is_admin = cursor.fetchone()[0]
        if is_admin:
            return render_template("inventory_update.html")
        else:
            return redirect('/')
    @app.route('/handle_form', methods=['POST'])
    # def update_table():
    #     # if the manager pressed the update button:
    #     if request.method == 'POST':
    #         # Get data from the form
    #         table_name = 'online_store.clothes'
    #         cloth_id = request.form['cloth_id']
    #         quantity_to_update = int(request.form['quantity_to_update'])
    #         query = f"UPDATE {table_name} SET available_amount = available_amount + %s WHERE cloth_id = %s"
    #         values = (quantity_to_update, cloth_id)
    #         # Execute the query
    #         cursor.execute(query, values)
    #         mydb.commit()
    #         return render_template("inventory_update.html", message="Record updated successfully!")
    def handle_form():
        form_id = request.form.get('form_id')  # Get the name of the submit button
        # extracting from the update form:
        if form_id == "update":
            table_name = 'online_store.clothes'
            cloth_id = int(request.form['cloth_id'])
            quantity_to_update = int(request.form['quantity_to_update'])
            query = f"UPDATE {table_name} SET available_amount = available_amount + %s WHERE cloth_id = %s"
            values = (quantity_to_update, cloth_id)
            # Execute the query
            cursor.execute(query, values)
            mydb.commit()
            return render_template("inventory_update.html", message="Record updated successfully!")
        elif form_id == "add":
            table_name = 'online_store.new_items'
            cloth_id = int(request.form['cloth_id'])
            now = datetime.now()
            adding_time = now.time()
            adding_date = now.date()

            query = f"INSERT INTO {table_name} (cloth_id, email, adding_date, adding_hour) VALUES (%s, %s)", (cloth_id, email, adding_date, adding_time)



        # If the request method is not POST, redirect back to the inventory update page
        return redirect(f'/inventory_update/{request.form.get("manager_email")}')
