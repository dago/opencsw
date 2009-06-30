GARNAME = pound2
GARVERSION = 2.4.5
CATEGORIES = net

DESCRIPTION = reverse proxy load balancer
define BLURB
  The Pound program is a reverse proxy, load balancer and HTTPS front-end for
  Web server(s). Pound was developed to enable distributing the load among
  several Web-servers and to allow for a convenient SSL wrapper for those Web
  servers that do not offer it natively. Pound is distributed under the GPL -
  no warranty, it's free to use, copy and give away.
endef

MASTER_SITES = http://www.apsis.ch/pound/
DISTFILES  = Pound-$(GARVERSION).tgz
DISTNAME   = Pound-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

# we require
REQUIRED_PKGS = CSWosslrt CSWpcrert

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-super
CONFIGURE_ARGS += --enable-msdav
CONFIGURE_ARGS += --with-maxbuf=8192
CONFIGURE_ARGS += --with-ssl=$(prefix)

# adjust log/run files
PATCHFILES  = patch-pound.h
PATCHFILES += patch-pound.8

# No test suite available
TEST_SCRIPTS =

# use a custom install
INSTALL_SCRIPTS = custom docs

include gar/category.mk

install-custom: 
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -m 555 $(WORKSRC)/pound $(DESTDIR)$(sbindir)/pound2
	ginstall -m 555 $(WORKSRC)/poundctl $(DESTDIR)$(sbindir)/pound2ctl
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall -m 644 $(WORKSRC)/pound.8 $(DESTDIR)$(mandir)/man8/pound2.8
	ginstall -m 644 $(WORKSRC)/poundctl.8 $(DESTDIR)$(mandir)/man8/pound2ctl.8
	ginstall -d $(DESTDIR)$(sysconfdir)/$(GARNAME)
	ginstall -m 644 $(FILEDIR)/pound2-sample.cfg $(DESTDIR)$(sysconfdir)/$(GARNAME)
	ginstall -d $(DESTDIR)/var/opt/csw/run

docs-list  = $(WORKSRC)/README
docs-list += $(WORKSRC)/FAQ
docs-list += $(WORKSRC)/CHANGELOG
docs-list += $(WORKSRC)/z2_2_5_1.py
docs-list += $(WORKSRC)/z2_2_6_1.py
install-docs:
	ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@( for file in $(docs-list) ; do \
		ginstall -m 644 $$file $(DESTDIR)$(docdir)/$(GARNAME) ; \
			done )
	@$(MAKECOOKIE)
