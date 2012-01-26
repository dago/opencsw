NAME = rapidsvn
VERSION = 0.12.0-1
SPKG_VERSION = $(subst -,.,$(VERSION))
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GUI front-end for the Subversion revision system
define BLURB
  This is the developer site for RapidSVN. You have access to the source code
  of RapidSVN, the issue tracker and the mailing lists. If you are a user of
  RapidSVN you might want to take a look at http://www.rapidsvn.org where we
  are working on the Documentation and Online Help of RapidSVN
endef

MASTER_SITES = http://www.rapidsvn.org/download/release/0.12/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
# DISTFILES += $(call admfiles,CSWrapidsvn,depend prototype)
# DISTFILES += $(call admfiles,CSWsvncpp,depend prototype)

PATCHFILES  = 0001-Use-explicit-constructor-for-wxString.patch
PATCHFILES += 0002-Make-sure-to-pass-norunpath-through-libtool.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

PACKAGES = CSWrapidsvn CSWlibsvncpp3

CATALOGNAME_CSWrapidsvn = rapidsvn
CATALOGNAME_CSWlibsvncpp3 = libsvncpp3

SPKG_DESC_CSWrapidsvn = $(DESCRIPTION)
SPKG_DESC_CSWlibsvncpp3 = Subversion C++ language binding

SPKG_SOURCEURL = http://rapidsvn.tigris.org/

BUILD_DEP_PKGS = CSWsvn-devel CSWapache2-devel

RUNTIME_DEP_PKGS_CSWrapidsvn += CSWwxwidgetscommon
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWoldaprt
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWapr
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWwxwidgetsgtk2
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWexpat
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWbdb48
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWncurses
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWapr-util
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWsunmath
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWiconv
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWlibsvncpp3
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWsvn

BUILD_DEP_PKGS += CSWdocbookxsl
DOCBOOK_MANPAGE = $(sharedstatedir)/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl

APR_CONFIG = $(bindir)/apr-1-config
APU_CONFIG = $(bindir)/apu-1-config
SVNLIBDIR = $(libdir)/svn

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr-config=$(APR_CONFIG)
CONFIGURE_ARGS += --with-apu-config=$(APU_CONFIG)
CONFIGURE_ARGS += --with-svn-lib=$(SVNLIBDIR)
CONFIGURE_ARGS += --with-svn-include=$(includedir)
CONFIGURE_ARGS += --with-docbook-xsl-manpages=$(DOCBOOK_MANPAGE)

# This must match the apr bdb binding. We need this to make sure
# libdb.so is found at the correct place.
EXTRA_LIB = $(SVNLIBDIR) $(prefix)/bdb48/lib

PKGFILES_CSWlibsvncpp3 = $(PKGFILES_RT)
PKGFILES_CSWlibsvncpp3 += $(PKGFILES_DEVEL)

# We don't have a devel package
CHECKPKG_OVERRIDES_CSWlibsvncpp3 += shared-lib-package-contains-so-symlink|file=/opt/csw/lib/libsvncpp.so

include gar/category.mk

post-install-modulated:
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall $(WORKSRC)/doc/manpage/rapidsvn.1 $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)

