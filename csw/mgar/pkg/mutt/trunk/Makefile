GARNAME = mutt
GARVERSION = 1.5.20
CATEGORIES = apps

EXTRA_MODULATORS = SLANG
MODULATIONS_SLANG = no yes

DESCRIPTION = A text-based mail client for Unix operating systems
define BLURB
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYRIGHT

PACKAGES = CSWmutt-base CSWmutt-ncurses CSWmutt-slang

REQUIRED_PKGS_CSWmutt-base = CSWggettextrt CSWiconv CSWlibidn
REQUIRED_PKGS_CSWmutt-ncurses = CSWmutt-base CSWncurses CSWggettextrt CSWiconv CSWlibidn
REQUIRED_PKGS_CSWmutt-slang = CSWmutt-base CSWslang CSWggettextrt CSWiconv CSWlibidn

CATALOGNAME_CSWmutt-base = mutt_base
CATALOGNAME_CSWmutt-ncurses = mutt_ncurses
CATALOGNAME_CSWmutt-slang = mutt_slang

SPKG_DESC_CSWmutt-base = $(DESCRIPTION)
SPKG_DESC_CSWmutt-ncurses = Mutt mail client with ncurses interface
SPKG_DESC_CSWmutt-slang = Mutt mail client with slang interface

# Raise optimizer level unless this bug has been fixed:
#   http://dev.mutt.org/trac/ticket/3347
OPT_FLAGS_SOS = -xO4

sysconfdir = /etc/opt/csw

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS_SLANG-no =
CONFIGURE_ARGS_SLANG-yes = --with-slang=$(prefix)
CONFIGURE_ARGS += $(CONFIGURE_ARGS_SLANG-$(SLANG))

TEST_SCRIPTS =

PRESERVECONF  = $(sysconfdir)/mime.types
PRESERVECONF += $(sysconfdir)/Muttrc

EXTRA_MERGE_EXCLUDE_FILES = .*\.dist

MIGRATE_FILES_CSWmutt-base = mime.types Muttrc

MERGE_SCRIPTS_isa-default-slang-no = copy-all
MERGE_SCRIPTS_isa-default-slang-yes = copy-mutt-only

PKGFILES_CSWmutt-ncurses = $(bindir)/mutt
PKGFILES_CSWmutt-slang = $(bindir)/mutt-slang

include gar/category.mk

merge-copy-mutt-only: $(PKGROOT)
	ginstall -d $(PKGROOT)$(bindir)
	ginstall $(INSTALLISADIR)$(bindir)/mutt $(PKGROOT)$(bindir)/mutt-slang
	@$(MAKECOOKIE)
