import cv2
import face_recognition


def prepare_images(base_img, to_compare_img):
    """
    Given the base image location and the image to compare(frame),
     this function convert the BGR image to RGB and encode images,
      finally it returns both images in tuple format.
      """

    rgb_base_img = cv2.cvtColor(base_img, cv2.COLOR_BGR2RGB)
    encode_base_img = face_recognition.face_encodings(rgb_base_img)[0]

    to_compare_img_rgb = cv2.cvtColor(to_compare_img, cv2.COLOR_BGR2RGB)
    encode_to_compare_img = face_recognition.face_encodings(to_compare_img_rgb)[0]
    return encode_base_img, encode_to_compare_img