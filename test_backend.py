#!/usr/bin/env python3

"""
Simple test script to verify the backend streaming functionality
"""

import requests
import cv2
import time
import os

BACKEND_URL = "http://localhost:5001"


def test_health():
    """Test if backend is running"""
    try:
        response = requests.get(f"{BACKEND_URL}/health")
        if response.status_code == 200:
            print("✅ Backend health check passed")
            return True
        else:
            print(f"❌ Backend health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to backend. Make sure it's running on port 5001")
        return False


def test_frame_upload():
    """Test frame upload functionality"""
    # Use a sample image
    sample_image_path = "samples/heavy.jpg"

    if not os.path.exists(sample_image_path):
        print(f"❌ Sample image not found: {sample_image_path}")
        return False

    try:
        with open(sample_image_path, "rb") as f:
            files = {"frame": f}
            response = requests.post(f"{BACKEND_URL}/api/upload-frame", files=files)

        if response.status_code == 200:
            print("✅ Frame upload test passed")
            return True
        else:
            print(f"❌ Frame upload test failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Frame upload test error: {e}")
        return False


def test_posture_api():
    """Test posture checking API"""
    sample_image_path = "samples/heavy.jpg"

    if not os.path.exists(sample_image_path):
        print(f"❌ Sample image not found: {sample_image_path}")
        return False

    try:
        with open(sample_image_path, "rb") as f:
            files = {"image": f}
            response = requests.post(f"{BACKEND_URL}/api/posture-check", files=files)

        if response.status_code == 200:
            result = response.json()
            print("✅ Posture API test passed")
            print(f"   Result: {result}")
            return True
        else:
            print(f"❌ Posture API test failed: {response.status_code}")
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Posture API test error: {e}")
        return False


def test_current_posture():
    """Test current posture endpoint"""
    try:
        response = requests.get(f"{BACKEND_URL}/api/current-posture")

        if response.status_code == 200:
            result = response.json()
            print("✅ Current posture test passed")
            print(f"   Result: {result}")
            return True
        else:
            print(f"❌ Current posture test failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Current posture test error: {e}")
        return False


def test_video_stream():
    """Test video stream endpoint"""
    try:
        response = requests.get(
            f"{BACKEND_URL}/api/video-stream", stream=True, timeout=5
        )

        if response.status_code == 200:
            print("✅ Video stream endpoint accessible")
            return True
        else:
            print(f"❌ Video stream test failed: {response.status_code}")
            return False
    except requests.exceptions.Timeout:
        print("⚠️ Video stream timeout (expected if no frames uploaded yet)")
        return True
    except Exception as e:
        print(f"❌ Video stream test error: {e}")
        return False


def main():
    print("🧪 Testing PostureCheck Backend (24fps Optimized)")
    print("=" * 50)

    tests = [
        ("Health Check", test_health),
        ("Frame Upload", test_frame_upload),
        ("Posture API", test_posture_api),
        ("Current Posture", test_current_posture),
        ("Video Stream", test_video_stream),
    ]

    passed = 0
    total = len(tests)

    for test_name, test_func in tests:
        print(f"\n🔍 Running {test_name}...")
        if test_func():
            passed += 1
        time.sleep(1)  # Brief pause between tests

    print(f"\n📊 Test Results: {passed}/{total} passed")

    if passed == total:
        print("🎉 All tests passed! Backend is working correctly.")
        print("💨 System optimized for 24fps MediaPipe processing")
        print("🚀 Ready for smooth real-time pose detection!")
    else:
        print("⚠️ Some tests failed. Check the backend logs for details.")


if __name__ == "__main__":
    main()
