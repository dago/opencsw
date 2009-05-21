GARNAME = httping
GARVERSION = 1.3.0
CATEGORIES = net

DESCRIPTION = Httping is like 'ping' but for http-requests.
define BLURB
  Httping is like 'ping' but for http-requests.  Give it an url, and it'll
  show you how long it takes to connect, send a request and retrieve the
  reply (only the headers). Be aware that the transmission across the
  network also takes time! 
endef

MASTER_SITES = http://www.vanheusden.com/httping/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz

REQUIRED_PKGS = CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tgz

PATCHFILES = gar-base.diff

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

CONFIGURE_ARGS = $(DIRPATHS)

LICENSE = license.txt

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(docdir)/$(GARNAME)
	@cp $(FILEDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)
