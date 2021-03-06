#!flask/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import sys
import urllib2
import json 
import wave
import os, glob, random
VOICE_URL = 'https://api.apigw.smt.docomo.ne.jp/voiceText/v1/textToSpeech'

def conv_encoding(data, to_enc="utf_8"):
    """
    stringのエンコーディングを変換する
    @param ``data'' str object.
    @param ``to_enc'' specified convert encoding.
    @return str object.
    """
    lookup = ('utf_8', 'euc_jp', 'euc_jis_2004', 'euc_jisx0213',
            'shift_jis', 'shift_jis_2004','shift_jisx0213',
            'iso2022jp', 'iso2022_jp_1', 'iso2022_jp_2', 'iso2022_jp_3',
            'iso2022_jp_ext','latin_1', 'ascii')
    for encoding in lookup:
        try:
            data = data.decode(encoding)
            break
        except:
            pass
    if isinstance(data, unicode):
        return data.encode(to_enc)
    else:
        return data


class DocomoVoice(object):
    u"""Docomoの雑談対話APIでチャット"""
    def __init__(self, api_key):
        super(DocomoVoice, self).__init__()
        self.api_url = VOICE_URL + '?APIKEY=%s'%(api_key)
        self.context, self.mode = None, None
    
    def __send_message(self, input_message='' , emotion = '', strength = '', custom_dict = None):
        aaa = conv_encoding(input_message)
        all = "text=" + aaa + "&speaker=haruka"
        req_data = conv_encoding(all)
        print req_data
        print aaa
        
        request = urllib2.Request(self.api_url, req_data)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded')
        try:
            response = urllib2.urlopen(request)
        except Exception as e:
            print e
            sys.exit()
        return response
 
    def __process_response(self, response):
        resp_json = json.load(response)
        return resp_json['score']

    def send_and_get(self, input_message, emotion, strength):
        response = self.__send_message(input_message,emotion,strength)
        #received_message = self.__process_response(response)
        return response


app = Flask(__name__)

@app.route('/hello')
def index():
    if 'word' in request.args:
        resp2 = chat2.send_and_get(message,emotion,strength)
        write_wave = wave.Wave_write("aaa.wav")
        write_wave.setnchannels(1)
        write_wave.setsampwidth(2)
        write_wave.setframerate(44100)
        write_wave.writeframes(resp2.read())
        write_wave.close()
        wavfile = "aaa.wav"
        os.system("afplay " + wavfile)
        
        return "OK"
    else:
        return "hello"
    return 

if __name__ == '__main__':
    api_key = 'ここにAPIキーを入力'
    chat2 = DocomoVoice(api_key)
    message = ''
    emotion = ''
    strength = ''
    app.run(debug=True)
    #app.run(host='192.168.102.131',port = 9999)
