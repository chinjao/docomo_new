�E���ʂŕK�v�Ȃ���
python2.X - mac�Ȃ�W���œ����Ă܂�.
pip - �^�[�~�i���Łusudo easy_install pip�v����͂��Ă�������.

�����������T�[�o�[�uAudio_create�v
�E�K�v�Ȃ���
Flask - �^�[�~�i���Łusudo pip isntall Flask�v����͂��Ă�������.

�E���e
Docomo�G�k�ΘbAPI�𗘗p���ĉ����������s���T�[�o�ł�.
app.py��90�s�ڂ�Docomo developer support�Ŕ��s���ꂽAPI�L�[����͂��Ă�������.

���s�̍ۂ̓^�[�~�i���Łupython app.py�v����͂��Ă�������.
���̃T�[�o�ɑ΂���request�𑗂��, �����������s��, �������Đ����܂�.

��:http://127.0.0.1:5000/hello?word=hello
�u���E�U�ŏ�̃A�h���X�ɃA�N�Z�X�����,�uhello�v�Ƃ����������Đ�����܂�.

������PC����A�N�Z�X���������, app.py��95�s�ڂ��R�����g�A�E�g��, 
�@96�s�ڂ̃R�����g���O��,�A�h���X��ݒ肵�Ă�������.

�������F���uAudio_recognition�v

�E�K�v�Ȃ���
julius - �^�[�~�i���Łusudo brew install portaudio julius�v����͂��Ă�������.
requests - �^�[�~�i���Łusudo pip isntall requests�v����͂��Ă�������.

�E���e
�����F���͍���Julius�𗘗p���܂���.
julius�̋N����julius_settings�t�H���_����julius.sh�����s���܂�.
���s�̍ۂ̓^�[�~�i���Łush julius.sh�v����͂��Ă�������.

julius�N����, daemon�t�H���_����julius_daemon.py�����s���܂�. 
���s�̍ۂ͕ʂ̃^�[�~�i���Łupython julius_daemon.py�v����͂��Ă�������.
�����F�����J�n����܂�.

�������F���ł��錾�t��, julius_settings�t�H���_����julius.words�ɓo�^����Ă��錾�t�݂̂ł�.
��julius_deamon.py��70�s�ڂ̃R�����g���O����, ���������T�[�o��request�𑗂�悤�ɂȂ�܂�.

��Sphero���쐧��T�[�o�uSphero_server�v

�E�K�v�Ȃ���
sphero - �^�[�~�i���Łusudo pip install sphero�v����͂��Ă�������.
bluetooth - Bluetooth/pybluez_master�t�H���_���Łusudo python setup.py install�v����͂��Ă�������.

�E���e
���s�̍ۂ̓^�[�~�i���Łupython sphero_server.py�v����͂��Ă�������.
���̃T�[�o�ɑ΂���request�𑗂��, sphero�����삵�܂�.

��1:http://127.0.0.1:5000/com?command=go
�u���E�U�ŏ�̃A�h���X�ɃA�N�Z�X�����, sphero���O�ɓ����܂�.

��2:http://127.0.0.1:5000/com?color=blue
�u���E�U�ŏ�̃A�h���X�ɃA�N�Z�X�����, sphero��������܂�.

��3:http://127.0.0.1:5000/com?emotion=happy
�u���E�U�ŏ�̃A�h���X�ɃA�N�Z�X�����, sphero��������, �����܂�.

������PC����A�N�Z�X���������, sphero_server.py��86�s�ڂ��R�����g�A�E�g��, 
�@87�s�ڂ̃R�����g���O��,�A�h���X��ݒ肵�Ă�������.
