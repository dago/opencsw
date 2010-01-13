--- Makefile	2010-01-13 19:25:50.435317055 +0100
+++ Makefile	2010-01-13 19:24:07.075661494 +0100
@@ -2,9 +2,9 @@
 DATE != date +%Y%m%d
 
 CC=/opt/studio/SOS11/SUNWspro/bin/cc
-CFLAGS=-xO3 -xarch=v8
-LIBS=-lresolv -lnsl -lsocket -lcurses 
+CFLAGS=-xO3 -xarch=v8 -I/opt/csw/include
+LIBS=-lresolv -lnsl -lsocket -lcurses -lpcap
 OPTFLAGS= -DUSE_IPV6=1
 
 prefix=/opt/csw
