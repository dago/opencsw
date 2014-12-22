NAME = openntpd
VERSION = 3.9p1
GARTYPE = v2

DESCRIPTION = OpenBSD Network Time Protocol
define BLURB
endef

MASTER_SITES = http://ftp.eu.openbsd.org/pub/OpenBSD/OpenNTPD/
DISTFILES = $(DISTNAME).tar.gz

RUNTIME_DEP_PKGS_CSWopenntpd += CSWlibssl1-0-0

INITSMF = /etc/opt/csw/init.d/cswopenntpd
USERGROUP = /etc/opt/csw/pkg/CSWopenntpd/cswusergroup
SAMPLECONF = /etc/opt/csw/ntpd.conf

GARCOMPILER = GNU

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --with-privsep-user=openntpd

# There are no tests
SKIPTEST = 1

include gar/category.mk

post-install:
	@echo " ==> Post-install of $(NAME)"
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -m 755 $(FILEDIR)/cswopenntpd $(DESTDIR)/etc/opt/csw/init.d/cswopenntpd
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWopenntpd
	ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWopenntpd/
	rm -rf $(DESTDIR)/var
