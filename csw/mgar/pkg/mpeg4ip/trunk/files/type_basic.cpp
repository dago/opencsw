diff --speed-large-files --minimal -Nru mpeg4ip.orig/common/video/iso-mpeg4/src/type_basic.cpp mpeg4ip/common/video/iso-mpeg4/src/type_basic.cpp
--- mpeg4ip.orig/common/video/iso-mpeg4/src/type_basic.cpp 2010-02-25 01:59:55.429555000 +0100
+++ mpeg4ip/common/video/iso-mpeg4/src/type_basic.cpp      2010-02-25 02:00:17.779765000 +0100
@@ -317,7 +317,7 @@
        iHalfY = m_vctTrueHalfPel.y - iMVY * 2;
 }

-Void CMotionVector::setToZero (Void)
+Void CMotionVector::setToZero ()
 {
        memset (this, 0, sizeof (*this));
 }

