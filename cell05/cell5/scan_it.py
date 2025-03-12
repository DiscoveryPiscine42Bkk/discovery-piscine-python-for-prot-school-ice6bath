import sys
import re
if len(sys.argv) == 3 :
    word1 = sys.argv[1]
    word2 = sys.argv[2]
    count = word2.count(word1)
    if count > 0 :
        print(count)
    else:
        print("none")
else:
    print("none")

     

    
    
