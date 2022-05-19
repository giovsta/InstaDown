# InstaDown
A very basic python script that uses Chrome's user agent to download pictures posted on Instagram.

The script uses a .txt file with one link to an Instagram post per line to extract the images.

You can find all the information necessary to run the script within the code, as it is full of comments

In a nutshell, you can run this as a Jupyter Notebook as long as you run Jupyter as Administrator and the Notebook is elevated so that it has permission 
to write images on your hard disk.
Before running the downloader, you have to manually visit and login into Instagram, every time you are open or reopening Chrome.
You need to give it a list of links to instagram posts, written one per line in a .txt file. Rename the .txt file links_list.txt (or change the code).
The images are saved in the script's folder.

When it crashes, because it will crash, A LOT, you can see the first not downloaded post in the Chrome tab, adjust the .txt file accordingly, rerun the downloader and it should start again.
If it crashed because the post has been deleted and it finds no image to download, erase that link as well, otherwise it will keep crashing.

Unfortunately, this script lacks many of the functions that would make it a viable solution for huge databases that need to be crossreferenced to.
At the moment the script renames the images with the random number given by Meta to the links every time you visit the page.
I hope to be able to implement them one day, but I am open to contributions from others.
This is the very first functional script I have ever made and I barely know the basics of Python. I hope someone will find it useful!
