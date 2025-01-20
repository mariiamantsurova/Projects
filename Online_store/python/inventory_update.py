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

            # extracting all SKUs from the clothes table
            cursor.execute("SELECT sku FROM online_store.clothes")
            cloth_ids = [row[0] for row in cursor.fetchall()]
            return render_template('inventory_update.html', cloth_ids=cloth_ids)

        except Exception as e:
            message = f"An unexpected error occurred: {e}"
            return render_template('inventory_update.html', message=message, is_error=True)

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


    # def handle_form():
    #     try:
    #         form_id = request.form.get('form_id')  # Get the name of the submit button
    #         if form_id is None:
    #             print("form_id is missing in the request")
    #             return render_template("inventory_update.html", error="An error occurred: form_id is missing.")
    #
    #         # extracting from the update form:
    #         if form_id == "update":
    #             try:
    #                 cloth_id = int(request.form['cloth_id'])
    #                 quantity_to_update = int(request.form['quantity_to_update'])
    #             except (TypeError, ValueError, KeyError):
    #                 return render_template("inventory_update.html", error="Invalid or missing data in update form.")
    #             # Proceed with the query...
    #
    #         elif form_id == "update":
    #             try:
    #                 cloth_id = int(request.form['cloth_id'])
    #                 quantity_to_update = int(request.form['quantity_to_update'])
    #             except (TypeError, ValueError, KeyError):
    #                 return render_template("inventory_update.html", error="Invalid or missing data in update form.")
    #             table_name = 'online_store.clothes'
    #             cloth_id = int(request.form['cloth_id'])
    #             quantity_to_update = int(request.form['quantity_to_update'])
    #             query = f"UPDATE {table_name} SET available_amount = available_amount + %s WHERE sku = %s"
    #             values = (quantity_to_update, cloth_id)
    #             # Execute the query
    #             cursor.execute(query, values)
    #             mydb.commit()
    #             return render_template("inventory_update.html", message="Record updated successfully!")
    #
    #         elif form_id == "add":
    #             table_name = 'online_store.new_items'
    #             cloth_id = int(request.form['cloth_id'])
    #
    #     except Exception as e:
    #         print(f"Error: {e}")
    #         return render_template("inventory_update.html", message=f"An error occurred: {e}")
    #
    #     query = f"INSERT INTO {table_name} (cloth_id, email, adding_date, adding_hour) VALUES (%s, %s)", (cloth_id, email, adding_date, adding_time)

    @app.route('/handle_form', methods=['POST'])
    def handle_form():
        try:
            form_id = request.form.get('form_id')
            if not form_id:
                return render_template("inventory_update.html", error="Form ID is missing.")

            if form_id == "update":
                # Handle update logic
                try:
                    cloth_id = int(request.form['cloth_id'])
                    quantity_to_update = int(request.form['quantity_to_update'])
                except (TypeError, ValueError, KeyError):
                    return render_template("inventory_update.html", error="Invalid or missing data in update form.")

                query = f"UPDATE online_store.clothes SET available_amount = available_amount + %s WHERE sku = %s"
                values = (quantity_to_update, cloth_id)
                cursor.execute(query, values)
                if cursor.rowcount == 0:
                    return render_template("inventory_update.html", error="No matching item found to update.")
                mydb.commit()
                return render_template("inventory_update.html", message="Record updated successfully!")

            elif form_id == "add":
                # Handle add logic
                try:
                    cloth_id = int(request.form['cloth_id'])
                    cloth_name = request.form['cloth_name']
                    cloth_price = float(request.form['cloth_price'])
                    available_amount = int(request.form['available_amount'])
                    img_path = request.form['img_path']
                except (TypeError, ValueError, KeyError):
                    return render_template("inventory_update.html", error="Invalid or missing data in add form.")

                query = """
                    INSERT INTO online_store.new_items (cloth_id, cloth_name, cloth_price, available_amount, img_path)
                    VALUES (%s, %s, %s, %s, %s)
                """
                values = (cloth_id, cloth_name, cloth_price, available_amount, img_path)
                cursor.execute(query, values)
                mydb.commit()
                return render_template("inventory_update.html", message="New item added successfully!")
        except Exception as e:
            print(f"Error: {e}")
            return render_template("inventory_update.html", error=f"An error occurred: {e}")

        # If the request method is not POST, redirect back to the inventory update page
        return redirect(f'/inventory_update/{request.form.get("manager_email")}')
