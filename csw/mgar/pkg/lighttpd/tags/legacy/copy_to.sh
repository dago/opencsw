#!/bin/sh
#

sudo cp ./lighttpd.xml /var/svc/manifest/network/
sudo cp ./cswlighttpd /lib/svc/method/
sudo chmod a+rx /lib/svc/method/cswlighttpd
sudo cp ./lighttpd.conf /opt/csw/etc/

#/opt/csw/share/lighttpd
#/opt/csw/var/lighttpd

sudo mkdir -p  /opt/csw/share/lighttpd/
sudo chown nobody:nobody /opt/csw/share/lighttpd/

sudo mkdir -p /opt/csw/var/lighttpd
sudo touch /opt/csw/var/lighttpd/access.log 
sudo chown -R nobody:nobody /opt/csw/var/lighttpd

sudo echo 'Lighttpd working.' > /opt/csw/share/lighttpd-root/index.html
