# $Id$

NAME = abcm2ps
VERSION = 8.2.2
GARTYPE = v2

DESCRIPTION = Convert ABC to music sheet in PostScript or SVG

VENDOR_URL = http://moinejf.free.fr/

MASTER_SITES = http://moinejf.free.fr/
DISTFILES  = $(DISTNAME).tar.gz

# abcm2ps comes with homegrown configure script and Makefile. Following
# patchset replaces this with simple autotools build. Upstream author (J-FM)
# wasn't interested in merging this change, most likely due to perceived
# complexity of autotools.
#
# As a result, maintaining this package will suck. Every time upstream changes
# their build script, this patch will stop applying cleanly and you'll need to
# figure out what has changed and adjust autotools patch. Alternatively, you
# can try modifying original homegrown build system to work with Solaris or
# convince upstream author to merge this patch. Both of those have been
# attempted before, and failed. You have been warned.
#
# --Maciej, 2014-09-12

PATCHFILES += 0005-Add-a-smoke-test.patch
PATCHFILES += 0006-subs.c-includes-config.h-to-get-HAVE_PANGO.patch
PATCHFILES += 0007-Add-Makefile.am-and-configure.ac.patch
PATCHFILES += 0008-Add-standard-GNU-project-files.patch

GARCOMPILER = GNU

CONFIGURE_ARGS = $(DIRPATHS)

RUNTIME_DEP_PKGS_CSWabcm2ps += CSWlibpango1-0-0
RUNTIME_DEP_PKGS_CSWabcm2ps += CSWlibpangoft2-1-0-0
RUNTIME_DEP_PKGS_CSWabcm2ps += CSWlibfreetype6
RUNTIME_DEP_PKGS_CSWabcm2ps += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWabcm2ps += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWabcm2ps += CSWlibpangocairo1-0-0

# libintl18 is only linked on sparc
RUNTIME_DEP_PKGS_CSWabcm2ps_sparc += CSWlibintl8
RUNTIME_DEP_PKGS_CSWabcm2ps += $(RUNTIME_DEP_PKGS_CSWabcm2ps_$(GARCH))

include gar/category.mk

pre-configure:
	(cd $(WORKSRC); rm -f Makefile Makefile.in configure configure.in config.h)
	(cd $(WORKSRC); autoreconf -fi)
	@$(MAKECOOKIE)
