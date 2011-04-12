NAME = less
VERSION = 443
CATEGORIES = utils

DESCRIPTION = Less is a free, open-source file pager
define BLURB
  Less is a free, open-source file pager. It can be found on most
  versions of Linux, Unix and Mac OS, as well as on many other operating systems.
endef

MASTER_SITES = http://www.greenwoodsoftware.com/$(NAME)/
DISTFILES = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

RUNTIME_DEP_PKGS_CSWless += CSWncurses
RUNTIME_DEP_PKGS_CSWless += CSWlibintl8

NOISALIST = 1
CONFIGURE_ARGS = $(DIRPATHS)

# There is no testsuite
TEST_TARGET =

# We replaced the problematic occurrence of sysless in post-install, the remaining one is just
# a default.
CHECKPKG_OVERRIDES_CSWless += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/less.1

include gar/category.mk

post-install-modulated:
	perl -pi -e 's,/usr/local/etc/sysless,$(sysconfdir)/sysless,g' \
		$(DESTDIR)$(mandir)/man1/less.1
