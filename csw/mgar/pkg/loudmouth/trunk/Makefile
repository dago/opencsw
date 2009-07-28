GARNAME = loudmouth
GARVERSION = 1.4.3
CATEGORIES = net

DESCRIPTION = The Loudmouth XMPP API for Jabber
define BLURB
  Loudmouth is a lightweight and easy-to-use C library for programming
  with the XMPP protocol. It's designed to be easy to get started with and
  yet extensible to let you do anything the XMPP protocol allows.
endef

MASTER_SITES = $(GNOME_MIRROR)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://www.loudmouth-project.org/

PACKAGES = CSWloudmouth CSWloudmouthdevel
PKGFILES_CSWloudmouth = $(PKGFILES_RT)

CATALOGNAME_CSWloudmouth = loudmouth
CATALOGNAME_CSWloudmouthdevel = loudmouth_devel

REQUIRED_PKGS_CSWloudmouth = CSWgcrypt CSWggettextrt CSWglib2 CSWgnutls
REQUIRED_PKGS_CSWloudmouth += CSWgpgerr CSWlibidn CSWlibtasn1

REQUIRED_PKGS_CSWloudmouthdevel = CSWloudmouth


# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = http://groups.google.com/group/loudmouth-dev/web/download-loudmouth
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-glibtest

# Unit tests need check http://check.sourceforge.net/
TEST_SCRIPTS = 

include gar/category.mk

post-install-modulated: EXTRA_DOCS = NEWS AUTHORS CONTRIBUTORS
post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(GARNAME)
post-install-modulated:
	ginstall -d $(DOCDEST)
	cp $(addprefix $(WORKSRC)/, $(EXTRA_DOCS)) $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	$(MAKECOOKIE)
