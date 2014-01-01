# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
# ! Linkage of libedit.so needs a SONAME, probably libedit.so.1
# ! Package creation is missing

NAME = libedit
VERSION = 0.3
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Non-GPL replacement for readline library
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTNAME = libedit
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES += 0001-Add-definitionPATCHFILES += 0001-Honour-LDFLAGS.patch

PACKAGES += CSWlibedit1
SPKG_DESC_CSWlibedit1 = Non-GPL replacement for readline library
PKGFILES_CSWlibedit1 += $(call pkgfiles_lib,libedit.so.1)

PACKAGES += CSWlibedit-dev
SPKG_DESC_CSWlibedit-dev = Development files to libedit.so.1
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibedit-dev += CSWlibedit1n-for-sig_t.patch

BUILD64_LIBS_ONLY = 1

# The vis.h is completely different what libedit expects
EXTRA_CONFIGURE_ENV += ac_cv_header_vis_h=no

EXTRA_CFLAGS += $CFLAGS += -KpicGS += $(CPPFLAGS)
EXTRA_INC += $(includedir)/ncurses

CONFIGURE_ARGS += $(DIRPATHS)

TEST_TARGET = TEST
TE+= LDADD
TEST_OVERRIDE_VAR_LDADD = $(LDFLAGS)

INSTALL_OVERRIDE_VARS += LIBDIR INCDIR MANDIR
INSTALL_OVERRIDE_VAR_LIBDIR = $(DESTDIR)$(libdir)
INSTALL_OVERRIDE_VAR_INCDIR = $(DESTDIR)$(includedir)
INSTALL_OVERRIDE_VAR_MANDIR = $(DESTDIR)$(mandir)

include gar/category.mk

post-install:
	cd $(DESTDIR)$(libdir) && mv libedit.so libedit.so.1
	ln -s libedit.so.1 $(DESTDIR)$(libdir)/libedit.so
	@$(MAKECOOKIE)
