import os
from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Initialise empty list to store all the todo's
list = []


@app.route("/", methods=["GET", "POST"])
def index():
    """Get the list the user has given you"""
    if request.method == "POST":
        item = request.form.get("todo")  # Get the input
        if not item:
            return render_template("index.html", error="Must input a value", list=list)
        # Append item to list
        list.append(item)
        # Return to page to view updated list
        return redirect("/")
    return render_template("index.html", list=list)


@app.route("/delete", methods=["POST"])
def new():
    """Create a new list"""
    list.clear()
    return redirect("/")


# Enable debugging mode
if __name__ == "__main__":
    app.run(debug=True)
