import cv2
image = cv2.imread('image.png')
if image is None:
  print("Oops ! your image is not loaded")
else:
  print("Image is loaded sucessfully")
  cv2.putText(image,"Hello Python",(300,300),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),2)
  cv2.imshow("Adding text over image",image)
  cv2.waitKey(0)
  cv2.destroyAllWindows()