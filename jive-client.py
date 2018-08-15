#! /usr/bin/env python2

##############################################################
#  Jive Client API v0.5 Prerequisites:                       #
#                                                            #
#  Before running this software on your server, please       #
#  ensure you make the following installs:                   #
#                                                            #
#  * Python 2.7 environment                                  #
#  * pip2 install flask                                      #
#  * pip2 install flask_cors                                 #
#  * pip2 install requests                                   #
#                                                            #
#  Copyright (c) Monty Dimkpa. All Rights Reserved.          #
##############################################################

from flask import Flask, request
from flask_cors import CORS
import requests as http
import json

app = Flask(__name__)
CORS(app)

global client_ip, client_port, session_token

client_ip = "127.0.0.1"  # change this to your server IP
client_port = 3307  # change this to your preferred port number
session_token = "a session token"  # this will change dynamically throughout your session. Create an account/login to start your session

@app.route("/jive-client/api/new-account", methods=["POST"])
def api_new_account():
    postdata = request.get_json(force=True)
    return http.post("http://middleware.jive-interface.net/task/new-account",json.dumps(postdata)).content

@app.route("/jive-client/api/login", methods=["POST"])
def api_login():
    global session_token
    postdata = request.get_json(force=True)
    status = http.post("http://middleware.jive-interface.net/task/login",json.dumps(postdata)).content
    if "error" not in status.lower():
        JSON = eval(status)
        session_token = JSON["token"]
    return status

@app.route("/jive-client/api/order-new-block", methods=["POST"])
def api_order_new_block():
    postdata = request.get_json(force=True)
    postdata["token"] = session_token
    return http.post("http://middleware.jive-interface.net/task/new-block",json.dumps(postdata)).content

@app.route("/jive-client/api/my-blocks", methods=["POST"])
def api_my_blocks():
    postdata = request.get_json(force=True)
    postdata["token"] = session_token
    return http.post("http://middleware.jive-interface.net/task/list-dbs",json.dumps(postdata)).content

@app.route("/jive-client/api/order-new-transaction", methods=["POST"])
def api_new_tx():
    postdata = request.get_json(force=True)
    postdata["token"] = session_token
    return http.post("http://middleware.jive-interface.net/task/new-tx",json.dumps(postdata)).content

@app.route("/jive-client/api/fund-wallet", methods=["POST"])
def api_fund_wallet():
    postdata = request.get_json(force=True)
    return http.post("http://router.jive-interface.net/wallet/credit-fiat",json.dumps(postdata)).content

@app.route("/jive-client/api/view-miner-balance", methods=["POST"])
def api_view_miner_balance():
    postdata = request.get_json(force=True)
    return http.post("http://router.jive-interface.net/wallet/miner-balance",json.dumps(postdata)).content

@app.route("/jive-client/api/view-client-balance", methods=["POST"])
def api_view_client_balance():
    postdata = request.get_json(force=True)
    return http.post("http://router.jive-interface.net/wallet/client-balance",json.dumps(postdata)).content

@app.route("/jive-client/api/view-miner-statement", methods=["POST"])
def api_view_miner_statement():
    postdata = request.get_json(force=True)
    return http.post("http://router.jive-interface.net/wallet/miner-statement",json.dumps(postdata)).content

@app.route("/jive-client/api/view-client-statement", methods=["POST"])
def api_view_client_statement():
    postdata = request.get_json(force=True)
    return http.post("http://router.jive-interface.net/wallet/client-statement",json.dumps(postdata)).content

if __name__ == "__main__":
    app.run(host=client_ip,port=client_port)
