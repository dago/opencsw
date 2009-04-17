GARNAME = ss5
GARVERSION = 3.6.7-1
CATEGORIES = lib

DESCRIPTION = A SOCKS server that implements SOCKS v4 and v5 protocol
define BLURB
	SS5 is a socks server that implements the SOCKS v4 and v5 protocol. 
	As a proxy server, SS5 authenticates, profiles and processes network 
	requests for clients. It establishes connections to application 
	hosts for client applications. When the client attempts to access 
	the network, the client connects to the SS5 daemon instead of the 
	application host.
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

DISTNAME = $(GARNAME)-$(shell gecho $(GARVERSION) |gsed -e 's/-[0-9]//')

PACKAGES = CSWss5
CATALOGNAME_CSWss5 = ss5
SPKG_DESC_CSWss5 = $(DESCRIPTION)

#REQUIRED_PKGS_CSWss5  = 

# We define upstream file regex so we can be notifed of 
# new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*(-\d)*).tar.bz2

GARCOMPILER = GNU
TEST_SCRIPTS = skip

test-skip:
	@$(DONADA)

#BUILD64 = 1
#NO_ISAEXEC = 1

prefix = $(DESTDIR)

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --with-configfile=/opt/csw/etc/ss5/ss5.conf
CONFIGURE_ARGS += --with-passwordfile=/opt/csw/etc/ss5/ss5.passwd
CONFIGURE_ARGS += --with-logfile=/opt/csw/var/log/ss5/ss5.log
CONFIGURE_ARGS += --with-profilepath=/opt/csw/etc/ss5
CONFIGURE_ARGS += --with-libpath=/opt/csw/lib
CONFIGURE_ARGS += --with-tracepath=/opt/csw/var/log/ss5

CONFIGURE_ARGS += --with-confpathbase=/opt/csw/etc
CONFIGURE_ARGS += --with-binpathbase=/opt/csw/sbin
CONFIGURE_ARGS += --with-docpathbase=/opt/csw/share/doc
CONFIGURE_ARGS += --with-manpathbase=/opt/csw/man
CONFIGURE_ARGS += --with-logpathbase=/opt/csw/var/log/ss5
CONFIGURE_ARGS += --with-tracepathbase=/opt/csw/var/log/ss5

post-install-modulated:
	@(gcp downlad/ss5.init $(DESTDIR)/etc/init.d/ss5

include gar/category.mk
