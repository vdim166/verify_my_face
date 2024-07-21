import face_recognition

# TODO: add webcam


class FaceRecognition:
    is_images_loaded = False

    def __init__(self, you_face) -> None:
        print("init loading...")

        known_face_image = face_recognition.load_image_file(you_face)
        known_face_encoding = face_recognition.face_encodings(known_face_image)[0]

        self.known_face_encodings = [known_face_encoding]
        # known_face_names = ["Your Face"]
        print("init completed")

    def is_your_face(
        self,
        image_path,
    ):

        if self.is_images_loaded == False:
            print("loading images...")

        unknown_image = face_recognition.load_image_file(image_path)

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


if __name__ == "__main__":

    fr = FaceRecognition("images/my_face.jpg")

    test_image_path = "images/test1.jpg"
    print("The image contains your face!", fr.is_your_face(test_image_path))

    test_image_path = "images/test2.jpg"
    print("The image contains your face!", fr.is_your_face(test_image_path))
