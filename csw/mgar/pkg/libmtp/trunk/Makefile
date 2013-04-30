# $Id$

NAME	=	libmtp
VERSION	=	1.1.6
GARTYPE	=	v2

DESCRIPTION	=	A LGPL library implementation of the Media Transfer Protocol
define BLURB
  A LGPL library implementation of the Media Transfer Protocol (MTP),
  a superset of the Picture Transfer Protocol (PTP).
endef

MASTER_SITES=	$(SF_MIRRORS)
DISTFILES	=	$(DISTNAME).tar.gz

GARCOMPILER		=	GNU
EXTRA_INC		=	/usr/sfw/include
EXTRA_LDFLAGS	=	-L/usr/sfw/lib -R/usr/sfw/lib -lusb
CONFIGURE_ARGS	=	$(DIRPATHS)
CONFIGURE_ARGS	+=	--enable-doxygen

PACKAGES							+=	CSWlibmtp-utils
CATALOGNAME_CSWlibmtp-utils			=	libmtp_utils
SPKG_DESC_CSWlibmtp-utils			=	$(DESCRIPTION), utilities
RUNTIME_DEP_PKGS_CSWlibmtp-utils	+=	CSWlibmtp9
CHECKPKG_OVERRIDES_CSWlibmtp-utils	+=	bad-rpath-entry|/usr/sfw/lib

PACKAGES					+=	CSWlibmtp9
CATALOGNAME_CSWlibmtp9		=	libmtp9
PKGFILES_CSWlibmtp9			+=	$(call baseisadirs,$(libdir),libmtp\.so\.9\.1\.0)
PKGFILES_CSWlibmtp9			+=	$(call baseisadirs,$(libdir),libmtp\.so\.9(\.\d+)*)
SPKG_DESC_CSWlibmtp9		+=	$(DESCRIPTION), libmtp.so.9
RUNTIME_DEP_PKGS_CSWlibmtp9	+=	CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibmtp9	+=	CSWlibiconv2
RUNTIME_DEP_PKGS_CSWlibmtp9	+=	CSWlibgcrypt11

PACKAGES							+=	CSWlibmtp-dev
CATALOGNAME_CSWlibmtp-dev			=	libmtp_dev
SPKG_DESC_CSWlibmtp-dev				+=	$(DESCRIPTION), development files
PKGFILES_CSWlibmtp-dev				+=	/opt/csw/lib/libmtp.so
PKGFILES_CSWlibmtp-dev				+=	$(PKGFILES_DEVEL)
ARCHALL_CSWlibmtp-dev				=	1
RUNTIME_DEP_PKGS_CSWlibmtp-dev		+=	CSWlibmtp9
CHECKPKG_OVERRIDES_CSWlibmtp-dev	+=	archall-devel-package

PACKAGES						+=	CSWlibmtp-doc
CATALOGNAME_CSWlibmtp-doc		=	libmtp_doc
SPKG_DESC_CSWlibmtp-doc			+=	$(DESCRIPTION), documentation
PKGFILES_CSWlibmtp-doc			+=	/opt/csw/share/doc/$(NAME)_doc/html/.*
ARCHALL_CSWlibmtp-doc			=	1

include gar/category.mk

post-install-modulated: pkgdocdir = $(docdir)/$(NAME)
post-install-modulated:
	ginstall --directory --mode=u=rwx,go=rx $(DESTDIR)$(pkgdocdir)_doc
	mv $(DESTDIR)/$(pkgdocdir)-$(VERSION)/html $(DESTDIR)/$(pkgdocdir)_doc
	rm -rf $(DESTDIR)$(pkgdocdir)-$(VERSION)
	$(MAKECOOKIE)
