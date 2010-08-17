--- rrdtool-1.4.2.orig/bindings/ruby/extconf.rb	2010-03-02 16:12:18.622716000 +0100
+++ rrdtool-1.4.2/bindings/ruby/extconf.rb	2010-03-02 17:27:47.399923107 +0100
@@ -6,7 +6,7 @@
 if /linux/ =~ RUBY_PLATFORM
    $LDFLAGS += '-Wl,--rpath -Wl,$(EPREFIX)/lib'
 elsif /solaris/ =~ RUBY_PLATFORM
-   $LDFLAGS += '-R$(EPREFIX)/lib'
+   $LDFLAGS += ' -R$(EPREFIX)/lib'
 elsif /hpux/ =~ RUBY_PLATFORM
    $LDFLAGS += '+b$(EPREFIX)/lib'
 elsif /aix/ =~ RUBY_PLATFORM
