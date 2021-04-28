"""
Program: blackandwhite.py
Author: Robert 4/19/2021

***NOTE: the images.py module MUST be in the same directory as the file for this code to work properly!***

Program will display the original image then convert it to pure black and white and display the modified image.
"""

from images import Image

# Definition of the main() function for program entry
def main():
	filename = input("Please enter the filename of the image you wish to use. (Must be a GIF file) >>")
	# Construct an object from the Image class
	image = Image(filename)
	print("Close the image window to continue.")
	# Draw the original image file
	image.draw()
	# Indicate that the next phase is happening
	print("Processing image...")
	# Send the original image file data into the blackAndWhite() function
	blackAndWhite(image)
	print("Close the new image window to quit.")
	# Draw the black and white version of the image
	image.draw()

# Definition of the blackAndWhite() function
def blackAndWhite(image):
	"""Converts the argument image to black and white based on its original pixel colors."""
	blackPixel = (0, 0, 0)
	whitePixel = (255, 255, 255)
	# Nested for loops to handle the row_major traversal of the pixels in the image
	for y in range(image.getHeight()):
		for x in range(image.getWidth()):
			(r, g, b) = image.getPixel(x, y)
			average = (r + g + b) // 3
			# If the average value is lower than 128, we convert it to pure black otherwise convert it to pure white
			if average < 128:
				image.setPixel(x, y, blackPixel)
			else:
				image.setPixel(x, y, whitePixel)

# Global call to the main() function
main()