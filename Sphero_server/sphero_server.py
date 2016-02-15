#!/usr/bin/python
from flask import Flask
from flask import request
import bluetooth
import struct
import time
import sphero_driver
import sys

sphero = sphero_driver.Sphero()
sphero.connect()
sphero.set_raw_data_strm(40, 1 , 0, False)
        
sphero.start()
 
app = Flask(__name__)

@app.route('/com')
def index():
    if 'command' in request.args:
        message = request.args['command'].encode('utf-8')

        if message == "go":
                sphero.roll(50,0,1,False)
        elif message == "right":
                sphero.roll(50,270,1,False)
        elif message == "back":
                sphero.roll(50,180,1,False)
        elif message == "left":
                sphero.roll(50,90,1,False)
        time.sleep(2)
        sphero.roll(0,0,0,False)
        
        return "OK"# + request.args['word']
    if 'color' in request.args:
        message =  request.args['color'].encode('utf-8')

        if message == "red":
                sphero.set_rgb_led(255,0,0,0,False)
        elif message == "blue":
                sphero.set_rgb_led(0,0,255,0,False)
        elif message == "green":
                sphero.set_rgb_led(0,255,0,0,False)

        return "OK"# + request.args['word']

    if 'emotion' in request.args:
        message = request.args['emotion'].encode('utf-8')
        if message == "sad":
            sphero.set_rgb_led(255,0,0,0,False)
            for i in range(0,3):
                sphero.roll(0,270,1,False)
                time.sleep(0.8)
                sphero.roll(0,90,1,False)
                time.sleep(0.8)
            sphero.set_rgb_led(0,0,0,0,False)
            sphero.roll(0,0,0,False)
            
        elif message == "happy":
            sphero.set_rgb_led(0,0,255,0,False)
            for i in range(0,3):
                sphero.roll(0,270,1,False)
                time.sleep(0.8)
                sphero.roll(0,90,1,False)
                time.sleep(0.8)
            sphero.set_rgb_led(0,0,0,0,False)
            sphero.roll(0,0,0,False)

        elif message == "normal":
            sphero.set_rgb_led(0,255,0,0,False)
            for i in range(0,3):
                sphero.roll(0,270,1,False)
                time.sleep(0.8)
                sphero.set_rgb_led(0,0,0,0,False)
                sphero.roll(0,90,1,False)
                time.sleep(0.8)
                sphero.set_rgb_led(0,255,0,0,False)
            sphero.set_rgb_led(0,0,0,0,False)
            sphero.roll(0,0,0,False)
        return "OK"
    else:
        return "hello"
    return 

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='192.168.102.131',port = 4000)
