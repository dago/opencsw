--- iftop-0.17.orig/ui.c	2005-10-26 22:12:33.000000000 +0200
+++ iftop-0.17/ui.c	2009-07-08 18:58:38.298151622 +0200
@@ -6,7 +6,7 @@
 #include <sys/types.h>
 
 #include <ctype.h>
-#include <curses.h>
+#include <ncurses/curses.h>
 #include <errno.h>
 #include <string.h>
 #include <math.h>
