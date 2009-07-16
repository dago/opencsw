# Uses an undocumented ioctl interface, limited binary compatibility.
# Build from Solaris 8 works on Solaris 8 & 9, Solaris 10 needs separate build
GARNAME = tcpdrop
GARVERSION = 1.4
CATEGORIES = net

DESCRIPTION = Tool to drop TCP sessions
define BLURB
endef

MASTER_SITES = http://shrike.submonkey.net/~ceri/util/tcpdrop-solaris/
DISTFILES = $(GARNAME)-solaris.tar.gz
DISTNAME = tcpdrop-solaris
SPKG_SOURCEURL = http://typo.submonkey.net/pages/tcpdrop-solaris
LICENSE = $(WORKSRC)/README

CONFIGURE_SCRIPTS =
INSTALL_SCRIPTS = custom
TEST_SCRIPTS = 

NORUNPATH = 1

include gar/category.mk

install-custom: DOCDEST=$(DESTDIR)$(docdir)/$(GARNAME)
install-custom:
	mkdir -p $(DOCDEST)
	cp $(FILEDIR)/changelog.CSW $(WORKSRC)/README $(DOCDEST)
	cp $(WORKSRC)/OPENSOLARIS.LICENSE $(DOCDEST)/CDDL
	ginstall -Dm 755 $(WORKSRC)/tcpdrop $(DESTDIR)$(bindir)/tcpdrop
	@$(MAKECOOKIE)
