NAME = pound
VERSION = 2.6
CATEGORIES = net
GARTYPE = v2

DESCRIPTION = Reverse proxy load balancer
define BLURB
  The Pound program is a reverse proxy, load balancer and HTTPS front-end for
  Web server(s). Pound was developed to enable distributing the load among
  several Web-servers and to allow for a convenient SSL wrapper for those Web
  servers that do not offer it natively. Pound is distributed under the GPL -
  no warranty, it's free to use, copy and give away.
endef

MASTER_SITES = http://www.apsis.ch/pound/
DISTNAME = Pound-$(VERSION)
DISTFILES += $(DISTNAME).tgz

# adjust log/run files
PATCHFILES  = patch-pound.h
PATCHFILES += patch-pound.8

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

VENDOR_URL = http://www.apsis.ch/pound/

LICENSE = GPL.txt

RUNTIME_DEP_PKGS += CSWlibssl-dev
RUNTIME_DEP_PKGS += CSWlibcurl-dev

PACKAGES += CSWpound
SPKG_DESC_CSWpound = Reverse proxy load balancer
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWpound += CSWlibpcreposix0
RUNTIME_DEP_PKGS_CSWpound += CSWlibssl1-0-0
OBSOLETED_BY_CSWpound = CSWpound2

# This is just for example scripts
CHECKPKG_OVERRIDES_CSWpound2 += missing-dependency|CSWpython

EXTRA_DOCS += README
EXTRA_DOCS += FAQ
EXTRA_DOCS += CHANGELOG
EXTRA_DOCS += z2_2_5_1.py
EXTRA_DOCS += z2_2_6_1.py

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-super
CONFIGURE_ARGS += --enable-msdav
CONFIGURE_ARGS += --with-maxbuf=8192
CONFIGURE_ARGS += --with-ssl=$(prefix)

# No test suite available
TEST_SCRIPTS =

# use a custom install
INSTALL_SCRIPTS = custom extra-docs

PRESERVECONF = $(sysconfdir)/pound.cfg

include gar/category.mk

install-custom: 
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -m 555 $(WORKSRC)/pound $(DESTDIR)$(sbindir)/pound
	ginstall -m 555 $(WORKSRC)/poundctl $(DESTDIR)$(sbindir)/poundctl
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall -m 644 $(WORKSRC)/pound.8 $(DESTDIR)$(mandir)/man8/pound.8
	ginstall -m 644 $(WORKSRC)/poundctl.8 $(DESTDIR)$(mandir)/man8/poundctl.8
	ginstall -d $(DESTDIR)$(sysconfdir)/$(NAME)
	ginstall -m 644 $(FILEDIR)/pound2-sample.cfg $(DESTDIR)$(sysconfdir)/pound.cfg

install-extra-docs:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 644 $(addprefix $(WORKSRC)/,$(EXTRA_DOCS)) $(DESTDIR)$(docdir)/$(NAME)
	@$(MAKECOOKIE)
