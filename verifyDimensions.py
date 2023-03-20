from skimage import io, color
from skimage.transform import resize
import matplotlib.pyplot as plt
import time

cornHealth = 1162
cornGraySpot = 574
cornCommonRust = 1306
cornBlight = 1145

def trainModelTest():
    print('Função de criação do modelo')

def resizeImages():
    # Corn Health
    for i in range(1, cornHealth + 1):
        img = io.imread('data/Health/Corn_Health (' + str(i) + ').jpg')
        if img.shape[2] == 4:
            img = color.rgba2rgb(img)
        
        if img.shape[0] > 256 and img.shape[1] > 256:
            resized_img = resize(img, (256, 256), anti_aliasing=True)
            io.imsave('adjustedData/Health/Corn_Health' + str(i) + ').jpg', resized_img)

        if img.shape[0] == 256 and img.shape[1] == 256:
             io.imsave('adjustedData/Health/Corn_Health (' + str(i) + ').jpg', img)
    
    # Corn Gray Spot
    for i in range(1, cornGraySpot + 1):
        img = io.imread('data/Gray_Leaf_Spot/Corn_Gray_Spot (' + str(i) + ').jpg')
        if img.shape[2] == 4:
            img = color.rgba2rgb(img)
        
        if img.shape[0] > 256 and img.shape[1] > 256:
            resized_img = resize(img, (256, 256), anti_aliasing=True)
            io.imsave('adjustedData/Gray_Leaf_Spot/Corn_Gray_Spot (' + str(i) + ').jpg', resized_img)

        if img.shape[0] == 256 and img.shape[1] == 256:
             io.imsave('adjustedData/Gray_Leaf_Spot/Corn_Gray_Spot (' + str(i) + ').jpg', img)
    
    # Corn Common Rust
    for i in range(1, cornCommonRust + 1):
        img = io.imread('data/Common_Rust/Corn_Common_Rust (' + str(i) + ').jpg')
        if img.shape[2] == 4:
            img = color.rgba2rgb(img)
        
        if img.shape[0] > 256 and img.shape[1] > 256:
            resized_img = resize(img, (256, 256), anti_aliasing=True)
            io.imsave('adjustedData/Common_Rust/Corn_Common_Rust (' + str(i) + ').jpg', resized_img)

        if img.shape[0] == 256 and img.shape[1] == 256:
             io.imsave('adjustedData/Common_Rust/Corn_Common_Rust (' + str(i) + ').jpg', img)

    # Corn Blight
    for i in range(1, cornBlight + 1):
        img = io.imread('data/Blight/Corn_Blight (' + str(i) + ').jpg')
        if img.shape[2] == 4:
            img = color.rgba2rgb(img)
        
        if img.shape[0] > 256 and img.shape[1] > 256:
            resized_img = resize(img, (256, 256), anti_aliasing=True)
            io.imsave('adjustedData/Blight/Corn_Blight (' + str(i) + ').jpg', resized_img)

        if img.shape[0] == 256 and img.shape[1] == 256:
             io.imsave('adjustedData/Blight/Corn_Blight (' + str(i) + ').jpg', img)

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
    for i in range(2, tam):
        try:
            img = io.imread('adjustedData/' + type + '/' + 'Corn_' + type + ' (' + str(i) + ').jpg')
            plt.imshow(img)
            plt.pause(1)
        except:
            print('Imagem ' + str(i) + ' não encontrada')

# verifyMinAndMaxDimensions('Common_Rust', 1306)
# countImageMinusThen('Common_Rust', 1306, 256, 256)
# showImages('Common_Rust', 1306)
# plt.ion()

# img = io.imread('data/Common_Rust/Corn_Common_Rust (1).jpg')
# plt.imshow(img)
# plt.pause(5)
# time.sleep(10)
# plt.close('all')

# resizeImages()
showImages('Common_Rust', cornCommonRust)