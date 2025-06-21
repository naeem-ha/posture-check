#!/bin/bash

echo "🚀 Starting Posture Check Frontend..."

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "📦 Installing Node.js dependencies..."
    npm install
fi

# Start the Next.js development server
echo "🌟 Starting Next.js frontend on http://localhost:3000..."
npm run dev 