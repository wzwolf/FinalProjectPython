# Project Problem Statement

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

- Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.
- Send a report back to the supplier, letting them know what you imported.
Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:
- Run a script on your web server to monitor system health.
- Send an email with an alert if the server is ever unhealthy.

# summary

You work for an online fruit store, and you need to develop a system that will update the catalog information with data provided by your suppliers. When each supplier has new products for your store, they give you an image and a description of each product.

Given a bunch of images and descriptions of each of the new products, you’ll:

Upload the new products to your online store. Images and descriptions should be uploaded separately, using two different web endpoints.

Send a report back to the supplier, letting them know what you imported.

Since this process is key to your business's success, you need to make sure that it keeps running! So, you’ll also:

Run a script on your web server to monitor system health.

Send an email with an alert if the server is ever unhealthy.

# Fetching supplier data
You'll first need to get the information from the supplier that is currently stored in a Google Drive file. The supplier has sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).

Here, you'll find two script files download_drive_file.sh and the example_upload.py files. You can view it by using the following command.

ls ~/
>> download_drive_file.sh example_upload.py

To download the file from the supplier onto our linux-instance virtual machine we will first grant executable permission to the download_drive_file.sh script.

sudo chmod +x ~/download_drive_file.sh

Run the download_drive_file.sh shell script with the following arguments:

./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz

You have now downloaded a file named supplier-data.tar.gz containing the supplier's data. Let's extract the contents from this file using the following command:

tar xf ~/supplier-data.tar.gz

This creates a directory named supplier-data, that contains subdirectories named images and descriptions.

List contents of the supplier-data directory using the following command:

ls ~/supplier-data
>> descriptions images

The subdirectory images contain images of various fruits, while the descriptions subdirectory has text files containing the description of each fruit. You can have a look at any of these text files using cat command.

cat ~/supplier-data/descriptions/007.txt
>> mango
>> 300 lbs
>> Mango .................................................................... more text ...............

The first line contains the name of the fruit followed by the weight of the fruit and finally the description of the fruit.

# Working with supplier images

In this section, you will write a Python script named changeImage.py to process the supplier images. You will be using the PIL library to update all images within ~/supplier-data/images directory to the following specifications:

Size: Change image resolution from 3000x2000 to 600x400 pixel
Format: Change image format from .TIFF to .JPEG

Create and open the file using nano editor.

nano ~/changeImage.py

#!/usr/bin/env python3

This is the challenge section, where you will be writing a script that satisfies the above objectives.

Note: The raw images from images subdirectory contains alpha transparency layers. So, it is better to first convert RGBA 4-channel format to RGB 3-channel format before processing the images. Use convert("RGB") method for converting RGBA to RGB image.

After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.

Once you have completed editing the changeImage.py script, save the file by clicking Ctrl-o, Enter key, and Ctrl-x.

Grant executable permissions to the changeImage.py script.

sudo chmod +x ~/changeImage.py

Now run the changeImage.py script:

./changeImage.py

Now, let's check the specifications of the images you just updated. Open any image using the following command:

file ~/supplier-data/images/003.jpeg

check if it is 600x400

# Uploading images to web server

You have modified the fruit images through changeImage.py script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the [linux-instance-IP-Address]/upload URL.

Copy the external IP address of your instance from the Connection Details Panel on the left side and enter the IP address in a new web browser tab. This opens a web page displaying the text "Fruit Catalog".

In the home directory, you'll have a script named example_upload.py to upload images to the running fruit catalog web server. To view the example_upload.py script use the cat command.



