NAME = Mail-SPF
VERSION = 2.007
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = JMEHNLE

DISTNAME = $(NAME)-v$(VERSION)
MODDIST = $(DISTNAME).tar.gz

DESCRIPTION = Perl extension for Sender Policy Framework
define BLURB
endef

PACKAGES = CSWpmmailspf
CATALOGNAME = pm_mailspf

LICENSE = LICENSE

# Required packages due to bug reports
#   http://www.opencsw.org/mantis/view.php?id=4139
#   http://www.opencsw.org/mantis/view.php?id=4140
DEP_PKGS = CSWpmversion CSWpmnetaddrip

# One more required package due to bug report
#   https://www.opencsw.org/mantis/view.php?id=4623
DEP_PKGS += CSWpmerror

ARCHALL = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
EXTRA_PERLBUILD_INSTALL_ARGS = --install_path sbin=$(sbindir)
INSTALL_SCRIPTS = $(WORKSRC)/Build

EXTRA_PAX_ARGS = '-s,spfquery,spfquery-cpan,p'
EXTRA_PAX_ARGS += '-s,spfd,spfd-cpan,p'

include gar/category.mk
