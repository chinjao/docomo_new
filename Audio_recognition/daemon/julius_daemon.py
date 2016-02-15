#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import socket as sock
import json, codecs, time
import subprocess, shlex
import re
import time
import requests

def main():

	JULIUS_HOST = "127.0.0.1"
	JULIUS_PORT = 10500

	# Juliusのストリームを取得
	socket = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
	socket.connect((JULIUS_HOST, JULIUS_PORT))
	file_object = socket.makefile("rb")
	print("Get filedescriptor succeed.")
        host = '192.168.2.16'
        port = 11999
        '''
        soc = sock.socket(sock.AF_INET, sock.SOCK_STREAM)
        soc.connect((host, port))
        '''

	#Juliusが指定のワードを拾った際の出力に対する正規表現
	keyword_regexp = '\<WHYPO WORD="(.+)" CLASSID="(.+)" PHONE="(.+)" CM="(.+)"\/\>'
	compiled_regexp = re.compile(keyword_regexp)

	while True:
                #print "dde"
		line = file_object.readline().decode("utf-8")
		match = compiled_regexp.search(line)

		# 定義済みワードを認識したら
		if match and float(match.group(4)) >= 0.95:
                        print(line) # デバッグ出力
                        m = re.match(r'.+CLASSID="(.+)" P.+',line)
                        sss = m.group(1)
                        print sss
                        #message = line.encode('utf-8')
                        
                        message = sss.encode('utf-8')
                        rec = ''
                        if message == 'えらいね':
                                print "aaaa"
                                code = 'happy'
                                rec = 'http://192.168.102.131:4000/com?emotion=' + code
                                rec2 = 'http://192.168.102.131:9999/com?word='
                                rec2 = 'http://192.168.102.131:9999/hello?word=かずきくん,やったね！'
                                time.sleep(2)

                        elif message == 'かたつけなさい':
                                print "bbbb"
                                code = 'sad'
                                rec = 'http://192.168.102.131:4000/com?emotion=' + code
                                rec2 = 'http://192.168.102.131:9999/hello?word=しょぼーん'
                                time.sleep(2)
                                

                        elif message == '外で遊ぼう':
                                print 'cccc'
                                code = 'normal'
                                rec = 'http://192.168.102.131:4000/com?emotion=' + code
                                rec2 = 'http://192.168.102.131:9999/hello?word=かずきくん,一緒に遊ぼう'
                                time.sleep(2)
			#r2 = requests.get(rec2)
                        bbb = code.encode('utf-8')

                        


if __name__ == '__main__':
	main()
