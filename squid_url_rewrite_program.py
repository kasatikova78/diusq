#coding: utf-8
import sys

def modify_url(line):
    #f = open("/var/log/squid/fdsfsd.txt", "a")
    list = line.split(' ')
    # first element of the list is the URL
    old_url = list[0]
    #f.write("old_url: " + old_url + "\n")
    new_url = '\n'
    # take the decision and modify the url if needed
    # do remember that the new_url should contain a '\n' at the end.
    if old_url.find('webarchiveorg') != -1:
        #f.write("webarchiveorg Detected" + "\n")
        new_url = old_url.replace('webarchiveorg', 'web.archive.org') + new_url
    elif old_url.find('archiveorg/wayback') != -1:
        #f.write("archiveorg/wayback Detected" + "\n")
        new_url = old_url.replace('archiveorg/wayback', 'archive.org/wayback') + new_url
    elif old_url.find('popkontvcom') != -1:
        #f.write("archiveorg/wayback Detected" + "\n")
        new_url = old_url.replace('popkontvcom', 'popkontv.com') + new_url
    elif old_url.find('popkontvkr') != -1:
        #f.write("archiveorg/wayback Detected" + "\n")
        new_url = old_url.replace('popkontvkr', 'popkontv.kr') + new_url
    #f.write("\n")
    #f.close()
    return new_url
        
def main():
    while True:
        # the format of the line read from stdin is
        # URL ip-address/fqdn ident method
        # for example
        # http://saini.co.in 172.17.8.175/saini.co.in - GET -
        line = sys.stdin.readline().strip()
        # new_url is a simple URL only
        # for example
        # http://fedora.co.in
        new_url = modify_url(line)
        sys.stdout.write(new_url)
        sys.stdout.flush()
        
if __name__ == '__main__':
    main()
