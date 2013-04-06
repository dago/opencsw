NAME = pound2
VERSION = 2.4.5
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

MASTER_SITES = http://www.apsFILES  = Pound-$(VERSION).tgz
DISTNAME   = Pound-$(VERSION)

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tgz

# we require
RUNTIME_DEP_PKGS = CSWlibssl1-0-0 CSWlibpcreposix0

# This is just for example scripts we can ignore it
CHECKPKG_OVERRIDES_CSWpound2 += missing-dependency|CSWpython

# These are harmless reference located in doc or man files
CHECKPKG_OVERRIDES_CSWpound2 += file-with-bad-content|/usr/local|root/opt/csw/share/doc/pound2/README
CHECKPKG_OVERRIDES_CSWpound2 += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/pound2.8
CS += z2_2_6_1.py

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-super
CONFIGURE_ARGS += --enable-msdav
CONFIGURE_ARGS += --with-maxbuf=8192
CONFIGURE_ARGS += --with-DISTNAME).tgz

# adjust log/run files
PATCHFILES  = patch-pound.h
PATCHFILES +# Patch taken from upstream to compile against libssl 1.0.0
PATCHFILES = openssl1.0.0.patchenh-ssl=$(prefix)

# No test suite available
TEST_SCRIPTS =

# use a custom install
INSTALL_docsonfdir)/pound.cfg

include gar/category.mk

install-custom: 
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -m 555 $(WORKSRC)/pound $(DESTDIR2
	ginstall -m 555 $(WORKSRC)/poundctl $(DESTDIR)$(sbindir)/pound2)$(sbindir)/poundctl
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall -m 644 $(WORKSRC)/pound.8 $(DESTDIR)$(m2.8
	ginstall -m 644 $(WORKSRC)/poundctl.8 $(DESTDIR)$(mandir)/man8/pound2andir)/man8/poundctl.8
	ginstall -d $(DESTDIR)$(sysconfdir)/$(NAME)
	ginstall -m 644 $(FILEDIR)/pound2-sample.cfg $(DESTD$(NAME)
	ginstall -d $(DESTDIR)/var/opt/csw/run

docs-list  = $(WORKSRC)/README
docs-list += $(WORKSRC)/FAQ
docs-list += $(WORKSRC)/CHANGELOG
docs-list += $(WORKSRC)/z2_2_5_1.py
docs-list += $(WORKSRC)/z2_2_6_1.py
install-docs:
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@( for file in $(docs-list) ; do \
		ginstall -m 644 $$file $(DESTDIR)$(docdir)/$(NAME) ; \
			done )
	@$(MAKECOOKIE)
