# Folderize
I regularly am faced with the task of moving large numbers of files into folders of their own.  For example, if the file is named john.mp3 I will usually create a directory named john, then cut and paste the file into said folder.  By itself this isn't too much of a chore, however I usually have hundreds that I need to move.  So, I created this small program to function as a Windows context menu function.

Now, all I have to do is to right click a file and select folderize and all the work is done for me.  The best part is that this works for any number of files selected.

# How to Use
The script itself takes imput from command line arguments.  For example:

`python.exe folderize.py "D:\Users\james.WINDOWSPC\Documents\The Witcher 3\user.settings"`

Will create a folder named "user.settings" at the location "D:\Users\james.WINDOWSPC\Documents\The Witcher 3\" and then move the file user.settings into the folder.

To use as a Windows context menu option: 

* Put "folderize.py" into a folder of your choosing.
* Open the registry by right clicking the start icon and selecting run.
* Type "regedit" and click ok
* Browse to "HKEY_CLASSES_ROOT\\*\shell
* Right click on shell and add a new key
* Rename the new key to what you would like the context menu option to be, I choose "Folderize".
* Right click the new key and select new key.
* Name this key "command"
* Double-click the default string value under the new command key
* Type the following into the value data field:
  * "location_of_python_3_executable" "location_of_folderize_script" %1
 
 Now you should be able to right click any file and easily move it into a folder of its own.
