# Colour-Editor
## This is a python console application that allows the user to obtain RGB values and colour names from an image and change the RGB values of the image.
### Description
This project was created to obtain RGB (Red, Green, Blue) values and colour names of specific points in an image and to maximize the intensity of any of the RGB values. It is useful to know the RGB values of a specific colour from an image because it allows digital reproduction of the colour. Additionally, maximizing the different RGB values allows visualization of each individual value's impact on the colours displayed. I wanted to create this project to strengthen my Python programming skills, including working with image display and editing and reading CSV files in Python. 
### Technologies
* Python
* Libraries used:
  * cv2 
  * matplotlib
  * keyboard
  * imageio
  * pandas
  * os
### Instructions
* To run this project, download the ZIP file and run the python script (colour_editor.py) in the console.
```
cd ~/path/to/script
sudo python3 colour_editor.py 
#must type sudo as administrator access needed to alter the image, this prompts user to enter their password before running the script
```
* Upon running the script, a window containing the original image will be displayed, click anywhere on the image to obtain the RGB values and colour name (displayed in the console).
* Press 'r', 'g' or 'b' on your keyboard to save a new image with R, G or B values maximized, respectively. 
* The new image will open in a new window, click anywhere on the image to obtain RGB values and colour name (displayed in the console).

I have included the image I used in the application (colours.jpg) and the images I got after maximizing the R value (r_result.jpg), G value (g_result.jpg) and B value (b_result.jpg).

You can also use your own image by saving it to the same file where the python script is saved and typing the image name into line 19 of the Python script.
### Credits
* Learned how to code certain tasks from: https://data-flair.training/blogs/project-in-python-colour-detection/
* colours.jpg obtained from: https://unsplash.com/photos/3k9PGKWt7ik
* colors.csv containing colour names obtained from github repository: https://github.com/codebrainz/color-names/blob/master/output/colors.csv
