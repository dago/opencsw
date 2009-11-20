GARNAME = icecast
GARVERSION = 2.3.2
CATEGORIES = apps

DESCRIPTION = A free server software for streaming multimedia
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/icecast/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.icecast.org/

REQUIRED_PKGS = CSWlibogg CSWosslrt CSWtheora CSWvorbis CSWzlib
REQUIRED_PKGS += CSWcurlrt CSWlibidn CSWoldaprt CSWspeex
REQUIRED_PKGS += CSWiconv CSWlibnet CSWlibxml2 CSWlibxslt CSWsasl

PREREQUISITE_PKGS = $(REQUIRED_PKGS)

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
PRESERVECONF = $(sysconfdir)/icecast.xml

CONFIGURE_ARGS = $(DIRPATHS)

TEST_TARGET = check

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(localstatedir)/log/icecast
