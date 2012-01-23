# $Id$
NAME = liburiparser
VERSION = 0.7.5
CATEGORIES = lib

DESCRIPTION = RFC 3986 Compliant URI Parsing Library
define BLURB
endef

SF_PROJ = uriparser
MASTER_SITES = $(SF_MIRROR)
DISTNAME = $(SF_PROJ)-$(VERSION)
DISTFILES  = $(DISTNAME).tar.lzma

PATCHFILES = 0001-Remove-superflous-extension-breaking-install-with-th.patch

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

BUILD_DEP_PKGS = CSWlibcpptestdevel

PACKAGES = CSWliburiparser1 CSWliburiparserdevel

CATALOGNAME_CSWliburiparser1 = liburiparser1
CATALOGNAME_CSWliburiparserdevel = liburiparser_devel

SPKG_DESC_CSWliburiparser1 = $(DESCRIPTION) Runtime
SPKG_DESC_CSWliburiparserdevel = $(DESCRIPTION) Development Files

RUNTIME_DEP_PKGS_CSWliburiparserdevel = CSWliburiparser1
CHECKPKG_OVERRIDES_CSWliburiparserdevel += surplus-dependency|CSWliburiparser1

BUILD64_LIBS_ONLY = 1
CONFIGURE_SCRIPTS  = $(WORKSRC)/configure
CONFIGURE_SCRIPTS += $(WORKSRC)/doc/configure

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --docdir=$(docdir)/$(NAME)

PKGFILES_CSWliburiparser1 = $(PKGFILES_RT)

include gar/category.mk
