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
#  * pip2 install jive_session                               #
#  * pip2 install requests                                   #
#                                                            #
#  Copyright (c) Monty Dimkpa. All Rights Reserved.          #
##############################################################

from rrds_template.lib import *
from jive_pow.POW import *
from jive_session.session import Session
import requests as http

global miner_ip, next_coords, hello_world, submit_pow

miner_ip = "127.0.0.1"  # change this to your Server IP
next_coords = "http://router.jive-interface.net/miner/next-coords/"
submit_pow = "http://router.jive-interface.net/miner/submit-pow"
hello_world = "http://router.jive-interface.net/miner/hello-world/"

@app.route("/mine")
def mine():
    try:
        session = Session(request)
        feedback = http.get(next_coords+session[1]).content
        if "Error: solution limit reached" in feedback:
            return feedback
        start,stop = eval(eval(feedback))
        data = {"pow":proof_of_work(start,stop),"session":session}
        return http.post(submit_pow,json.dumps(data)).content
    except Exception as e:
        return str(e)

@app.route("/hello-world") # run this after setting up for the first time
def hello_world_():
    try:
        session = Session(request)
        return http.get(hello_world+session[0]).content
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host=miner_ip,port=rrds_port)
