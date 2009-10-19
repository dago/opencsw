GARNAME = oinkmaster
GARVERSION = 2.0
CATEGORIES = utils

DESCRIPTION = Update and manage Snort rules
define BLURB
  Update and manage Snort rules
endef

MASTER_SITES += $(SF_MIRRORS)
SF_PROJ = oinkmaster
DISTFILES += $(GARNAME)-$(GARVERSION).tar.gz

LICENSE = LICENSE

REQUIRED_PKGS = CSWperl CSWwget
ARCHALL = 1

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

PATCHFILES = patch-oinkmaster.pl.diff

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

SAMPLECONF = /etc/opt/csw/oinkmaster.conf

include gar/category.mk

DOCLIST = ChangeLog FAQ INSTALL README README.gui README.templates UPGRADING template-examples.conf

install-custom:
	@echo "Installing $(GARNAME) (custom)"
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw
	@ginstall -m 644 $(WORKSRC)/oinkmaster.conf $(DESTDIR)/etc/opt/csw
	@ginstall -d -m 755 $(DESTDIR)$(bindir)
	@ginstall -m 755 $(WORKSRC)/oinkmaster.pl $(DESTDIR)$(bindir)
	@ginstall -d -m 755 $(DESTDIR)$(mandir)/man1
	@ginstall -m 644 $(WORKSRC)/oinkmaster.1 $(DESTDIR)$(mandir)/man1
	@ginstall -d -m 755 $(DESTDIR)$(docdir)/$(GARNAME)
	@$(foreach DOC,$(DOCLIST),ginstall -m 644 $(WORKSRC)/$(DOC) $(DESTDIR)$(docdir)/$(GARNAME);)
	$(MAKECOOKIE)
