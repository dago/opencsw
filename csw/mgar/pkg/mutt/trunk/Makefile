NAME = mutt
VERSION = 1.5.21
CATEGORIES = apps
GARTYPE = v2

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
DISTFILES    = $(NAME)-$(VERSION).tar.gz
DISTFILES   += CSWmutt.postmsg
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

LICENSE = COPYRIGHT

PACKAGES = CSWmutt CSWmutt-base CSWmutt-ncurses CSWmutt-slang

RUNTIME_DEP_PKGS_core  = CSWgdbm
RUNTIME_DEP_PKGS_core += CSWggettextrt
RUNTIME_DEP_PKGS_core += CSWgpgerr
RUNTIME_DEP_PKGS_core += CSWgpgme
RUNTIME_DEP_PKGS_core += CSWiconv
RUNTIME_DEP_PKGS_core += CSWlibidn
RUNTIME_DEP_PKGS_core += CSWosslrt
RUNTIME_DEP_PKGS_core += CSWsasl
RUNTIME_DEP_PKGS_core += CSWzlib
RUNTIME_DEP_PKGS_CSWmutt-ncurses = $(RUNTIME_DEP_PKGS_core) CSWmutt-base CSWncurses
RUNTIME_DEP_PKGS_CSWmutt-slang   = $(RUNTIME_DEP_PKGS_core) CSWmutt-base CSWslang
RUNTIME_DEP_PKGS_CSWmutt-base    = CSWggettextrt CSWiconv CSWlibidn
RUNTIME_DEP_PKGS_CSWmutt         = CSWmutt-ncurses CSWmutt-slang

CATALOGNAME_CSWmutt-base = mutt_base
CATALOGNAME_CSWmutt-ncurses = mutt_ncurses
CATALOGNAME_CSWmutt-slang = mutt_slang
CATALOGNAME_CSWmutt = mutt

SPKG_DESC_CSWmutt-base = $(DESCRIPTION)
SPKG_DESC_CSWmutt-ncurses = Mutt mail client with ncurses interface
SPKG_DESC_CSWmutt-slang = Mutt mail client with slang interface
SPKG_DESC_CSWmutt = Metapackage for mutt with ncurses- and slang-interface

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
MERGE_SCRIPTS_isa-default-slang-yes = copy-all

EXTRA_PAX_ARGS_slang-no = -s ",\.$(bindir)/mutt$$,.$(bindir)/mutt-ncurses,p"
EXTRA_PAX_ARGS_slang-yes = -s ",\.$(bindir)/mutt$$,.$(bindir)/mutt-slang,p" -s ",.*,,"
EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_slang-$(SLANG))

POSTMSG = $(docdir)/mutt/CSWmutt.postmsg

# CSWmutt-base gets all the rest
PKGFILES_CSWmutt-ncurses = $(bindir)/mutt-ncurses
PKGFILES_CSWmutt-slang = $(bindir)/mutt-slang
PKGFILES_CSWmutt = $(POSTMSG)

ARCHALL_CSWmutt = 1

ALTERNATIVES_CSWmutt-ncurses = ncurses
ALTERNATIVES_CSWmutt-slang = slang
ALTERNATIVE_ncurses = $(bindir)/mutt mutt $(bindir)/mutt-ncurses 100
ALTERNATIVE_slang = $(bindir)/mutt mutt $(bindir)/mutt-slang 200

# This warning from checkpkg is obviously wrong...
CHECKPKG_OVERRIDES_CSWmutt-base = missing-dependency|CSWperl

# These overrides are specific to the structure of the package
CHECKPKG_OVERRIDES_CSWmutt += surplus-dependency|CSWmutt-ncurses
CHECKPKG_OVERRIDES_CSWmutt += surplus-dependency|CSWmutt-slang
CHECKPKG_OVERRIDES_CSWmutt-ncurses += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWmutt-ncurses += surplus-dependency|CSWmutt-base
CHECKPKG_OVERRIDES_CSWmutt-slang += surplus-dependency|CSWalternatives
CHECKPKG_OVERRIDES_CSWmutt-slang += surplus-dependency|CSWmutt-base

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(docdir)/mutt/
	ginstall $(WORKDIR)/CSWmutt.postmsg $(PKGROOT)$(docdir)/mutt/CSWmutt.postmsg
	@$(MAKECOOKIE)
	
