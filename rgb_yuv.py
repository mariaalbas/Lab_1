# We define the RGB values randomly
R = 100
G = 200
B = 50

# We define the three YUV values equivalent to the RGB values chosen above
Y = 152
U = 69
V = 90


# Translator from RGB to YUV values using the equivalent conversion for each value
def rgb_to_yuv(R, G, B):
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16
    U = -0.148 * R - 0.291 * G + 0.439 * B + 128
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128
    return Y, U, V


# Translator from YUV to RGB values using the equivalent conversion for each value
def yuv_to_rgb(Y, U, V):
    R = 1.164 * Y + 1.596 * V
    G = 1.164 * Y - 0.392 * U - 0.813 * V
    B = 1.164 * Y + 2.017 * U
    return R, G, B


# Calling functions and printing the results
y, u, v = rgb_to_yuv(R, G, B)
r, g, b = yuv_to_rgb(Y, U, V)




