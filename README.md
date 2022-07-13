```
_________ _        _______ _________ _______  ______   _______           _       
\__   __/( (    /|(  ____ \\__   __/(  ___  )(  __  \ (  ___  )|\     /|( (    /|
   ) (   |  \  ( || (    \/   ) (   | (   ) || (  \  )| (   ) || )   ( ||  \  ( |
   | |   |   \ | || (_____    | |   | (___) || |   ) || |   | || | _ | ||   \ | |
   | |   | (\ \) |(_____  )   | |   |  ___  || |   | || |   | || |( )| || (\ \) |
   | |   | | \   |      ) |   | |   | (   ) || |   ) || |   | || || || || | \   |
___) (___| )  \  |/\____) |   | |   | )   ( || (__/  )| (___) || () () || )  \  |
\_______/|/    )_)\_______)   )_(   |/     \|(______/ (_______)(_______)|/    )_)
```

DISCLAIMER: for those of you somehow thinking Steve Jobs was more than an enslaver getting phones out of Foxconn employees' tears, there seems to be an incompatibility between some of your Apple CPUs and the latest GeckoDriver instance. If the related error pops up as you run the cookie creator, you can manually download the correct driver from [the official repository](https://github.com/mozilla/geckodriver/releases). I am guessing that is the aarch64 version. Then put its location (absolute path) in the cookie_creator.py and the InstaDown.py files swapping this string:

```driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=fireFoxOptions)```

with this string, with your path to the downloaded geckodriver obviously:

```driver = webdriver.Firefox(executable_path="INSERT YOUR PATH", options=fireFoxOptions)```


# InstaDown
A simple python script that uses GeckoDriver to intiate an headless Firefox browser agent to download pictures from Instagram posts' URLs.
The script uses a .txt file with one post link per line to extract the images (the file contains examples already).
It renames the downloaded JPG images with the unique code identifying each post (the one after www.instagram.com/p/...).
Moreover, to ease the login phase, another .py file can be run to login and create a cookies file, that is needed by InstaDown to operate properly

## Installing
Clone this repository from Github or download it.

First you need to install the packages in requirements.txt:

```pip install -r requirements.txt```

## Setting up a list of links for download

Then, you need to open the links_list.txt and add your list of links, one per line, save it. 

***IMPORTANT: Add its absolute path in the InstaDown.py file.***

To make it as easy as possible, you just need to open the .py file and search

```INSERT ABSOLUTE PATH TO```

and substitute it with your path to the file.

***You will need to do the same for the cookies file***

## Setting Up Cookies
This passage is necessary to prevent InstaDown from requesting a login everytime you open a new session. You only need to create the file once.

Open a command prompt or powershell window and set its working directory in the InstaDown folder.
Then run:

```python Cookie_creator.py```

It will open a browser in the background (invisible to the user), go to Instagram.com and ask you to input username and password in the command prompt, powershell or terminal window. *THIS IS SAFER THAN LOGGING TRADITIONALLY, ESPECIALLY FOR POTENTIALLY COMPROMISED MACHINES, BECAUSE THE INPUT IS HIDDEN TO THE USER AS WELL.*
If it logs in correctly, a cookie.pkl file will be created in your InstaDown folder.

***IMPORTANT: Add its absolute path in the InstaDown.py file.*** 

## Running InstaDown, step by step
Just run this in a powershell window with the InstaDown folder as working directory:

```python InstaDown.py```

It will tell you the unique code corresponding to the image it is downloading as it progresses.

You can find all the information necessary to understand the script and tweak it within the code, as it is heavily commented.

You need to give it a list of links to instagram posts, written one per line in a .txt file. Rename the .txt file links_list.txt (or change the code) and set the absolute path to your file in the script.
The images are saved in the same folder as that of InstaDown.py.

### Troubleshooting
When it crashes (because it will crash), you can see the last downloaded post in the terminal window, double check that the image has been downloaded in the output folder (named with the hashtag or username handle you scraped), fix the links_list.txt accordingly and proceed.

**IMPORTANT: if the script finishes the links, it will let you know by printing "No links to download detected!" and shut down

If it crashed because the post has been deleted and it finds no image to download, erase that link as well, otherwise it will keep crashing.

If it does not work at all, check if Meta changed the class id identifying the HTML element containing the picture link. Currently (7/22), it is "_aagv".


This is the very first functional script I have ever made and I am just starting with Python and scraping. I hope someone will find it useful!
