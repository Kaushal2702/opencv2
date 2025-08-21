import cv2
image=cv2.imread('image.png')
if image is None:
    print("Image is not found")
else:
    print("Image is found")
    resized=cv2.resize(image,(300,300))
    cv2.imshow("Original Image",image)
    cv2.imshow("Resized Image",resized)
    cv2.imwrite("resized image.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
