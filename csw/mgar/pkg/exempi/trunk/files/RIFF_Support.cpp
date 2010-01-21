diff -Nru exempi-2.1.1.orig/source/XMPFiles/FormatSupport/RIFF_Support.cpp exempi-2.1.1/source/XMPFiles/FormatSupport/RIFF_Support.cpp
--- exempi-2.1.1.orig/source/XMPFiles/FormatSupport/RIFF_Support.cpp	2009-02-17 05:10:42.000000000 +0100
+++ exempi-2.1.1/source/XMPFiles/FormatSupport/RIFF_Support.cpp	2010-01-20 21:35:32.833002097 +0100
@@ -550,7 +550,7 @@
 
 // *** Could be moved to a separate header
 
-#pragma pack(push,1)
+//#pragma pack(push,1)
 
 //	[TODO] Can we switch to using just a full path here?
 struct FSSpecLegacy
@@ -603,7 +603,7 @@
 	FSSpecLegacy		fullPath;		// Full path of the project file
 };
 
-#pragma pack(pop)
+//#pragma pack(pop)
 
 // -------------------------------------------------------------------------------------------------
 
