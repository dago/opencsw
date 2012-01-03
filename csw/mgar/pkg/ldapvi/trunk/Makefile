NAME = ldapvi
VERSION = 1.7
CATEGORIES = utils

DESCRIPTION = Interactive LDAP client for Unix terminals
define BLURB
  ldapvi is an interactive LDAP client for Unix terminals.
  Using it, you can update LDAP entries with a text editor.
  Think of it as vipw(1) for LDAP.
endef

MASTER_SITES = http://www.lichteblau.com/download/
DISTFILES += $(DISTNAME).tar.gz
PATCHFILES += 0001-Use-putenv-instead-of-setenv.patch

VENDOR_URL = http://www.lichteblau.com/ldapvi/

BUILD_DEP_PKGS = CSWoldapdevel

PACKAGES += CSWldapvi
SPKG_DESC_CSWldapvi = Interactive LDAP client for Unix terminals
RUNTIME_DEP_PKGS_CSWldapvi += CSWlibpopt0
RUNTIME_DEP_PKGS_CSWldapvi += CSWlibintl8
RUNTIME_DEP_PKGS_CSWldapvi += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWldapvi += CSWosslrt
RUNTIME_DEP_PKGS_CSWldapvi += CSWoldaprt
RUNTIME_DEP_PKGS_CSWldapvi += CSWglib2

TEST_TARGET = test
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir) $(DESTDIR)$(mandir)/man1 $(DESTDIR)$(sharedstatedir)/doc/$(NAME)
	cd $(WORKSRC) && ginstall -m 755 ldapvi $(DESTDIR)$(bindir)
	cd $(WORKSRC) && ginstall -m 644 ldapvi.1 $(DESTDIR)$(mandir)/man1
	cd $(WORKSRC) && ginstall -m 644 manual/manual.css manual/manual.xml manual/bg.png manual/html.xsl \
		$(DESTDIR)$(sharedstatedir)/doc/$(NAME)

