from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") 
def home():
    return render_template("home.html")
    
@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

@app.route("/programs/")
def programs():
    return render_template("programs.html")

if __name__ == "__main__":
    app.run()