GARNAME = ldapvi
GARVERSION = 1.7
CATEGORIES = utils

DESCRIPTION = Interactive LDAP client for Unix terminals
define BLURB
  ldapvi is an interactive LDAP client for Unix terminals.
  Using it, you can update LDAP entries with a text editor.
  Think of it as vipw(1) for LDAP.
endef

MASTER_SITES = http://www.lichteblau.com/download/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWldapvi,depend)

PATCHFILES = patch-putenv.diff

PREREQUISITE_PKGS = CSWoldapdevel

CONFIGURE_ARGS = $(DIRPATHS)

INSTALL_SCRIPTS = custom

SPKG_SOURCEURL = http://www.lichteblau.com/ldapvi/

include gar/category.mk

install-custom:
	ginstall -d $(DESTDIR)$(bindir) $(DESTDIR)$(mandir)/man1 $(DESTDIR)$(sharedstatedir)/doc/$(GARNAME)
	cd $(WORKSRC) && ginstall -m 755 ldapvi $(DESTDIR)$(bindir)
	cd $(WORKSRC) && ginstall -m 644 ldapvi.1 $(DESTDIR)$(mandir)/man1
	cd $(WORKSRC) && ginstall -m 644 manual/manual.css manual/manual.xml manual/bg.png manual/html.xsl \
		$(DESTDIR)$(sharedstatedir)/doc/$(GARNAME)

