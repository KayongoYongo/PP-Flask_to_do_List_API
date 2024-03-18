from flask import Flask, request, jsonify

"""
This line tells flask to use the module 
as the starting point for resolving resources 
like templates and static files
"""
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify("Hello world")

if __name__ == "__main__":
    app.run(debug=True)