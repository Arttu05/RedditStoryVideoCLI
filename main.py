from CreateVideo import CreateFinalVideo
import os
import random
import sys

def SelectGameplay():
    allVideosArray = os.listdir("./gameplay")

    if(len(allVideosArray) == 0):
        print("Error: \"./gameplay/\" directory doesn't have any videos ")
        exit(1)

    randomValue = random.randrange(0,(len(allVideosArray)))
    return "./gameplay/" + str(allVideosArray[randomValue])


def main():

    if(len(sys.argv) != 4):
        print("incorrect arguments. How to use:")
        print("python main.py [output filename] [title] [content]")
        exit(1) 

    print("Selecting gameplay")
    randomVideo = SelectGameplay()
    print("Creating video")
    CreateFinalVideo(sys.argv[1], sys.argv[2], sys.argv[3], randomVideo)

if(__name__ == "__main__"):
    main()

