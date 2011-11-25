--- babl-0.1.2.orig/docs/tools/xml_insert.sh	2009-09-25 18:14:41.000000000 +0200
+++ babl-0.1.2/docs/tools/xml_insert.sh	2010-02-18 13:57:12.000000000 +0100
@@ -11,7 +11,7 @@
 #
 # FIXME: add argument checking / error handling
 
-: ${AWK="awk"}
+: ${AWK="nawk"}
 : ${ECHO="echo"}
 : ${MKDIR="mkdir"}
 : ${SED="sed"}
@@ -84,8 +84,27 @@
 
     $ECHO "X$my_tmpdir" | $Xsed
 }
+# tmp_dir="`func_mktempdir`"
+
+func_perlfunc_mktempdir ()
+{
+    my_template="${TMPDIR-/tmp}/${1-$progname}"
+    if test "$opt_dry_run" = ":"; then
+      # Return a directory name, but don't create it in dry-run mode
+      my_tmpdir="${my_template}-$$"
+    else
+      my_template="${my_template}-XXXXXXXX"
+      my_tmpdir=`/opt/csw/bin/perl -e 'use File::Temp qw/ :mktemp  /; print mkdtemp("'${my_template}'")."\n"'`
+      if test ! -d "$my_tmpdir"; then
+        func_fatal_error "cannot create temporary directory \`$my_tmpdir'"
+      fi
+   
+    fi
+    
+    $ECHO "X$my_tmpdir" | $Xsed
+}
+tmp_dir="`func_perlfunc_mktempdir`"
 
-tmp_dir="`func_mktempdir`"
 tmp_file="$tmp_dir/one"
 
 cp $1 $tmp_file
