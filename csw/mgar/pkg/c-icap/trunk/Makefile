# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = c-icap
VERSION = 0.1.7
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = Brief description
define BLURB
  C-ICAP is an implementation of an ICAP server. It can be used with HTTP proxies that support the ICAP protocol to implement content adaptation and filtering services. 
endef

SF_PROJ = c-icap
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = c_icap-$(VERSION).tar.gz
WORKSRC = $(WORKDIR)/c_icap-$(VERSION)
LICENSE_TEXT = Licensed under LGPL2

GARCOMPILER = GNU

sysconfdir = /etc$(prefix)/$(NAME)
CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)
CONFIGURE_ARGS += --localstatedir=/var$(prefix)/$(NAME)
CONFIGURE_ARGS += --libexecdir=$(prefix)/libexec/$(NAME)
CONFIGURE_ARGS += --libdir=$(prefix)/lib

REINPLACEMENTS = sockdir
REINPLACE_MATCH_sockdir = /var/run/c-icap
REINPLACE_WITH_sockdir = /var$(prefix)/$(NAME)/run
REINPLACE_FILES_sockdir += Makefile.in
REINPLACE_FILES_sockdir += c-icap.conf.in
REINPLACE_FILES_sockdir += c-icap-config
REINPLACE_FILES_sockdir += c-icap-libicapapi-config
REINPLACE_FILES_sockdir += cfg_param.c
REINPLACE_FILES_sockdir += docs/man/Makefile.in
REINPLACE_FILES_sockdir += docs/man/c-icap.8.in
REINPLACE_FILES_sockdir += docs/man/Makefile.am
REINPLACE_FILES_sockdir += utils/Makefile.in

REINPLACEMENTS += usrlocal
REINPLACE_MATCH_usrlocal = /usr/local/c-icap/etc
REINPLACE_WITH_usrlocal = $(sysconfdir)
REINPLACE_FILES_usrlocal += c-icap.conf
REINPLACE_FILES_usrlocal += c-icap.conf.in

PACKAGES = CSWc-icap
CATALOGNAME_CSWc-icap = c_icap
SPKG_DESC_CSWc-icap = C-ICAP library
RUNTIME_DEP_PKGS_CSWc-icap += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWc-icap += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWc-icap += CSWlibz1

PACKAGES += CSWlibicapapi0
CATALOGNAME_CSWlibicapapi0 = libicapapi0
PKGFILES_CSWlibicapapi0 += $(call baseisadirs,$(libdir),libicapapi\.so\.0\.0\.7)
PKGFILES_CSWlibicapapi0 += $(call baseisadirs,$(libdir),libicapapi\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibicapapi0 += $(DESCRIPTION), libicapapi.so.0
RUNTIME_DEP_PKGS_CSWc-icap += CSWlibicapapi0
RUNTIME_DEP_PKGS_CSWlibicapapi0 += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibicapapi0 += CSWlibz1

PACKAGES += CSWc-icap-dev
CATALOGNAME_CSWc-icap-dev = c_icap_dev
SPKG_DESC_CSWc-icap-dev += $(DESCRIPTION), development files
PKGFILES_CSWc-icap-dev += /opt/csw/lib/libicapapi.so
PKGFILES_CSWc-icap-dev += $(PKGFILES_DEVEL)
RUNTIME_DEP_PKGS_CSWc-icap-dev += CSWlibicapapi0

include gar/category.mk

