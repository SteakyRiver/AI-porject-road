import cv2
from matplotlib import pyplot as plt

img = cv2.imread('road4.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

stop_data = cv2.CascadeClassifier('stopsign1.xml')
car_data = cv2.CascadeClassifier('cars1.xml')

stop_coords = []
car_coords = []

try:
    stop_coords = stop_data.detectMultiScale(img_gray, minSize=(20, 20)).tolist()
except:
    print('No stop signs found')

try:
    car_coords = car_data.detectMultiScale(img_gray, minSize=(20, 20)).tolist()
except:
    print('No cars found')

img_height, img_width, img_channels = img.shape
left_border = img_width / 2
right_border = img_width

def check_forward(car_coords,stop_coords):
    if len(stop_coords) != 0:
        return False
    elif len(car_coords) == 0:
        return True
    else:
        for (x, y, width, height) in car_coords:
            if x > left_border and x + width < right_border:
                if width / img_width > 0.15:
                    return False
        return True

for (x, y, width, height) in car_coords:
    cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (0, 255, 0), 5)

for (x, y, width, height) in stop_coords:
    cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (0, 255, 0), 5)


plt.subplot(1, 1, 1)
plt.imshow(img_rgb)
plt.show()
print('Permission to go:', check_forward(car_coords,stop_coords))
