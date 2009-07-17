--- xpdf-3.02.orig/goo/GString.cc	2007-02-27 23:05:51.000000000 +0100
+++ xpdf-3.02/goo/GString.cc	2009-07-17 08:14:34.059621276 +0200
@@ -528,7 +528,7 @@
   if ((neg = x < 0)) {
     x = -x;
   }
-  x = floor(x * pow(10, prec) + 0.5);
+  x = floor(x * pow((double)10, prec) + 0.5);
   i = bufSize;
   started = !trim;
   for (j = 0; j < prec && i > 1; ++j) {
