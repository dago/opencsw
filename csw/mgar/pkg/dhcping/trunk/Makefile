NAME = dhcping
VERSION = 1.2
GARTYPE = v2

DESCRIPTION = DHCP daemon ping program
define BLURB
  This small tool let you perform a dhcp-request to find out if a dhcp-server is still running.
endef

MASTER_SITES = http://www.mavetju.org/download/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

LICENSE = LICENSE

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

SKIPTEST = 1

include gar/category.mk

DOCLIST = CHANGES CONTACT

post-install-modulated:
	@echo " ==> Post-Install $(NAME) (custom)"
	@ginstall -d $(DESTDIR)$(docdir)/$(NAME)
	@$(foreach DOC,$(DOCLIST),cp $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(NAME);)
	@$(MAKECOOKIE)
