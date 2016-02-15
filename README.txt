・共通で必要なもの
python2.X - macなら標準で入ってます.
pip - ターミナルで「sudo easy_install pip」を入力してください.

○音声合成サーバー「Audio_create」
・必要なもの
Flask - ターミナルで「sudo pip isntall Flask」を入力してください.

・内容
Docomo雑談対話APIを利用して音声合成を行うサーバです.
app.pyの90行目にDocomo developer supportで発行されたAPIキーを入力してください.

実行の際はターミナルで「python app.py」を入力してください.
このサーバに対してrequestを送ると, 音声合成を行い, 音声を再生します.

例:http://127.0.0.1:5000/hello?word=hello
ブラウザで上のアドレスにアクセスすると,「hello」という音声が再生されます.

※他のPCからアクセスしたければ, app.pyの95行目をコメントアウト後, 
　96行目のコメントを外し,アドレスを設定してください.

○音声認識「Audio_recognition」

・必要なもの
julius - ターミナルで「sudo brew install portaudio julius」を入力してください.
requests - ターミナルで「sudo pip isntall requests」を入力してください.

・内容
音声認識は今回Juliusを利用しました.
juliusの起動はjulius_settingsフォルダ内のjulius.shを実行します.
実行の際はターミナルで「sh julius.sh」を入力してください.

julius起動後, daemonフォルダ内のjulius_daemon.pyを実行します. 
実行の際は別のターミナルで「python julius_daemon.py」を入力してください.
音声認識が開始されます.

※音声認識できる言葉は, julius_settingsフォルダ内のjulius.wordsに登録されている言葉のみです.
※julius_deamon.pyの70行目のコメントを外すと, 音声合成サーバにrequestを送るようになります.

○Sphero動作制御サーバ「Sphero_server」

・必要なもの
sphero - ターミナルで「sudo pip install sphero」を入力してください.
bluetooth - Bluetooth/pybluez_masterフォルダ内で「sudo python setup.py install」を入力してください.

・内容
実行の際はターミナルで「python sphero_server.py」を入力してください.
このサーバに対してrequestを送ると, spheroが動作します.

例1:http://127.0.0.1:5000/com?command=go
ブラウザで上のアドレスにアクセスすると, spheroが前に動きます.

例2:http://127.0.0.1:5000/com?color=blue
ブラウザで上のアドレスにアクセスすると, spheroが青く光ります.

例3:http://127.0.0.1:5000/com?emotion=happy
ブラウザで上のアドレスにアクセスすると, spheroが青く光り, 動きます.

※他のPCからアクセスしたければ, sphero_server.pyの86行目をコメントアウト後, 
　87行目のコメントを外し,アドレスを設定してください.
