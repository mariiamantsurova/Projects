from flask import Flask, render_template, request, redirect
from datetime import datetime

def inventory_update_route(app,cursor,mydb):
    @app.route('/inventory_update/<email>')
    def inventory_update(email):
        try:
            # Check if the user exists and is an admin
            cursor.execute("SELECT u.is_admin FROM online_store.users u WHERE u.email = %s", (email,))
            result = cursor.fetchone()
            # if the user doesn't exist
            if result is None:
                message = "User not found. Please register."
                return render_template('register.html', message=message, is_error=True)
            # checking if the user is an admin
            is_admin = result[0]
            if not is_admin:
                message = "Access denied. Admin privileges required."
                return render_template('home_page.html', message=message, is_error=True)
            # if the user is an admin:
            # extracting all SKUs from the clothes table
            cursor.execute("SELECT sku FROM online_store.clothes")
            cloth_ids = [row[0] for row in cursor.fetchall()]
            print(f"Email passed to template: {email}")
            return render_template('inventory_update.html', cloth_ids=cloth_ids, email=email)

        except Exception as e:
            message = f"An unexpected error occurred: {e}"
            return render_template('inventory_update.html', message=message, is_error=True)

    @app.route('/handle_form', methods=['POST'])
    def handle_form():
        try:
            manager_email = request.form.get('manager_email')
            if not manager_email:
                return render_template("inventory_update.html", error="Manager email is missing.")

            form_id = request.form.get('form_id')
            if not form_id:
                return render_template("inventory_update.html", error="Form ID is missing.")
            # checks that the information is being transferred correctly
            print(f"Manager Email: {manager_email}")  # This will help you check the email value
            print(f"Form Data: {request.form}")
            print(f"Manager Email: {manager_email}")
            print(f"Form ID: {form_id}")

            if form_id == "Update":
                # handle update
                try:
                    cloth_id = int(request.form['cloth_id'])
                    quantity_to_update = int(request.form['quantity_to_update'])
                except (TypeError, ValueError, KeyError):
                    return render_template("inventory_update.html", error="Invalid or missing data in update form.")
                # updating amount in clothes table
                query = f"UPDATE online_store.clothes SET available_amount = available_amount + %s WHERE sku = %s"
                values = (quantity_to_update, cloth_id)
                cursor.execute(query, values)
                if cursor.rowcount == 0:
                    return render_template("inventory_update.html", error="No matching item found to update.")
                mydb.commit()

                # insert into inventory_update table
                query2 = f"INSERT INTO online_store.inventory_update(sku, email, quantity) VALUES (%s, %s, %s)"
                values2 = (cloth_id, manager_email, quantity_to_update)
                cursor.execute(query2, values2)
                mydb.commit()
                return render_template("inventory_update.html", message="Record updated successfully!")

            elif form_id == "Add":
                # handle add
                try:
                    cloth_id = int(request.form['cloth_id'])
                    cloth_name = request.form['cloth_name']
                    cloth_price = float(request.form['cloth_price'])
                    available_amount = int(request.form['available_amount'])
                    is_promoted = int(request.form['is_promoted'])
                    img_path = request.form['img_path']
                except (TypeError, ValueError, KeyError):
                    return render_template("inventory_update.html", error="Invalid or missing data in add form.")
                # Add the new item to clothes table
                query3 = f"INSERT INTO online_store.clothes(sku, name, price, available_amount, is_promoted, img_path) VALUES (%s, %s, %s, %s, %s, %s)"
                values3 = (cloth_id, cloth_name, cloth_price, available_amount,is_promoted, img_path )
                cursor.execute(query3, values3)
                mydb.commit()
                # Add to the New_clothes table
                query4 = f"INSERT INTO online_store.new_items (sku, email) VALUES (%s, %s)"
                values4 = (cloth_id, manager_email)
                cursor.execute(query4, values4)
                mydb.commit()
                return render_template("inventory_update.html", message="New item added successfully!")
        except Exception as e:
            print(f"Error: {e}")
            return render_template("inventory_update.html", error=f"An error occurred: {e}")

        # If the request method is not POST, redirect back to the inventory update page

        return redirect(f'/inventory_update/{manager_email}')

    # @app.route('/handle_form', methods=['POST'])
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

