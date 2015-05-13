# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = libasr
VERSION = 201505061057
GARTYPE = v2

DESCRIPTION = libasr is a free, simple and portable asynchronous resolver library.
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
DISTFILES  = $(DISTNAME).tar.gz

ifneq ($(GAROSREL),11)
PATCHFILES += 0001-add-openbsd-compat-getifaddrs.c.patch
endif
PATCHFILES += 0002-fix-possible-MAX-redefinition.patch

GARCOMPILER = GNU

PACKAGES += CSWlibasr
CATALOGNAME_CSWlibasr = libasr
PKGFILES_CSWlibasr += $(call baseisadirs,$(libdir),libasr\.so(\.\d+)*)
SPKG_DESC_CSWlibasr += $(DESCRIPTION), libasr.so

PACKAGES += CSWlibasr-dev
CATALOGNAME_CSWlibasr-dev = libasr_dev
SPKG_DESC_CSWlibasr-dev += $(DESCRIPTION), development files
RUNTIME_DEP_PKGS_CSWlibasr-dev += CSWlibasr

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-mantype=man

include gar/category.mk

ifneq ($(GAROSREL),11)
# ifaddrs.h    taken from https://java.net/projects/solaris/sources/on-src/content/usr/src/head/ifaddrs.h?raw=true
# getifaddrs.c taken from https://java.net/projects/solaris/sources/on-src/content/usr/src/lib/libsocket/inet/getifaddrs.c?raw=true
# libsocket_priv.h is a gruik hack
pre-build-modulated:
	cp $(FILEDIR)/openbsd-compat/ifaddrs.h $(WORKSRC)/openbsd-compat/
	cp $(FILEDIR)/openbsd-compat/getifaddrs.c $(WORKSRC)/openbsd-compat/
	cp $(FILEDIR)/openbsd-compat/libsocket_priv.h $(WORKSRC)/openbsd-compat/
	@$(MAKECOOKIE)
endif
