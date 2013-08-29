# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = procmail
VERSION = 3.22
GARTYPE = v2

DESCRIPTION = The procmail mail processing program 
define BLURB
  Procmail can be used to create mail-servers, mailing lists, sort your incoming mail into separate folders/files (real convenient when subscribing to one or more mailing lists or for prioritising your mail), preprocess your mail, start any programs upon mail arrival (e.g. to generate different chimes on your workstation for different types of mail) or selectively forward certain incoming mail automatically to someone
endef

VENDOR_URL = http://www.procmail.org/

# The official repository appears broken as of 2013/08/29
MASTER_SITES = ftp://ftp.fu-berlin.de/pub/unix/mail/procmail/
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES  += Makefile config.h

LICENSE = COPYING

CONFIGURE_SCRIPTS = custom
TEST_SCRIPTS =

PROTOTYPE_MODIFIERS += lockfile
PROTOTYPE_FILES_lockfile = $(bindir)/lockfile.*
PROTOTYPE_PERMS_lockfile = 2755
PROTOTYPE_GROUP_lockfile = mail

PROTOTYPE_MODIFIERS += procmail
PROTOTYPE_FILES_procmail = $(bindir)/procmail.*
PROTOTYPE_PERMS_procmail = 6755
PROTOTYPE_GROUP_procmail = mail

include gar/category.mk

configure-custom:
	cp $(WORKDIR)/Makefile $(WORKDIR)/config.h $(WORKSRC)
	@$(MAKECOOKIE)

pre-install-modulated:
	ginstall -d $(DESTDIR)$(mandir)/man1
	@$(MAKECOOKIE)


