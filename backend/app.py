import requests
from flask import Flask, json, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/points", methods=["GET"])
@cross_origin()
def points():

    if request.method == "GET":
        params = {
            "language": request.args.get("language"),
            "origin": request.args.get("origin"),
            "waypoints": request.args.get("waypoints"),
            "destination": request.args.get("destination"),
            "key": request.args.get("key"),
        }
        data = requests.get(
            url="https://maps.googleapis.com/maps/api/directions/json",
            params=params,
        )
        response = app.response_class(
            response=json.dumps(data.json()), status=200, mimetype="application/json"
        )
    return response


if __name__ == "__main__":
    app.run(debug=True)
