# $Id$
#
# There is still a number of errors thrown by checkpkg; they need to be
# investigated.

NAME = graphviz
VERSION = 2.30.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Graph visualization tools 
define BLURB
    graphviz is a set of graph visualization tools and libraries. It supports
    hierarchical and mass-spring drawings; although the tools are scalable,
    their emphasis is on making very good drawings of reasonably-sized graphs.
endef

MASTER_SITES = http://www.graphviz.org/pub/graphviz/stable/SOURCES/

LICENSE = COPYING

GARCOMPILER = G0001_configure_tcl_bin_path_not_good_for_64bit.patch
PATCHFILES += 0002_configure_guile_version_detection_needs_gsed.patch
#PATCHFILES += configure.patch
#PATCHFILES += Makefile.am.patch
#PATCHFILES += trapezoid.c.patch
#PATCHFILES += post_process.c.patch
#PATCHFILES += gvpr_Makefile.am.patch
#_Makefile.am.patch
PATCHFILES += gv_Makefile.am.patch

INCOMPATIBLE_PKGS = CSWgraphvis
# defer for some time to allow CSWgraphviz2 upgrades
# INCOMPATIBLE_PKBUILD64 = 1
ISAEXEC = 1

BUILD_DEP_PKGS += CSWliblasi-dev
BUILD_DEP_PKGS += CSWlibgd-dev
BUILD_DEP_PKGS += CSWgts-dev
BUILD_DEP_PKGS += CSWghostscript-dev
BUILD_DEP_PKGS += CSWtcl-dev
BUILD_DEP_PKGS += CSWtk-dev
BUILD_DEP_PKGS += CSWswig
BUILD_DEP_PKGS += CSWlibgc-dev
BUILD_DEP_PKGS += CSWpython27-dev

BUILD_DEP_PKGS = 

# This is a compatibility package which should go away after some time.
# It only contains a link to CSWgraphviz.
PACKAGES += CSWgraphviz2
SPKG_DESC_CSWgraphviz2 = Stub to the CSWgraphviz package
PKGFILES_CSWgraphviz2 = $(prefix)/graphviz2
ARCHALL_CSWgraphviz2 = 1

PACKAGES += CSWgraphviz
SPKG_DESC_CSWgraphviz = Graph Visualization Tools
RUNTIME_DE+= CSWpangohviz += CSWlibintl8
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWvc6hviz += CSWlibgvpr2
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSrsvg2-2
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgdk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgdk-pixbuf2-0-0
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgts0-7-5
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgtk-x11-2-0-0
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgs9
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibatk1-0-0
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgraphviz += CSWlibgvpr2
PKGFILES_CSWgraphviz += $(call baseisadirs,$(bindir),(?:(?!diffimg|dot_static).)*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_core\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_gdk_pixbuf\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_gs\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_gtk\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_lasi\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_neato_layout\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_pango\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_rsvg\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_xlib\.so\..*)
PKGFILES_CSWgraphviz += $(call baseisadirs,$(libdir),graphviz/libgvplugin_.*layout\.so\..*)in_.*layout\.so\..*
PKGFILES_CSWgraphviz += $(sharedstatedir)/graphviz/lefty/.* 
PKGFILES_CSWgraphviz += $(mandir)/man1/.*\.1
PKGFILES_CSWgraphviz += $(mandir)/man7/.*\.7

PACK-dev
SPKG_DESC_CSWgraphviz-dev = Graphviz Headers etc. for development

RUNTIME_DEP_PKGS_CSWgraphviz-dev += CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphviz-dev += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphviz-dev += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphviz-dev += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphviz-dev += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphviz-dev += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWgraphviz-dev += CSWlibgvpr2
PKGFILES_CSWgraphviz-dev += $(call baseisadirs,$(libdir),pkgconfig/.*\.pc)
PKGFILES_CSWgraphviz-dev += $(call baseisadirs,$(libdir),lib.*\.so)
PKGFILES_CSWgraphviz-dev += $(includedir)/.*\.h
PKGFILES_CSWgraphviz-dev += $(mandir)/man3/.*\.3
OBSOLETED_BY_CSWgraphviz-dev = CSWgraphvizdevel(mandir)/man3/.*\.3

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
SPKG_DESC_CSWgraphvizgd = Graphviz RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibgd3
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWpango
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibz1
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibgts0-7-5
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibcairo2
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWgraphvizgd += CSWlibgvc6
PKGFILES_CSWgraphvizgd += $(call baseisadirs,$(libdir),graphviz/libgvplugin_gd\.so.*)
PKGFILES_CSWgraphvizgd += $(call baseisadirs,$(bindir),diffimg)
PKGFILES_CSWgraphvizgd += $(call baseisadirs,$(bindir),dot_static)(bindir)/dot_static

#PACKAGES += CSWgraphvizdevil
SPKG_DESC_CSWgraphvizdevil = Graphviz renderers using DevIL
RUNTIME_DEP_PKG+= CSWdevilvizdevil += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizdevil += CSWgraphviz
PKGFILES_CSWgraphvizdevil = $(libdir)/graphviz/libgvplugin_devil\.so\..*

PACKAGES += CSWgraphvizsharp
SPKG_DESC_CSWgraphvizsharp = Graphviz lan\#sharp += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphcc-s1
RUNTIME_DEP_PKGS_CSWgraphvizsharp += CSWlibcgraph6arp += CSWlibgraph5
PKGFILES_CSWgraphvizsharp = $(libdir)/graphviz/sharp/.*
PKGFILES_CSWgraphvizsharp += $(mandir)/man3/.*\.3sharp
PKGFILES_CSWgraphvizsharp += $(sharedstatedir)/gr# Nothing 64 bit there?
CHECKPKG_OVERRIDES_CSWgraphvizsharp += 64-bit-binaries-missingraphviz/demo/.*\.cs

PACKAGES += CSWgraphvizguile
SPKG_DESC_CSWgraphvizguile = Graphviz language binding for guile
RUNTIME_DEP_PKG+= CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibguile2-0-22
RUNTIME_DEP_PKGS_CSWgraphvizguile += CSWlibcgraph6ile += CSWlibgraph5
PKGFILES_CSWgraphvizguile = $(libdir)/graphviz/guile/.*
PKGFILES_CSWgraphvizguile += $(mandir)/man3/.*\.3guile
PKGFILES_CSWgraphvizguile += $(sharedstatedir)/graph# No 64 bit guile
CHECKPKG_OVERRIDES_CSWgraphvizguile += 64-bit-binaries-missinghviz/demo/.*\.guile

#PACKAGES += CSWgraphvizjava
SPKG_DESC_CSWgraphvizjava = Graphviz language binding for java
RUNTIME_DEP_PK+= CSWjavahvizjava += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizjava += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvizva += CSWlibgraph5
PKGFILES_CSWgraphvizjava = $(libdir)/graphviz/java/.*
PKGFILES_CSWgraphvizjava += $(mandir)/man3/.*\.3java
PKGFILES_CSWgraphvizjava += $(sharedstatedir)/graphviz/demo/.*\.java

#PACKAGES += CSWgraphvizlua
SPKG_DESC_CSWgraphvizlua = Graphviz language binding for lua
RUNTIME_DEP_P+= CSWluaphvizlua += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizlua += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphviua += CSWlibgraph5
PKGFILES_CSWgraphvizlua = $(libdir)/graphviz/lua/.*
PKGFILES_CSWgraphvizlua += $(mandir)/man3/.*\.3lua
PKGFILES_CSWgraphvizlua += $(sharedstatedir)/graphviz/demo/.*\.lua

#PACKAGES += CSWgraphvizocaml
SPKG_DESC_CSWgraphvizocaml = Graphviz language binding for ocaml
RUNTIME_DEP_PKG+= CSWocamlvizocaml += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizocaml += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvizoml += CSWlibgraph5
PKGFILES_CSWgraphvizocaml = $(libdir)/graphviz/ocaml/.*
PKGFILES_CSWgraphvizocaml += $(mandir)/man3/.*\.3ocaml
PKGFILES_CSWgraphvizocaml += $(sharedstatedir)/graphviz/demo/.*\.ml

PACKAGES += CSWgraphvizperl
SPKG_DESC_CSWgraphvizperl = Graphviz language binding for perl
RUNTIME_DEP_PK+= CSWperl
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgraphvizperl += CSWlibcgraph6erl += CSWlibgraph5
PKGFILES_CSWgraphvizperl = $(libdir)/graphviz/perl/.*
PKGFILES_CSWgraphvizperl += $(mandir)/man3/.*\.3perl
PKGFILES_CSWgraphvizperl += $(sharedstatedir)/gr# No 64 bit perl
CHECKPKG_OVERRIDES_CSWgraphvizperl += 64-bit-binaries-missingraphviz/demo/.*\.pl

#PACKAGES += CSWgraphvizphp
SPKG_DESC_CSWgraphvizphp = Graphviz language binding for php
RUNTIME_DEP_P+= CSWphp5phvizphp += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizphp += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphvihp += CSWlibgraph5
PKGFILES_CSWgraphvizphp = $(libdir)/graphviz/php/.*
PKGFILES_CSWgraphvizphp += $(mandir)/man3/.*\.3php
PKGFILES_CSWgraphvizphp += $(sharedstatedir)/graphviz/demo/.*\.php

PACKAGES += CSWgraphvizpython
SPKG_DESC_CSWgraphvizpython = Graphviz language binding for python
RUNTIME_DEP_PKGS+= CSWpython27
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWgraphvizpython += CSWlibgcc-s1
PKGFILES_CSWgraphvizpython += $(call baseisadirs,$(libdir),graphviz/python.*)
PKGFILES_CSWgraphvizpython += $(call baseisadirs,$(libdir),python.*)/graphviz/python/.*
PKGFILES_CSWgraphvizpython += $(mandir)/man3/.*\.3python
PKGFILES_CSWgraphvizpython += $(sharedstatedir)/gr# Keep the right Python as a dependency
CHECKPKG_OVERRIDES_CSWgraphvizpython += surplus-dependency|CSWpython27
# No 64 bit python
CHECKPKG_OVERRIDES_CSWgraphvizpython += 64-bit-binaries-missing
# Those ones should be considered
CHECKPKG_OVERRIDES_CSWgraphvizpython += pkgname-does-not-start-with-CSWpy-
CHECKPKG_OVERRIDES_CSWgraphvizpython += catalogname-does-not-start-with-py_raphviz/demo/.*\.py

#PACKAGES += CSWgraphvizr
SPKG_DESC_CSWgraphvizr = Graphviz language binding for R
RUNTIME_DEP+= CSWrraphvizr += CSWzlib
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWgcc4corert
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWgcc4g++rt
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWlibxdot4
RUNTIME_DEP_PKGS_CSWgraphvizr += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphzr += CSWlibgraph5
PKGFILES_CSWgraphvizr = $(libdir)/graphviz/R/.*
PKGFILES_CSWgraphvizr += $(mandir)/man3/.*\.3r
PKGFILES_CSWgraphvizr += $(sharedstatedir)/graphviz/demo/.*\.r

PACKAGES += CSWgraphvizruby
SPKG_DESC_CSWgraphvizruby = Graphviz language binding for ruby
RUNTIME_DEP_PK+GS_CSWgraphvizruby = CSWruby
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWlibruby18-1
RUNTIME_DEP_PKGS_CSWlibgvc6
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgraphvizruby += CSWlibcgraph6uby += CSWlibgraph5
PKGFILES_CSWgraphvizruby = $(libdir)/graphviz/ruby/.*
PKGFILES_CSWgraphvizruby += $(mandir)/man3/.*\.3ruby
PKGFILES_CSWgraphvizruby += $(sharedstatedir)/gr# No 64 bit ruby
CHECKPKG_OVERRIDES_CSWgraphvizruby += 64-bit-binaries-missingraphviz/demo/.*\.rb

PACKAGES += CSWgraphviztcl
SPKG_DESC_CSWgraphviztcl = Graphviz language binding for tcl
RUNTIME_DEP_P+= CSWlibltdl7
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWpango
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibgd3iztcl += CSWlibcdt5
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibpathplan4
RUNTIME_DEP_PKGS_CSWgrgvc6
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibz1
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibgts0-7-5
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWgraphviztcl += CSWlibcairo2
PKGFILES_CSWgraphviztcl += $(call baseisadirs,$(libdir),graphviz/tcl/.*)ir)/graphviz/tcl/.*
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
RUNTIME_DEP_PKGS_Cgcc-s1t5 += CSWgcc4corert

PACKAGES += CSWlibcgraph6
CATALOGNAME_CSWlibcgraph6 = libcgraph6
PKGFILES_CSWlibcgraph6 += $(call baseisadirs,$(libdir),libcgraph\.so\.6\.0\.0)
PKGFILES_CSWlibcgraph6 += $(call baseisadirs,$(libdir),libcgraph\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibcgraph6 += Graph Visualization Tools, libcgraph.so.6
RUNTIME_DEP_PKGS_CSWlcdt5
RUNTIME_DEP_PKGS_CSWlibcgraph6 += CSWlibgcc-s1raph5 += CSWlibcdt5

PACKAGES += CSWlibgvc6
CATALOGNAME_CSWlibgvc6 = libgvc6
PKGFILES_CSWlibgvc6 += $(call baseisadirs,$(libdir),libgvc\.so\.6\.0\.0)
PKGFILES_CSWlibgvc6 += $(call baseisadirs,$(libdir),libgvc\.so\.6(\.\d+)*)
SPKG_DESC_CSWlibgvc6 += Graph Visualization Tools, libgvc.so.6
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibltdl7
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibpathplan4
RUNTIME_DEP_PKGS_Ccdt5
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibexpat1
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWlibgvc6 += CSWlibz1vc6 += CSWlibgraph5

PACKAGES += CSWlibgvpr2
CATALOGNAME_CSWlibgvpr2 = libgvpr2
PKGFILES_CSWlibgvpr2 += $(call baseisadirs,$(libdir),libgvpr\.so\.2\.0\.0)
PKGFILES_CSWlibgvpr2 += $(call baseisadirs,$(libdir),libgvpr\.so\.2(\.\d+)*)
SPKG_DESC_CSWlibgvpr2 += Graph Visualization Tools, libgvpr.so.2
RUNTIME_DEP_PKGS_CScdt5
RUNTIME_DEP_PKGS_CSWlibgvpr2 += CSWlibcgraph6
RUNTIME_DEP_PKGS_CSWlibgvpr2 += CSWlibgcc-s12 += CSWlibcgraph6


PACKAGES += CSWlibpathplan4
CATALOGNAME_CSWlibpathplan4 = libpathplan4
PKGFILES_CSWlibpathplan4 += $(call baseisadirs,$(libdir),libpathplan\.so\.4\.0\.0)
PKGFILES_CSWlibpathplan4 += $(call baseisadirs,$(libdir),libpathplan\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibpathplan4 += Graph Visualization Tools, libpathplan.so.4
RUNTIME_DEP_PKGS_CSWlibgcc-s1n4 += CSWgcc4corert

PACKAGES += CSWlibxdot4
CATALOGNAME_CSWlibxdot4 = libxdot4
PKGFILES_CSWlibxdot4 += $(call baseisadirs,$(libdir),libxdot\.so\.4\.0\.0)
PKGFILES_CSWlibxdot4 += $(call baseisadirs,$(libdir),libxdot\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibxdot4 += Graph Visualization Tools, libxdot.so.4
RUNTIME_DEP_PKGS_CSgcc-s1t4 += CSWgcc4corert

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWgraphviz.postinstall
DISTFILES += CSWgraphvizgd.postinstall CSWgraphvizgd.postuninstall
DISTFILES += CSWgraphvizdevil.postinstall CSWgraphvizdevil.postuninstall

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-sfdp
CONFIGURE_ARGS += --without-smyrna
CONFIGURE_ARGS += --with-gtk
CONFIGqt=no_ARGS += --with-gtk
CONFIGURE_ARGS += --with-gdk-pixbuf
CONFIGURE_ARGS += --with-ghostscript
CONFIGURE_ARGS += --with-lasi
CONFIGURE_ARGS += --without-ipsepcola
CONFIGURE_ARGS += --with-rsvg
Cenable-python=no
CONFIGURE_ARGS += --enable-python27=yesARGS += --with-rsvg
CONFIGURE_ARGS += --disable-devil
CONFIGURE_ARGS += --disable-java
CONFIGURE_ARGS += --disable-lua
CONFIGURE_ARGS += --disable-ocaml
CONFIGURE_ARGS += --disable-php
CONFIGURE_ARGS += --disable-r
CONFIGURE_ARGS += --enable-static --enable-shared
CONFIGURE_ARGS += --disable-silent-rules
CONFIGURE_ARGS += "PANGOCAIRO_CFLAGS=`pkg-config --cf# Yes, configure is making silly assumption of what the CPU type can be on
# Solaris, and that's one of the things needed to properly detect tclConfig.sh
CONFIGURE_ARGS-isa-amd64   += --build=x86_64-solaris2.10
CONFIGURE_ARGS-isa-sparcv9 += --build=sparc64-sun-solaris2.10
# Also, no 64 bit perl
CONFIGURE_ARGS-isa-amd64   += --enable-perl=no 
CONFIGURE_ARGS-isa-sparcv9 += --enable-perl=no
# No 64 bit guile
CONFIGURE_ARGS-isa-amd64   += --enable-guile=no
CONFIGURE_ARGS-isa-sparcv9 += --enable-guile=no
# No 64 bit Ruby
CONFIGURE_ARGS-isa-amd64   += --enable-ruby=no
CONFIGURE_ARGS-isa-sparcv9 += --enable-ruby=no
CONFIGURE_ARGS += $(CONFIGURE_ARGS-isa-$(ISA))

EXTRA_LD_FLAGS = -lm

# Ugly, but without it, there are tons of errors with Guile
EXTRA_CXXFLAGS = -fpermissive

STRIP_LIBTOOL=1

TEST_SCRIPTS =iz/demo/modgraph.pl

#FIXME - maybe - poss false alarm? - can't find any "/usr/local" in sources
CHECKPKG_OVERRIDES_CSWlibgvpr2 += file-with-bad-content|/usr/local|root/opt/csw/lib/libgvpr.so.2.0.0
CHElibgvpr2 += file-with-bad-content|/usr/local|root/opt/csw/lib/amd64/libgvpr.so.2.0.0r/local" in sources
CHECKPKG_OVERRIDES_CSWlibgvpr2 += file-with-bad-content|/usr/locasparcv9/libgvpr.so.2.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += file-with-bad-content|/usr/local|root/opt/csw/bin/pentium_pro/gvpr_static
CHECKPKG_OVERRIDES_CSWgraphviz += file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/gvpr_static
CHECKPKG_OVERRIDES_CSWgraphviz += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/gvpr_static
CHECKPKG_OVERRIDES_CSWgraphviz += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv8plus/gvpr_static

include gar/category.mk
