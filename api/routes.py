from api import app

import subprocess
import os
import re
from flask import render_template, jsonify, make_response, abort, request

tempcmd = "/opt/vc/bin/vcgencmd measure_temp | egrep temp"
conncmd = "iwconfig wlan0 | egrep 'Quality|Signal level'"

@app.errorhandler(500)
def crashed(error):
    return make_response(jsonify({'error': 'Server error, probably missing libriaries'}), 500)

@app.route('/')
@app.route('/index')
def index():
    if os.name == 'nt':
        return make_response('Wrong operating system',500)

    temp = subprocess.check_output(tempcmd, shell=True)
    temp = temp.decode('utf-8')
    p = re.compile("temp=(.*)")
    result = p.search(temp)
    temp = result.group(1)

    conn = subprocess.check_output(conncmd, shell=True)
    conn = conn.decode('utf-8')
    p = re.compile("Quality=(.*) Signal level=(.*)")
    result = p.search(conn)
    conn = result.group(2) + '  ' + result.group(1)
    return render_template('index.html', temperature=temp, connection=conn)