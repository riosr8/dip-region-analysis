###Raul Rios

#Assignment 2

####Region Counting

1a. I have first computed the histogram by creating a list of size 256 initialized to zeros. I then iterate through the image and count the frequency of each pixel value between 0 and 255. In order to find the optimal threshold, I have applied the algorithm from the slides to find the optimal threshold. In order to binarize the image I have used the optimal threshold to to set the pixel value of the binary image to 255 if the pixel value is below the threshold, otherwise set it to 0.

1b. For this task, I have made use of the blob coloring algorithm and finding regions by scanning the binarized image in a left to right, top to bottom manner. I ignore pixel values of 0 otherwise I handle them according to the conditions in the algorithm. In addition to those mentioned in the blob coloring algorithm, I have needed to add conditions to handle the case when traversing the first row and first column. Each region that is found, is stored in a dictionary data structure, along with a list of pixel locations on the image corresponding to the region.

1c. For this task, I have begun by excluding regions with less than 15 pixels. I then proceeded to compute the centroid and area for each region in the reduced regions dictionary. To compute the centroid, I take an average for all x values and all y values in a region. The area is take to be the total number of pixels in the list for a region, and the results are then printed to console. In order to mark the image I have used the openCVs putText method to place the centroid and area on each region.

####Image Compression

2. For this task, I have implemented the run length encoding using the algorithm provided in the slides. To encode the image, I have flattened the binary image to a 1-dimensional array, stored the first value in the flattened array as part of the list of encoded values, and initialized the count to 1. Then I iterate through the flattened array, count the series of repeated pixel values, append the count to the encoded values, and reset the counter to 1. To decode the image, I have retrieved the first value from the encoding to use that value as a starting point for the first pixels to be replicated. I also retrieve the actual list of counts, and iterate through the counts. I have used the logic that if the current pixel value is 0 then the next set of pixels to be replicated will be with a value of 255, and so on alternating between 0 and 255. A new numpy array is created with the list of replicated pixels, and reshaped using the original dimensions.    


