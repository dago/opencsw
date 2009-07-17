--- xpdf-3.02.orig/xpdf/XPDFCore.cc     2007-02-27 23:05:52.000000000 +0100
+++ xpdf-3.02/xpdf/XPDFCore.cc  2009-07-17 12:45:53.330184593 +0200
@@ -271,7 +271,7 @@
     XtVaSetValues(shell, XmNwidth, width + (topW - daW),
                  XmNheight, height + (topH - daH), NULL);
   } else {
-    XtVaSetValues(drawArea, XmNwidth, width, XmNheight, height, NULL);
+    XtVaSetValues(shell, XmNwidth, width, XmNheight, height, NULL);
   }
 }
