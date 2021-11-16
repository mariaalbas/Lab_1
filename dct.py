from scipy.fftpack import dct
from skimage.io import imread
from skimage.color import rgb2gray


# We read the image Lenna.png and convert it to gray scale
image = rgb2gray(imread("lenna.png"))


# DCT convertor
def discrete_cosine_transform(input):
    # We use the dct function from the scipy package
    DCT = dct(input)
    return DCT  # Return the Discrete Cosine Transform of the image


# Computing the DCT
DCT = discrete_cosine_transform(input=image)


