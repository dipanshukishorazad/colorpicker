from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    # For development only. For production, use gunicorn or another WSGI server.
    app.run(debug=True, host="0.0.0.0", port=5000)
