GARNAME = libnids
GARVERSION = 1.23
CATEGORIES = net

DESCRIPTION = implementation of an e-component of network intrusion detection
define BLURB
 Libnids is a library that provides a functionality of one of NIDS 
 (Network Intrusion Detection System) components, namely E-component. It means 
 that libnids code watches all local network traffic, cooks received datagrams 
 a bit (quite a bit ;)), and provides convenient information on them to 
 analyzing modules of NIDS.
endef

SF_PROJ = $(GARNAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

SPKG_SOURCEURL = http://libnids.sourceforge.net/

REQUIRED_PKGS += CSWggettextrt CSWglib2 CSWlibnet CSWlibpcap

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=92215
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES  = Makfile.in.diff
PATCHFILES += checksum.c.diff
PATCHFILES += configure.diff
PATCHFILES += ip_options.c.diff
PATCHFILES += utils.c.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

TEST_TARGET = 

include gar/category.mk
