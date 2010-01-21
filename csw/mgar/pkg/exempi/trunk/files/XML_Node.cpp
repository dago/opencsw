diff -Nru exempi-2.1.1.orig/source/common/XML_Node.cpp exempi-2.1.1/source/common/XML_Node.cpp
--- exempi-2.1.1.orig/source/common/XML_Node.cpp	2009-02-17 05:10:42.000000000 +0100
+++ exempi-2.1.1/source/common/XML_Node.cpp	2010-01-20 21:30:44.823511273 +0100
@@ -9,6 +9,7 @@
 #include "XMP_Environment.h"	// ! Must be the first #include!
 #include "XMLParserAdapter.hpp"
 
+#include <stdio.h>
 #include <string.h>
 #include <cstring>
 #include <cstdio>
