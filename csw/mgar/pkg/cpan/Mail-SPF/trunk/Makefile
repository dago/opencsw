GARNAME = Mail-SPF
GARVERSION = 2.007
CATEGORIES = cpan
AUTHOR = JMEHNLE

DISTNAME = $(GARNAME)-v$(GARVERSION)
MODDIST = $(DISTNAME).tar.gz

DESCRIPTION = Perl extension for Sender Policy Framework
define BLURB
endef

PACKAGES = CSWpmmailspf
CATALOGNAME = pm_mailspf

# Required packages due to bug reports
#   http://www.opencsw.org/mantis/view.php?id=4139
#   http://www.opencsw.org/mantis/view.php?id=4140
RUNTIME_DEP_PKGS = CSWpmversion CSWpmnetaddrip

ARCHALL = 1

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
EXTRA_PERLBUILD_INSTALL_ARGS = --install_path sbin=$(sbindir)
INSTALL_SCRIPTS = $(WORKSRC)/Build

EXTRA_PAX_ARGS = '-s,spfquery,spfquery-cpan,p'
EXTRA_PAX_ARGS += '-s,spfd,spfd-cpan,p'

include gar/category.mk
