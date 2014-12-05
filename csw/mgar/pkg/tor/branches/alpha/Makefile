# $Id$
NAME = tor
VERSION = 0.2.6.1-alpha
GARTYPE = v2

DESCRIPTION = Secure network traffic router
define BLURB
Basically tor provides a distributed network of servers (onion routers). Users bounce their TCP streams (web traffic, ftp, ssh, etc) around the routers, and recipients, observers, and even the routers themselves have difficulty tracking the source of the stream.uter
def# This is where the source git repo is located but we are building from the
# official alpha release tar.gz distfile downloaded from MATER_SITES.
# GIT_REPOS = git://git.torproject.org/tor.gitefine BLURB
endef

MASTER_SITES = http://www.torproject.org/dist/
DISTFILES  = $(DPATCHFILES += 0001-add-test-to-detect-we-are-on-Solaris.patch(DISTNAME).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

VENDOR_URL = http://www.torproject.org
LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWtor += CSWlibevent2-0-5
RUNTIME_DEP_PKGS_CSWtor += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWtor += CSWlibz1

sysconfdir = /etc/opt/csw
CONFIGURE_ARGS = $(DIRPATHS)

EXTRA_PAX_ARGS = -s ',/torrc\.sample,/torrc.CSW,p'

PRESERVECONF += $(sysconfdir)/tor/tor-tsocks.conf
PRESERVECONF += $(sysconfdir)/tor/torrc

MIGRATE_FILES += tor/tor-tsocks.conf
MIGRATE_FILINITSMF = /etc/opt/csw/init.d/cswtorILUSERGROUP = /etc/opt/csw/pkg/CSWtor/cswusergroupILES += tor/torrc

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include
post-install-modulated:

	# Copy SMF script
	ginstall -Dm 755 $(FILEDIR)/cswtor \
		$(DESTDIR)/etc/opt/csw/init.d/cswtor

	# Copy README.CSW to docs
	ginstall -m 444 $(FILEDIR)/README.CSW \
		$(DESTDIR)/opt/csw/share/doc/tor/

	# Copy cswusergroup
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWtor
	ginstall -m 444 $(FILEDIR)/cswusergroup \
		$(DESTDIR)/etc/opt/csw/pkg/CSWtor/

	@$(MAKECOOKIE)
