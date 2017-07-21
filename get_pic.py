import cv2

video_path = 'test_videos/challenge.mp4'
cap = cv2.VideoCapture(video_path)
count = 1
while count <2:
    print(cap)
    ret, frame = cap.read()
    print(frame)
    cv2.imwrite('./challenge.jpg', frame)
    count +=1
cap.release()
