from flask import Flask, redirect, request, render_template
import numpy as np

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main_page.html")


@app.route('/calculate')
def calculate():
    # Get the query parameters
    operation = request.args.get('operation')
    mat1 = request.args.get('mat1')
    mat2 = request.args.get('mat2')

    # Check for all required variables
    if not operation or not mat1 or not mat2:
        return "Missing parameters"
        #### url to homepage

    # operation validation
    if not operation.lower() in ('multiply', 'add'):
        return 'Operation is not valid'
        #### url to homepage

    # matrix validation
    try:
        mat1 = mat1.split(',')
        mat2 = mat2.split(',')

        # matrix's must be with the same size
        if len(mat1) != len(mat2):
            return 'Invalid format.<br>Please provide square matrix\'s and in the same size, contain only integers separated by commas'
            #### url to homepage

        # matrix's must be square
        elif len(mat1) % 2 != 0:
            return 'Invalid format.<br>Please provide square matrix\'s and in the same size, contain only integers separated by commas'
            #### url to homepage

        # matrix's must contain only int
        else:
            try:
                # Try to convert all elements to integers
                mat1 = list(map(int, mat1))
                mat2 = list(map(int, mat2))
            except:
                return 'Invalid format.<br>Please provide square matrix\'s and in the same size, contain only integers separated by commas'
                #### url to homepage

    except:
        return 'Invalid format.<br>Please provide square matrix\'s and in the same size, contain only integers separated by commas'
        #### url to homepage

    return render_template("calculator.html")


@app.errorhandler(404)  # Handle 404 errors - in case of page do not exist
def invalid_route(e):
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
