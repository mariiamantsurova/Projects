from flask import Flask, redirect, request, render_template, flash
import math
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
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
        error_message = 'Invalid format.<br>Please provide square matrices of the same size, containing only integers separated by commas.'
        return render_template("calculator.html", error=error_message)


    # operation validation
    if not operation.lower() in ('multiply', 'add'):
        error_message = 'Invalid format.<br>Please provide square matrices of the same size, containing only integers separated by commas.'
        return render_template("calculator.html", error=error_message)


    # matrix validation
    try:
        mat1 = mat1.split(',')
        mat2 = mat2.split(',')
        error_message = 'Invalid format.<br>Please provide square matrices of the same size, containing only integers separated by commas.'
        # matrix's must be square
        # if the sqrt(mat) is int then it's a quadric mat
        if not math.sqrt(len(mat1)).is_integer():
            return render_template("calculator.html", error=error_message)

        # matrix's must be with the same size
        elif len(mat1) != len(mat2):
            return render_template("calculator.html", error=error_message)

        # matrix's must contain only int
        else:
            try:
                # Try to convert all elements to integers
                mat1 = list(map(int, mat1))
                mat2 = list(map(int, mat2))
            except:
                return render_template("calculator.html", error=error_message)

    except:
        return render_template("calculator.html", error=error_message)

    # Determine the size of the square matrix
    n = int(math.sqrt(len(mat1)))

    # Reshape the flat lists into matrix
    mat1 = np.array(mat1).reshape(n, n)
    mat2 = np.array(mat2).reshape(n, n)

    # matrix multiplication
    if operation == "multiply":
        result = np.dot(mat1, mat2)  # Or equivalently, result = mat1 @ mat2
    elif operation == "add":
        result = mat1 + mat2
    # Perform the operation
    if operation.lower() == "multiply":
        result = np.dot(mat1, mat2)
        operation_type = "Multiplication"
    elif operation.lower() == "add":
        result = mat1 + mat2
        operation_type = "Addition"

    # Render the result page
    return render_template("calculator.html", result=result.tolist(), operation=operation_type)

    #return render_template("calculator.html")


@app.errorhandler(404)  # Handle 404 errors - in case of page do not exist
def invalid_route(e):
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
