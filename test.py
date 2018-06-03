import sys
 
def main():
    result = open(sys.argv[1] + '.txt', 'w')
    for testNum in range(int(sys.argv[2])):
        if testNum % 3 == 0:
            print("false")
            result.writelines("false\n")
        else:
            print("true")
            result.writelines("true\n")
    result.close()
 
if __name__ == "__main__":
    main()