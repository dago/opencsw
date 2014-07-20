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
RUNTIME_DEP_PKGS += CSWpmdigestnilsimsaa CSWpmdigesthmac

# We define upstream file regex so we can be notifed of new upstream #UFILES_REGEX = $(NAME)-agents-(\d+(?:\.\d+)*).tar.bz2

CONFIGURE_SCRIPTS = custom
TEST_SCRIPTS =_SCRIPTS = custom

EXTRA_MERGE_EXCLUDE_FILES = .*\/perllocal\.pod

include gar/category.mk

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( cd $(WORKSRC) ; \
	   perl Makefile.PL INSTALLDIRS=vendor DESTDIR=$(DESTDIR) )