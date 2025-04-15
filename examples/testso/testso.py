#!/usr/bin/env python3

import os,sys
import easycpp
import ctypes


#build/bin/sense-voice-main -m ../sense-voice-gguf/sense-voice-small-q8_0.gguf ../01.wav -t 18 -ng --max_speech_duration_ms 5000  --min_silence_duration_ms 550
#EXPORT int sense_voice_load(const char *str_params);
#EXPORT int sense_voice_speech2text(const char *audio_data, const char *str_params);

if __name__ == '__main__':
    cpp = easycpp.easycpp('build/lib/libsense-voice.so')
    cpp.sense_voice_speechbuff2text.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_char_p)
    ]
    cpp.sense_voice_speechbuff2text.restype = ctypes.c_int
    out_ptr = ctypes.c_char_p()

    mode = 2
    if mode == 1:

        # ./examples/testso/testso.py -m ../sense-voice-gguf/sense-voice-small-q8_0.gguf -t 18 -ng --max_speech_duration_ms 5000  --min_silence_duration_ms 550 ../01.wav
        cmdarg = ' '.join(sys.argv[1:]).encode('utf-8')
        print(f'cmdarg: {cmdarg}')
        r = cpp.sense_voice_load(cmdarg)
        print(f'sense_voice_load: {r}')
        r = cpp.sense_voice_speech2text(cmdarg)
        print(f'sense_voice_speech2text: {r}')
    else:

        # ./examples/testso/testso.py ../01.wav
        cmdarg = '-m ../sense-voice-gguf/sense-voice-small-q8_0.gguf -t 18 -ng --max_speech_duration_ms 5000  --min_silence_duration_ms 550'.encode('utf-8')
        print(f'cmdarg: {cmdarg}')
        r = cpp.sense_voice_load(cmdarg)
        print(f'sense_voice_load: {r}')
        audio = open(sys.argv[1], 'rb').read()
        r = cpp.sense_voice_speechbuff2text(cmdarg, audio, len(audio), ctypes.byref(out_ptr))
        if r > 0:
            print(out_ptr.value.decode('utf-8'))
        else:
            print("cpp.sense_voice_speechbuff2text failed.")

