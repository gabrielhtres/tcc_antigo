from skimage import io
import matplotlib.pyplot as plt
import time

cornHealth = 1162
cornGraySpot = 574
cornCommonRust = 1306
cornBlight = 1145

def countImageMinusThen(type, tam, height, width):
    total = 0
    minusList = []
    for i in range(1, tam):
        img = io.imread('data/' + type + '/' + 'Corn_' + type + ' (' + str(i) + ').jpg')
        if img.shape[0] < height or img.shape[1] < width:
            total += 1
            minusList.append(i)
    print('Tipo: ' + type)
    print('Total: ' + str(total))
    print('Lista: ' + str(minusList))

def verifyMinAndMaxDimensions(type, tam):
    wMin = 0
    wMax = 0
    hMin = 0
    hMax = 0
    for i in range(1, tam):
        img = io.imread('data/' + type + '/' + 'Corn_' + type + ' (' + str(i) + ').jpg')
        if i == 1:
            wMin = img.shape[1]
            hMin = img.shape[0]
            wMax = img.shape[1]
            hMax = img.shape[0]
        else:
            if img.shape[0] < hMin:
                hMin = img.shape[0]
            if img.shape[0] > hMax:
                hMax = img.shape[0]
            if img.shape[1] < wMin:
                wMin = img.shape[1]
            if img.shape[1] > wMax:
                wMax = img.shape[1]

    print('Tipo: ' + type)
    print('Altura minima: ' + str(hMin))
    print('Altura maxima: ' + str(hMax))
    print('Largura minima: ' + str(wMin))
    print('Largura maxima: ' + str(wMax))

def showImages(type, tam):
    for i in range(1, tam):
        img = io.imread('data/' + type + '/' + 'Corn_' + type + ' (' + str(i) + ').jpg')
        plt.imshow(img)
        plt.pause(5)

# verifyMinAndMaxDimensions('Common_Rust', 1306)
# countImageMinusThen('Common_Rust', 1306, 256, 256)
showImages('Common_Rust', 1306)
# plt.ion()

img = io.imread('data/Common_Rust/Corn_Common_Rust (1).jpg')
# plt.imshow(img)
# plt.pause(5)
# time.sleep(10)
# plt.close('all')