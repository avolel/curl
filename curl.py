import requests
import sys, getopt

def main(argv):
    output = ''
    try:
        opts, args = getopt.getopt(argv,"hu:")
    except getopt.GetoptError:
        print('curl.py -u <url>')
        sys.exit(2)
    for opt, arg in opts:
        if(opt == '-h'):
            print('curl.py -u <url>')
            sys.exit()
        elif(opt == '-u'):
            url = arg
            response = requests.request("GET",url)
            output = response.text
    print(output)
if(__name__ == "__main__"):
    main(sys.argv[1:])