GARNAME = imapsync
GARVERSION = 1.267
CATEGORIES = utils

DESCRIPTION = IMAP synchronization, copy and migration tool
define BLURB
  imapsync is a tool for facilitating incremental recursive IMAP
  transfers from one mailbox to another. It is useful for mailbox
  migration, and reduces the amount of data transferred by only copying
  messages that are not present on both servers. Read, unread, and
  deleted flags are preserved, and the process can be stopped and
  resumed. The original messages can optionally be deleted after a
  successful transfer. 
endef

SPKG_SOURCEURL = http://freshmeat.net/projects/imapsync/

MASTER_SITES = http://www.linux-france.org/prj/imapsync/dist/
DISTFILES  = $(GARNAME)-$(GARVERSION).tgz
DISTFILES += $(call admfiles,CSWimapsync,)

REQUIRED_PKGS  = CSWperl CSWpmmailimapclient CSWpmdatemanip CSWpmiosocketssl
REQUIRED_PKGS += CSWpmtermreadkey CSWpmdigesthmac

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS = 
BUILD_SCRIPTS     =
TEST_SCRIPTS      =
INSTALL_SCRIPTS   = imapsync

CONFIGURE_ARGS = $(DIRPATHS)

install-imapsync:
	@ginstall -d $(DESTDIR)$(bindir)
	@ginstall -d $(DESTDIR)$(mandir)/man1
	@sed 's#/usr/bin/perl#/opt/csw/bin/perl#' $(WORKSRC)/$(GARNAME) \
		> $(DESTDIR)$(bindir)/$(GARNAME)
	@chmod 755 $(DESTDIR)$(bindir)/$(GARNAME)
	@pod2man $(WORKSRC)/$(GARNAME) > $(DESTDIR)$(mandir)/man1/$(GARNAME).1
	@$(MAKECOOKIE)

include gar/category.mk
