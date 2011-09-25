--- Makefile	Sat Mar  5 00:33:14 2011
+++ Makefile.new	Sat Mar  5 00:34:19 2011
@@ -2,8 +2,8 @@
 
 OPTFLAGS= -DUSE_IPV6=1
 CC=/opt/SUNWspro/bin/cc
-CFLAGS=-xO3 -m32 -xarch=v8 ${OPTFLAGS}
-LIBS=-lresolv -lnsl -lsocket -lpcap -lncurses 
+CFLAGS=-xO3 -m32 -xarch=v8 ${OPTFLAGS} -I/opt/csw/include
+LIBS=-lresolv -lnsl -lsocket -lpcap -lcurses 
 LDFLAGS=-m32 -xarch=v8 -L/opt/csw/lib
 
 prefix=/opt/csw
