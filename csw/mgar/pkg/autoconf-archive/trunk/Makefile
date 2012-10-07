# $Id: Makefile 13420 2011-02-20 21:04:03Z bdwalton $
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = autoconf-archive
VERSION = 2012.09.08
GARTYPE = v2
CATEGORIES = devel
ARCHALL = 1

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DESCRIPTION = Collection of macros for GNU Autoconf
define BLURB
  The GNU Autoconf Archive is a collection of more than 450 macros for GNU Autoconf that have been contributed as free software by friendly supporters of the cause from all over the Internet.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(DISTNAME).tar.xz
DISTFILES += changelog.CSW

# File name regex to get notifications about upstream software releases
# NOTE: Use this only if the automatic regex creation
#       does not work for your package
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.xz

# If the url used to check for software update is different of MASTER_SITES, then
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES =

CHECKPKG_OVERRIDES_CSWautoconf-archive += file-with-bad-content|
CHECKPKG_OVERRIDES_CSWautoconf-archive += surplus-dependency|CSWautoconf

RUNTIME_DEP_PKGS = CSWautoconf

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

post-merge:
	if [ -d $(PKGROOT)$(datadir)/autoconf-archive ] ; then \
		mv $(PKGROOT)$(datadir)/autoconf-archive/* $(PKGROOT)$(docdir)/autoconf_archive/ ; \
		rmdir $(PKGROOT)$(datadir)/autoconf-archive ; \
	fi
	@$(MAKECOOKIE) 
