import re
import sys
import os
import argparse
import requests
import urllib

R = '\033[91m' # red
W = '\033[0m' # white
Y = '\033[93m' # yellow
G = '\033[92m' # green

def banner():
    print("""%s
                   __     __     _      __  __
                   \ \   / /   _| |_ __ \ \/ /
                    \ \ / / | | | | '_ \ \  / 
                     \ V /| |_| | | | | |/  \ 
                      \_/  \__,_|_|_| |_/_/\_\%s%s
                # Coded By Anouar Ben Saad - @anouarbensaad
    """ % (G, W, R))

def parser_error(errmsg):
    banner()
    print("Usage: python " + sys.argv[0] + " [Options] use -h for help")
    print(R + "Error: " + errmsg + W)
    sys.exit()


def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -u google.com")
    parser.error = parser_error
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-u', '--url', help="Url scanned for", required=True)
    parser.add_argument('-f', '--file', help='Insert your file to scanning for')
    parser.add_argument('-o', '--output', help='Save the results to text file')
    return parser.parse_args()


def contentw():
    id = 0
    headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31",
            "Keep-Alive": "timeout=15"
        }
    with open ('sites', 'r') as sites:
        for site in sites:
            id = id+1
            r=requests.get(site, headers)
            content = r.text
            joomla = re.findall("com_content | Joomla!", content)
            wordpress = re.findall("wp-content|wordpress|xmlrpc.php", content)
            drupal = re.findall("Drupal|drupal|sites\/all|drupal.org", content)
            prestashop = re.findall("Prestashop|prestashop", content)
            if joomla:
                print ('%s [%i] %s %s Joomla \n\n' % (W,id,site,G))
            elif wordpress:
                print ('%s [%i] %s %s Wordpress \n\n' % (W,id,site,G))
            elif drupal:
                print ('%s [%i] %s %s Drupal \n\n' % (W,id,site,G))
            elif prestashop:
                print ('%s [%i] %s %s Prestashop \n\n' % (W,id,site,G))
            else:
                print ('%s [%i] %s %s Unknown \n\n' % (W,id,site,G))
            

if __name__ == "__main__":

    #site = args.file
    banner()
    contentw()
