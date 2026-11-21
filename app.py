from flask import Flask, render_template, request, redirect, url_for
from database import (
    create_tables, add_farmer,
    save_history, get_history
)
from irrigation import irrigation_advice

app = Flask(__name__)

create_tables()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        name = request.form["name"]
        village = request.form["address"]
        mobile = request.form["phone"]

        return render_template(
            "farm.html",
            name=name,
            village=village,
            mobile=mobile
        )

    return render_template("register.html")


@app.route("/dashboard", methods=["POST"])
def dashboard():

    name = request.form["name"]
    village = request.form["village"]
    mobile = request.form["mobile"]
    crop = request.form["crop"]
    soil = request.form["soil"]
    size = float(request.form["field_size"])

    farmer_id = add_farmer(
        name, village, mobile, crop, soil, size
    )

    return render_template(
        "dashboard.html",
        farmer_id=farmer_id,
        name=name,
        crop=crop
    )


@app.route("/advice", methods=["POST"])
def advice():

    farmer_id = int(request.form["farmer_id"])
    soil = request.form["condition"]
    rain = request.form["rain"]

    suggestion = irrigation_advice(soil, rain)

    save_history(farmer_id, soil, rain, suggestion)

    return render_template(
        "dashboard.html",
        farmer_id=farmer_id,
        suggestion=suggestion
    )


@app.route("/history/<int:farmer_id>")
def history(farmer_id):
    records = get_history(farmer_id)

    return render_template(
        "history.html",
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)