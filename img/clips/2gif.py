import cv2 as cv


def main():
    # Importar archivos de video, parámetros: 
    #0 viene con una cámara, 1 cámara USB, 
    #lee el archivo de video cuando el nombre del archivo es
        #video_caputre = cv.VideoCapture ("img/clips/Banca Múltiple - Google Chrome 2021-05-10 12-25-56.mp4")
        video_caputre = cv.VideoCapture ("Banca Múltiple - Google Chrome 2021-05-10 12-25-56.mp4")

         # Obtener los parámetros del video importado
        fps = video_caputre.get(cv.CAP_PROP_FPS)
        width = video_caputre.get(cv.CAP_PROP_FRAME_WIDTH)
        height = video_caputre.get(cv.CAP_PROP_FRAME_HEIGHT)
        
        print("fps:", fps)
        print("width:", width)
        print("height:", height)
        
        # Defina el tamaño de la intersección, la altura y 
        # la anchura de cada fotograma definido más adelante deben ser 
        # las mismas aquí, de lo contrario, el video no se puede reproducir
        # Tenga en cuenta que aquí está la altura (altura, ancho)
        # size = (int(height-100), int(width))
        size = (int(width),int(height-100))
        
        # Crear objeto de escritura de video
        fourcc = cv.VideoWriter_fourcc('M', 'J', 'P', 'G')
        # fourcc = cv.VideoWriter_fourcc(*'DIVX') # https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
        # fourcc = cv.VideoWriter_fourcc(*'mp4v')
        # fourcc = cv.VideoWriter_fourcc(*'VIDX') 
        videp_write = cv.VideoWriter("videoFrameTarget.mp4",fourcc, int(fps*0.5), size)
        
        # Lea el fotograma del video, luego escriba el archivo y muéstrelo en la ventana
        success, frame_src = video_caputre.read()
        i=1
        while success and not cv.waitKey(1) == 27: 
                # Salir después de leer o presionar esc para salir
                
                # [ancho, alto] Para ser coherente con el parámetro de tamaño 
                # definido anteriormente, 
                # preste atención a la posición del parámetro
                # frame_target = frame_src[0:int(width), 0:int(height-144)]
                frame_target = frame_src[100:int(height), 0:int(width)]
                         # Escribir archivo de video
                videp_write.write(frame_target)
                
                         # Muestre el video recortado y el video original
                cv.imshow("video", frame_target)
                cv.imshow("Video_src", frame_src)
                
                         # Sigue leyendo
                success, frame_src = video_caputre.read()
                i+=1
                print(i)
        
        print("Recorte de video completado")
        
        videp_write.release()
         # Destruye la ventana, libera recursos
        # cv.destroyWindow("video")
        # cv.destroyWindow("Video_src")
        # # cv.release()


if __name__=="__main__":
    main()

cv.destroyAllWindows()





#import numpy as np
#import cv2 as cv
#cap = cv.VideoCapture('img/clips/Banca Múltiple - Google Chrome 2021-05-10 12-25-56 origal.mp4')
## Define the codec and create VideoWriter object
#fourcc = cv.VideoWriter_fourcc(*'DIVX')
#out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480))
#while cap.isOpened():
#    ret, frame = cap.read()
#    if not ret:
#        print("Can't receive frame (stream end?). Exiting ...")
#        break
#    frame = cv.flip(frame[0:480,0:640], 0)
#    # write the flipped frame
#    out.write(frame)
#    cv.imshow('frame', frame)
#    if cv.waitKey(1) == ord('q'):
#        break
## Release everything if job is finished
#cap.release()
#out.release()
#cv.destroyAllWindows()
