NAME = razor
VERSION = 2.85
CATEGORIES = net
GARTYPE = v2
DISTNAME = $(NAME)-agents-$(VERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)

DESCRIPTION = Spam detection and filtering network
define BLURB
  Spam detection and filtering network
endef

MASTER_SITES = http://prdownloads.sourceforge.net/razor/
DISTFILES  = $(DISTNAME).tar.bz2

LICENSE = LICENSE

RUNTIME_DEP_PKGS = CSWperl CSWpmuri CSWpmnetdns CSWpmdigestsha1 CSWpmdigestnilsimsa CSWpmdigesthmac

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-agents-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS = custom

EXTRA_MERGE_EXCLUDE_FILES = .*\/perllocal\.pod

include gar/category.mk

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) )
	@$(MAKECOOKIE)
