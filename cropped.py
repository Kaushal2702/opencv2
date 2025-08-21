import cv2
image = cv2.imread('image.png')
if image is not None:
    cropped =image[200:400,200:450]
    cv2.imshow("Original Image",image)
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()