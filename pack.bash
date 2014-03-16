#/bin/bash
./build.bash
rm packed.tar.gz
tar cvzf packed.tar.gz *.html images/* build/*
tar -tvf packed.tar.gz
