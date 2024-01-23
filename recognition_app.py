import cv2
import face_recognition


def face_id():
    """
    This function by using cv2 module, try to find a valid camera port,
    if it finds then the camera starts and after few seconds it takes a photo(base_img),
    saves it like "faceid.jpg" and return False, if not then the function return True.
    """

    no_camera = True
    for port in (0, 1, 2, 3):
        try:
            cam = cv2.VideoCapture(port)
            print(cam)
            rectangle_text = "Don't move!"
            counter = 0
            while True:
                ret, frame = cam.read()
                try:
                    if counter == 120:
                        cv2.imwrite("faceid.jpg", frame)
                        cv2.destroyWindow("frame")
                        break
                    add_rectangle_and_text(frame, rectangle_text)
                    counter += 1
                except:
                    pass
                cv2.imshow("frame", frame)
                key = cv2.waitKey(1)
                no_camera = False
        except:
            pass
    return no_camera

def add_rectangle_and_text(frame, name):
    """
    This function add a rectangle around the face,
    and add some text, to find the face location coordinates,
     it's using the face_location method from face_recognition module.
    """

    resized_frame = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3)
    rgb_resized_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
    y0, x1, y1, x0 = face_recognition.face_locations(rgb_resized_frame)[0]
    cv2.rectangle(frame,
                  (int(x0 / 0.3), int(y0 / 0.3)),
                  (int(x1 / 0.3), int(y1 / 0.3)),
                  (0, 248, 6), 2)
    cv2.putText(frame,
                name,
                (int(x0 / 0.3),
                 int(y0 / 0.3) - 5),
                cv2.FONT_ITALIC,
                1, (0, 248, 6), 2)

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

def compare_images(base_img, to_compare_img):
    """
    By using compare_faces method from face_recognition module,
    it compares the base image with image to compare(frame),
    and return a boolean value, True or False.
    """

    compare_img = face_recognition.compare_faces([base_img], to_compare_img)
    compare_img = compare_img[0]
    return compare_img

def video_capture_logic(name, base_image_path="faceid.jpg"):
    """
    This is the main function return True,
     if on both images the faces are similar and False otherwise.
    """

    base_image_path = cv2.imread(base_image_path)
    cam = cv2.VideoCapture(0)
    compare = None
    rectangle_text = "Scanning, Don't move!"
    counter = 0
    not_recognized = 0
    while True:
        ret, frame = cam.read()
        try:
            add_rectangle_and_text(frame, rectangle_text)
            counter += 1
            if counter > 180 and compare == True or not_recognized == 3:
                cv2.destroyWindow("frame")
                break
            if (compare is None or compare == False) and counter == 90:
                not_recognized += 1
                counter = 0
                base_img, to_compare_img = prepare_images(base_image_path, frame)
                compare = compare_images(base_img, to_compare_img)
                if compare == False:
                    base_img, to_compare_img = prepare_images(base_image_path, frame)
                    compare = compare_images(base_img, to_compare_img)
                    rectangle_text = "I don' know who are you!"
                elif compare == True:
                    rectangle_text = f"Hi {name}!"
        except:
            pass
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)
    return compare