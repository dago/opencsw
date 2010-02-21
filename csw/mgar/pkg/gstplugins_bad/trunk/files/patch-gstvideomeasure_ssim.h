--- gst-plugins-bad-0.10.17.orig/gst/videomeasure/gstvideomeasure_ssim.h	2009-10-12 12:23:35.000000000 +0200
+++ gst-plugins-bad-0.10.17/gst/videomeasure/gstvideomeasure_ssim.h	2010-02-21 16:23:33.000000000 +0100
@@ -37,16 +37,11 @@
 
 
 #define GST_TYPE_SSIM            (gst_ssim_get_type())
-#define GST_SSIM(obj)            (G_TYPE_CHECK_INSTANCE_CAST((obj),            \
-    GST_TYPE_SSIM,GstSSim))
-#define GST_IS_SSIM(obj)         (G_TYPE_CHECK_INSTANCE_TYPE((obj),            \
-    GST_TYPE_SSIM))
-#define GST_SSIM_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST((klass) ,            \
-    GST_TYPE_SSIM,GstSSimClass))
-#define GST_IS_SSIM_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE((klass) ,            \
-    GST_TYPE_SSIM))
-#define GST_SSIM_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS((obj) ,            \
-    GST_TYPE_SSIM,GstSSimClass))
+#define GST_SSIM(obj)            (G_TYPE_CHECK_INSTANCE_CAST((obj), GST_TYPE_SSIM,GstSSim))
+#define GST_IS_SSIM(obj)         (G_TYPE_CHECK_INSTANCE_TYPE((obj), GST_TYPE_SSIM))
+#define GST_SSIM_CLASS(klass)    (G_TYPE_CHECK_CLASS_CAST((klass) , GST_TYPE_SSIM,GstSSimClass))
+#define GST_IS_SSIM_CLASS(klass) (G_TYPE_CHECK_CLASS_TYPE((klass) , GST_TYPE_SSIM))
+#define GST_SSIM_GET_CLASS(obj)  (G_TYPE_INSTANCE_GET_CLASS((obj) , GST_TYPE_SSIM,GstSSimClass))
 
 typedef struct _GstSSim             GstSSim;
 typedef struct _GstSSimClass        GstSSimClass;
