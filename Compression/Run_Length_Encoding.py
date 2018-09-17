import numpy as np

class rle:

    def encode_image(self,binary_image):
        """
        Compress the image
        :param binary_image:
        :return:
        """


        return np.zeros(100) #replace zeros with rle_code 



    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        Height, width: height and width of the original image
        """


        return  np.zeros((100,100), np.uint8) #replace zeros with image reconstructed from rle_Code





        




