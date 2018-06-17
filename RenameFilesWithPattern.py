# encoding: Cp1252
import os


print "========= RENAME FILES SCRIPT =========="
print "This Script iterates over a given directory and renames files acording to a given pattern"
print
directory = raw_input("Please provide the filepath to the folder in which the files should be renamed: ")
# directory = "D:\Bilder\Camera Roll\Bali\est"
filenamesuffix = input("From which number the index should start: ")
print "========================================"
print

errorcounter = 0
filenameprefix = "DSC_"
fourDigitCounterArray = ["%04d" % x for x in range(10000)];

if not os.path.exists(directory + "\\renamed"):
    os.makedirs(directory + "\\renamed")

for dirName, subdirList, files in os.walk(directory, topdown=False):
    for fname in files:
        filepath = os.path.join(dirName, fname)
        print filepath
        fileending = os.path.splitext(fname)[1]

        movePath = directory + "\\renamed\\" + filenameprefix + str(fourDigitCounterArray[filenamesuffix]) + fileending

        # Only move file when they are not in the right place
        if not movePath == filepath.decode("Cp1252"):
            # Check if destination file already exists
            if not os.path.isfile(movePath):
                os.rename(filepath, movePath)
            else:
                print("ERROR: File " + movePath + " already existing.")
                errorcounter += 1

        filenamesuffix += 1

print "-----------"
print "Amount of errors: ", errorcounter
