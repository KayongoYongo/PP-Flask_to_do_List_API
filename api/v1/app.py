from flask import Flask
from api.v1.views import app_views
import sys

"""
This line tells flask to use the module 
as the starting point for resolving resources 
like templates and static files
"""
app = Flask(__name__)

app.register_blueprint(app_views)

print(sys.path)

if __name__ == "__main__":
    app.run(debug=True)