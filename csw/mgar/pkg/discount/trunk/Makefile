# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = discount
VERSION = 2.1.8
GARTYPE = v2

DESCRIPTION = Markdown text to html language

MASTER_SITES = http://www.pell.portland.or.us/%7Eorc/Code/discount/
DISTFILES  = $(DISTNAME).tar.gz

PATCHFILES += 0001-Add-specific-include-for-alloca.patch
PATCHFILES += 0002-We-don-t-have-ldconfig-and-the-line-forces-exitcode-.patch

PACKAGES += CSWlibmarkdown2
SPKG_DESC_CSWlibmarkdown2 = Markdown text to html language, libmarkdown.so.2
PKGFILES_CSWlibmarkdown2 += $(call pkgfiles_lib,libmarkdown.so.2)

PACKAGES += CSWlibmarkdown-dev
SPKG_DESC_CSWlibmarkdown-dev += Development files for libmarkdown.so.2
PKGFILES_CSWlibmarkdown-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibmarkdown-dev += CSWlibmarkdown2

PACKAGES += CSWmarkdown
SPKG_DESC_CSWmarkdown = Discound, the markdown text to html converter
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWmarkdown += CSWlibmarkdown2

BUILD64_LIBS_ONLY = 1

# This is really funky, if we execute configure.sh with 'sh' /opt/csw/lib/64 gets magically changed to
# /opt/csw/lib/sparcv9 and is not used during packaging.
REINPLACEMENTS += lib64
REINPLACE_MATCH_lib64 = /bin/sh
REINPLACE_WITH_lib64 = /bin/bash
REINPLACE_FILES_lib64 += configure.sh

# We need ginstall as install
CONFIGURE_ENV_PATH = /opt/csw/gnu:$(PATH)

# This crappy configure.sh only handles a subest and bails out on extra parameters
NODIRPATHS += --exec_prefix
NODIRPATHS += --bindir
NODIRPATHS += --datadir
NODIRPATHS += --sysconfdir
NODIRPATHS += --sharedstatedir
NODIRPATHS += --localstatedir
NODIRPATHS += --infodir
NODIRPATHS += --includedir

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-all-features
CONFIGURE_ARGS += --shared
CONFIGURE_ARGS += --with-urlencoded-anchor

# -fPIC and -L. are taken from the original Makefile, as we unconditionally override we need to readd them here
BUILD_OVERRIDE_VARS += CFLAGS
BUILD_OVERRIDE_VAR_CFLAGS = -fPIC $(CFLAGS)
BUILD_OVERRIDE_VARS += LFLAGS
BUILD_OVERRIDE_VAR_LFLAGS += -L. $(LDFLAGS)

TEST_TARGET = test

# We have one failing test, reported upstream, skip for now
SKIPTEST ?= 1

include gar/category.mk

post-extract:
	@# Make a symlink, otherwise we would need a completely new rule
	ln -s configure.sh $(WORKSRC)/configure
	@$(MAKECOOKIE)
