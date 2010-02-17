--- Term-ReadLine-Gnu-1.19.orig/t/readline.t	2010-02-17 17:20:01.298647840 +0100
+++ Term-ReadLine-Gnu-1.19/t/readline.t	2010-02-17 17:18:59.672212090 +0100
@@ -90,7 +90,7 @@
 # 2.3 Readline Variables
 
 my ($maj, $min) = $a->{library_version} =~ /(\d+)\.(\d+)/;
-my $version = $a->{readline_version};
+my $version = $a->{readline_version} + 1;
 $res = ($version == 0x100 * $maj + $min); ok('readline_version');
 
 # Version 2.0 is NOT supported.
