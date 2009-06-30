GARNAME = pound
GARVERSION = 1.10
CATEGORIES = net

DESCRIPTION = reverse proxy load balancer
define BLURB
  The Pound program is a reverse proxy, load balancer and HTTPS front-end for
  Web server(s). Pound was developed to enable distributing the load among
  several Web-servers and to allow for a convenient SSL wrapper for those Web
  servers that do not offer it natively. Pound is distributed under the GPL -
  no warranty, it's free to use, copy and give away.
  As of release 1.0 Pound is declared to be production-quality code.
endef

MASTER_SITES = http://www.apsis.ch/pound/
DISTFILES  = Pound-$(GARVERSION).tgz
DISTNAME   = Pound-$(GARVERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

# we require
REQUIRED_PKGS = CSWosslrt

# patch conf/pid directory to fit our needs
PATCHFILES  = patch-pound.h
PATCHFILES += patch-pound.8
# remove linux specific logfacility
PATCHFILES += patch-config.c

# configure args
CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-super
CONFIGURE_ARGS += --enable-msdav
CONFIGURE_ARGS += --with-maxbuf=8192
CONFIGURE_ARGS += --with-ssl=$(prefix)

# No test suite available
TEST_SCRIPTS =

# use a custom install
INSTALL_SCRIPTS = custom docs

include gar/category.mk

install-custom: 
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -m 555 $(WORKSRC)/pound $(DESTDIR)$(sbindir)/pound
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall -m 644 $(WORKSRC)/pound.8 $(DESTDIR)$(mandir)/man8/pound.8
	ginstall -d $(DESTDIR)$(sysconfdir)/$(GARNAME)
	ginstall -m 644 $(FILEDIR)/pound-sample.cfg $(DESTDIR)$(sysconfdir)/$(GARNAME)
	ginstall -d $(DESTDIR)/var/opt/csw/run

docs-list  = $(WORKSRC)/README
docs-list += $(WORKSRC)/FAQ
docs-list += $(WORKSRC)/z2_2_5_1.py
docs-list += $(WORKSRC)/z2_2_6_1.py
install-docs:
	ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@( for file in $(docs-list) ; do \
                ginstall -m 644 $$file $(DESTDIR)$(docdir)/$(GARNAME) ; \
                        done )
	@$(MAKECOOKIE)
