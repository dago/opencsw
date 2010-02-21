--- gst-plugins-bad-0.10.17.orig/gst/videomeasure/gstvideomeasure_collector.h	2009-10-12 12:23:35.000000000 +0200
+++ gst-plugins-bad-0.10.17/gst/videomeasure/gstvideomeasure_collector.h	2010-02-21 16:23:40.000000000 +0100
@@ -29,17 +29,11 @@
 typedef struct _GstMeasureCollectorClass GstMeasureCollectorClass;
 
 #define GST_TYPE_MEASURE_COLLECTOR            (gst_measure_collector_get_type())
-#define GST_MEASURE_COLLECTOR(obj)                                             \
-    (G_TYPE_CHECK_INSTANCE_CAST((obj),GST_TYPE_MEASURE_COLLECTOR,              \
-    GstMeasureCollector))
-#define GST_IS_MEASURE_COLLECTOR(obj)         \
-    (G_TYPE_CHECK_INSTANCE_TYPE((obj), GST_TYPE_MEASURE_COLLECTOR))
-#define GST_MEASURE_COLLECTOR_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST((klass),\
-    GST_TYPE_MEASURE_COLLECTOR, GstMeasureCollectorClass))
-#define GST_IS_MEASURE_COLLECTOR_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE((klass),\
-    GST_TYPE_MEASURE_COLLECTOR))
-#define GST_MEASURE_COLLECTOR_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS((obj),\
-    GST_TYPE_MEASURE_COLLECTOR, GstMeasureCollectorClass))
+#define GST_MEASURE_COLLECTOR(obj)            (G_TYPE_CHECK_INSTANCE_CAST((obj),GST_TYPE_MEASURE_COLLECTOR,              GstMeasureCollector))
+#define GST_IS_MEASURE_COLLECTOR(obj)          (G_TYPE_CHECK_INSTANCE_TYPE((obj), GST_TYPE_MEASURE_COLLECTOR))
+#define GST_MEASURE_COLLECTOR_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST((klass), GST_TYPE_MEASURE_COLLECTOR, GstMeasureCollectorClass))
+#define GST_IS_MEASURE_COLLECTOR_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE((klass), GST_TYPE_MEASURE_COLLECTOR))
+#define GST_MEASURE_COLLECTOR_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS((obj), GST_TYPE_MEASURE_COLLECTOR, GstMeasureCollectorClass))
 
 typedef enum {
   GST_MEASURE_COLLECTOR_0 = 0,
