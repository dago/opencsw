--- Net-ext-1.011.orig/Gen.xs	2002-04-10 13:05:58.000000000 +0200
+++ Net-ext-1.011/Gen.xs	2010-02-17 14:28:53.354298154 +0100
@@ -146,7 +146,7 @@
     CV *cv;
     klen = strlen(name);
     (void) hv_fetch(missing, name, klen, TRUE);
-    cv = newXS(name, NULL, file); /* newSUB with no block */
+    cv = newXS(name, Perl_cv_undef, file); /* newSUB with no block */
     sv_setsv((SV*)cv, &PL_sv_no); /* prototype it as "()" */
 }
 
