from flask import Flask, request, jsonify
from flask_cors import CORS
from kafka import KafkaProducer
import json
import time

app = Flask(__name__)
CORS(app)

# Initialize Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

@app.route('/click', methods=['POST'])
def track_click():
    try:
        data = request.json
        click_event = {
            'page': data.get('page', 'unknown'),
            'timestamp': time.time(),
            'user_agent': request.headers.get('User-Agent', 'unknown')
        }
        
        # Send to Kafka
        producer.send('clicks', click_event)
        producer.flush()
        
        return jsonify({
            'status': 'success',
            'message': 'Click tracked successfully',
            'event': click_event
        }), 200
        
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    print("🚀 Producer (Flask API) starting on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)