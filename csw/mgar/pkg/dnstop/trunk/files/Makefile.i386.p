--- Makefile	2010-01-13 17:55:54.574796795 +0100
+++ Makefile	2010-01-13 18:00:42.582082173 +0100
@@ -2,8 +2,8 @@
 
 OPTFLAGS= -DUSE_IPV6=1
 CC=/opt/SUNWspro/bin/cc
-CFLAGS=-xO3 -m32 -xarch=386 -xnorunpath ${OPTFLAGS}
-LIBS=-lresolv -lnsl -lsocket -lpcap -lncurses 
+CFLAGS=-xO3 -m32 -xarch=386 -xnorunpath ${OPTFLAGS} -I/opt/csw/include
+LIBS=-lresolv -lnsl -lsocket -lpcap -lcurses 
 
 prefix=/opt/csw
 exec_prefix=/opt/csw
