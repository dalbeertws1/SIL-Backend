import cv2
import mediapipe as mp
from math import hypot


def bhabhi(person_image):

    image = cv2.imread(person_image)

    #add background
    image = cv2.copyMakeBorder(
        image, 100, 100, 100, 100, cv2.BORDER_CONSTANT, value=[255, 255, 255])
    hair = cv2.imread("/home/dalbeer/Documents/filterr/Women-Hair-PNG-HD.png")

    #face mesh
    mp_face_mesh =  mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Facial landmarks
    result = face_mesh.process(rgb_image)

    height, width, _ = image.shape
    for facial_landmarks in result.multi_face_landmarks:
        bottom=((facial_landmarks.landmark[152].x *width)), ((facial_landmarks.landmark[152].y*height))
        left_side=((facial_landmarks.landmark[103].x *width)), ((facial_landmarks.landmark[103].y*height))
        right_side=((facial_landmarks.landmark[332].x *width)), ((facial_landmarks.landmark[332].y*height))
        forehead_width = int(hypot(left_side[0] - right_side[0],
                    left_side[1] - right_side[1]))
        forehead_height = int(forehead_width*1.1)  
        left_side=((facial_landmarks.landmark[103].x *width)-forehead_width), ((facial_landmarks.landmark[103].y*height-forehead_width/1.5))
        right_side=((facial_landmarks.landmark[332].x *width)+forehead_width), ((facial_landmarks.landmark[332].y*height))
        forehead_width = int(hypot(left_side[0] - right_side[0],
                    left_side[1] - right_side[1]))
        forehead_height = int(hypot(bottom[0]-forehead_width/2 - left_side[0],
                    bottom[1] - left_side[1]))

        #hair position
        top_left=(int(left_side[0]),int(left_side[1]))
        # bottom_right =  (int(right_side[0]),int(right_side[1]))

        # addning new hair
        hair = cv2.resize(hair, (forehead_width, forehead_height))

        hair_gray = cv2.cvtColor(hair, cv2.COLOR_BGR2GRAY)
        _, nose_mask = cv2.threshold(hair_gray, 0, 240, cv2.THRESH_BINARY_INV)

        hair_area = image[top_left[1]: top_left[1]+forehead_height ,
                    top_left[0]: top_left[0] + forehead_width]
        
        hair_area_no_hair = cv2.bitwise_and(hair_area, hair_area, mask=nose_mask)
        
        final_hair = cv2.add(hair_area_no_hair, hair)
        image[top_left[1]: top_left[1] + forehead_height,
                    top_left[0]: top_left[0] + forehead_width] = final_hair
    resize=cv2.resize(image , (500,500))

    return(resize)