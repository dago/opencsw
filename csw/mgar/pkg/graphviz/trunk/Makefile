GARNAME = graphviz
GARVERSION = 2.24.0
CATEGORIES = utils

DESCRIPTION = Graph visualization tools 
define BLURB
    graphviz is a set of graph visualization tools and libraries. It supports
    hierarchical and mass-spring drawings; although the tools are scalable,
    their emphasis is on making very good drawings of reasonably-sized graphs.
endef

MASTER_SITES = http://www.graphviz.org/pub/graphviz/stable/SOURCES/

# disable dependency checks because plugins depend on libs from base package
ENABLE_CHECK = 0

PATCHFILES = no_svg_in_libcairo.diff

PACKAGES = CSWgraphviz \
	CSWgraphvizdevel \
	CSWgraphvizdoc \
	CSWgraphvizgraphs \
	CSWgraphvizgd \
	CSWgraphvizsharp \
	CSWgraphvizguile \
	CSWgraphvizperl \
	CSWgraphvizpython \
	CSWgraphviztcl

#	CSWgraphvizdevil \
#	CSWgraphvizjava \
#	CSWgraphvizlua \
#	CSWgraphvizocaml \
#	CSWgraphvizphp \
#	CSWgraphvizr \
#	CSWgraphvizruby \
#

INCOMPATIBLE_PKGS = CSWgraphvis CSWgraphviz2

ARCHALL_CSWgraphvizdoc = 1
ARCHALL_CSWgraphvizgraphs = 1

PREREQUISITE_PKGS = 

REQUIRED_PKGS_CSWgraphviz = CSWexpat CSWpango CSWlibcairo CSWgts CSWlibxrender CSWgs \
	CSWfconfig CSWftype2 CSWggettextrt CSWglib2 CSWgtk2 CSWiconv \
	CSWlibatk CSWliblasi CSWpng CSWzlib CSWxpm
REQUIRED_PKGS_CSWgraphvizdevel =
REQUIRED_PKGS_CSWgraphvizdoc = 
REQUIRED_PKGS_CSWgraphvizgraphs = 
REQUIRED_PKGS_CSWgraphvizgd = CSWgd CSWjpeg CSWxpm
REQUIRED_PKGS_CSWgraphvizdevil = CSWdevil
REQUIRED_PKGS_CSWgraphvizsharp = CSWmono
REQUIRED_PKGS_CSWgraphvizguile = CSWguile
REQUIRED_PKGS_CSWgraphvizjava = CSWjava
REQUIRED_PKGS_CSWgraphvizlua = CSWlua
REQUIRED_PKGS_CSWgraphvizocaml = CSWocaml
REQUIRED_PKGS_CSWgraphvizperl = CSWperl
REQUIRED_PKGS_CSWgraphvizphp = CSWphp5
REQUIRED_PKGS_CSWgraphvizpython = CSWpython-rt
REQUIRED_PKGS_CSWgraphvizr = CSWr
REQUIRED_PKGS_CSWgraphvizruby = CSWruby
REQUIRED_PKGS_CSWgraphviztcl = CSWtcl CSWtk

LICENSE_CSWgraphviz = COPYING
LICENSE_CSWgraphvizdevel = COPYING
LICENSE_CSWgraphvizdoc = COPYING
LICENSE_CSWgraphvizgraphs = COPYING
LICENSE_CSWgraphvizgd = COPYING
LICENSE_CSWgraphvizdevil = COPYING
LICENSE_CSWgraphvizsharp = COPYING
LICENSE_CSWgraphvizguile = COPYING
LICENSE_CSWgraphvizjava = COPYING
LICENSE_CSWgraphvizlua = COPYING
LICENSE_CSWgraphvizocaml = COPYING
LICENSE_CSWgraphvizperl = COPYING
LICENSE_CSWgraphvizphp = COPYING
LICENSE_CSWgraphvizpython = COPYING
LICENSE_CSWgraphvizr = COPYING
LICENSE_CSWgraphvizruby = COPYING
LICENSE_CSWgraphviztcl = COPYING

SPKG_DESC_CSWgraphviz = Graph Visualization Tools
SPKG_DESC_CSWgraphvizdevel = Graphviz Headers etc. for development
SPKG_DESC_CSWgraphvizdoc = Graphviz documentation
SPKG_DESC_CSWgraphvizgraphs = Graphviz example graphs
SPKG_DESC_CSWgraphvizgd = Graphviz renderers using gd
SPKG_DESC_CSWgraphvizdevil = Graphviz renderers using DevIL
SPKG_DESC_CSWgraphvizsharp = Graphviz language binding for C#
SPKG_DESC_CSWgraphvizguile = Graphviz language binding for guile
SPKG_DESC_CSWgraphvizjava = Graphviz language binding for java
SPKG_DESC_CSWgraphvizlua = Graphviz language binding for lua
SPKG_DESC_CSWgraphvizocaml = Graphviz language binding for ocaml
SPKG_DESC_CSWgraphvizperl = Graphviz language binding for perl
SPKG_DESC_CSWgraphvizphp = Graphviz language binding for php
SPKG_DESC_CSWgraphvizpython = Graphviz language binding for python
SPKG_DESC_CSWgraphvizr = Graphviz language binding for R
SPKG_DESC_CSWgraphvizruby = Graphviz language binding for ruby
SPKG_DESC_CSWgraphviztcl = Graphviz language binding for tcl

PKGFILES_CSWgraphviz = $(bindir)/(?!diffimg).*
PKGFILES_CSWgraphviz += $(libdir)/lib.*.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_core\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_pango\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_rsvg\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_lasi\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_gtk\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_gdk_pixbuf\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_xlib\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_.*layout\..*
PKGFILES_CSWgraphviz += $(sharedstatedir)/graphviz/lefty/.* 
PKGFILES_CSWgraphviz += $(mandir)/man1/.*\.1
PKGFILES_CSWgraphviz += $(mandir)/man7/.*\.7

PKGFILES_CSWgraphvizdevel = $(libdir)/pkgconfig/.*\.pc
PKGFILES_CSWgraphvizdevel += $(includedir)/.*\.h
PKGFILES_CSWgraphvizdevel += $(mandir)/man3/.*\.3

PKGFILES_CSWgraphvizdoc = $(sharedstatedir)/graphviz/doc/.*

PKGFILES_CSWgraphvizgraphs = $(sharedstatedir)/graphviz/graphs/.* 

PKGFILES_CSWgraphvizgd = $(libdir)/graphviz/libgvplugin_gd\..*
PKGFILES_CSWgraphvizgd += $(bindir)/diffimg

PKGFILES_CSWgraphvizdevil = $(libdir)/graphviz/libgvplugin_devil\..*

PKGFILES_CSWgraphvizsharp = $(libdir)/graphviz/sharp/.*
PKGFILES_CSWgraphvizsharp += $(mandir)/man3/.*\.3sharp
PKGFILES_CSWgraphvizsharp += $(sharedstatedir)/graphviz/demo/.*\.cs

PKGFILES_CSWgraphvizguile = $(libdir)/graphviz/guile/.*
PKGFILES_CSWgraphvizguile += $(mandir)/man3/.*\.3guile
PKGFILES_CSWgraphvizguile += $(sharedstatedir)/graphviz/demo/.*\.guile

PKGFILES_CSWgraphvizjava = $(libdir)/graphviz/java/.*
PKGFILES_CSWgraphvizjava += $(mandir)/man3/.*\.3java
PKGFILES_CSWgraphvizjava += $(sharedstatedir)/graphviz/demo/.*\.java

PKGFILES_CSWgraphvizlua = $(libdir)/graphviz/lua/.*
PKGFILES_CSWgraphvizlua += $(mandir)/man3/.*\.3lua
PKGFILES_CSWgraphvizlua += $(sharedstatedir)/graphviz/demo/.*\.lua

PKGFILES_CSWgraphvizocaml = $(libdir)/graphviz/ocaml/.*
PKGFILES_CSWgraphvizocaml += $(mandir)/man3/.*\.3ocaml
PKGFILES_CSWgraphvizocaml += $(sharedstatedir)/graphviz/demo/.*\.ml

PKGFILES_CSWgraphvizperl = $(libdir)/graphviz/perl/.*
PKGFILES_CSWgraphvizperl += $(mandir)/man3/.*\.3perl
PKGFILES_CSWgraphvizperl += $(sharedstatedir)/graphviz/demo/.*\.pl

PKGFILES_CSWgraphvizphp = $(libdir)/graphviz/php/.*
PKGFILES_CSWgraphvizphp += $(mandir)/man3/.*\.3php
PKGFILES_CSWgraphvizphp += $(sharedstatedir)/graphviz/demo/.*\.php

PKGFILES_CSWgraphvizpython = $(libdir)/graphviz/python/.*
PKGFILES_CSWgraphvizpython += $(mandir)/man3/.*\.3python
PKGFILES_CSWgraphvizpython += $(sharedstatedir)/graphviz/demo/.*\.py

PKGFILES_CSWgraphvizr = $(libdir)/graphviz/R/.*
PKGFILES_CSWgraphvizr += $(mandir)/man3/.*\.3r
PKGFILES_CSWgraphvizr += $(sharedstatedir)/graphviz/demo/.*\.r

PKGFILES_CSWgraphvizruby = $(libdir)/graphviz/ruby/.*
PKGFILES_CSWgraphvizruby += $(mandir)/man3/.*\.3ruby
PKGFILES_CSWgraphvizruby += $(sharedstatedir)/graphviz/demo/.*\.rb

PKGFILES_CSWgraphviztcl = $(libdir)/graphviz/tcl/.*
PKGFILES_CSWgraphviztcl += $(mandir)/man3/.*\.3tcl
PKGFILES_CSWgraphviztcl += $(mandir)/man3/.*\.3tk
PKGFILES_CSWgraphviztcl += $(sharedstatedir)/graphviz/demo/.*\.tcl
PKGFILES_CSWgraphviztcl += $(sharedstatedir)/graphviz/demo/.*\.tcl.README
PKGFILES_CSWgraphviztcl += $(sharedstatedir)/graphviz/demo/pathplan_data/.*

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWgraphviz.postinstall
DISTFILES += CSWgraphvizgd.postinstall CSWgraphvizgd.postuninstall
DISTFILES += CSWgraphvizdevil.postinstall CSWgraphvizdevil.postuninstall

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-sfdp
CONFIGURE_ARGS += --with-gtk
CONFIGURE_ARGS += --with-gdk-pixbuf
CONFIGURE_ARGS += --with-ghostscript
CONFIGURE_ARGS += --with-lasi
CONFIGURE_ARGS += --without-ipsepcola
CONFIGURE_ARGS += --without-rsvg
CONFIGURE_ARGS += --disable-ruby
CONFIGURE_ARGS += --disable-devil
CONFIGURE_ARGS += --disable-java
CONFIGURE_ARGS += --disable-lua
CONFIGURE_ARGS += --disable-ocaml
CONFIGURE_ARGS += --disable-php
CONFIGURE_ARGS += --disable-r
CONFIGURE_ARGS += PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig:/opt/csw/X11/lib/pkgconfig

STRIP_LIBTOOL=1

TEST_SCRIPTS = custom

include gar/category.mk

test-custom:
	@echo " ==> Testing $(GARNAME) (custom)"
	@$(MAKECOOKIE)
