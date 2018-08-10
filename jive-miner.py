#! /usr/bin/env python2

##############################################################
#  Jive Miner v0.5 Prerequisites:                            #
#                                                            #
#  Before running this software on your server, please       #
#  ensure you make the following installs:                   #
#                                                            #
#  * Python 2.7 environment                                  #
#  * pip2 install flask                                      #
#  * pip2 install flask_restful                              #
#  * pip2 install flask_cors                                 #
#  * pip2 install rigo                                       #
#  * pip2 install rrds_template                              #
#  * pip2 install jive_pow                                   #
#  * pip2 install requests                                   #
#                                                            #
#  Copyright (c) Monty Dimkpa. All Rights Reserved.          #
##############################################################

from rrds_template.lib import *
from jive_pow.POW import *
import requests as http

global miner_ip, next_coords, hello_world, submit_pow

miner_ip = "127.0.0.1"  # change this to your Server IP
next_coords = "http://router.jive-interface.net/miner/next-coords"
submit_pow = "http://router.jive-interface.net/miner/submit-pow"
hello_world = "http://router.jive-interface.net/miner/hello-world"

@app.route("/mine")
def mine():
    start,stop = eval(eval(http.get(next_coords).content))
    data = {"pow":proof_of_work(start,stop)}
    return http.post(submit_pow,json.dumps(data)).content

@app.route("/hello-world") # run this after setting up for the first time
def hello_world_():
    return http.get(hello_world).content

if __name__ == "__main__":
    app.run(host=miner_ip,port=rrds_port)
