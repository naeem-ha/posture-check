import numpy as np

def calculate_angle(a, b, c):
    """Calculate angle at point b given three 2D points a, b, c"""
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    ba = a - b
    bc = c - b
    
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    return np.degrees(angle)

def check_lifting_posture(pose_landmarks, threshold=150):
    """
    Check if the lifting posture is good based on knee bend.
    
    Args:
        pose_landmarks: MediaPipe pose landmarks object
        threshold: Knee angle threshold in degrees (default: 150)
    
    Returns:
        tuple: (is_good_posture: bool, knee_angle: float, message: str)
               Returns (None, None, error_message) if detection fails
    """
    try:
        # Extract landmarks
        landmarks = pose_landmarks.landmark
        
        def get_point(landmark_id):
            lm = landmarks[landmark_id]
            return [lm.x, lm.y]
        
        # Get points for both legs using MediaPipe landmark IDs
        left_hip = get_point(23)    # LEFT_HIP
        left_knee = get_point(25)   # LEFT_KNEE
        left_ankle = get_point(27)  # LEFT_ANKLE
        
        right_hip = get_point(24)   # RIGHT_HIP
        right_knee = get_point(26)  # RIGHT_KNEE
        right_ankle = get_point(28) # RIGHT_ANKLE
        
        # Calculate knee angles for both legs
        left_knee_angle = calculate_angle(left_hip, left_knee, left_ankle)
        right_knee_angle = calculate_angle(right_hip, right_knee, right_ankle)
        
        # Use the average of both knee angles
        avg_knee_angle = (left_knee_angle + right_knee_angle) / 2
        
        # Determine if posture is good
        is_good_posture = avg_knee_angle < threshold
        
        # Generate appropriate message
        if is_good_posture:
            message = "Good posture - Knees bent"
        else:
            message = "Bad posture - Bend your knees!"
        
        return is_good_posture, avg_knee_angle, message
        
    except Exception as e:
        return None, None, f"Error detecting posture: {str(e)}"

"""# Code to use the function with MediaPipe Pose

import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if results.pose_landmarks:
        # Call the function
        is_good, angle, message = check_lifting_posture(results.pose_landmarks)
        
        if is_good is not None:
            # Use the results
            color = (0, 255, 0) if is_good else (0, 0, 255)
            cv2.putText(image, f'Knee Angle: {int(angle)}', (30, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
            cv2.putText(image, message, (30, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
    
    cv2.imshow('Posture Check', image)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""