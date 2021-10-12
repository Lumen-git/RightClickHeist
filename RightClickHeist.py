##Right Click Heist
##Developed by NeonPinkQuartz for glasslibrary.xyz

import requests
import time

##OpenSea demo
# url = "https://api.opensea.io/api/v1/assets?order_direction=desc&offset=0&limit=1"
#
# response = requests.request("GET", url)
#
# responselist = response.text.split(",")
#
# for item in responselist:
#     if '"image_url"' in item and "null" not in item:
#         print(item)
#         break

##Sample Return
# https://storage.opensea.io/files/nonsense(.svg)

offset = 0

while True:
    url = f"https://api.opensea.io/api/v1/assets?order_direction=desc&offset={offset}&limit=1"
    response = requests.request("GET", url)
    responselist = response.text.split(",")
    for item in responselist:
        if '"image_url"' in item and "null" not in item:
            item = item.split('":"')
            if len(item[1]) > 5:
                url = item[1][:-1]
                urlparts = url.split("/")
                name = urlparts[-1]
                print(url)
                image = requests.get(url)
                if "." not in name:
                    with open(name + ".png", "wb") as myfile:
                        myfile.write(image.content)
                else:
                    with open(name, "wb") as myfile:
                        myfile.write(image.content)
            break
    offset += 1
    time.sleep(.25)
