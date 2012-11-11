NAME = mailx
VERSION = 12.4
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = Simple mail user agent, formerly known as nail
define BLURB
  Mailx is derived from Berkeley Mail and is intended provide the
  functionality of the POSIX mailx command with additional support
  for MIME, IMAP, POP3, SMTP, and S/MIME. It provides enhanced
  features for interactive use, such as caching and disconnected
  operation for IMAP, message threading, scoring, and filtering.
  It is also usable as a mail batch language, both for sending
  and receiving mail.
endef

MASTER_SITES = $(SECTF_MIRRORS)
SF_PROJ = heirloom
DISTFILES  = $(NAME)-$(VERSION).tar.bz2

SPKG_CLASSES = none cswcpsampleconf

RUNTIME_DEP_PKGS = CSWcswclassutils CSWosslrt CSWiconv

# nail _is_ mailx now
INCOMPATIBLE_PKGS = CSWnail

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=106236
UPSTREAM_USE_SF = 1
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
TEST_SCRIPTS =

PROTOTYPE_FILTER  = awk '\
	$$$$3 ~ /nail.rc.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } \
	 { print }'

include gar/category.mk

MAKE_ARGS = \
	PREFIX=$(prefix) \
	BINDIR=$(bindir) \
	MANDIR=$(mandir) \
	SYSCONFDIR=$(sysconfdir)/$(NAME) \
	MAILSPOOL=/var/mail \
	SENDMAIL=/usr/lib/sendmail \
 	UCBINSTALL=/usr/ucb/install

BUILD_ARGS = $(MAKE_ARGS)
INSTALL_ARGS = $(MAKE_ARGS)

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/$(NAME)
post-install-modulated: DOCS = README TODO AUTHORS ChangeLog mailx.1.html
post-install-modulated:
	@ginstall -d $(DOCDEST)
	@$(foreach DOC,$(DOCS),cp $(WORKSRC)/$(DOC) $(DOCDEST);)
	@cp $(FILEDIR)/changelog.CSW $(DOCDEST)
	@mv $(DESTDIR)$(sysconfdir)/$(NAME)/nail.rc \
		$(DESTDIR)$(sysconfdir)/$(NAME)/nail.rc.CSW
	@cd $(DESTDIR)$(bindir) && ln -s mailx nai