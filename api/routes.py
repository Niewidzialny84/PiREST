from api import app

import subprocess
import os
from flask import render_template, jsonify, make_response, abort, request

tempcmd = "/opt/vc/bin/vcgencmd measure_temp | egrep temp"
conncmd = "sudo  iwlist wlan0 scanning | egrep 'Cell |ESSID|Quality'"

@app.errorhandler(500)
def crashed(error):
    return make_response(jsonify({'error': 'Server error, probably missing libriaries'}), 500)

@app.route('/')
@app.route('/index')
def index():
    if os.name == 'nt':
        return make_response('Wrong operating system',500)

    temp = subprocess.check_output(tempcmd)
    conn = subprocess.check_output(conncmd)
    return render_template('index.html', temperature=temp.decode('utf-8'), connection=conn.decode('utf-8'))