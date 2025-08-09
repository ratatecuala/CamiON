from flask import Flask, request, jsonify
from routes.optimize import optimize_routes

app = Flask(__name__)

@app.get("/salud")
def salud():
    return {"estado": "ok"}

@app.post("/optimizar")
def optimizar():
    data = request.get_json(force=True)
    try:
        resultado = optimize_routes(data)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
