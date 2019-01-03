import cv2

def main():
       
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()


    while ret:
        
        framediff = cv2.absdiff(frame1, frame2)
        
        grey = cv2.cvtColor(framediff, cv2.COLOR_BGR2GRAY)
        
        ret, thresh = cv2.threshold( grey, 20, 255, cv2.THRESH_BINARY)
        
        img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame2, contours, -1, (0, 0, 255), 2)

        cv2.imshow("Original", frame1)
        cv2.imshow("Output", frame2)
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        frame2 = frame1
        ret, frame1 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()