import os

from flask import Flask, render_template, request

app = Flask(__name__)


# Illustrative trips for the landing page design preview. Replace with a
# query on the trips table once database/db.py is implemented.
SAMPLE_TRIPS = [
    {"id": 1, "slug": "dharamshala", "title": "Dharamshala Escape", "destination": "Dharamshala", "date": "6 Nov", "duration": "3D/2N", "departs": "Delhi", "price_inr": 5999, "category": "mountains"},
    {"id": 2, "slug": "rishikesh", "title": "Rishikesh Adventure", "destination": "Rishikesh", "date": "13 Nov", "duration": "2D/1N", "departs": "Delhi", "price_inr": 3999, "category": "adventure"},
    {"id": 3, "slug": "kasol", "title": "Kasol Weekend", "destination": "Kasol", "date": "20 Nov", "duration": "3D/2N", "departs": "Delhi", "price_inr": 4999, "category": "mountains"},
    {"id": 4, "slug": "jibhi", "title": "Jibhi Getaway", "destination": "Jibhi", "date": "27 Nov", "duration": "3D/2N", "departs": "Delhi", "price_inr": 5499, "category": "relax"},
    {"id": 5, "slug": "bir-billing", "title": "Bir Billing Paragliding", "destination": "Bir Billing", "date": "4 Dec", "duration": "3D/2N", "departs": "Delhi", "price_inr": 6499, "category": "adventure"},
    {"id": 6, "slug": "coorg", "title": "Coorg Coffee Trails", "destination": "Coorg", "date": "11 Dec", "duration": "3D/2N", "departs": "Bangalore", "price_inr": 6999, "category": "relax"},
]

TRIP_FILTERS = [
    ("all", "All trips"),
    ("mountains", "Mountains"),
    ("adventure", "Adventure"),
    ("relax", "Relax & unwind"),
]


def trip_image(slug):
    # Drop a photo at static/images/trips/<slug>.jpg and the card uses it.
    filename = f"images/trips/{slug}.jpg"
    return filename if os.path.exists(os.path.join(app.static_folder, filename)) else None


@app.route("/")
def landing():
    trips = [dict(trip, image=trip_image(trip["slug"])) for trip in SAMPLE_TRIPS]
    return render_template("landing.html", trips=trips, filters=TRIP_FILTERS)


# Form screens only. Implement account creation and sessions as you learn.
@app.route("/register", methods=["GET", "POST"])
def register():
    message = "Account creation is a future lesson. Nothing has been saved." if request.method == "POST" else None
    return render_template("register.html", error=message)


@app.route("/login", methods=["GET", "POST"])
def login():
    message = "Sign-in is a future lesson. No session has been created." if request.method == "POST" else None
    return render_template("login.html", error=message)


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


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
