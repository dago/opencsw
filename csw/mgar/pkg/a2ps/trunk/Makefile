# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = a2ps
VERSION = 4.13
SPKG_VERSION = 4.13b
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Any to PostScript filter
define BLURB
  Any to PostScript filter
endef

MASTER_SITES = http://ftp.gnu.org/pub/gnu/a2ps/
DISTFILES  = $(NAME)-$(VERSION)b.tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

include gar/category.mk

#
PRESERVECONF = /opt/csw/etc/a2ps-site.cfg
PRESERVECONF = /opt/csw/etc/a2ps.cfg

#RUNTIME_DEP_PKGS += 
RUNTIME_DEP_PKGS_CSWa2ps += CSWggettextrt
RUNTIME_DEP_PKGS_CSWa2ps += CSWemacscommon

