from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("landing.html")


# Form screens only. Implement account creation and sessions as you learn.
@app.route("/register", methods=["GET", "POST"])
def register():
    message = "Account creation is a future lesson. Nothing has been saved." if request.method == "POST" else None
    return render_template("register.html", error=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = "Sign-in is a future lesson. No session has been created." if request.method == "POST" else None
    return render_template("login.html", error=message)


def coming_soon(title, description):
    return render_template("coming_soon.html", title=title, description=description)


# Placeholder routes — implement these while following the playlist.
@app.route("/logout")
def logout():
    return coming_soon("Sign out", "Build session logout after implementing sign-in.")


@app.route("/profile")
def profile():
    return coming_soon("Your profile", "Build traveller and organiser profiles here.")


@app.route("/trips")
def trips():
    return coming_soon("Explore weekend trips", "Build a list of published trips, then add destination, departure city, date and price filters.")


@app.route("/trips/add")
def add_trip():
    return coming_soon("List a weekend trip", "Build an organiser form with a title, destination, departure city, dates, price per person and description.")


@app.route("/trips/<int:id>")
def trip_detail(id):
    return coming_soon("Trip details", "Build an itinerary and organiser details page for each published trip.")


@app.route("/trips/<int:id>/edit")
def edit_trip(id):
    return coming_soon("Edit a trip", "Let organisers edit only the trips they own.")


@app.route("/trips/<int:id>/delete")
def delete_trip(id):
    return coming_soon("Remove a trip", "Build a confirmation screen, then a protected POST action. Never delete a trip through a GET request.")


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5001)
