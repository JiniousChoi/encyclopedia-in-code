# FFMPEG

# How to download m3u8

```bash
$ ffmpeg \
    -user_agent "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0" \
    -i 'https://cdn.example.com/index.m3u8' \
    -c copy \
    output.mp4
```

You can pick youw resolution with -map option as follows:

it's second program 
```bash
$ ffmpeg \
    -i 'https://cdn.example.com/index.m3u8' \
    -map p:1 (or -map 1) which means second one \
    -c copy \
    output.mp4
```

