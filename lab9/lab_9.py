import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

"""img = cv2.imread("testocr.png")
custom_config = r'--oem 3 --psm 6'
image_to_string(img)
print(pytesseract.image_to_string(img))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""


def read_text_from_image(a: str):
    return pytesseract.image_to_string(cv2.imread(a), config=r'--oem 3 --psm 6')


print(read_text_from_image("testocr.png"))
