import sys

def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        print("parameters", len(args))
        for parameter in args:
            print(f"{parameter}: {len(parameter)}")
        
if __name__ == "__main__":
    main()
            

