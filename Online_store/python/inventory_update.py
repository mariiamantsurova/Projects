from flask import Flask, flash, render_template, request, session, redirect, url_for
import urllib.parse

def inventory_update_route(app,cursor,mydb):
    @app.route('/inventory_update/<email>', methods=['GET', 'POST'])
    def inventory_update(email):
        if request.method == 'GET':
            try:
                # # First, check if the user is logged in by verifying the session email
                # Check if the user exists and is an admin
                cursor.execute("SELECT u.is_admin FROM online_store.users u WHERE u.email = %s", (email,))
                result = cursor.fetchone()
                # if the user doesn't exist
                if result is None:
                    error = "User not found."
                    return render_template('error.html', error=error)
                # checking if the user is an admin
                is_admin = result[0]
                if not is_admin or session['email']!= email:
                    message = "Access denied. Admin privileges required."
                    return render_template('error.html', error=message)
                # if the user is an admin:
                # extract all SKUs from the clothes table
                cursor.execute("SELECT sku FROM online_store.clothes")
                cloth_ids = [row[0] for row in cursor.fetchall()]
                # print(f"Email passed to template: {email}")
                # extract user's name from the DB to display it in the page
                cursor.execute("SELECT username FROM users WHERE email = %s", (email,))
                user_name = cursor.fetchone()
                if user_name:
                    user_name = user_name[0]
                # Render the inventory update page with the necessary data
                return render_template('inventory_update.html', cloth_ids=cloth_ids, email=email, user_name=user_name)

            except Exception as e:
                error = f"An unexpected error occurred: {e}"
                return render_template('error.html', error=error)
        # method = "POST"
        else:
                manager_email = request.form.get('manager_email')
                if not manager_email:
                    error = "Manager email is missing."
                    return render_template('error.html', error=error)
                form_id = request.form.get('form_id')
                if not form_id:
                    error = "Form ID is missing."
                    return render_template('error.html', error=error)

                if form_id == "Update":
                    # handle update
                    try:
                        cloth_id = int(request.form['cloth_id'])
                        quantity_to_update = int(request.form['quantity_to_update'])
                    # updating amount in clothes table
                        query = f"UPDATE online_store.clothes SET available_amount = available_amount + %s WHERE sku = %s"
                        values = (quantity_to_update, cloth_id)
                        cursor.execute(query, values)
                        if cursor.rowcount == 0:
                            return render_template('error.html', error=error)
                        mydb.commit()

                    # insert into inventory_update table
                        query2 = f"INSERT INTO online_store.inventory_update(sku, email, quantity) VALUES (%s, %s, %s)"
                        values2 = (cloth_id, manager_email, quantity_to_update)
                        cursor.execute(query2, values2)
                        mydb.commit()
                        # redirect to success message page
                        return redirect(url_for('inventory_message', email= email))

                    except (TypeError, ValueError, KeyError):
                        return render_template("inventory_update.html", error="Invalid or missing data in update form.")                

                elif form_id == "Add":
                    # handle add
                    try:
                        cloth_id = int(request.form['cloth_id'])
                        cloth_name = request.form['cloth_name']
                        cloth_price = float(request.form['cloth_price'])
                        available_amount = int(request.form['available_amount'])
                        is_promoted = int(request.form['is_promoted'])
                        img_path = request.form['img_path']

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
                        # redirect to success message page
                        return redirect(url_for('inventory_message', email=email))

                    except (TypeError, ValueError, KeyError):
                        return render_template("error.html", error="Invalid or missing data in add form.")

    # Display the success message
    @app.route('/inventory_message')
    def inventory_message():
        # Decode the email from URL parameters
        email = request.args.get('email')
        decoded_email = urllib.parse.unquote(email)  # Decodes the URL-encoded email
        return render_template('inventory_message.html', message="The action was completed successfully!", email=decoded_email)
