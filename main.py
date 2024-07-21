from FaceRecognition import FaceRecognition

if __name__ == "__main__":
    fr = FaceRecognition("my_faces")

    print(
        "The image contains your face ->", fr.is_your_face("images/test1.jpg")
    )  # TRUE
    print(
        "The image contains your face ->", fr.is_your_face("images/test2.jpg")
    )  # FALSE
    print("The webcam image contains your face ->", fr.capture_from_webcam())
