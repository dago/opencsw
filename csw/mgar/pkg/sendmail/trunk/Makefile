# $Id$

# TODO
# - Build separate 9/10 packages?

# + #4486 Provide sendmail's contrib/ tools as a separate package?
# + Include activate/deactivate scripts
# + migrate conf from /opt/csw/etc/mail
# + Tests? Not really possible to test during build
# + libmilter
# + use alternatives to clear collisions with postfix, see sudo as example
# + post message
# + never start cswsendmail by default (collides with system sendmail)
# + path to sendmail.cf (/etc/opt/csw/mail)
# + bdb hash support
# + cpsample conf files
# + remove COPYING file
# + copy usergroup file into place
# + #3864 Sendmail must be relinked with new berkeley db -> bdb48
# + #2915 Must stop built-in sendmail manually -> n/a
# + #4150 Sendmail 8.14.4 released -> this is 8.14.5

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
DISTFILES += aliases helpfile local-host-names sendmail.cf
DISTFILES += sm-client.st statistics submit.cf trusted-users
DISTFILES += README.CSW sendmail.schema site.config.m4
DISTFILES += oracle-sendmail-deactivate.sh oracle-sendmail-reactivate.sh
DISTFILES += cswsendmail cswusergroup
#DISTFILES += $(foreach FILE,$(shell cd $(FILEDIR) && ls *.CSW),$(FILE))
#DISTFILES += CSWsendmail.preremove CSWsendmail.preinstall CSWsendmail.space
#DISTFILES += cswsendmail site.config.m4 $(MY_CLASSES) CSWsendmail.checkinstall
#DISTFILES += README.CSW sendmail.schema CSWsendmail.postinstall

LICENSE = LICENSE

PACKAGES                      = CSWsendmail 
CATALOGNAME_CSWsendmail       = sendmail
SPKG_DESC_CSWsendmail         = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWsendmail  = CSWoldaprt
RUNTIME_DEP_PKGS_CSWsendmail += CSWosslrt
RUNTIME_DEP_PKGS_CSWsendmail += CSWsasl
RUNTIME_DEP_PKGS_CSWsendmail += CSWtcpwrap 
RUNTIME_DEP_PKGS_CSWsendmail += CSWbdb48

PACKAGES                += CSWlibmilter 
CATALOGNAME_CSWlibmilter = libmilter
SPKG_DESC_CSWlibmilter   = Sendmail MTA milter
PKGFILES_CSWlibmilter    = $(docdir)/libmilter/.*
PKGFILES_CSWlibmilter   += /opt/csw/include/libmilter.h
PKGFILES_CSWlibmilter   += $(libdir)/libmilter.a
PKGFILES_CSWlibmilter   += $(libdir)/libsm.a
PKGFILES_CSWlibmilter   += $(libdir)/libsmdb.a
PKGFILES_CSWlibmilter   += $(libdir)/libsmutil.a

PACKAGES                            += CSWsendmail-contrib 
CATALOGNAME_CSWsendmail-contrib      = sendmail_contrib
SPKG_DESC_CSWsendmail-contrib        = Sendmail MTA contrib
RUNTIME_DEP_PKGS_CSWsendmail-contrib = CSWperl
ARCHALL_CSWsendmail-contrib          = 1
PKGFILES_CSWsendmail-contrib         = $(docdir)/sendmail_contrib/.*
PKGFILES_CSWsendmail-contrib        += $(bindir)/link_hash.sh
PKGFILES_CSWsendmail-contrib        += $(bindir)/movemail.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/smcontrol.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/passwd-to-alias.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/socketmapClient.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/bounce-resender.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/doublebounce.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/mailprio
PKGFILES_CSWsendmail-contrib        += $(bindir)/socketmapServer.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/qtool.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/buildvirtuser
PKGFILES_CSWsendmail-contrib        += $(bindir)/etrn.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/re-mqueue.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/cidrexpand
PKGFILES_CSWsendmail-contrib        += $(bindir)/expn.pl
PKGFILES_CSWsendmail-contrib        += $(mandir)/man1/etrn.0
PKGFILES_CSWsendmail-contrib        += $(mandir)/man8/qtool.8
PKGFILES_CSWsendmail-contrib        += $(sysconfdir)/movemail.conf

INITSMF     = /etc/opt/csw/init.d/cswsendmail
SAMPLECONF  = $(addprefix /etc/opt/csw/mail/,$(CONFFILES))
SAMPLECONF += /var/opt/csw/spool/clientmqueue/sm-client.st
USERGROUP   = /etc/opt/csw/pkg/CSWsendmail/cswusergroup
POSTMSG     = $(docdir)/sendmail/README.postinstall

# Enable support for files > 2GB in size.
EXTRA_CFLAGS = -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE

# Do not remove the static libs from libmilter
MERGE_EXCLUDE_STATICLIBS =

#PROTOTYPE_FILTER = awk \
#	'$$$$2 ~/i.sol9/ { next } \
#	$$$$2 ~/i.sol10/ { next } \
#	$$$$3 ~/\/init\.d\/cswsendmail$$$$/ {$$$$2 = "cswinitsmf"} \
#	$$$$3 ~/sol9\./ { $$$$2 = "sol9" } \
#	$$$$3 ~/sol10\./ { $$$$2 = "sol10" } \
#	{ print } \
#	END { { print "i i.sol9=CSWsendmail.i.sol9" } \
#	{ print "i i.sol10=CSWsendmail.i.sol10" } }'

# Patch away GNUism
PATCHFILES += 0001-add-libmilter-to-the-Makefile.patch
PATCHFILES += 0002-no-gnuism.patch

MIGRATE_FILES_CSWsendmail      = aliases helpfile local-host-names sendmail.cf
MIGRATE_FILES_CSWsendmail     += statistics submit.cf trusted-users
MIGRATE_SOURCE_DIR_CSWsendmail = /opt/csw/etc/mail
MIGRATE_DEST_DIR_CSWsendmail   = /etc/opt/csw/mail

CONFIGURE_SCRIPTS   = custom
BUILD_SCRIPTS       = custom
TEST_SCRIPTS        = custom
INSTALL_SCRIPTS     = custom
#EXTRA_MERGE_SCRIPTS = OS

# Some files collide with CSWpostfix
ALTERNATIVES_CSWsendmail  = mailq newaliases mailq.1 newaliases.1 aliases.5
ALTERNATIVE_mailq         = $(bindir)/mailq mailq $(bindir)/mailq.sendmail 100
ALTERNATIVE_newaliases   += $(bindir)/newaliases newaliases $(bindir)/newaliases.sendmail 100
ALTERNATIVE_mailq.1      += $(mandir)/man1/mailq.1 mailq.1 $(mandir)/man1/mailq1.1.sendmail 100
ALTERNATIVE_newaliases.1 += $(mandir)/man1/newaliases.1 newaliases.1 $(mandir)/man1/newaliases.1.sendmail 100
ALTERNATIVE_aliases.5    += $(mandir)/man5/aliases.5 aliases.5 $(mandir)/man5/aliases.5.sendmail 100

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
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/etc/opt/csw/movemail.conf
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/opt/csw/share/doc/sendmail_contrib/mmuegel
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/opt/csw/bin/etrn.pl
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/opt/csw/bin/doublebounce.pl
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/opt/csw/bin/movemail.pl
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/opt/csw/bin/expn.pl
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/opt/csw/bin/bounce-resender.pl
CHECKPKG_OVERRIDES_CSWsendmail-contrib += file-with-bad-content|/usr/local|root/opt/csw/bin/re-mqueue.pl

# The static libs from libmilter
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libsmutil.a
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libmilter.a
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libsm.a
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libsmdb.a

include gar/category.mk

#ADMSCRIPTS = preremove preinstall space depend i.sol9 i.sol10

#SOLVER    = sol$(shell uname -r |sed 's/5\.//')
PLATFORM  = $(shell if [ `uname -i` = "i86pc" ] ; then echo i86pc ; else echo sun4 ; fi )
OBJDIR    = $(WORKDIR)/$(DISTNAME)/obj.SunOS.$(GAROSREL).$(PLATFORM)
LIBFILES  = sendmail/sendmail mail.local/mail.local smrsh/smrsh rmail/rmail
LIBMILTER = libmilter/libmilter.a libsm/libsm.a libsmdb/libsmdb.a libsmutil/libsmutil.a
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
INCLFILES = libmilter/libmilter.h
CONTBIN   = link_hash.sh movemail.pl smcontrol.pl \
            passwd-to-alias.pl socketmapClient.pl bounce-resender.pl \
            doublebounce.pl mailprio socketmapServer.pl \
            qtool.pl buildvirtuser etrn.pl re-mqueue.pl \
            cidrexpand expn.pl
CONTDOC   = dnsblaccess.m4 domainmap.m4 mmuegel
CONTMAN1  = etrn.0
CONTMAN8  = qtool.8
CONTCONF  = movemail.conf

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
	@echo " ==> Installing $(NAME) (custom)"

	@# Install dirs
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
	ginstall -d $(DESTDIR)/opt/csw/include
	ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)_contrib
	ginstall -m 755 -d $(DESTDIR)$(docdir)/libmilter
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWsendmail

	@# Install the libraries
	( for file in $(LIBFILES) ; do \
		ginstall -c -m 755 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )

	@# Install the binaries
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

	@# Install manpages
	( for file in $(MANFILES1) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man1 ; \
		done )
	( for file in $(MANFILES5) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man5 ; \
		done )
	( for file in $(MANFILES8) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man8 ; \
		done )

	@# Install milter lib files
	( for file in $(LIBMILTER) ; do \
		ginstall -m 444 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )

	@# Install include files
	( for file in $(INCLFILES) ; do \
		ginstall -m 444 $(OBJDIR)/$$file $(DESTDIR)/opt/csw/include ; \
		done )

	@# Install m4/cf macros
	find $(WORKSRC)/cf -type f -exec chmod 644 {} +
	cp -r $(WORKSRC)/cf $(DESTDIR)$(sharedstatedir)/mail

	@# Install startup script
	chmod +x $(DOWNLOADDIR)/cswsendmail && \
		cp -p $(DOWNLOADDIR)/cswsendmail $(DESTDIR)/etc/opt/csw/init.d

	@# Install configurations, XXX missing submit.cf/sendmail.cf
	( for file in $(CONFFILES) ; do \
		ginstall -m 644 $(DOWNLOADDIR)/$$file \
		$(DESTDIR)$(sysconfdir)/mail/$$file; \
		done )
	( ginstall -m 644  $(DOWNLOADDIR)/sm-client.st \
		$(DESTDIR)/var/opt/csw/spool/clientmqueue/ )

	@# usergroup
	ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWsendmail/

	@# README
	ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)/

	@# Create links in bindir
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/newaliases
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/mailq
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/purgestats
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/hoststat

	@# Fix alternatives files
	mv $(DESTDIR)$(bindir)/mailq $(DESTDIR)$(bindir)/mailq.sendmail
	mv $(DESTDIR)$(bindir)/newaliases $(DESTDIR)$(bindir)/newaliases.sendmail
	mv $(DESTDIR)$(mandir)/man1/mailq.1 $(DESTDIR)$(mandir)/man1/mailq1.1.sendmail
	mv $(DESTDIR)$(mandir)/man1/newaliases.1 $(DESTDIR)$(mandir)/man1/newaliases.1.sendmail
	mv $(DESTDIR)$(mandir)/man5/aliases.5 $(DESTDIR)$(mandir)/man5/aliases.5.sendmail

	@# Post install message
	ginstall -m 444 $(FILEDIR)/CSWsendmail.postmsg $(DESTDIR)$(docdir)/sendmail/README.postinstall

	@# Milter doc files
	ginstall -m 644 $(WORKSRC)/libmilter/docs/* $(DESTDIR)$(docdir)/libmilter

	@# Contrib files
	( for file in $(CONTBIN) ; do \
		ginstall -m 755 $(WORKSRC)/contrib/$$file $(DESTDIR)$(bindir) ; \
		done )
	( for file in $(CONTCONF) ; do \
		ginstall -m 644 $(WORKSRC)/contrib/$$file $(DESTDIR)$(sysconfdir) ; \
		done )
	( for file in $(CONTDOC) ; do \
		ginstall -m 444 $(WORKSRC)/contrib/$$file $(DESTDIR)$(docdir)/sendmail_contrib ; \
		done )
	( for file in $(CONTMAN1) ; do \
		ginstall -m 644 $(WORKSRC)/contrib/$$file $(DESTDIR)$(mandir)/man1 ; \
		done )
	( for file in $(CONTMAN8) ; do \
		ginstall -m 644 $(WORKSRC)/contrib/$$file $(DESTDIR)$(mandir)/man8 ; \
		done )

	@# Deactivate/reactivate scripts
	ginstall -m 755 $(DOWNLOADDIR)/oracle-sendmail-deactivate.sh $(DESTDIR)$(docdir)/sendmail
	ginstall -m 755 $(DOWNLOADDIR)/oracle-sendmail-reactivate.sh $(DESTDIR)$(docdir)/sendmail

	@$(MAKECOOKIE)

merge-OS:
	@echo " ==> Merging $(NAME) (custom)"
	@# create links in bindir
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
