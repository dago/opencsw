# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = netatalk
VERSION = 3.0.1
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Brief description
define BLURB
  Long description
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(DISTNAME).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386
GARCOMPILER = GNU

PACKAGES += CSWlibatalk1
CATALOGNAME_CSWlibatalk1 = libatalk1
PKGFILES_CSWlibatalk1 += $(call baseisadirs,$(libdir),libatalk\.so\.1\.0\.0)
PKGFILES_CSWlibatalk1 += $(call baseisadirs,$(libdir),libatalk\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibatalk1 += $(DESCRIPTION), libatalk.so.1
RUNTIME_DEP_PKGS_CSWlibatalk1 += CSWlibiconv2

PACKAGES += CSWetatalk
SPKG_DESC_CSWetatalk = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWnetatalk += CSWlibatalk1


# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS) --disable-static --with-ssl-dir=/opt/csw --with-bdb=/opt/csw/bdb47 --with-libiconv=/opt/csw --disable-tcp-wrappers --disable-silent-rules --with-libevent-header=/opt/csw/include --with-libevent-lib=/opt/csw/lib

#EXTRA_LINKER_FLAGS = -levent

include gar/category.mk

