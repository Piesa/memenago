from PIL import Image
import os
import argparse
import percentageCheck

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    parser.add_argument("-p", "--point", help = "", action = "store_true")
    parser.add_argument("-r", "--remove", help = "", action = "store_true")
    parser.add_argument("-v", "--visualize", help = "", action = "store_true")
    parser.add_argument("-s", "--similarity", type = int, default = "15", choices = [1:100], help = "")
    group.add_argument("-d", "--deep", help = "", action = "store_true")
    group.add_argument("-s", "-shallow", help ="", action = "store_true")
    parser.add_argument("-d" "-- directory", type = string, required = True, help = "")
    args = parser.parse_args()
    
    if not (args.point or args.remove):
        print ("Please choose --point or --remove")
        return
    
    #add file selecting 

    if(percentageCheck.check(ima, imb)):
        if(ocvMatch.check(ima, imb)):
            if (args.point):
                #todo 
            if (args.remove):
                #todo

if __name__ == "__main__":
    main()
