NAME = Net-Daemon
VERSION = 0.43
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MNOONING

DESCRIPTION = Perl extension for portable daemons
define BLURB
endef

# Good thing the locations have standards. But why have a standard when
# people don't use it? :-(
MASTER_SITES = $(addsuffix $(NAME)/,$(CPAN_MIRRORS))
DISTNAME = $(NAME)

DISTFILES = COPYING

PATCHFILES = Net-Daemon-5.10-support.patch

PACKAGES = CSWpmnetdaemon
CATALOGNAME = pm_netdaemon

ARCHALL = 1

include gar/category.mk
