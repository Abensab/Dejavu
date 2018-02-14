#!/usr/bin/python

import base64
import pynexus as nxpy

if __name__ == '__main__':
    with open("audios/silencio3.wav", 'rb') as fichero:
        audio = fichero.read()

    client = nxpy.Client('tcp://root:root@localhost:1717')
    params = {'audio_stream': base64.b64encode(audio)}
    res, err = client.taskPush("nayar.common.speech.recognize", params, 10)
    print res
