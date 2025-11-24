from flask import Flask, jsonify
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# Définition des métriques
REQUEST_COUNT = Counter('app_requests_total', 'Nombre total de requêtes')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Latence des requêtes en secondes')

@app.route('/')
def index():
    start_time = time.time()
    REQUEST_COUNT.inc()
    # Simulation d’un traitement aléatoire
    time.sleep(random.uniform(0.1, 0.5))
    REQUEST_LATENCY.observe(time.time() - start_time)
    return jsonify(message="Hello DevOps!"), 200

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
