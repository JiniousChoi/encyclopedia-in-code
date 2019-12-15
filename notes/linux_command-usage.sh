find ~ -type f -name "*.xml" | tar -cf result.tar -T -

tar -cvf "*.mp4" | gzip -9 > music.tar.gz

find . -type f -size '+1k' -size '-3k' | tar cf - -T - | gzip -9c > /tmp/test33.tar.gz

rsync -avzh . jinuine@dgw01.nhnsystem.com:~/
