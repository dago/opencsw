# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = znc
VERSION = 1.0
GARTYPE = v2
CATEGORIES = apps

DESCRIPTION = ZNC, an advanced IRC bouncer
define BLURB
  ZNC, an advanced IRC bouncer that is left connected so an IRC client can disconnect/reconnect without losing the chat session.
endef

VENDOR_URL = http://http://wiki.znc.in/ZNC
MASTER_SITES = http://znc.in/releases/ 
DISTFILES  = $(DISTNAME).tar.gz
Pcheck-for-and-define-timeradd-and-timersub.patch
PATCHFILES += 0002-fix-znc.1-manpage.patch
PATCHFILES += 0003-Fix-mt-libraries.patch
PATCHFILES += 0004-Use-proper-zoneinfo-path.patch
PATCHFILES += 0005-fix-man-pages.patch
LICENSE = LICENSE

# Do not create .git
NOGITPATCH = 1

PACKAGES += CSWznc
SPKG_DESC_CSWznc = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWznc += CSWlibiconvznc += CSWlibcares2
RUNTIME_DEP_PKGS_CSWznc += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWznc += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWznc += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWznc += CSWlibgnugetopt0

PACKAGES += CSWznc-dev
SPKG_DESC_CSWznc-dev += $(DESCRIPTION), development files
PKGFILES_CSWznc-dev += /opt/csw/bin/znc-buildmod
PKGFILES_CSWznc-dev += /opt/csw/bin/znc-config
PKGFILES_CSWznc-dev += /opt/csw/lib/pkgconfig/znc.pc
PKGFILES_CSWznc-dev += /opt/csw/include/znc/.*
RUNTIME_DEP_PKGS_CSWznc-dev += CSWznc
RUNTIME_DEP_PKGS_CSWznc-dev +=
# SWlibcares-dev

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i3NUGARCOMPILER = GCC4
CONFIGURE_ARCONFIGURE_ARGS += --with-openssl=/opt/csw
CONFIGURE_ARGS += --with-module-prefix=$(libexecdir)/zncRGS = $(DIRPATHS) 

# --enable-perl and --enable-python do not work. perl autotools check is broke; python module does not compile
#CONFIGURE_ARGS = $(DIRPATHS) --enable-perl --enable-python

SKIPTEST = 1

include