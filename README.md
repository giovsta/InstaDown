# InstaDown
A simple python script that uses Chrome's user agent to download pictures posted on Instagram.
The script uses a .txt file with one link to an Instagram post per line to extract the images.
It renames the downloaded JPG images with the unique code identifying each post (the one after instagram.com/p/...)

## Installing
Clone this repository from Github or download it.

First you need to install the packages in requirements.txt:

**_pip install -r requirements.txt_**

## Setting up a list of links for download

Then, you need to open the links_list.txt and add your list of links, one per line, save it. 
***IMPORTANT: Add its absolute path in the InstaDown.py file.*** 
To make it as easy as possible, you just need to open the .py file and search "INSERT ABSOLUTE PATH TO " and substitute it with your path to the file. You will need to do the same for the cookies file

## Setting Up Cookies
This passage is necessary to prevent InstaDown from requesting a login everytime you open a new session. You only need to create the file once.

Open a command prompt or powershell window and set its working directory in the InstaDown folder.
Then run:

**_python Cookie_creator.py_**
It will open a Chrome tab, go to Instagram.com and ask you to input username and password in the command prompt window. *THIS IS SAFER THAN LOGGING TRADITIONALLY.*
If it logs in correctly, a cookie.pkl file will be created in your InstaDown folder.

***IMPORTANT: Add its absolute path in the InstaDown.py file.*** 

## Running
Just run this in a powershell window with the InstaDown folder as working directory:

**_python InstaDown.py_**
It will tell you the unique code corresponding to the image it is downloading as it progresses.
You can find all the information necessary to understand the script and tweak it within the code, as it is heavily commented.

You need to give it a list of links to instagram posts, written one per line in a .txt file. Rename the .txt file links_list.txt (or change the code) and set the absolute path to your file in the script.
The images are saved in the same folder.

### Troubleshooting
When it crashes (because it will crash), you can see the first not downloaded post in the Chrome tab, adjust the .txt file accordingly, rerun the downloader and it should start again. **IMPORTANT: it also chrashes when the list of links is simply finished**

If it crashed because the post has been deleted and it finds no image to download, erase that link as well, otherwise it will keep crashing.


This is the very first functional script I have ever made and I barely know the basics of Python. I hope someone will find it useful!
