# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = a2ps
VERSION = 4.14
GARTYPE = v2

DESCRIPTION = Any to PostScript filter
define BLURB
  Any to PostScript filter
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES += $(DISTNAME).tar.gz

PACKAGES += CSWa2ps
SPKG_DESC_CSWa2ps = Any to PostScript filter
RUNTIME_DEP_PKGS_CSWa2ps += CSWlibintl8
RUNTIME_DEP_PKGS_CSWa2ps += CSWlibpaper1

# These are just docs
CHECKPKG_OVERRIDES_CSWa2ps += file-with-bad-content|/usr/local|root/opt/csw/share/info/a2ps.info
CHECKPKG_OVERRIDES_CSWa2ps += file-with-bad-content|/usr/local|root/opt/csw/share/emacs/site-lisp/a2ps.el
CHECKPKG_OVERRIDES_CSWa2ps += file-with-bad-content|/usr/local|root/opt/csw/share/emacs/site-lisp/a2ps.elc
CHECKPKG_OVERRIDES_CSWa2ps += file-with-bad-content|/usr/share|root/opt/csw/share/info/a2ps.info

# Just for one .el file? No.
CHECKPKG_OVERRIDES_CSWa2ps += missing-dependency|CSWemacscommon

PRESERVECONF += $(sysconfdir)/a2ps.cfg
PRESERVECONF += $(sysconfdir)/a2ps-site.cfg

MIGRATE_FILES += a2ps.cfg
MIGRATE_FILES += a2ps-site.cfg

# There is one test failing:
SKIPTEST ?= 1

include gar/category.mk



