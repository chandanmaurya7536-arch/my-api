from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

FILES = [
    "db.txt",
    "db2.txt"
]

@app.route("/")
def home():
    return "API Running"

@app.route("/search")
def search():
    phone = request.args.get("phone")

    if not phone:
        return jsonify({"error": "phone required"}), 400

    results = []

    for file in FILES:
        try:
            with open(file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)

                for row in reader:
                    if row.get("phoneNumber") == phone:
                        results.append(row)
        except FileNotFoundError:
            pass

    return jsonify(results)

app = app
