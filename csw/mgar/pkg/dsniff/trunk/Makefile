NAME = dsniff
VERSION = 2.4b1
GARTYPE = v2

DESCRIPTION = A

DESCRIPTION = a collection of tools for network auditing and penetration testing
define BLURB
  dsniff is a collection of tools for network auditing and penetration testing.
	dsniff, filesnarf, mailsnarf, msgsnarf, urlsnarf, and webspy passively monitor
	a network for interesting data (passwords, e-mail, files, etc.). arpspoof,
	dnsspoof, and macof facilitate the interception of network traffic normally
	unavailable to an attacker (e.g, due to layer-2 switching). sshmitm and
	webmitm implement active monkey-in-the-middle attacks against redirected SSH
	and HTTPS sessions by exploiting weak bindings in ad-hoc PKI. 
endef

MASTER_SITES = http://www.monkey.org/~dugsong/dsniff/beta/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

DISTNAME = $(NAME)-2.4

RUNTIME_D48 CSWlibnet1 CSWlibnids1-24 CSWlibpcap1 CSWlibssl1-0-0

CHECKPKG_OVERRIDES_CSWdsniff += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/dnsspoof.8
CHECKPKG_OVERRIDES_CSWdsniff += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/dsniff.8libpcap CSWosslrt

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PATCHFIL# configure tries to detect libdb.a presence but we don't
# have it in the opencsw package, we just have libdb.so (which is fine)
PATCHFILES += 0002-fix-berkeleydb-detection.patch

# update code to be able to compile against libnet 1.1
# Patch borrowed from Debian
PATCHFILES += 07_libnet_1.1.patch

# Include Solaris <sys/ethernet.h> header
# and fix prototypes
PATCHFILES += 0004-ethernet-header-inclusion.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-db=/opt/csw/bdb48

TEST_SCRIPTS =

EXTRA_LD_OPTIONS = -L$(prefix)/lib/libnet-new/
EXTRA_LIB += $(prefix)/bdb48/lib

include gar/category.mk

# we re-run autoconf because we patched configure.in
pre-configure-modulated:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)
