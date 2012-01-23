NAME = loudmouth
VERSION = 1.4.3
CATEGORIES = net

DESCRIPTION = The Loudmouth XMPP API for Jabber
define BLURB
  Loudmouth is a lightweight and easy-to-use C library for programming
  with the XMPP protocol. It's designed to be easy to get started with and
  yet extensible to let you do anything the XMPP protocol allows.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGES += CSWloudmouth
CATALOGNAME_CSWloudmouth = loudmouth
SPKG_DESC_CSWloudmouth = $(DESCRIPTION)
PKGFILES_CSWloudmouth = $(PKGFILES_RT)
RUNTIME_DEP_PKGS_CSWloudmouth += CSWgcrypt
RUNTIME_DEP_PKGS_CSWloudmouth += CSWggettextrt
RUNTIME_DEP_PKGS_CSWloudmouth += CSWglib2
RUNTIME_DEP_PKGS_CSWloudmouth += CSWgnutls
RUNTIME_DEP_PKGS_CSWloudmouth += CSWgpgerr
RUNTIME_DEP_PKGS_CSWloudmouth += CSWlibidn
RUNTIME_DEP_PKGS_CSWloudmouth += CSWlibtasn1

PACKAGES += CSWloudmouth-dev
CATALOGNAME_CSWloudmouth-dev = loudmouth_dev
SPKG_DESC_CSWloudmouth-dev = Development Files for Loudmouth XMPP
RUNTIME_DEP_PKGS_CSWloudmouth-dev = CSWloudmouth-dev

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://groups.google.com/group/loudmouth-dev/web/download-loudmouth
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

VENDOR_URL = http://groups.google.com/group/loudmouth-dev

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-glibtest

# Unit tests need check http://check.sourceforge.net/
TEST_SCRIPTS = 

include gar/category.mk

post-install-modulated: EXTRA_DOCS = NEWS AUTHORS CONTRIBUTORS
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(WORKSRC)/, $(EXTRA_DOCS)) $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	$(MAKECOOKIE)
