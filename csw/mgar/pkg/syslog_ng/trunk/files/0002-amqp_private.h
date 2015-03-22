*** amqp_private.h.orig	Sat Mar 21 20:07:11 2015
--- amqp_private.h	Sat Mar 21 20:09:29 2015
***************
*** 33,38 ****
--- 33,54 ----
   * ***** END LICENSE BLOCK *****
   */
  
+ /* cwalther@opencsw.org:
+  * Fix missing htonll and ntohll by providing one.
+  * The following code is based on:
+  * https://web.archive.org/web/20090221024054/http://bugs.opensolaris.org/bugdatabase/view_bug.do?bug_id=5007142
+  */
+ 
+ #ifndef htonll
+ #ifdef _BIG_ENDIAN
+ #define htonll(x)   (x)
+ #define ntohll(x)   (x)
+ #else
+ #define htonll(x)   ((((uint64_t)htonl(x)) << 32) + htonl(x >> 32))
+ #define ntohll(x)   ((((uint64_t)ntohl(x)) << 32) + ntohl(x >> 32))
+ #endif
+ #endif
+ 
  #ifdef HAVE_CONFIG_H
  #include "config.h"
  #endif
