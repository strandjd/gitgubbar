import cv2
 
from fer import FER
 
import matplotlib.pyplot as plt
 
import matplotlib.image as mpimg

import os

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

input_image = cv2.imread("happy.jpg")

emotion_detector = FER()
#emotion_detector = FER(mtcnn=True)

# Output image's information
print(emotion_detector.detect_emotions(input_image))
print(emotion_detector)

# Save output in result variable
result = emotion_detector.detect_emotions(input_image)


# Now it is time to Highlight Yellow Bounding Box around face:
bounding_box = result[0]["box"]
emotions = result[0]["emotions"]
cv2.rectangle(input_image,(
  bounding_box[0], bounding_box[1]),(
  bounding_box[0] + bounding_box[2], bounding_box[1] + bounding_box[3]),
              (0, 155, 255), 2,)


# Now we will add Score to Bounding Box by using the following code:




emotion_name, score = emotion_detector.top_emotion(input_image)
for index, (emotion_name, score) in enumerate(emotions.items()):
  color = (211, 211,211) if score < 0.01 else (255, 0, 0)
  emotion_score = "{}: {}".format(emotion_name, "{:.2f}".format(score))

  cv2.putText(input_image,emotion_score,
               (bounding_box[0], bounding_box[1] + bounding_box[3] + 30 + index * 15),
               cv2.FONT_HERSHEY_SIMPLEX,0.5,color,1,cv2.LINE_AA,)
 
#Save the result in new image file
cv2.imwrite("emotion.jpg", input_image)



# Read image file using matplotlib's image module
result_image = mpimg.imread('emotion.jpg')
imgplot = plt.imshow(result_image)
# Display Output Image
plt.show()