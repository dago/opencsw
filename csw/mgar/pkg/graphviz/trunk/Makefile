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

# disable dependency checks because plugins depend on libs from base package
ENABLE_CHECK = 0

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
	CSWlibatk CSWliblasi CSWpng CSWzlib CSWxpm CSWlibrsvg \
	CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 
RUNTIME_DEP_PKGS_CSWgraphvizdevel = CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizdoc = 
RUNTIME_DEP_PKGS_CSWgraphvizgraphs = 
RUNTIME_DEP_PKGS_CSWgraphvizgd = CSWgd CSWjpeg CSWglib2 CSWxpm CSWftype2 CSWiconv CSWgts \
	CSWpango CSWlibintl8 CSWpng CSWfconfig CSWlibcairo CSWexpat CSWzlib \
	CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizdevil = CSWdevil CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizsharp = CSWmono CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizguile = CSWguile CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizjava = CSWjava CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizlua = CSWlua CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizocaml = CSWocaml CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizperl = CSWperl CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizphp = CSWphp5 CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizpython = CSWpython CSWexpat CSWzlib  CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizr = CSWr CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphvizruby = CSWruby CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphviztcl = CSWtcl CSWtk CSWlibcairo CSWfconfig CSWpango CSWftype2 CSWgts CSWlibintl8 \
	CSWglib2 CSWexpat CSWzlib CSWgcc4corert CSWgcc4g++rt CSWlibltdl7 CSWgraphviz
RUNTIME_DEP_PKGS_CSWgraphviz2 = CSWgraphviz

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
LICENSE_CSWgraphviz2 = COPYING

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
PKGFILES_CSWgraphviz += $(libdir)/lib.*\.so\..*
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

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWgraphviz.postinstall
DISTFILES += CSWgraphvizgd.postinstall CSWgraphvizgd.postuninstall
DISTFILES += CSWgraphvizdevil.postinstall CSWgraphvizdevil.postuninstall

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

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

TEST_SCRIPTS = custom

include gar/category.mk

test-custom:
	@echo " ==> Testing $(NAME) (custom)"
	@$(MAKECOOKIE)

post-merge:
	gln -s . $(PKGROOT)$(prefix)/graphviz2
	@$(MAKECOOKIE)

CHECKPKG_OVERRIDES_CSWgraphvizperl += file-with-bad-content|/usr/local|root/opt/csw/share/graphviz/demo/modgraph.pl
CHECKPKG_OVERRIDES_CSWgraphvizperl += soname-not-found|libgraph.so.4|is|needed|by|opt/csw/lib/graphviz/perl/libgv_perl.so
CHECKPKG_OVERRIDES_CSWgraphvizperl += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/perl/libgv_perl.so
CHECKPKG_OVERRIDES_CSWgraphvizperl += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/graphviz/perl/libgv_perl.so
CHECKPKG_OVERRIDES_CSWgraphvizsharp += surplus-dependency|CSWmono
CHECKPKG_OVERRIDES_CSWgraphvizsharp += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/sharp/libgv_sharp.so
CHECKPKG_OVERRIDES_CSWgraphvizsharp += soname-not-found|libgraph.so.4|is|needed|by|opt/csw/lib/graphviz/sharp/libgv_sharp.so
CHECKPKG_OVERRIDES_CSWgraphvizsharp += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/graphviz/sharp/libgv_sharp.so
CHECKPKG_OVERRIDES_CSWgraphviz2 += surplus-dependency|CSWgraphviz
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWglib2
CHECKPKG_OVERRIDES_CSWgraphvizgd += surplus-dependency|CSWgd
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWexpat
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWxpm
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWzlib
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWftype2
CHECKPKG_OVERRIDES_CSWgraphvizgd += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_gd.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWlibltdl7
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWiconv
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWgts
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWpango
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWpng
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWfconfig
CHECKPKG_OVERRIDES_CSWgraphvizgd += missing-dependency|CSWlibcairo
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWlibcairo
CHECKPKG_OVERRIDES_CSWgraphviztcl += surplus-dependency|CSWtcl
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWfconfig
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWgcc3corert|or|CSWgcc4corert
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWpango
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWftype2
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWgts
CHECKPKG_OVERRIDES_CSWgraphviztcl += file-with-bad-content|/usr/local|root/opt/csw/share/man/man3/tcldot.3tcl
CHECKPKG_OVERRIDES_CSWgraphviztcl += file-with-bad-content|/export/medusa|root/opt/csw/lib/graphviz/tcl/libtcldot.so.0.0.0
CHECKPKG_OVERRIDES_CSWgraphviztcl += file-with-bad-content|/export/medusa|root/opt/csw/lib/graphviz/tcl/libtclplan.so.0.0.0
CHECKPKG_OVERRIDES_CSWgraphviztcl += file-with-bad-content|/export/medusa|root/opt/csw/lib/graphviz/tcl/libtcldot_builtin.so.0.0.0
CHECKPKG_OVERRIDES_CSWgraphviztcl += file-with-bad-content|/export/medusa|root/opt/csw/lib/graphviz/tcl/libtkspline.so.0.0.0
CHECKPKG_OVERRIDES_CSWgraphviztcl += file-with-bad-content|/export/medusa|root/opt/csw/lib/graphviz/tcl/libgv_tcl.so
CHECKPKG_OVERRIDES_CSWgraphviztcl += soname-not-found|libgraph.so.4|is|needed|by|opt/csw/lib/graphviz/tcl/libgv_tcl.so
CHECKPKG_OVERRIDES_CSWgraphviztcl += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/tcl/libtcldot.so.0.0.0
CHECKPKG_OVERRIDES_CSWgraphviztcl += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/tcl/libgv_tcl.so
CHECKPKG_OVERRIDES_CSWgraphviztcl += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/graphviz/tcl/libgv_tcl.so
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWlibltdl7
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWexpat
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWgcc3g++rt|or|CSWgcc4g++rt
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWlibintl8
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWglib2
CHECKPKG_OVERRIDES_CSWgraphviztcl += missing-dependency|CSWzlib
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_lasi.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_pango.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/libgraph.so.5.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/libcgraph.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += file-with-bad-content|/usr/local|root/opt/csw/bin/gvpr_static
CHECKPKG_OVERRIDES_CSWgraphviz += file-with-bad-content|/usr/local|root/opt/csw/lib/libgvpr.so.2.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += non-uniform-lib-versions-in-package|sonames=libcdt.so.5,libcgraph.so.6,libgraph.so.5,libgvc.so.6,libgvpr.so.2,libpathplan.so.4,libxdot.so.4
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_neato_layout.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgraph.so.4|is|needed|by|opt/csw/lib/libgvc.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgraph.so.4|is|needed|by|opt/csw/lib/graphviz/libgvplugin_lasi.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/graphviz/libgvplugin_lasi.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libcgraph.so.5|is|needed|by|opt/csw/lib/libgvpr.so.2.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_core.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_gs.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_rsvg.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_dot_layout.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphviz += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/libgvplugin_gdk_pixbuf.so.6.0.0
CHECKPKG_OVERRIDES_CSWgraphvizpython += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/graphviz/python/libgv_python.so
CHECKPKG_OVERRIDES_CSWgraphvizpython += soname-not-found|libgraph.so.4|is|needed|by|opt/csw/lib/graphviz/python/libgv_python.so
CHECKPKG_OVERRIDES_CSWgraphvizpython += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/python/libgv_python.so
CHECKPKG_OVERRIDES_CSWgraphvizgraphs += file-with-bad-content|/usr/share|root/opt/csw/share/graphviz/graphs/directed/pmpipe.gv
CHECKPKG_OVERRIDES_CSWgraphvizdoc += file-with-bad-content|/usr/share|root/opt/csw/share/graphviz/doc/html/FAQ.html
CHECKPKG_OVERRIDES_CSWgraphvizdoc += file-with-bad-content|/usr/local|root/opt/csw/share/graphviz/doc/html/FAQ.html
CHECKPKG_OVERRIDES_CSWgraphvizdoc += file-with-bad-content|/usr/local|root/opt/csw/share/graphviz/doc/ChangeLog
CHECKPKG_OVERRIDES_CSWgraphvizdoc += file-with-bad-content|/usr/local|root/opt/csw/share/graphviz/doc/html/winbuild.html
CHECKPKG_OVERRIDES_CSWgraphvizdoc += file-with-bad-content|/usr/local|root/opt/csw/share/graphviz/doc/html/build.html
CHECKPKG_OVERRIDES_CSWgraphvizdoc += file-with-bad-content|/usr/share|root/opt/csw/share/graphviz/doc/html/info/command.html
CHECKPKG_OVERRIDES_CSWgraphvizguile += soname-not-found|libcdt.so.4|is|needed|by|opt/csw/lib/graphviz/guile/libgv_guile.so
CHECKPKG_OVERRIDES_CSWgraphvizguile += soname-not-found|libgraph.so.4|is|needed|by|opt/csw/lib/graphviz/guile/libgv_guile.so
CHECKPKG_OVERRIDES_CSWgraphvizguile += soname-not-found|libgvc.so.5|is|needed|by|opt/csw/lib/graphviz/guile/libgv_guile.so

