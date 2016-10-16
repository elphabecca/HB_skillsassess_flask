from flask import Flask, render_template, request, flash
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

@app.route("/application-form")
def show_application():
    """Shows the form submission for fname, lname, salary requirement, and position."""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def show_app_submission():
    """Gets the first name, last name, salary, and job title from the form submission then 
    returns a response that acknowledges their application.
    """

    full_name = request.form.get("first-name") + " " + request.form.get("last-name")
    position = request.form.get("job")
    sal_req = request.form.get("sal-req")

    return render_template("application-response.html",
                            fullname=full_name,
                            position=position,
                            salreq=sal_req)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()

    # put this inside app.run when turning in? host="0.0.0.0"

