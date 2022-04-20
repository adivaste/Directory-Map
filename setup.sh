#!/bin/sh

if [ $(whoami) = root ]
then
	mv listDir.py dmap rdmap /usr/bin/
else
	sudo mv listDir.py dmap rdmap /usr/bin/
fi
chmod +x /usr/bin/listDir.py
chmod +x /usr/bin/dmap
chmod +x /usr/bin/rdmap

