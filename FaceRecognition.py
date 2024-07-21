import face_recognition
import cv2
import datetime
import os


class FaceRecognition:
    is_images_loaded = False

    def __init__(self, known_faces_dir) -> None:
        print("init loading...")

        self.known_face_encodings = []
        self.load_known_faces(known_faces_dir)

        print("init completed")

    def load_known_faces(self, known_faces_dir):
        for filename in os.listdir(known_faces_dir):
            if filename.endswith((".jpg", ".jpeg", ".png")):
                known_face_image = face_recognition.load_image_file(
                    os.path.join(known_faces_dir, filename)
                )
                known_face_encoding = face_recognition.face_encodings(known_face_image)[
                    0
                ]
                self.known_face_encodings.append(known_face_encoding)
        print(f"Loaded {len(self.known_face_encodings)} known faces.")

    def is_your_face(self, image_path=None, frame=None):
        if self.is_images_loaded == False:
            print("loading images...")

        if image_path:
            unknown_image = face_recognition.load_image_file(image_path)
        elif frame is not None:
            unknown_image = frame
        else:
            raise ValueError("Either image_path or frame must be provided")

        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

        if self.is_images_loaded == False:
            self.is_images_loaded = True
            print("images loaded")

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                self.known_face_encodings, face_encoding
            )

            if True in matches:
                return True
        return False

    def capture_from_webcam(self):
        video_capture = cv2.VideoCapture(0)

        filename = ""

        while True:
            ret, frame = video_capture.read()
            cv2.imshow("video feed", frame)

            key = cv2.waitKey(1)

            if key == 13:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                filename = f"saved_photos/photo_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"Photo saved as {filename}")
                break

            if key == ord("q"):
                return

        video_capture.release()
        cv2.destroyAllWindows()

        if filename == "":
            raise ValueError("filename is not valid")

        return self.is_your_face(filename)
