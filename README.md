# PostureCheck - AI-Powered Posture Monitoring

A real-time posture monitoring system that uses AI to analyze your posture while lifting objects and provides feedback to prevent injury.

## Features

- 📸 **Smart Detection**: Automatically detects when you're carrying heavy items using Google's Gemini AI
- ⚡ **Real-time Analysis**: Instant posture feedback with MediaPipe pose detection
- 🤖 **Live Pose Visualization**: Stream processed video with skeleton overlay from MediaPipe
- 🔍 **Debug Mode**: Detailed skeleton with landmark indices, coordinates, and visibility scores
- 📹 **Incident Recording**: Records and replays posture incidents for review
- 🎯 **Interactive Dashboard**: Live camera feed with posture incident tracking
- 👁️ **Dual View Mode**: Toggle between raw camera feed and AI-processed view

## Quick Start

### Prerequisites

- Python 3.8+ 
- Node.js 18+
- Webcam access
- Google AI API key (optional, for item detection)

### Setup

1. **Clone and navigate to the project:**
   ```bash
   git clone <your-repo>
   cd posture-check
   ```

2. **Set up Google AI API (optional):**
   ```bash
   export GOOGLE_API_KEY=your_api_key_here
   ```

3. **Start the application:**
   ```bash
   chmod +x start.sh
   ./start.sh
   ```
   
   Or run separately:
   ```bash
   # Terminal 1 - Backend
   ./run-backend.sh
   
   # Terminal 2 - Frontend  
   ./run-frontend.sh
   ```

5. **Open your browser:**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:5001

6. **(Optional) Test the backend:**
   ```bash
   python test_backend.py
   ```

## Usage

1. **Start on the home page** - Read about posture importance and click "Start Recording"
2. **Enable camera access** when prompted
3. **Position yourself** in front of the camera
4. **The system will:**
   - Monitor your posture in real-time
   - Show live skeleton overlay with MediaPipe pose detection
   - Display landmark indices and coordinates in debug mode
   - Detect bad posture (knees not bent enough when lifting)
   - Record incidents lasting more than 5 seconds
   - Analyze items you're carrying for weight assessment
   - Display real-time knee angles and posture feedback

## How It Works

### Posture Detection & Visualization
- Uses MediaPipe to detect body landmarks in real-time
- Streams processed video with skeleton overlay back to frontend
- **Debug Mode Features:**
  - Green landmarks (circles) and magenta connections (lines)
  - Landmark indices and labels for key body points
  - Real-time coordinates and visibility scores
  - Toggle on/off via frontend button
- Calculates knee angles to determine if you're bending properly
- Threshold: Knee angle < 150° = Good posture
- Live pose visualization with landmarks and connections at 24fps
- Real-time posture feedback overlaid on video
- Optimized for smooth real-time performance

### Incident Recording
- Triggers when bad posture is detected for >5 seconds
- Records 10-second video clips
- Stores incidents with timestamps and posture data

### Item Analysis (Optional)
- Periodically captures frames for item detection (every 10 seconds)
- Uses Google's Gemini AI to identify carried objects
- Estimates object weight to determine lifting importance

### Performance Optimizations
- **24fps MediaPipe processing** for smooth real-time analysis
- **Optimized model complexity** (level 0) for fastest detection
- **Reduced detection thresholds** for faster tracking
- **Frame-based scheduling** for expensive operations
- **Optimized JPEG compression** (75% quality) for faster streaming
- **Selective debug rendering** (every other frame) to maintain performance

## Project Structure

```
posture-check/
├── app/                    # Next.js frontend
│   ├── components/         # React components
│   ├── api/               # API routes (legacy)
│   └── globals.css        # Styles
├── backend_server.py      # Flask backend server
├── posture_check.py       # Posture analysis logic
├── image_analysis.py      # AI image analysis
├── run-backend.sh         # Backend startup script
├── run-frontend.sh        # Frontend startup script
└── requirements.txt       # Python dependencies
```

## Development

This is a hackathon MVP focused on rapid prototyping. The system is designed to be:
- **Minimalistic**: Simple UI and core functionality
- **Interoperable**: Separate frontend/backend for flexibility
- **Quick to deploy**: Automated setup scripts

## Troubleshooting

**Camera not working?**
- Ensure browser permissions are granted
- Try refreshing the page
- Check if another app is using the camera

**Backend connection issues?**
- Make sure the Flask server is running on port 5001
- Check for CORS errors in browser console

**Python dependencies failing?**
- Try: `pip install --upgrade pip`
- Ensure you're using Python 3.8+

**MediaPipe visualization not showing?**
- Wait a few seconds after starting recording for AI processing to begin
- Toggle between "Raw Feed" and "AI View" using the button
- Use "🔍 Debug: ON/OFF" button to show/hide landmark details
- Check browser console for any connection errors to backend

**Debug features:**
- **Green circles**: Body landmarks detected by MediaPipe
- **Magenta lines**: Skeleton connections between landmarks
- **Yellow text labels**: Landmark indices and names (nose, shoulders, hips, knees, etc.)
- **White coordinate text**: Real-time x,y coordinates and visibility scores
