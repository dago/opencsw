--- gst-plugins-good-0.10.18.orig/gst/matroska/matroska-demux.c	2010-02-04 18:36:43.000000000 +0100
+++ gst-plugins-good-0.10.18/gst/matroska/matroska-demux.c	2010-02-21 15:32:53.643034561 +0100
@@ -2298,7 +2298,7 @@
   {
     GST_OBJECT_UNLOCK (demux);
     GST_PAD_STREAM_UNLOCK (demux->sinkpad);
-    GST_ELEMENT_ERROR (demux, STREAM, DEMUX, NULL, ("Got a seek error"));
+    GST_ELEMENT_ERROR (demux, STREAM, DEMUX, (NULL), ("Got a seek error"));
     return FALSE;
   }
 }
