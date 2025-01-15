from flask import Flask, render_template

def error_route(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', error=e)