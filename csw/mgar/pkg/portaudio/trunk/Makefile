# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = portaudio
VERSION = 19_20111121
GARTYPE = v2
CATEGORIES = utils

DESCRIPTION = Portable cross-platform audio I/O
define BLURB
endef

MASTER_SITES = http://www.portaudio.com/archives/
DISTFILES  = pa_stable_v$(VERSION).tgz

DISTNAME = $(NAME)

PACKAGES += CSWmypkg
SPKG_DESC_CSWmypkg = My package
PKGFILES_CSWmypkg += $(call pkgfiles_lib,libabc.so.1)
PKGFILES_CSWmypkg += $(call baseisadirs,$(bindir),myexec)
PKGFILES_CSWmypkg += $(sysconfdir)/myconf

CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk

