NAME = razor
VERSION = 2.85
CATEGORIES = net
GARTYPE = v2
DISTNAME = $(NAME)-agents-$(VERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)

DESCRIPTION = Spam detection and filtering netwiltering network
endef

MASTER_SITES = http://prdownloads.sourceforge.net/razor/
DISTFILES  = $(DISTNAME).tar.bz2

LICENSE = LICENSE

 = CSWperl
RUNTIME_DEP_PKGS += CSWpm-digest-hmac
RUNTIME_DEP_PKGS += CSWpm-digest-sha1
RUNTIME_DEP_PKGS += CSWpm-net-dns
RUNTIME_DEP_PKGS += CSWpm-uri
RUNTIME_DEP_PKGS += CSWpmdigestnilsimsaa CHECKPKG_OVERRIDES_CSWrazor += surplus-dependency|CSWpm-digest-sha1
CHECKPKG_OVERRIDES_CSWrazor += surplus-dependency|CSWpmdigestnilsimsa
CHECKPKG_OVERRIDES_CSWrazor += surplus-dependency|CSWpm-digest-hmac
CHECKPKG_OVERRIDES_CSWrazor += surplus-dependency|CSWpm-uri
CHECKPKG_OVERRIDES_CSWrazor += surplus-dependency|CSWpm-net-dns

CONFIGURE_SCRIPTS = custom
# No tests
TEST_SCRIPTS =_SCRIPTS = custom

EXTRA_MERGE_EXCLUDE_FILES = .*\/perllocal\.pod

include gar/category.mk

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) )