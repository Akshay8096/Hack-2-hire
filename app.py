from flask import Flask, render_template, request, url_for


app = Flask(__name__)

@app.route("/")
def home():
    pass
@app.route("/login")
def login():
    pass

@app.route("/appointmentrequest)
def appointmentrequest():
    pass

if __name__ == "__main__":
    app.run(debug=True)
