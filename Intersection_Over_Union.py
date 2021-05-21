import cv2
import numpy as np

image = cv2.imread("C:\CV\Learning_Tutorials\Data\image.jpg")
print("Shape of Image ", image.shape)
# Ground Truth
gt_x1 ,gt_y1, gt_x2, gt_y2= 290,13,350,300
# Predicted Box
pred_x1,pred_y1, pred_x2, pred_y2= 316,142,300,350

cv2.rectangle(image,(gt_x1,gt_y1), ((gt_x1 + gt_x2),(gt_y1+gt_y2)),(0,0,255),2) # Actual Red
cv2.rectangle(image,(pred_x1,pred_y1), ((pred_x1 + pred_x2),(pred_y1+pred_y2)),(255,0,0),2) # Predicted Blue

cv2.imshow("IMAGE", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Intersection Over Union
intersection_top_left = [np.maximum(gt_x1,pred_x1) , np.maximum(gt_y1,pred_y1)] # Taking the maximum point from the left and from the top(Either from gt or predict)
intersection_bottom_right = [np.minimum((gt_x1 +gt_x2) , (pred_x1 +pred_x2)) , np.minimum((gt_y1 + gt_y2),(pred_y1 +pred_y2))]
intersection_width = intersection_bottom_right[0] - intersection_top_left[0]
intersection_height = intersection_bottom_right[1] - intersection_top_left[1]

intersection = intersection_width * intersection_height
union = (gt_x2 * gt_y2) + (pred_x2 * pred_y2) - intersection # Ground Truth Area + Prediction area - Intersection
iou = intersection / union

print("IOU Score is :", iou)


# Print Intersection area With Green Color
cv2.rectangle(image,(intersection_top_left[0], intersection_top_left[1]),(intersection_bottom_right[0], intersection_bottom_right[1]),(0,255,0),-1)
cv2.imshow("IMAGE",image)
cv2.waitKey(0)
cv2.destroyAllWindows()