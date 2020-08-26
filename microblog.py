from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}

# TODO: Em user registration
# TODO: link: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins
