import cv2
from fer import FER

def detect_emotion():
    detector = FER(mtcnn=True)
    cap = cv2.VideoCapture(0)
    
    ret, frame = cap.read()
    cap.release()
    
    if ret:
        result = detector.top_emotion(frame)
        if result:
            emotion, score = result
            return emotion
    return "neutral"
