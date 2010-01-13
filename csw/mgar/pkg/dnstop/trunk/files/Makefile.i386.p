--- Makefile	2010-01-13 17:55:54.574796795 +0100
+++ Makefile	2010-01-13 18:00:42.582082173 +0100
@@ -2,8 +2,8 @@
 DATE != date +%Y%m%d
 
 CC=/opt/studio/SOS11/SUNWspro/bin/cc
-CFLAGS=-xO3 -xarch=386
-LIBS=-lresolv -lnsl -lsocket -lcurses 
+CFLAGS=-xO3 -xarch=386 -I/opt/csw/include
+LIBS=-lresolv -lnsl -lsocket -lcurses -lpcap
 OPTFLAGS= -DUSE_IPV6=1
 
 prefix=/opt/csw
