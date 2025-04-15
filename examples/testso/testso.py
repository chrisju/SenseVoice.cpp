#!/usr/bin/env python3

import os,sys
import easycpp


#build/bin/sense-voice-main -m ../sense-voice-gguf/sense-voice-small-q8_0.gguf ../01.wav -t 18 -ng --max_speech_duration_ms 5000  --min_silence_duration_ms 550
#EXPORT int sense_voice_load(const char *str_params);
#EXPORT int sense_voice_speech2text(const char *audio_data, const char *str_params);

if __name__ == '__main__':
    #cmdarg = '-m ../sense-voice-gguf/sense-voice-small-q8_0.gguf -t 18 -ng --max_speech_duration_ms 5000  --min_silence_duration_ms 550'
    cmdarg = ' '.join(sys.argv[1:]).encode('utf-8')
    print(f'cmdarg: {cmdarg}')
    cpp = easycpp.easycpp('build/lib/libsense-voice.so')
    r = cpp.sense_voice_load(cmdarg)
    print(f'sense_voice_load: {r}')
    r = cpp.sense_voice_speech2text(cmdarg)
    print(f'sense_voice_speech2text: {r}')

