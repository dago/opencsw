# $Id$

# TODO
# - migrate conf from /opt/csw/etc/mail
# - post message
# - libmilter
# - try to fix bugs
#   - 2915 Must stop built-in sendmail manually
#   - 3864 Sendmail must be relinked with new berekeley db
#   - 4150 Sendmail 8.14.4 released
#   - 4486 Provide sendmail's contrib/ tools as a separate package?

# + cpsample conf files
# + remove COPYING file
# + copy usergroup file into place

NAME = sendmail
VERSION = 8.14.5
CATEGORIES = server

DESCRIPTION = Sendmail MTA
define BLURB
  Sendmail MTA
endef

#INSTALLISADIR = $(WORKROOTDIR)/install-$(GAROSREL)-$(MODULATION)
#WORKDIR = $(WORKROOTDIR)/build-$(GAROSREL)-$(MODULATION)
#WORKDIR_FIRSTMOD = $(WORKROOTDIR)/build-$(GAROSREL)-$(firstword $(MODULATIONS))
#COOKIEDIR = $(COOKIEROOTDIR)/$(GAROSREL)-$(MODULATION)

MASTER_SITES = ftp://ftp.sendmail.org/pub/sendmail/
SPKG_SOURCEURL = http://www.sendmail.org

#MY_CLASSES = CSWsendmail.i.sol9 CSWsendmail.i.sol10

DISTFILES  = $(NAME).$(VERSION).tar.gz
DISTFILES += Sun-sendmail-deactivate.sh Sun-sendmail-reactivate.sh
DISTFILES += aliases helpfile local-host-names sendmail.cf
DISTFILES += sm-client.st statistics submit.cf trusted-users
DISTFILES += README.CSW sendmail.schema
DISTFILES += cswsendmail site.config.m4
#DISTFILES += $(foreach FILE,$(shell cd $(FILEDIR) && ls *.CSW),$(FILE))
#DISTFILES += CSWsendmail.preremove CSWsendmail.preinstall CSWsendmail.space
#DISTFILES += cswsendmail site.config.m4 $(MY_CLASSES) CSWsendmail.checkinstall
#DISTFILES += README.CSW sendmail.schema CSWsendmail.postinstall

LICENSE = LICENSE

PACKAGES = CSWsendmail 
CATALOGNAME_CSWsendmail = sendmail
SPKG_DESC_CSWsendmail = $(DESCRIPTION)

RUNTIME_DEP_PKGS_CSWsendmail  = CSWoldaprt
RUNTIME_DEP_PKGS_CSWsendmail += CSWosslrt
RUNTIME_DEP_PKGS_CSWsendmail += CSWsasl
RUNTIME_DEP_PKGS_CSWsendmail += CSWtcpwrap 
#RUNTIME_DEP_PKGS_CSWsendmail += CSWbdb48 # not needed? makemap not compiled with hash support?

INITSMF     = /etc/opt/csw/init.d/cswsendmail
SAMPLECONF += $(addprefix /etc/opt/csw/mail/,$(CONFFILES))
SAMPLECONF += /var/opt/csw/spool/clientmqueue/sm-client.st
USERGROUP   = /etc/opt/csw/pkg/CSWsendmail/cswusergroup

# Enable support for files > 2GB in size.
EXTRA_CFLAGS = -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE

#PROTOTYPE_FILTER = awk \
#	'$$$$2 ~/i.sol9/ { next } \
#	$$$$2 ~/i.sol10/ { next } \
#	$$$$3 ~/\/init\.d\/cswsendmail$$$$/ {$$$$2 = "cswinitsmf"} \
#	$$$$3 ~/sol9\./ { $$$$2 = "sol9" } \
#	$$$$3 ~/sol10\./ { $$$$2 = "sol10" } \
#	{ print } \
#	END { { print "i i.sol9=CSWsendmail.i.sol9" } \
#	{ print "i i.sol10=CSWsendmail.i.sol10" } }'

#ENABLE_CHECK = 0

# Patch away GNUism
PATCHFILES = patch-CC-M.m4

CONFIGURE_SCRIPTS   = custom
BUILD_SCRIPTS       = custom
TEST_SCRIPTS        = custom
INSTALL_SCRIPTS     = custom
EXTRA_MERGE_SCRIPTS = OS

# Collisions with Postfix naming it's files after the Sendmail de facto standard
CHECKPKG_OVERRIDES_CSWsendmail += file-collision|/opt/csw/share/man/man1/mailq.1|CSWpostfix|CSWsendmail
CHECKPKG_OVERRIDES_CSWsendmail += file-collision|/opt/csw/bin/newaliases|CSWpostfix|CSWsendmail
CHECKPKG_OVERRIDES_CSWsendmail += file-collision|/opt/csw/share/man/man5/aliases.5|CSWpostfix|CSWsendmail
CHECKPKG_OVERRIDES_CSWsendmail += file-collision|/opt/csw/bin/mailq|CSWpostfix|CSWsendmail
CHECKPKG_OVERRIDES_CSWsendmail += file-collision|/opt/csw/share/man/man1/newaliases.1|CSWpostfix|CSWsendmail
# Look thru these to see if they are harmless, e.g. examples
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/README
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/share|root/opt/csw/share/mail/cf/README
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/smrsh.8
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/man/man8/sendmail.8
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/ostype/freebsd6.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/ostype/freebsd5.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/ostype/powerux.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/ostype/dragonfly.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/feature/local_procmail.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/cf/mail.cs.mc
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/cf/mail.eecs.mc
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/cf/knecht.mc
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/mailer/qpage.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/mailer/fax.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/mailer/procmail.m4
CHECKPKG_OVERRIDES_CSWsendmail += file-with-bad-content|/usr/local|root/opt/csw/share/mail/cf/mailer/phquery.m4

include gar/category.mk

#ADMSCRIPTS = preremove preinstall space depend i.sol9 i.sol10

#SOLVER    = sol$(shell uname -r |sed 's/5\.//')
PLATFORM  = $(shell if [ `uname -i` = "i86pc" ] ; then echo i86pc ; else echo sun4 ; fi )
OBJDIR    = $(WORKDIR)/$(DISTNAME)/obj.SunOS.$(GAROSREL).$(PLATFORM)
LIBFILES  = sendmail/sendmail mail.local/mail.local smrsh/smrsh rmail/rmail
BINFILES  = vacation/vacation
SBINFILES = makemap/makemap editmap/editmap praliases/praliases \
            mailstats/mailstats
MANFILES1 = sendmail/mailq.1 sendmail/newaliases.1 vacation/vacation.1
MANFILES5 = sendmail/aliases.5
MANFILES8 = sendmail/sendmail.8 mailstats/mailstats.8 makemap/makemap.8 \
            praliases/praliases.8 smrsh/smrsh.8 mail.local/mail.local.8 \
            rmail/rmail.8 editmap/editmap.8
CONFFILES = aliases helpfile local-host-names sendmail.cf \
            statistics submit.cf trusted-users

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( gsed 's,%CFLAGS%,$(CFLAGS),;s,%OCSWCC%,$(CC),' \
		$(DOWNLOADDIR)/site.config.m4 > \
		$(WORKSRC)/devtools/Site/site.config.m4 )
	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(NAME) (custom)"
	cd $(WORKSRC) && ./Build
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(NAME) (custom)"
	@$(MAKECOOKIE)

install-custom:
	@# install dirs
	@echo " ==> Installing $(NAME) (custom)"
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(mandir)/man5
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall -d $(DESTDIR)/var/opt/csw/spool/clientmqueue
	ginstall -d $(DESTDIR)$(sharedstatedir)/mail
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d $(DESTDIR)$(sysconfdir)/mail

	@# install the libraries
	@( for file in $(LIBFILES) ; do \
		ginstall -c -m 755 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )

	@# install the binaries
	ginstall -m 755 $(OBJDIR)/$(BINFILES) $(DESTDIR)$(bindir)
	( for file in $(SBINFILES) ; do \
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(sbindir) ; \
		done )

	@# rename libraries and binaries os-specific
#	( for file in `ls $(DESTDIR)$(libdir)`; do  \
#		mv $(DESTDIR)$(libdir)/$$file $(DESTDIR)$(libdir)/$(SOLVER).$$file; \
#		done )
#	( for file in `ls $(DESTDIR)$(bindir)`; do  \
#		mv $(DESTDIR)$(bindir)/$$file $(DESTDIR)$(bindir)/$(SOLVER).$$file; \
#		done )
#	( for file in `ls $(DESTDIR)$(sbindir)`; do  \
#		mv $(DESTDIR)$(sbindir)/$$file $(DESTDIR)$(sbindir)/$(SOLVER).$$file;\
#		done )

	@# install manpages
	( for file in $(MANFILES1) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man1 ; \
		done )
	( for file in $(MANFILES5) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man5 ; \
		done )
	( for file in $(MANFILES8) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man8 ; \
		done )

	@# install m4/cf macros
	find $(WORKSRC)/cf -type f -exec chmod 644 {} +
	cp -r $(WORKSRC)/cf $(DESTDIR)$(sharedstatedir)/mail

	@# install startup script
	chmod +x $(DOWNLOADDIR)/cswsendmail && \
		cp -p $(DOWNLOADDIR)/cswsendmail $(DESTDIR)/etc/opt/csw/init.d

	@# install configurations, XXX missing submit.cf/sendmail.cf
	( for file in $(CONFFILES) ; do \
		ginstall -m 644 $(DOWNLOADDIR)/$$file \
		$(DESTDIR)$(sysconfdir)/mail/$$file; \
		done )
	( mv $(DOWNLOADDIR)/sm-client.st \
		$(DESTDIR)/var/opt/csw/spool/clientmqueue/ )

	@# usergroup
	@ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWsendmail
	@ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWsendmail/

	@# README
	@ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	@ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)/

	@$(MAKECOOKIE)

merge-OS:
	@# create links in bindir
	@echo " ==> Merging $(NAME) (custom)"
	ln -s $(libdir)/sendmail $(PKGROOT)$(bindir)/newaliases
	ln -s $(libdir)/sendmail $(PKGROOT)$(bindir)/mailq
	ln -s $(libdir)/sendmail $(PKGROOT)$(bindir)/purgestats
	ln -s $(libdir)/sendmail $(PKGROOT)$(bindir)/hoststat

	@# Install the other install trees
	( for dir in `ls -d $(abspath $(WORKROOTDIR)/install*-$(MODULATION))` ; do \
		( if [ "x`echo $$dir |sed "s/.*install-\(5.[0-9]*\)-$(MODULATION).*/\1/"`x" != "x$(GAROSREL)x" ]; then \
			cd $$dir$(bindir) && \
				/usr/bin/pax -rw -v * $(PKGROOT)$(bindir);\
			cd $$dir$(sbindir) && \
				/usr/bin/pax -rw -v * $(PKGROOT)$(sbindir);\
			cd $$dir$(libdir) && \
				/usr/bin/pax -rw -v * $(PKGROOT)$(libdir); \
		fi ) \
	done )
