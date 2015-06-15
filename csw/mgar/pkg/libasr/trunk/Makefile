# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libasr
VERSION = 1.0.2
GARTYPE = v2

DESCRIPTION = A free, simple and portable asynchronous resolver library
define BLURB
 libasr is a free, simple and portable asynchronous resolver library.
 
 It allows to run dns queries and perform hostname resolutions in a fully asynchronous fashion. The implementation is thread-less, fork-less, and does not make use of signals or other "tricks" that might get in the developer's way. The API was initially developped for the OpenBSD operating system, where it is natively supported.
 
 This library is intended to bring this interface to other systems. It is originally provided as a support library for the portable version of the OpenSMTPD daemon, but it can be used in any other contexts. It is known to work on the following systems:
 
     * Linux
     * FreeBSD
     * NetBSD
     * DragonFly
     * MacOSX
 
 The primary source of information about libasr is the github repository.
endef

MASTER_SITES = http://www.opensmtpd.org/archives/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += openbsd-compat.tgz

PATCHFILES-5.10 += 0001-add-openbsd-compat-getifaddrs.c.patch
PATCHFILES += 0002-fix-possible-MAX-redefinition.patch
PATCHFILES += $(PATCHFILES-$(GAROSREL))

PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386
PACKAGING_PLATFORMS += solaris11-sparc solaris11-i386

BUILD64 = 1

PACKAGES += CSWlibasr0
PKGFILES_CSWlibasr0 += $(call pkgfiles_lib,libasr.so.0)
SPKG_DESC_CSWlibasr0 += $(DESCRIPTION), libasr.so.0

PACKAGES += CSWlibasr-dev
SPKG_DESC_CSWlibasr-dev += Development files for libasr.so.0
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlibasr-dev += CSWlibasr0

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mantype=man

include gar/category.mk

# ifaddrs.h    taken from https://java.net/projects/solaris/sources/on-src/content/usr/src/head/ifaddrs.h?raw=true
# getifaddrs.c taken from https://java.net/projects/solaris/sources/on-src/content/usr/src/lib/libsocket/inet/getifaddrs.c?raw=true
# libsocket_priv.h is a gruik hack
pre-build:
	$(if $(filter 5.10,$(GAROSREL)),cp -rp $(WORKDIR)/openbsd-compat/* $(WORKSRC)/openbsd-compat)
	@$(MAKECOOKIE)
