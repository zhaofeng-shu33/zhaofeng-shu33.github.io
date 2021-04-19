# Offline speech recognition
2021/4/19

Using `julius`, which supports Japanese.
```
../julius/julius -C julius.jconf -dnnconf dnn.jconf -nolog > a.txt
grep "sentence1.*" a.txt
```

## How to transform mp3 file to wav file in 16000 sampling rate

```shell
ffmpeg -i TRACK03.MP3 -ac 1 -ar 16000 track03.wav # one channel, sampling rate is 16k HZ
```

## Online alternative
https://speech-to-text-demo.ng.bluemix.net/

Users can use it without registration.