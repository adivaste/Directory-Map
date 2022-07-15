#!/bin/sh

if [ $(whoami) = root ]
then
	cp listDir.py dmap rdmap /usr/bin/
else
	sudo cp listDir.py dmap rdmap /usr/bin/
fi
chmod +x /usr/bin/listDir.py
chmod +x /usr/bin/dmap
chmod +x /usr/bin/rdmap

