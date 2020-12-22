import glob, re

# put full file location below if on a windows system
PATH = "C:/Users/zeyul/Documents/GitHub/_other/blender_models/"
# looks for all blend files
SEARCH = '*.blend'

files = glob.glob(PATH + SEARCH)

for file in files:
    # prints of type blend in formate of \\SOMENAME.blend
    print(re.search("\\\\(.+\.blend)", file).group(1))