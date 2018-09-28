import numpy as np


class rle:

    def encode_image(self,binary_image):
        """
        Compress the image
        takes as input:
        image: binary_image
        returns run length code
        """

        pixels = binary_image.flatten()
        rle_code = [pixels[0]]
        count = 1

        for i in range(1, len(pixels)):

            if pixels[i] == pixels[i-1]:
                count += 1
            else:
                rle_code.append(count)
                count = 1

        rle_code.append(count)

        return rle_code



    def decode_image(self, rle_code, height , width):
        """
        Get original image from the rle_code
        takes as input:
        rle_code: the run length code to be decoded
        Height, width: height and width of the original image
        returns decoded binary image
        """
        # s = rle_code.split()
        pixel_value = rle_code[0]
        run_counts = rle_code[1:]
        image = []
        for i in run_counts:
            p = [pixel_value]*i
            image += p
            pixel_value = 255 if pixel_value == 0 else 0

        image = np.asarray(image)
        image = image.reshape(height, width)
        return image





        




