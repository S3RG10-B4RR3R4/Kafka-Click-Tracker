# Real-Time Click Tracker System

A real-time click tracking system built with Apache Kafka, Docker, Python (Flask + WebSockets), and vanilla JavaScript.

## 🏗️ Architecture

```
Frontend (HTML/JS) → Producer (Flask API) → Kafka → Consumer (WebSocket) → Dashboard (HTML/JS)
```

## 📦 Project Structure

```
kafka-click-tracker/
├── docker-compose.yml          # Kafka + Zookeeper configuration
├── producer/
│   ├── app.py                 # Flask API (Kafka Producer)
│   └── requirements.txt
├── consumer/
│   ├── app.py                 # WebSocket Server (Kafka Consumer)
│   └── requirements.txt
├── frontend/
│   └── index.html             # Click tracking interface
└── dashboard/
    └── index.html             # Real-time analytics dashboard
```

## 🚀 Getting Started

### Prerequisites

- Docker and Docker Compose
- Python 3.8+
- pip

### Step 1: Start Kafka & Zookeeper

Open Terminal 1:

```bash
docker-compose up -d
docker-compose logs -f
```

Wait until you see "Kafka started" in the logs.

### Step 2: Start the Producer (Flask API)

Open Terminal 2:

```bash
cd producer
pip install -r requirements.txt
python app.py
```

The Producer API will start on `http://localhost:5000`

### Step 3: Start the Consumer (WebSocket Server)

Open Terminal 3:

```bash
cd consumer
pip install -r requirements.txt
python app.py
```

The Consumer WebSocket will start on `ws://localhost:8765`

### Step 4: Serve the Frontend & Dashboard

Open Terminal 4 (from project root):

```bash
python -m http.server 8000
```

### Step 5: Open in Browser

- **Frontend**: http://localhost:8000/frontend/index.html
- **Dashboard**: http://localhost:8000/dashboard/index.html

## 🧪 Testing the System

1. Open the **Frontend** page
2. Open the **Dashboard** page in another browser tab
3. Click the "Click Me!" button on the Frontend
4. Watch the Dashboard update in real-time

## 📊 System Flow

1. User clicks button on **Frontend**
2. Frontend sends POST request to **Producer API** (Flask)
3. Producer sends event to **Kafka topic** (`clicks`)
4. **Consumer** reads from Kafka topic
5. Consumer broadcasts event via **WebSocket**
6. **Dashboard** receives WebSocket message and updates UI

## 🛠️ Technologies Used

- **Apache Kafka**: Message broker
- **Zookeeper**: Kafka coordination
- **Docker**: Containerization
- **Flask**: Python web framework (Producer)
- **WebSockets**: Real-time communication (Consumer)
- **Python**: Backend language
- **JavaScript**: Frontend interactivity

## 📝 API Endpoints

### Producer (Flask API)

- `POST /click` - Track a click event
  ```json
  {
    "page": "frontend",
    "clickNumber": 1
  }
  ```

- `GET /health` - Health check

## 🐛 Troubleshooting

### Kafka not starting

```bash
docker-compose down
docker-compose up -d
```

### Producer/Consumer connection errors

Make sure Kafka is running:
```bash
docker-compose ps
```

### WebSocket not connecting

1. Check if Consumer is running on port 8765
2. Check browser console for errors

## 📸 Screenshots

Include screenshots showing:
1. Frontend with clicks registered
2. Dashboard showing real-time updates

## 🎯 Key Features

- ✅ Real-time click tracking
- ✅ Scalable Kafka-based architecture
- ✅ WebSocket-powered live dashboard
- ✅ Beautiful, responsive UI
- ✅ Docker containerization

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

Created as part of a real-time data streaming assignment.