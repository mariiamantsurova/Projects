from flask import Flask, render_template, redirect, request, session
# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session


def register_and_login(app, cursor, mydb):
    @app.route("/register", methods=["POST", "GET"])
    def register():
        # if the user pressed the registration button
        if request.method == "POST":
            email = request.form.get("email")  # unique value
            name = request.form.get("name")
            password = request.form.get("password")
            sex = request.form.get("sex")
            if sex == "Male":  # in DB: 0 male, 1 female
                sex = 0
            else:
                sex = 1
            age = int(request.form.get("age"))
            faculty = request.form.get("faculty")
            is_admin = False  # Necessarily a regular user

            ###### needs to deal with enetring already existing email becuase its unique value #####

            # insert new user info the users table.
            query = "INSERT INTO online_store.users(email, username, password, age, sex, faculty, is_admin) VALUES(%s,%s,%s,%s,%s,%s,%s);"
            values = (email, name, password, age, sex, faculty, is_admin)
            # Execute the query
            cursor.execute(query, values)
            mydb.commit()
            cursor.execute("SELECT * FROM users;")
            print(cursor.fetchall())
            return render_template("register.html")

            # if temp_db.get(email) == password:
            #    session['email'] = email
            #    return redirect("/")
            # else:
            #    return render_template("register.html", message='Incorrect Login Details.')
        return render_template("register.html")

    @app.route("/login", methods=["POST", "GET"])
    def login():
        if request.method == "POST":
            email = request.form.get("email")  # unique value
        return render_template("login.html")

        """
                
        
@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/login")


        """
