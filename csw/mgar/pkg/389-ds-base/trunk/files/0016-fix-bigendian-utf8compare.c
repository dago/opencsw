--- a/ldap/servers/slapd/utf8compare.c
+++ b/ldap/servers/slapd/utf8compare.c
@@ -60,6 +60,7 @@ typedef struct sUpperLowerTbl {
 int
 slapi_has8thBit(unsigned char *s)
 {
+#if (defined(CPU_x86) || defined(CPU_x86_64)) 
 #define MY8THBITWIDTH 4 /* sizeof(PRUint32) */
 #define MY8THBITFILTER 0x80808080
     unsigned char *p, *stail, *ltail;
@@ -73,14 +74,20 @@ slapi_has8thBit(unsigned char *s)
              return 1;
         }
     }
-    for (; p < ltail; p++) {
+#undef MY8THBITWIDTH 
+#undef MY8THBITFILTER 
+    for (; p < ltail; p++) 
+#else 
+    unsigned char *p, *tail; 
+    tail = s + strlen((char *)s);  
+    for (p = s; p < tail; p++) 
+#endif 
+    { 
         if (0x80 & *p) {
              return 1;
         }
     }
     return 0;
-#undef MY8THBITWIDTH
-#undef MY8THBITFILTER
 }
 
 /*
