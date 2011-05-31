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

LICENSE = COPYING

GARCOMPILER = GCC4

PATCHFILES += configure.patch
PATCHFILES += Makefile.am.patch
PATCHFILES += trapezoid.c.patch
PATCHFILES += post_process.c.patch
PATCHFILES += gvpr_Makefile.am.patch
PATCHFILES += gv_Makefile.am.patch

INCOMPATIBLE_PKGS = CSWgraphvis
# defer for some time to allow CSWgraphviz2 upgrades
# INCOMPATIBLE_PKGS = CSWgraphviz2

# Waiting for liblasi, gts, gd, ghostscript and tcl/tk
#BUILD64 = 1

BUILD_DEP_PKGS = 

# This is a compatibility package which should go away after some time.
# It only contains a link to CSWgraphviz.
PACKAGES += CSWgraphviz2
SPKG_DESC_CSWgraphviz2 = Stub to the CSWgraphviz package
RUNTIME_DEP_PKGS_CSWgraphviz2 = CSWgraphviz
PKGFILES_CSWgraphviz2 = $(prefix)/graphviz2
ARCHALL_CSWgraphviz2 = 1

PACKAGES += CSWgraphviz
SPKG_DESC_CSWgraphviz = Graph Visualization Tools
RUNTIME_DEP_PKGS_CSWgraphviz = CSWexpat
RUNTIME_DEP_PKGS_CSWgraphviz += CSWpango
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgraphviz += CSWgts
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibxrender
RUNTIME_DEP_PKGS_CSWgraphviz += CSWgs
RUNTIME_DEP_PKGS_CSWgraphviz += CSWfconfig
RUNTIME_DEP_PKGS_CSWgraphviz += CSWftype2
RUNTIME_DEP_PKGS_CSWgraphviz += CSWglib2
RUNTIME_DEP_PKGS_CSWgraphviz += CSWgtk2
RUNTIME_DEP_PKGS_CSWgraphviz += CSWiconv
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibatk
RUNTIME_DEP_PKGS_CSWgraphviz += CSWliblasi
RUNTIME_DEP_PKGS_CSWgraphviz += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphviz += CSWxpm
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibrsvg
RUNTIME_DEP_PKGS_CSWgraphviz += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphviz += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibintl8
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

PACKAGES += CSWgraphvizdevel
SPKG_DESC_CSWgraphvizdevel = Graphviz Headers etc. for development

RUNTIME_DEP_PKGS_CSWgraphvizdevel = CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibgraph5
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWgraphvizdevel += CSWlibgvpr2
PKGFILES_CSWgraphvizdevel = $(libdir)/pkgconfig/.*\.pc
PKGFILES_CSWgraphvizdevel += $(libdir)/lib.*\.so
PKGFILES_CSWgraphvizdevel += $(includedir)/.*\.h
PKGFILES_CSWgraphvizdevel += $(mandir)/man3/.*\.3

PACKAGES += CSWgraphvizdoc
SPKG_DESC_CSWgraphvizdoc = Graphviz documentation
ARCHALL_CSWgraphvizdoc = 1
RUNTIME_DEP_PKGS_CSWgraphvizdoc = 
PKGFILES_CSWgraphvizdoc = $(sharedstatedir)/graphviz/doc/.*

PACKAGES += CSWgraphvizgraphs
SPKG_DESC_CSWgraphvizgraphs = Graphviz example graphs
ARCHALL_CSWgraphvizgraphs = 1
RUNTIME_DEP_PKGS_CSWgraphvizgraphs = 
PKGFILES_CSWgraphvizgraphs = $(sharedstatedir)/graphviz/graphs/.* 

PACKAGES += CSWgraphvizgd
SPKG_DESC_CSWgraphvizgd = Graphviz renderers using gd
RUNTIME_DEP_PKGS_CSWgraphvizgd = CSWgd
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWjpeg
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWglib2
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWxpm
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWftype2
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWiconv
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWgts
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWpango
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWpng
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWfconfig
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibgraph5
PKGFILES_CSWgraphvizgd = $(libdir)/graphviz/libgvplugin_gd\.so\..*
PKGFILES_CSWgraphvizgd += $(bindir)/diffimg
PKGFILES_CSWgraphvizgd += $(bindir)/dot_static

#PACKAGES += CSWgraphvizdevil
SPKG_DESC_CSWgraphvizdevil = Graphviz renderers using DevIL
RUNTIME_DEP_PKGS_CSWgraphvizdevil = CSWdevil
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWgraphviz
PKGFILES_CSWgraphvizdevil = $(libdir)/graphviz/libgvplugin_devil\.so\..*

PACKAGES += CSWgraphvizsharp
SPKG_DESC_CSWgraphvizsharp = Graphviz language binding for C#
RUNTIME_DEP_PKGS_CSWgraphvizsharp = CSWmono
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWlibxdot4
PKGFILES_CSWgraphvizsharp = $(libdir)/graphviz/sharp/.*
PKGFILES_CSWgraphvizsharp += $(mandir)/man3/.*\.3sharp
PKGFILES_CSWgraphvizsharp += $(sharedstatedir)/graphviz/demo/.*\.cs

PACKAGES += CSWgraphvizguile
SPKG_DESC_CSWgraphvizguile = Graphviz language binding for guile
RUNTIME_DEP_PKGS_CSWgraphvizguile = CSWguile
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibxdot4
PKGFILES_CSWgraphvizguile = $(libdir)/graphviz/guile/.*
PKGFILES_CSWgraphvizguile += $(mandir)/man3/.*\.3guile
PKGFILES_CSWgraphvizguile += $(sharedstatedir)/graphviz/demo/.*\.guile

#PACKAGES += CSWgraphvizjava
SPKG_DESC_CSWgraphvizjava = Graphviz language binding for java
RUNTIME_DEP_PKGS_CSWgraphvizjava = CSWjava
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWgraphviz
PKGFILES_CSWgraphvizjava = $(libdir)/graphviz/java/.*
PKGFILES_CSWgraphvizjava += $(mandir)/man3/.*\.3java
PKGFILES_CSWgraphvizjava += $(sharedstatedir)/graphviz/demo/.*\.java

#PACKAGES += CSWgraphvizlua
SPKG_DESC_CSWgraphvizlua = Graphviz language binding for lua
RUNTIME_DEP_PKGS_CSWgraphvizlua = CSWlua
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWgraphviz
PKGFILES_CSWgraphvizlua = $(libdir)/graphviz/lua/.*
PKGFILES_CSWgraphvizlua += $(mandir)/man3/.*\.3lua
PKGFILES_CSWgraphvizlua += $(sharedstatedir)/graphviz/demo/.*\.lua

#PACKAGES += CSWgraphvizocaml
SPKG_DESC_CSWgraphvizocaml = Graphviz language binding for ocaml
RUNTIME_DEP_PKGS_CSWgraphvizocaml = CSWocaml
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWgraphviz
PKGFILES_CSWgraphvizocaml = $(libdir)/graphviz/ocaml/.*
PKGFILES_CSWgraphvizocaml += $(mandir)/man3/.*\.3ocaml
PKGFILES_CSWgraphvizocaml += $(sharedstatedir)/graphviz/demo/.*\.ml

PACKAGES += CSWgraphvizperl
SPKG_DESC_CSWgraphvizperl = Graphviz language binding for perl
RUNTIME_DEP_PKGS_CSWgraphvizperl = CSWperl
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibxdot4
PKGFILES_CSWgraphvizperl = $(libdir)/graphviz/perl/.*
PKGFILES_CSWgraphvizperl += $(mandir)/man3/.*\.3perl
PKGFILES_CSWgraphvizperl += $(sharedstatedir)/graphviz/demo/.*\.pl

#PACKAGES += CSWgraphvizphp
SPKG_DESC_CSWgraphvizphp = Graphviz language binding for php
RUNTIME_DEP_PKGS_CSWgraphvizphp = CSWphp5
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWgraphviz
PKGFILES_CSWgraphvizphp = $(libdir)/graphviz/php/.*
PKGFILES_CSWgraphvizphp += $(mandir)/man3/.*\.3php
PKGFILES_CSWgraphvizphp += $(sharedstatedir)/graphviz/demo/.*\.php

PACKAGES += CSWgraphvizpython
SPKG_DESC_CSWgraphvizpython = Graphviz language binding for python
RUNTIME_DEP_PKGS_CSWgraphvizpython = CSWpython
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibpython2-6-1-0
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibxdot4
PKGFILES_CSWgraphvizpython = $(libdir)/graphviz/python/.*
PKGFILES_CSWgraphvizpython += $(mandir)/man3/.*\.3python
PKGFILES_CSWgraphvizpython += $(sharedstatedir)/graphviz/demo/.*\.py

#PACKAGES += CSWgraphvizr
SPKG_DESC_CSWgraphvizr = Graphviz language binding for R
RUNTIME_DEP_PKGS_CSWgraphvizr = CSWr
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWgraphviz
PKGFILES_CSWgraphvizr = $(libdir)/graphviz/R/.*
PKGFILES_CSWgraphvizr += $(mandir)/man3/.*\.3r
PKGFILES_CSWgraphvizr += $(sharedstatedir)/graphviz/demo/.*\.r

#PACKAGES += CSWgraphvizruby
SPKG_DESC_CSWgraphvizruby = Graphviz language binding for ruby
RUNTIME_DEP_PKGS_CSWgraphvizruby = CSWruby
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWgraphviz
PKGFILES_CSWgraphvizruby = $(libdir)/graphviz/ruby/.*
PKGFILES_CSWgraphvizruby += $(mandir)/man3/.*\.3ruby
PKGFILES_CSWgraphvizruby += $(sharedstatedir)/graphviz/demo/.*\.rb

PACKAGES += CSWgraphviztcl
SPKG_DESC_CSWgraphviztcl = Graphviz language binding for tcl
RUNTIME_DEP_PKGS_CSWgraphviztcl = CSWtcl
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWtk
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibcairo
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWfconfig
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWpango
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWftype2
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWgts
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibintl8 
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWglib2
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWexpat
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibgraph5
PKGFILES_CSWgraphviztcl = $(libdir)/graphviz/tcl/.*
PKGFILES_CSWgraphviztcl += $(mandir)/man3/.*\.3tcl
PKGFILES_CSWgraphviztcl += $(mandir)/man3/.*\.3tk
PKGFILES_CSWgraphviztcl += $(sharedstatedir)/graphviz/demo/.*\.tcl
PKGFILES_CSWgraphviztcl += $(sharedstatedir)/graphviz/demo/.*\.tcl.README
PKGFILES_CSWgraphviztcl += $(sharedstatedir)/graphviz/demo/pathplan_data/.*

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
