import cv2
image =cv2.imread('image.png')
if image is None:
   print("Oops ! your image is not loaded")
else:
   print("Image loaded finally")
   pt1=(50,50)
   pt2=(200,200)
   color=(0,0,255)
   thickness=3
   cv2.rectangle(image,pt1,pt2,color,thickness)
   cv2.imshow("Image focusing rectangle",image)
   cv2.waitKey(0)
   cv2.destroyAllWindows()