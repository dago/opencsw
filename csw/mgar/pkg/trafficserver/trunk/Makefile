# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = trafficserver
VERSION = 3.2.3
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server.
define BLURB
  Apache Traffic Server is fast, scalable and extensible HTTP/1.1 compliant caching proxy server
endef

MASTER_SITES = http://people.apache.org/~igalic/releases
DISTFILES  = $(DISTNAME).tar.bz2

PACKAGING_PLATFORMS = solaris10-i386
BUILD64_ONLY = 1
ISAEXEC = 1

# this breaks, since its introduction, so disable it (for now)
LINKER_MAPS = 

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/$(NAME)
CONFIGURE_ARGS += --libexecdir=$(libexecdir)/$(NAME)
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-tcl=$(libdir)
CONFIGURE_ARGS += --with-zlib=$(prefix)
CONFIGURE_ARGS += --with-pcre=$(prefix)
CONFIGURE_ARGS += --with-lzma=$(prefix)
CONFIGURE_ARGS += --with-expat=$(prefix)
CONFIGURE_ARGS += --enable-hwloc
CONFIGURE_ARGS += --disable-silent-rules

PROTOTYPE_MODIFIERS += data
PROTOTYPE_FILES_data += $(sysconfdir)/?.*
PROTOTYPE_FILES_data += $(datadir)/?.*
PROTOTYPE_USER_data = nobody
PROTOTYPE_GROUP_data = nobody

STRIP_LIBTOOL = 1

GARCOMPILER = SOS12U3

RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibz1
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibtcl8-5
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibpcre1
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWstlport                                                                                                                                                                 
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibhwloc5
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibexpat1                                                                                                                                                                   
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWtrafficserver += CSWliblzma5

include gar/category.mk

PATH := /opt/csw/gnu:$(PATH)

pre-configure-modulated:
	cd $(WORKSRC) && /opt/csw/bin/perl -p -i -e 's|.*/usr/local/lib.*||' configure.ac
	cd $(WORKSRC) && /opt/csw/bin/autoreconf -if
	@$(MAKECOOKIE)
