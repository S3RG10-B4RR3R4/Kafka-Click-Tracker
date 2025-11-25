import asyncio
import json
import websockets
from kafka import KafkaConsumer
from threading import Thread

# Store connected WebSocket clients
connected_clients = set()

# Kafka Consumer
consumer = KafkaConsumer(
    'clicks',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='latest',
    enable_auto_commit=True
)

def consume_kafka():
    """Background thread to consume from Kafka and broadcast to WebSocket clients"""
    print("📥 Kafka Consumer started, listening for messages...")
    for message in consumer:
        click_data = message.value
        print(f"📨 Received click event: {click_data}")
        
        # Broadcast to all connected WebSocket clients
        asyncio.run(broadcast_message(click_data))

async def broadcast_message(data):
    """Send message to all connected WebSocket clients"""
    if connected_clients:
        message = json.dumps(data)
        await asyncio.gather(
            *[client.send(message) for client in connected_clients],
            return_exceptions=True
        )

async def websocket_handler(websocket, path):
    """Handle WebSocket connections"""
    connected_clients.add(websocket)
    print(f"✅ New client connected. Total clients: {len(connected_clients)}")
    
    try:
        # Keep connection alive
        await websocket.wait_closed()
    finally:
        connected_clients.remove(websocket)
        print(f"❌ Client disconnected. Total clients: {len(connected_clients)}")

async def start_websocket_server():
    """Start WebSocket server"""
    print("🌐 WebSocket Server starting on ws://localhost:8765")
    async with websockets.serve(websocket_handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == '__main__':
    # Start Kafka consumer in background thread
    kafka_thread = Thread(target=consume_kafka, daemon=True)
    kafka_thread.start()
    
    # Start WebSocket server
    asyncio.run(start_websocket_server())