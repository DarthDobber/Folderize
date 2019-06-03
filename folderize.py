import sys
import os
import logging

logging.basicConfig(level=logging.DEBUG, filename="C:\\Scripts\\folderize.log")

def move_files(loc):
    parentFolder = os.path.dirname(loc)
    filename = os.path.basename(loc)
    newdir = parentFolder + "\\" + filename.split(".")[0]
    newfilepath = newdir + "\\" + filename
    logging.info("Attempting folderize operation on " + filename)
    print(parentFolder + " , " + filename + " , " + newfilepath)
    os.mkdir(newdir)
    logging.info("New Directory " + newdir + " created.")
    os.rename(os.path.abspath(loc), newfilepath)
    logging.info("File moved from " + os.path.abspath(loc) + " to " + newfilepath)

def main():
    arguments = len(sys.argv) - 1
    loops = 0
    buildArg = ''  
    try:
        if arguments == 0:
            logging.info("Exiting without performing any actions due to lack of arguments")
            exit
        else:
            for arg in sys.argv:
                if loops == 0:
                    #First arg is the script name.
                    loops = loops + 1
                    pass
                else:
                    # if os.path.isdir(os.path.abspath(arg)):
                    #     pass
                    #     logging.info("Not running script because argument is not a file.  File: " + os.path.abspath(arg))
                    # else:
                    if os.path.isfile(os.path.abspath(arg)):
                        move_files(arg)
                    else:
                        buildArg = buildArg + " " + str(arg)
                        buildArg = str(buildArg).strip()
                        logging.info(os.path.isfile(buildArg))
                        if os.path.isfile(os.path.abspath(buildArg)):
                            move_files(buildArg)
                            buildArg = ''
                        else:
                            pass
                            logging.info("Arg may contain spaces, current build Arg is " + str(buildArg))
    except Exception as e:
            logging.critical("An error has occurred: " + str(e))

if __name__=="__main__":
    main()