NAME = icecast
VERSION = 2.3.2
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = A free server software for streaming multimedia
define BLURB
endef

MASTER_SITES = http://downloads.xiph.org/releases/icecast/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.icecast.org/

RUNTIME_DEP_PKGS = CSWlibogg CSWosslrt CSWtheora CSWvorbis CSWzlib
RUNTIME_DEP_PKGS += CSWcurlrt CSWlibidn CSWoldaprt CSWspeex
RUNTIME_DEP_PKGS += CSWiconv CSWlibnet CSWlibxml2 CSWlibxslt CSWsasl

BUILD_DEP_PKGS = $(RUNTIME_DEP_PKGS)

sysconfdir = /etc/opt/csw
localstatedir = /var/opt/csw
PRESERVECONF = $(sysconfdir)/icecast.xml

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-install-modulated:
	@ginstall -d $(DESTDIR)$(localstatedir)/log/icecast
