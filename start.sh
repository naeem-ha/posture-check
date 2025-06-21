#!/bin/bash

echo "🚀 Starting PostureCheck Application"
echo "===================================="
echo ""

# Function to run backend in the background
run_backend() {
    echo "🔧 Starting Backend Server..."
    ./run-backend.sh &
    BACKEND_PID=$!
    echo "Backend PID: $BACKEND_PID"
}

# Function to run frontend
run_frontend() {
    echo "🎨 Starting Frontend Server..."
    sleep 3  # Give backend time to start
    ./run-frontend.sh
}

# Function to cleanup on exit
cleanup() {
    echo ""
    echo "🛑 Shutting down servers..."
    if [ ! -z "$BACKEND_PID" ]; then
        kill $BACKEND_PID 2>/dev/null
    fi
    pkill -f "backend_server.py" 2>/dev/null
    pkill -f "next dev" 2>/dev/null
    echo "✅ Cleanup complete"
    exit 0
}

# Set up signal handlers
trap cleanup SIGINT SIGTERM

# Check if both script files exist and are executable
if [ ! -x "run-backend.sh" ] || [ ! -x "run-frontend.sh" ]; then
    echo "❌ Error: Backend or frontend scripts not found or not executable"
    echo "Please run: chmod +x run-backend.sh run-frontend.sh"
    exit 1
fi

# Start backend
run_backend

# Start frontend (this will block)
run_frontend

# This should never be reached, but just in case
cleanup 