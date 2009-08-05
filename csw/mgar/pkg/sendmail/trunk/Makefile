GARNAME = sendmail
GARVERSION = 8.14.3
CATEGORIES = server

DESCRIPTION = Sendmail MTA
define BLURB
  XXX anacronism ;-) need text here
endef

INSTALLISADIR = $(WORKROOTDIR)/install-$(GAROSREL)-$(MODULATION)
WORKDIR = $(WORKROOTDIR)/build-$(GAROSREL)-$(MODULATION)
COOKIEDIR = $(COOKIEROOTDIR)/$(GAROSREL)-$(MODULATION)

MASTER_SITES = ftp://ftp.sendmail.org/pub/sendmail/

DISTFILES  = $(GARNAME).$(GARVERSION).tar.gz
DISTFILES += README.CSW sendmail.schema
DISTFILES += Sun-sendmail-deactivate.sh Sun-sendmail-reactivate.sh
DISTFILES += cswsendmail site.config.m4 i.sol8 i.sol9 i.sol10
DISTFILES += CSWsendmail.preremove CSWsendmail.preinstall CSWsendmail.space
DISTFILES += $(foreach FILE,$(shell cd $(FILEDIR) && ls *.CSW),$(FILE))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# we require
PACKAGES = CSWsendmail CSWsendmailcommon
SPKG_SOURCEURL = http://www.sendmail.org/
SPKG_DESC_CSWsendmail = $(DESCRIPTION)
SPKG_DESC_CSWsendmailcommon = $(DESCRIPTION) common files
CATALOGNAME_CSWsendmail = sendmail
CATALOGNAME_CSWsendmailcommon = sendmail_common

REQUIRED_PKGS_CSWsendmail = CSWbdb CSWoldaprt CSWosslrt CSWsasl CSWtcpwrap CSWcswclassutils CSWsendmailcommon
REQUIRED_PKGS_CSWsendmailcommon = CSWbdb CSWoldaprt CSWosslrt CSWsasl CSWtcpwrap CSWcswclassutils
ARCHALL_CSWsendmailcommon = 1
SPKG_CLASSES_CSWsendmail = none cswinitsmf cswosrel
PROTOTYPE_FILTER = (awk \
				   '$$$$3 ~/\/init\.d\/cswsendmail$$$$/ {$$$$2 = "cswinitsmf"} \
					$$$$3 ~/sol8\./ { $$$$2 = "sol8" } \
					$$$$3 ~/sol9\./ { $$$$2 = "sol9" } \
					$$$$3 ~/sol10\./ { $$$$2 = "sol10" } \
					$$$$3 ~/\/sol[0-9]*\.sendmail$$$$/ { $$$$4 = "2755" } \
					{ print }')
PROTOTYPE_FILTER += (fgrep -v "i.sol8";echo "i i.sol8=\$$$$WORKDIR_FIRSTMOD/i.sol8")
PROTOTYPE_FILTER += (fgrep -v "i.sol9";echo "i i.sol9=\$$$$WORKDIR_FIRSTMOD/i.sol9")
PROTOTYPE_FILTER += (fgrep -v "i.sol10";echo "i i.sol10=\$$$$WORKDIR_FIRSTMOD/i.sol10")

PKGFILES_CSWsendmailcommon  = .*$(sharedstatedir)/.*
PKGFILES_CSWsendmailcommon += .*$(mandir)/.*
PKGFILES_CSWsendmailcommon += .*$(sysconfdir)/.*
PKGFILES_CSWsendmailcommon += .*/clientmqueue/.*

ENABLE_CHECK = 0

# patch away GNUism
PATCHFILES = patch-CC-M.m4

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = custom
TEST_SCRIPTS      = custom
INSTALL_SCRIPTS   = custom
EXTRA_MERGE_SCRIPTS = OS

include gar/category.mk
ADMSCRIPTS = preremove preinstall space depend i.sol8 i.sol9 i.sol10

SOLVER = sol$(shell uname -r |sed 's/5\.//')
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

configure-custom:
	@( gsed 's,%CFLAGS%,$(CFLAGS),;s,%OCSWCC%,$(CC),' \
		$(DOWNLOADDIR)/site.config.m4 > \
		$(WORKSRC)/devtools/Site/site.config.m4 )
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC) && ./Build
	@$(MAKECOOKIE)

test-custom:
	@$(MAKECOOKIE)

install-custom:
	@# install dirs
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
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )

	@# install the binaries
	ginstall -m 755 $(OBJDIR)/$(BINFILES) $(DESTDIR)$(bindir)
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/newaliases
	( for file in $(SBINFILES) ; do \
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(sbindir) ; \
		done )

	@# rename libraries and binaries os-specific
	( for file in `ls $(DESTDIR)$(libdir)`; do  \
		mv $(DESTDIR)$(libdir)/$$file $(DESTDIR)$(libdir)/$(SOLVER).$$file; \
		done )
	( for file in `ls $(DESTDIR)$(bindir)`; do  \
		mv $(DESTDIR)$(bindir)/$$file $(DESTDIR)$(bindir)/$(SOLVER).$$file; \
		done )
	( for file in `ls $(DESTDIR)$(sbindir)`; do  \
		mv $(DESTDIR)$(sbindir)/$$file $(DESTDIR)$(sbindir)/$(SOLVER).$$file;\
		done )

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
	( for file in `cd $(DOWNLOADDIR) && ls *.CSW`; do \
		ginstall -m 644  $(DOWNLOADDIR)/$$file \
		$(DESTDIR)$(sysconfdir)/mail/$$file; \
		done )
	( mv $(DESTDIR)$(sysconfdir)/mail/sm-client.st.CSW \
		$(DESTDIR)/var/opt/csw/spool/clientmqueue/ )
	@$(MAKECOOKIE)

merge-OS:
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
