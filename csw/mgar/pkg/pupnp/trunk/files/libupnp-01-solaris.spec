--- libupnp-1.6.0/README.orig	2007-07-15 15:19:30.541726415 +0700
+++ libupnp-1.6.0/README	2007-07-15 15:20:12.555440132 +0700
@@ -111,7 +111,7 @@
 options enabled (see below for options available at configure time).
 
 % cd $(LIBUPNP)
-% ./configure CFLAGS="-DSPARC_SOLARIS -mtune=<cputype> -mcpu=<cputype>"
+% ./configure CFLAGS="-DSOLARIS -mtune=<cputype> -mcpu=<cputype>"
 % make
 
 will build a Sparc Solaris version of the binaries without debug support
@@ -247,7 +247,7 @@
 described above. Only the call to ./configure has to be done using an
 additional parameter:
 
-./configure CFLAGS="-mcpu=<cputype> -mtune=<cputype> -DSPARC_SOLARIS"
+./configure CFLAGS="-mcpu=<cputype> -mtune=<cputype> -DSOLARIS"
 
 where <cputype> has to be replaced by the appropriate CPU tuning flag (e.g.
 "supersparc"). Afterwards
--- libupnp-1.6.6/upnp/src/genlib/net/uri/uri.c.orig	2008-11-13 13:58:53.675111848 +0800
+++ libupnp-1.6.6/upnp/src/genlib/net/uri/uri.c	2008-11-13 14:36:42.044847654 +0800
@@ -627,7 +627,7 @@
         // platform-specific stuff below
 #if defined(WIN32) || defined(__CYGWIN__)
         h = gethostbyname(temp_host_name);
-#elif defined(SPARC_SOLARIS)
+#elif defined(SOLARIS)
         errCode = gethostbyname_r(
                 temp_host_name,
                 &h,
--- libupnp-1.6.6/upnp/src/api/upnpapi.c.orig	2008-11-13 14:51:07.131616887 +0800
+++ libupnp-1.6.6/upnp/src/api/upnpapi.c	2008-11-13 14:51:52.992915327 +0800
@@ -56,7 +56,7 @@
 	#include <unistd.h>
 
 
-	#if defined(_sun)
+	#if defined(SOLARIS)
 		#include <sys/sockio.h>
 		#include <fcntl.h>
 	#elif defined(BSD) && BSD >= 199306
