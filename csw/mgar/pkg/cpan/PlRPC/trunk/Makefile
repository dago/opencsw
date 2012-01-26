NAME = PlRPC
VERSION = 0.2020
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = MNOONING

DESCRIPTION = Perl extension for writing perl RPC servers and clients
define BLURB
endef

# Good thing the locations have standards. But why have a standard when
# people don't use it? :-(
MASTER_SITES = $(addsuffix $(NAME)/,$(CPAN_MIRRORS))
DISTNAME = $(NAME)

DISTFILES = COPYING

PACKAGES = CSWpmplrpc
CATALOGNAME = pm_plrpc

ARCHALL = 1

include gar/category.mk
