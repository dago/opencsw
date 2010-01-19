GARNAME = mutt
GARVERSION = 1.5.20
CATEGORIES = apps

EXTRA_MODULATORS = SLANG
MODULATIONS_SLANG = no yes

DESCRIPTION = A text-based mail client for Unix operating systems
define BLURB
  Mutt is a small but very powerful text-based MIME mail client. Mutt is
  highly configurable, and is well suited to the mail power user with
  advanced features like key bindings, keyboard macros, mail threading,
  regular expression searches and a powerful pattern matching language for
  selecting groups of messages.
endef

VENDOR_URL   = http://www.mutt.org
MASTER_SITES = $(SF_MIRRORS)
DISTFILES    = $(GARNAME)-$(GARVERSION).tar.gz
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYRIGHT

PACKAGES = CSWmutt-base CSWmutt-ncurses CSWmutt-slang

REQUIRED_PKGS_CSWmutt-base = CSWggettextrt CSWiconv CSWlibidn
REQUIRED_PKGS_CSWmutt-ncurses = CSWmutt-base CSWncurses CSWggettextrt CSWiconv CSWlibidn CSWgdbm CSWsasl 
REQUIRED_PKGS_CSWmutt-slang = CSWmutt-base CSWslang CSWggettextrt CSWiconv CSWlibidn CSWgdbm CSWsasl

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

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-pop
CONFIGURE_ARGS += --enable-imap
CONFIGURE_ARGS += --enable-smtp
CONFIGURE_ARGS += --enable-gpgme
# Add IMAP header caching and SASL as requested per:
#   http://www.opencsw.org/mantis/view.php?id=3726
CONFIGURE_ARGS += --enable-hcache
CONFIGURE_ARGS += --with-sasl
CONFIGURE_ARGS += --with-ssl

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
