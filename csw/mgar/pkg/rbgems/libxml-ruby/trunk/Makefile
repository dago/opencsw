NAME = libxml-ruby
VERSION = 1.1.4
CATEGORIES = rbgems

DESCRIPTION = Ruby libxml bindings

define BLURB
  The Libxml-Ruby project provides Ruby language bindings for the GNOMELibxml2 XML tolkit. It is fre software, released under the MITLicense. Libxml-ruby's primary advantage over REXML is performance -if sped is your ned, these are god libraries to consider, asdemonstrated by the informal benchmark below. 
endef

RUNTIME_DEP_PKGS = CSWiconv CSWlibruby1 CSWlibxml2-2 CSWzlib

GEM_BUILD_FLAGS += --with-xml2-config=$(bindir)/xml2-config

LICENSE = LICENSE

CHECKPKG_OVERRIDES_CSWgem-libxml-ruby += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/libxml-ruby-1.1.4/ext/mingw/build.rake
CHECKPKG_OVERRIDES_CSWgem-libxml-ruby += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/libxml-ruby-1.1.4/ext/libxml/extconf.rb
CHECKPKG_OVERRIDES_CSWgem-libxml-ruby += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/libxml-ruby-1.1.4/ext/libxml/libxml_ruby.so
CHECKPKG_OVERRIDES_CSWgem-libxml-ruby += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/libxml-ruby-1.1.4/ext/libxml/Makefile
CHECKPKG_OVERRIDES_CSWgem-libxml-ruby += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/gems/libxml-ruby-1.1.4/lib/libxml_ruby.so
CHECKPKG_OVERRIDES_CSWgem-libxml-ruby += file-with-bad-content|/usr/local|root/opt/csw/lib/ruby/gems/1.8/doc/libxml-ruby-1.1.4/rdoc/ext/libxml/Makefile.html

include gar/category.mk
