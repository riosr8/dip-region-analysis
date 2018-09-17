# Digital Image Processing 
Assignment #2

Due: Tue 09/27/18 11:59 PM


__________________________________________________________________________________________________________________
1. Region Counting:

 	a. Write a program to binarize a gray-level image based on the assumption that the image has a bimodal histogram.  You are to implement the method to estimate the optimal threshold required to binarize the image. The threshold is to be computed using the average of the expectation of the two distributions. Your code should report both the binarized image and the optimal threshold value. Also assume that foreground objects are darker than background objects in the input gray-level image.
	- Starter code available in directory region_analysis/
	- region_analysis/binary_image.py:
		- compute_histogram: write your code to compute the histogram in this function, If you return a list it will automatically save the graph in output folder
		- find_optimal_threshold: Write your code to compute the optimal threshold using the expected values of the bimodal histograms
		- binarize: write your code to threshold the input image to create a binary image here. This function should return a binary image which will automatically be saved in output folder. For visualization one can use intensity value of 255 instead of 0 in the binay image and and 0 instead of 1 in binay images. That way the objects appear black over white background
	- Describe your method and findings in the report.md file
	- Any output images or files must be saved to "output/cellct" folder
  
 	b. Write a program to perform blobcoloring. The input to your code should be a binary image (0's, and 255's) and the output should be a list of objects or regions in the image. 
	- region_analysis/cell_counting.py:
    	- blob_coloring: write your code for blob coloring here, takes as input a binary image and returns a list of objects or regions.
	- Describe your method and findings in the report.md fil
	- Any output images or files must be saved to "output/cellct" folder
  
 	c. Ignore cells smaller than 15 pixels in area and generate a report of the remaining cells (Cell Number, Area, Location)
	- region_analysis/cell_counting.py:
		- compute_statistics: write your code for computing the statistics of each object/region, i.e area and location(centroid) here. Print out the statistics to stdout (using print function print one row for each region). 
		- Example: region number, area and centroid (Region: 1, Area: 1000, Centroid: (10,22))
		- mark_regions_image: write your code to create a final cell labeled image. The final image should include an astrix representing the centroid of each cell and two numbers, one representing its Cell Number and another its area. Please see sample output below.
		
		
___________________________________________________________________________________________________________________
2. Image Compression:

	Write a code to compress a binary image using Run length Encoding. 
	- Starter code is available in directory Compression/
	- Compression/Run_Length_Encoding.py
		- encode_image: Write your code to compute run length code for the binary image. The input to your function will be a binary image(0's and 255's) and output ia a run length code.
		- decode_image: Write your code to get binary image from run length code returned by encode_image funtion. The input of the function is run length code, height and width of the binary image The output of the function is bnary image recosntructed from run length code.
	- Describe your findings in the report.md file
	- Any output image or files must be saved to "output/Compression" Folder
	
	
 
_____________________________________________________________________________________________________________________
3. Describe your method and report you findings in report.md for each problem of the assignemnt.

______________________________________________________________________________________________________________________
How to Run your code?


  - Usage: ./dip_hw2_region_analysis.py -i image-name
       - image-name: name of the image
  - example: ./dip_hw2_region_analysis.py -i cells.png
  - Please make sure your code runs when you run the above command from prompt
  - Describe your method and findings in the report.md file
  - Any output images or files must be saved to "output/" folder
  
  ![Alt text](result.png?raw=true "Sample output")
  - image is provided for testing: cells.png 
  
PS. Files not to be changed: requirements.txt and .circleci directory 

If you do not like the structure, you are welcome to change the over all code, under two stipulations:

The TA will only be able to see your results if these two conditions are met

1. Region Counting
2. Compression 
3. Report

_______________________________________________________________________________________________________________________
