--- PDL-2.4.6.orig/Basic/Math/quiet_nan.c	2009-10-17 23:37:41.000000000 +0200
+++ PDL-2.4.6/Basic/Math/quiet_nan.c	2010-02-17 22:03:09.788528006 +0100
@@ -1,6 +1,6 @@
 #include "mconf.h"
 /* Patch NaN function where no system NaN is available */
-double quiet_nan(void)
+double quiet_nan(long unused)
 {
 #ifdef NaN
   double a;
