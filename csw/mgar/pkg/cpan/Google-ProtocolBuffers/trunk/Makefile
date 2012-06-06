# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = Google-ProtocolBuffers
VERSION = 0.08
GARTYPE = v2
CATEGORIES = cpan
AUTHOR = GARIEV

DESCRIPTION = Simple Interface To Google Protocol Buffers
define BLURB
  Simple Interface To Google Protocol Buffers
endef

MASTER_SITES = 
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += LICENSE

LICENSE = LICENSE

PACKAGES = CSWpm-google-protocolbuffers
CATALOGNAME = pm_google_protocolbuffers

RUNTIME_DEP_PKGS  = CSWpmparserecdescent
RUNTIME_DEP_PKGS += CSWpmclsaccessor

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
# UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

ARCHALL = 1

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

