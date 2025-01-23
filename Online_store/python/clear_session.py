from flask import session, redirect

def clear_session_route(app):
    @app.route('/clear_session')
    def clear_session():
        session.clear()  # Remove all keys from the session
        return redirect('/login')
    