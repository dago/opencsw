NAME = Net-UCP
VERSION = 0.41
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = NEMUX

DESCRIPTION = Perl extension for EMI UCP Protocol
define BLURB
  Perl extension for EMI - UCP Protocol
endef

MODDIST = $(NAME)-$(VERSION).tgz

PACKAGES = CSWpm-net-ucp
CATALOGNAME = pm_net_ucp

DISTFILES += LICENSE
ARCHALL = 1

LICENSE = LICENSE

RUNTIME_DEP_PKGS_CSWpmnetucp = CSWpm-net-ucp-common
RUNTIME_DEP_PKGS_CSWpmnetucp = CSWpm-net-ucp-inttimeout
RUNTIME_DEP_PKGS_CSWpmnetucp = CSWpm-net-ucp-transactionmanager

include gar/category.mk
