NAME = rapidsvn
VERSION = 0.12.1
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = GUI front-end for the Subversion revision system
define BLURB
  This is the developer site for RapidSVN. You have access to the source code
  of RapidSVN, the issue tracker and the mailing lists. If you are a user of
  RapidSVN you might want to take a look at http://www.rapidsvn.org where we
  are working on the Documentation and Online Help of RapidSVN
endef

MASTER_SITES = http://www.rapidsvn.org/do.1/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PATCHFILES +type)

PATCHFILES  = 0001-Use-explicit-constructor-for-wxString.patc1-Do-not-strip-norunpath-on-libtool.patch
PATCHFILES += 0001-Add-missing-svncpp.dox-not-in-tarbalpath-through-libtool.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(VENDOR_URL = http://rapidsvn.tigris.org/

BUILD_DEP_PKGS += CSWsvn-dev
BUILD_DEP_PKGS += CSWapache2-dev
BUILD_DEP_PKGS += CSWdocbookxsl

PACKAGES += CSWrapidsvn
SPKG_DESC_CSWrapidsvn = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWwxwidgets
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWlibapr1-0
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWlibsvncpp3
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWsvn
RUNTIME_DEP_PKGS_CSWrapidsvn += CSWwxwidgetsgtk2

PACKAGES += CSWlibsvncpp3
SPKG_DESC_CSWlibsvncpp3 = Subversion C++ language binding
PKGFILES_CSWlibsvncpp3 += $(call pkgfiles_lib,libsvncpp.so.3)

PACKAGES += CSWlibsvncpp-dev
SPKG_DESC_CSWlibsvncpp-dev = Development files for libsvncpp.so.3
PKGFILES_CSWlibsvncpp-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWlibsvncpp-dev += CSWlibsvncpp3
GS += CSWdocbookxsl
DOCBOOK_MANPAGE = $(sharedstatedir)/sgml/docbook/xsl-stylesheets/manpages/docbook.xsl

APR_CONFIG = $(bindir)/apr-1-config
APU_CONFIG = $(bindir)/apu-1-config
SVNLIBDIEXTRA_LINKER_FLAGS += -norunpathDIR = $(libdir)/svn

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-apr-config=$(APR_CONFIG)
CONFIGURE_ARGS += --with-apu-config=$(APU_CONFIG)
CONFIGURE_ARGS += --with-svn-lib=$(SVNLIBDIR)
CONFIGURE_ARGS += --with-svn-include=$(includedir)
CONFIGURE_ARGS += --with-docbook-xsl-manpages=CONFIGURE_ARGS += --with-manpage=yes=$(DOCBOOK_MANPAGE)

# This must match the apr bdb binding. We need this to make sure
# libdb.so is found at the correct place.
EXTRA_LIB = $(SVNLIBDIR) $(include gar/category.mk

#post-install-modulated:
#	ginstall -d $(DESTDIR)$(mandir)/man1
#	ginstall $(WORKSRC)/doc/manpage/rapidsvn.1 $(DESTDIR)$(mandir)/man1
#	@$(MAKECOOKIE)

