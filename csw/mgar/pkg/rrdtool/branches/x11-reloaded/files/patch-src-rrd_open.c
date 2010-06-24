--- rrdtool-1.4.2.orig/src/rrd_open.c	2009-11-15 12:54:23.000000000 +0100
+++ rrdtool-1.4.2/src/rrd_open.c	2010-02-26 15:18:37.546048288 +0100
@@ -683,7 +683,7 @@
 /* this is a leftover from the old days, it serves no purpose
    and is therefore turned into a no-op */
 void rrd_flush(
-    rrd_file_t *rrd_file  __attribute__((unused)))
+    rrd_file_t *rrd_file)
 {
 }
 
@@ -745,10 +745,10 @@
  * aligning RRAs within stripes, or other performance enhancements
  */
 void rrd_notify_row(
-    rrd_file_t *rrd_file  __attribute__((unused)),
-    int rra_idx  __attribute__((unused)),
-    unsigned long rra_row  __attribute__((unused)),
-    time_t rra_time  __attribute__((unused)))
+    rrd_file_t *rrd_file,
+    int rra_idx,
+    unsigned long rra_row,
+    time_t rra_time)
 {
 }
 
@@ -760,8 +760,8 @@
  * don't change to a new disk block at the same time
  */
 unsigned long rrd_select_initial_row(
-    rrd_file_t *rrd_file  __attribute__((unused)),
-    int rra_idx  __attribute__((unused)),
+    rrd_file_t *rrd_file,
+    int rra_idx,
     rra_def_t *rra
     )
 {
