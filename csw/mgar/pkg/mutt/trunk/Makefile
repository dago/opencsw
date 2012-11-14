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

POSTMSG = $(docdir)/mutt/CSWmutt.postmsg

LICENSE = COPYRIGHT

PACKAGES += CSWmutt
SPKG_DESC_CSWmutt = Metapackage for mutt with ncurses- and slang-interface
RUNTIME_DEP_PKGS_CSWmutt += CSWmutt-ncurses
RUNTIME_DEP_PKGS_CSWmutt += CSWmutt-slang
PKGFILES_CSWmutt += $(POSTMSG)
ARCHALL_CSWmutt = 1

# These overrides are specific to the structure of the package
CHECKPKG_OVERRIDES_CSWmutt += surplus-dependency|CSWmutt-ncurses
CHECKPKG_OVERRIDES_CSWmutt += surplus-dependency|CSWmutt-slang

PACKAGES += CSWmutt-base
SPKG_DESC_CSWmutt-base = $(DESCRIPTION)
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWmutt-bae += CSWlibiconv2

# This warning from checkpkg is obviously wrong...
CHECKPKG_OVERRIDES_CSWmutt-base = missing-dependency|CSWperl

PACKAGES += CSWmutt-ncurses
SPKG_DESC_CSWmutt-ncurses = Mutt mail client with ncurses interface
PKGFILES_CSWmutt-ncurses = $(bindir)/mutt-ncurses
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibncursesw5
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibintl8
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWlibidn11
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWgpgme
RUNTIME_DEP_PKGS_CSWmutt-ncurses += CSWmutt-base
CHECKPKG_OVERRIDES_CSWmutt-ncurses += surplus-dependency|CSWmutt-base

PACKAGES += CSWmutt-slang
SPKG_DESC_CSWmutt-slang = Mutt mail client with slang interface
PKGFILES_CSWmutt-slang = $(bindir)/mutt-slang
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibslang2
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibintl8
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibgpg-error0
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWgpgme
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibgdbm4
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWlibidn11
RUNTIME_DEP_PKGS_CSWmutt-slang += CSWmutt-base
CHECKPKG_OVERRIDES_CSWmutt-slang += surplus-dependency|CSWmutt-base

CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/etc/opt/csw/Muttrc.CSW
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/reference.html
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/ChangeLog
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/INSTALL
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/configuration.html
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/samples/sample.muttrc
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/share|root/opt/csw/share/doc/mutt/devel-notes.txt
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/mimesupport.html
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/manual.txt
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/doc/mutt/manual.html
CHECKPKG_OVERRIDES_CSWmutt-base += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/muttrc.5
CHECKPKG_OVERRIDES_CSWmutt-base += pkginfo-opencsw-repository-uncommitted

REINPLACEMENTS += mailcap
REINPLACE_MATCH_mailcap = /usr/local/etc/mailcap
REINPLACE_WITH_mailcap = /opt/csw/etc/mailcap
REINPLACE_FILES_mailcap += init.c
REINPLACE_FILES_mailcap += doc/manual.xml
REINPLACE_FILES_mailcap += doc/mimesupport.html

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
CONFIGURE_ARGS += --enable-external-dotlock

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
EXTRA_PAX_ARGS_slang-yes = -s ",\.$(bindir)/mutt$$,.$(bindir)/mutt-slang,p" -m
EXTRA_PAX_ARGS = $(EXTRA_PAX_ARGS_slang-$(SLANG))

ALTERNATIVES_CSWmutt-ncurses = ncurses
ALTERNATIVES_CSWmutt-slang = slang
ALTERNATIVE_ncurses = $(bindir)/mutt mutt $(bindir)/mutt-ncurses 100
ALTERNATIVE_slang = $(bindir)/mutt mutt $(bindir)/mutt-slang 200

include gar/category.mk

post-merge:
	ginstall -d $(PKGROOT)$(docdir)/mutt/
	ginstall $(WORKDIR)/CSWmutt.postmsg $(PKGROOT)$(docdir)/mutt/CSWmutt.postmsg
