--- siege-2.69.orig/src/auth.c	2008-08-19 15:53:31.000000000 +0200
+++ siege-2.69/src/auth.c	2010-01-24 00:37:36.433891267 +0100
@@ -491,7 +491,7 @@
     }
   }
   else {
-    fprintf(stderr, "invalid call to %s algorithm is [%s]\n", __FUNCTION__, challenge->algorithm);
+    fprintf(stderr, "invalid call to %s algorithm is [%s]\n", __func__, challenge->algorithm);
     return NULL;
   }
 
