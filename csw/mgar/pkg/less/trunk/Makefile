NAME = less
VERSION = 451
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Less is a free, open-source file pager
define BLURB
  Less is a free, open-source file pager. It can be found on most
  versions of Linux, Unix and Mac OS, as well as on many other operating systems.
endef

MASTER_SITES = http://www.greenwoodsoftware.com/$(NAME)/
DISTFILES = $(DISTNAME).tar.gz

LICENSE = LICENSE

PACKAGES += CSWless
SPKG_DESC_CSWless = A free open-source file pager
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWless += CSWlibncursesw5

NOISALIST = 1

REINPLACEMENTS += sysless
REINPLACE_MATCH_sysless = /usr/local/etc/sysless
REINPLACE_WITH_sysless = $(sysconfdir)/sysless
REINPLACE_FILES_sysless += less.man

# There is no testsuite
TEST_TARGET =

# We reinplaced the problematic occurrence of sysless, the remaining one is just
# a default.
CHECKPKG_OVERRIDES_CSWless += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/less.1

include gar/category.mk
