# $Id$
#
# There is still a number of errors thrown by checkpkg; they need to be
# investigated.

NAME = graphviz
VERSION = 2.28.0
CATEGORIES = utils

DESCRIPTION = Graph visualization tools 
define BLURB
    graphviz is a set of graph visualization tools and libraries. It supports
    hierarchical and mass-spring drawings; although the tools are scalable,
    their emphasis is on making very good drawings of reasonably-sized graphs.
endef

MASTER_SITES = http://www.graphviz.org/pub/graphviz/stable/SOURCES/

GARCOMPILER = GCC4

PATCHFILES += configure.patch
PATCHFILES += Makefile.am.patch
PATCHFILES += trapezoid.c.patch
PATCHFILES += post_process.c.patch
PATCHFILES += gvpr_Makefile.am.patch
PATCHFILES += gv_Makefile.am.patch

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

INCOMPATIBLE_PKGS = CSWgraphvis

# This is a compatibility package which should go away after some time.
# It only contains a link to CSWgraphviz.
PACKAGES += CSWgraphviz2

# defer for some time to allow CSWgraphviz2 upgrades
# INCOMPATIBLE_PKGS = CSWgraphviz2

ARCHALL_CSWgraphvizdoc = 1
ARCHALL_CSWgraphvizgraphs = 1
ARCHALL_CSWgraphviz2 = 1

# Waiting for liblasi, gts, gd, ghostscript and tcl/tk
#BUILD64 = 1

BUILD_DEP_PKGS = 

RUNTIME_DEP_PKGS_CSWgraphviz = CSWexpat CSWpango CSWlibcairo CSWgts CSWlibxrender \
	CSWgs CSWfconfig CSWftype2 CSWglib2 CSWgtk2 CSWiconv \
	CSWlibatk CSWliblasi CSWzlib CSWxpm CSWlibrsvg \
	CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibintl8

RUNTIME_DEP_PKGS_CSWgraphvizdevel = CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibgraph5
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibgvpr2
RUNTIME_DEP_PKGS_CSWgraphvizdoc = 
RUNTIME_DEP_PKGS_CSWgraphvizgraphs = 
RUNTIME_DEP_PKGS_CSWgraphvizgd = CSWgd CSWjpeg CSWglib2 CSWxpm CSWftype2 CSWiconv CSWgts \
	CSWpango CSWlibintl8 CSWpng CSWfconfig CSWlibcairo CSWexpat CSWzlib \
	CSWgcc4corert CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibgraph5
RUNTIME_DEP_PKGS_CSWgraphvizdevil = CSWdevil CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizsharp = CSWmono CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizguile = CSWguile CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizjava = CSWjava CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizlua = CSWlua CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizocaml = CSWocaml CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizperl = CSWperl CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizphp = CSWphp5 CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizpython = CSWpython CSWexpat CSWzlib  CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizr = CSWr CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizruby = CSWruby CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphviztcl = CSWtcl CSWtk CSWlibcairo CSWfconfig CSWpango CSWftype2 CSWgts CSWlibintl8 \
	CSWglib2 CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibgraph5
RUNTIME_DEP_PKGS_CSWgraphviz2 = CSWgraphviz

LICENSE = COPYING

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
SPKG_DESC_CSWgraphviz2 = Stub to the CSWgraphviz package

PKGFILES_CSWgraphviz = $(bindir)/(?!(diffimg|dot_static)).*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_core\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_gdk_pixbuf\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_gs\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_gtk\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_lasi\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_pango\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_rsvg\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_xlib\.so\..*
PKGFILES_CSWgraphviz += $(libdir)/graphviz/libgvplugin_.*layout\.so\..*
PKGFILES_CSWgraphviz += $(sharedstatedir)/graphviz/lefty/.* 
PKGFILES_CSWgraphviz += $(mandir)/man1/.*\.1
PKGFILES_CSWgraphviz += $(mandir)/man7/.*\.7

PKGFILES_CSWgraphvizdevel = $(libdir)/pkgconfig/.*\.pc
PKGFILES_CSWgraphvizdevel += $(libdir)/lib.*\.so
PKGFILES_CSWgraphvizdevel += $(includedir)/.*\.h
PKGFILES_CSWgraphvizdevel += $(mandir)/man3/.*\.3

PKGFILES_CSWgraphvizdoc = $(sharedstatedir)/graphviz/doc/.*

PKGFILES_CSWgraphvizgraphs = $(sharedstatedir)/graphviz/graphs/.* 

PKGFILES_CSWgraphvizgd = $(libdir)/graphviz/libgvplugin_gd\.so\..*
PKGFILES_CSWgraphvizgd += $(bindir)/diffimg
PKGFILES_CSWgraphvizgd += $(bindir)/dot_static

PKGFILES_CSWgraphvizdevil = $(libdir)/graphviz/libgvplugin_devil\.so\..*

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

PKGFILES_CSWgraphviz2 = $(prefix)/graphviz2

# Shared libraries
PACKAGES += CSWlibcdt5
CATALOGNAME_CSWlibcdt5 = libcdt5
PKGFILES_CSWlibcdt5 += $(call baseisadirs,$(libdir),libcdt\.so\.5\.0\.0)
PKGFILES_CSWlibcdt5 += $(call baseisadirs,$(libdir),libcdt\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibcdt5 += Graph Visualization Tools, libcdt.so.5
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWlibcdt5 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibcdt5 += CSWgcc4corert

PACKAGES += CSWlibcgraph6
CATALOGNAME_CSWlibcgraph6 = libcgraph6
PKGFILES_CSWlibcgraph6 += $(call baseisadirs,$(libdir),libcgraph\.so\.6\.0\.0)
PKGFILES_CSWlibcgraph6 += $(call baseisadirs,$(libdir),libcgraph\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibcgraph6 += Graph Visualization Tools, libcgraph.so.6
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWlibcgraph6 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibcgraph6 += CSWgcc4corert

PACKAGES += CSWlibgraph5
CATALOGNAME_CSWlibgraph5 = libgraph5
PKGFILES_CSWlibgraph5 += $(call baseisadirs,$(libdir),libgraph\.so\.5\.0\.0)
PKGFILES_CSWlibgraph5 += $(call baseisadirs,$(libdir),libgraph\.so\.5(\.\d+)*)
SPKG_DESC_CSWlibgraph5 += Graph Visualization Tools, libgraph.so.5
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgraph5
RUNTIME_DEP_PKGS_CSWlibgraph5 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibgraph5 += CSWgcc4corert

PACKAGES += CSWlibgvc6
CATALOGNAME_CSWlibgvc6 = libgvc6
PKGFILES_CSWlibgvc6 += $(call baseisadirs,$(libdir),libgvc\.so\.6\.0\.0)
PKGFILES_CSWlibgvc6 += $(call baseisadirs,$(libdir),libgvc\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibgvc6 += Graph Visualization Tools, libgvc.so.6
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWzlib
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWexpat
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWgcc4corert

PACKAGES += CSWlibgvpr2
CATALOGNAME_CSWlibgvpr2 = libgvpr2
PKGFILES_CSWlibgvpr2 += $(call baseisadirs,$(libdir),libgvpr\.so\.2\.0\.0)
PKGFILES_CSWlibgvpr2 += $(call baseisadirs,$(libdir),libgvpr\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibgvpr2 += Graph Visualization Tools, libgvpr.so.2
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgvpr2
RUNTIME_DEP_PKGS_CSWlibgvpr2 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibgvpr2 += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWlibgvpr2 += CSWgcc4corert

PACKAGES += CSWlibpathplan4
CATALOGNAME_CSWlibpathplan4 = libpathplan4
PKGFILES_CSWlibpathplan4 += $(call baseisadirs,$(libdir),libpathplan\.so\.4\.0\.0)
PKGFILES_CSWlibpathplan4 += $(call baseisadirs,$(libdir),libpathplan\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibpathplan4 += Graph Visualization Tools, libpathplan.so.4
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWlibpathplan4 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibpathplan4 += CSWgcc4corert

PACKAGES += CSWlibxdot4
CATALOGNAME_CSWlibxdot4 = libxdot4
PKGFILES_CSWlibxdot4 += $(call baseisadirs,$(libdir),libxdot\.so\.4\.0\.0)
PKGFILES_CSWlibxdot4 += $(call baseisadirs,$(libdir),libxdot\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibxdot4 += Graph Visualization Tools, libxdot.so.4
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWlibxdot4 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibxdot4 += CSWgcc4corert

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWgraphviz.postinstall
DISTFILES += CSWgraphvizgd.postinstall CSWgraphvizgd.postuninstall
DISTFILES += CSWgraphvizdevil.postinstall CSWgraphvizdevil.postuninstall

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-sfdp
CONFIGURE_ARGS += --without-smyrna
CONFIGURE_ARGS += --with-gtk
CONFIGURE_ARGS += --with-gdk-pixbuf
CONFIGURE_ARGS += --with-ghostscript
CONFIGURE_ARGS += --with-lasi
CONFIGURE_ARGS += --without-ipsepcola
CONFIGURE_ARGS += --with-rsvg
CONFIGURE_ARGS += --disable-ruby
CONFIGURE_ARGS += --disable-devil
CONFIGURE_ARGS += --disable-java
CONFIGURE_ARGS += --disable-lua
CONFIGURE_ARGS += --disable-ocaml
CONFIGURE_ARGS += --disable-php
CONFIGURE_ARGS += --disable-r
CONFIGURE_ARGS += --enable-static --enable-shared
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += "PANGOCAIRO_CFLAGS=`pkg-config --cflags pangocairo`"


EXTRA_LD_FLAGS = -lm

STRIP_LIBTOOL=1

TEST_SCRIPTS =

# It's a known problem with the tcl library.
CHECKPKG_OVERRIDES_CSWgraphviztcl += file-with-bad-content

# checkpkg can't detect a dependency on CSWmono
CHECKPKG_OVERRIDES_CSWgraphvizsharp += surplus-dependency|CSWmono

# /usr/local references from the docs are allright
CHECKPKG_OVERRIDES_CSWgraphvizdoc += file-with-bad-content

include gar/category.mk

post-merge:
	gln -s . $(PKGROOT)$(prefix)/graphviz2
	@$(MAKECOOKIE)
