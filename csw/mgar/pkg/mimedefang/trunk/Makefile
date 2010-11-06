GARNAME = mimedefang
GARVERSION = 2.71
CATEGORIES = net

DESCRIPTION = Framework for filtering e-mail using Sendmail milter API, C and Perl
define BLURB
  Framework for filtering e-mail using Sendmail milter API, C and Perl
endef

MASTER_SITES = http://www.mimedefang.com/static/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

UPSTREAM_MASTER_SITES = http://www.mimedefang.com/static/
UFILES_REGEX = (\d+(?:\.\d+)*)

RUNTIME_DEP_PKGS += CSWperl CSWsendmail CSWlibmilter
RUNTIME_DEP_PKGS += CSWpmmimetools CSWpmiostringy
RUNTIME_DEP_PKGS += CSWpmmimebase64 CSWpmmailtools
RUNTIME_DEP_PKGS += CSWpmdigestsha1 CSWpmhtmlparser

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-sendmail=/opt/csw/lib/sendmail
CONFIGURE_ARGS += --with-milterinc=/opt/csw/include
CONFIGURE_ARGS += --with-milterlib=/opt/csw/lib

SKIPTEST = 1

CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmdigestsha1
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmiostringy
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWsendmail
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWlibmilter
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmmimebase64
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmmailtools
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmmimetools
CHECKPKG_OVERRIDES_CSWmimedefang += surplus-dependency|CSWpmhtmlparser

include gar/category.mk
