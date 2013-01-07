# $Id$

NAME = libnids
VERSION = 1.24
GARTYPE = v2

DESCRIPTION = Ementation of an e-component of network intrusion detection
define BLURB
 Libnids is a library that provides a functionali
 (Network Intrusion Detection System) components, namely E-component. It means
 that libnids code watches all local network traffic, cooks received datagrams
 a bit (quite a bit ;)), and provides convenient information on them toation on them to 
 analyzing modules of NIDECTS.
endef

SF_PROJ = $(NAME)
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://libnids.sbnet CSWlibpcap

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=92215
UPS
# PATCHFILES  = Makfile.in.diff
PATCHFILES += checksum.c.diff
PATCHFILES += configure.diff
# PATCHFILES += ip_options.c.diff
# PATCHFILES += utils.c.diff
PATCHFILES += 0004-Solaris-linking-in-Makefile.in.patch
PATCHFILES += 0004-Install-into-DESTDIR.patch
PATCHFILES += 0005-Use-LDFLAGS-when-linking.patch

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --enable-shared

BUILD64 = 1

# http://wiki.opencsw.org/project-libnet
EXTRA_LINKER_FLAGS = -L$(libdir)/libnet-new

PACKAGES += CSWlibnids1-24
PKGFILES_CSWlibnids1-24 += $(call baseisadirs,$(libdir),libnids\.so\.1\.24(\.\d+)*)
SPKG_DESC_CSWlibnids1-24 += $(DESCRIPTION), libnids.so.1.24
RUNTIME_DEP_PKGS_CSWlibnids1-24 += CSWlibnet1
RUNTIME_DEP_PKGS_CSWlibnids1-24 += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWlibnids1-24 += CSWlibpcap1
RUNTIME_DEP_PKGS_CSWlibnids1-24 += CSWlibglib2-0-0

PACKAGES += CSWlibnids-dev
SPKG_DESC_CSWlibnids-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibnids-dev += CSWlibnids1-24

OBSOLETED_BY_CSWlibnids1-24 = CSWlibnids

TEST_TARGET =

include gar/category.mk
