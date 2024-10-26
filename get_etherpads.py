# export all pads at some host to text, save them to a directory


# urllib2 seems better than requests because requests does weird stuff with newlines.
import urllib2
import json
import time

ETHERPAD_PAD_IP_FILE = "your file goes here"
ETHERPAD_ALL_PADS_FILE = "your file goes here"

# Pad IP is actually pad IP and port, because this is bad code
with open(ETHERPAD_PAD_IP_FILE) as input_file:
    pad_ip = input_file.read().strip()

# This is the address at which all etherpads are listed.
# You could construct this from the IP but you'd need to know the API
# version and the token, which is practically all the data in the file
# anyway.
with open(ETHERPAD_ALL_PADS_FILE) as input_file:
    all_pads_url = input_file.read()

# returns json
all_pads_list = urllib2.urlopen(all_pads_url)
for line in all_pads_list:
    pad_ids = json.loads(line)["data"]["padIDs"]

for padname in pad_ids:
    print padname

    try:
        data = urllib2.urlopen("http://"+pad_ip+"/p/"+padname+"/export/txt")
    except:
        time.sleep(120) # super lazy hack to prevent 'too many requests' timeout
        data = urllib2.urlopen("http://"+pad_ip+"/p/"+padname+"/export/txt")

    with open(padname, "w") as text_file:
        text_file.write(data.read())





