import cv2
import numpy as np
import sys
import os
import re
import pytesseract
import time
def usage():
    print("--- text recognition ---")
    print('ocrsearch ImageFileOrDirPath WordToSearch')
    sys.exit(0)


# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#dilation
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)


def preprocess(image):

    img = cv2.imread('image.jpg')
    gray = get_grayscale(image)
    thresh = thresholding(gray)
    opening = opening(gray)
    canny = canny(gray)
    return canny

def getargs():
    try:
        Path = sys.argv[1]
        wordtosearch = sys.argv[2]
    except:
        usage()
    if os.path.isfile(Path):
        return [Path],wordtosearch
    elif os.path.isdir(Path):
        return [os.path.join(Path, f) for f in os.listdir(Path) if os.path.isfile(os.path.join(Path, f))],wordtosearch




pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
files,WordToSearch= getargs()

try:
    destdir  = os.getcwd()+ "/OCR"+str(time.time())
    os.mkdir(destdir)
except OSError:
    print ("Creation of the directory %s failed" % path)

print(files)
i=0
for image in files:
    i+=1
    img = cv2.imread(image)
    d = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    for i in range(len(d["text"])):
        if re.search(r""+WordToSearch,d["text"][i],re.IGNORECASE):
            print(d["text"][i]+ " Found in "+image)
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            imgc = cv2.rectangle(img, (x, y), (x + w, y + h), (100, 255, 100), 2)
            cv2.imwrite("G:/Luxant/Zimmerman/"+WordToSearch+str(i)+".png", img) 
            
