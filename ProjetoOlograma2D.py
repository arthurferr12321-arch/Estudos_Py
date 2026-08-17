import mediapipe as mp
import cv2

def main():
    #captura da webcan #

    cap = cv2.VideoCapture(0)

    while True:
        _, imagem = cap.read()

        cv2.imshow('captura', imagem)

        cv2.waitKey(1)

if __name__ == '__main__':
    main()