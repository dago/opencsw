# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = deluge
VERSION = 1.3.5
GARTYPE = v2
CATEGORIES = python

DESCRIPTION = Full-features BitTorrent client

MASTER_SITES = http://download.deluge-torrent.org/source/
DISTFILES  = $(DISTNAME).tar.lzma

# boost gxx is only available for Solaris 10
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

LICENSE = LICENSE

PACKAGES += CSWmypkg
SPKG_DESC_CSWmypkg = My package
PKGFILES_CSWmypkg += $(call pkgfiles_lib,libabc.so.1)
PKGFILES_CSWmypkg += $(call baseisadirs,$(bindir),myexec)
PKGFILES_CSWmypkg += $(sysconfdir)/myconf

GARCOMPILER = GCC4
EXTRA_INC += /opt/csw/gxx/include
EXTRA_LIB += /opt/csw/gxx/lib

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

