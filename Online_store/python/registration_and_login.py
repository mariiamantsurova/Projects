from flask import Flask, render_template, redirect, request, session
# The Session instance is not used for direct access, you should always use flask.session
from flask_session import Session


def register(app, cursor, mydb):
    @app.route("/register", methods=["POST", "GET"])
    def register():
        if request.method == "POST":
            email = request.form.get("email")  # unique value
            password = request.form.get("password")
            sex = request.form.get("sex")
            age = request.form.get("age")
            is_manager = request.form.get("is_manager")
            faculty = request.form.get("faculty")


            # if temp_db.get(email) == password:
            #    session['email'] = email
            #    return redirect("/")
            # else:
            #    return render_template("login.html", message='Incorrect Login Details.')
        return render_template("login.html")


        """
                
        
        @app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/login")


        """ 
