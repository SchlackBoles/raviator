import cv2

def main():
    # Replace the src with your video stream address
    src = 'tcp://192.168.8.3:8000'
    cap = cv2.VideoCapture(src)

    if not cap.isOpened():
        print(f"Error: Failed to open the stream {src}")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to read frame from the video stream")
                break

            cv2.imshow("Frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
