--- p7zip_4.65.orig/CPP/7zip/Archive/Zip/ZipHandler.cpp 2009-02-07 17:44:56.000000000 +0100
+++ p7zip_4.65/CPP/7zip/Archive/Zip/ZipHandler.cpp      2009-06-18 14:49:38.167225788 +0200
@@ -806,6 +806,7 @@
     RINOK(extractCallback->PrepareOperation(askMode));
 
     Int32 res;
+    UInt32 _numThreads;
     RINOK(myDecoder.Decode(
         EXTERNAL_CODECS_VARS
         m_Archive, item, realOutStream, extractCallback,
