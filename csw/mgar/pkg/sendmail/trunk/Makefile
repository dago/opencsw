GARNAME = sendmail
GARVERSION = 8.14.3
CATEGORIES = server

DESCRIPTION = Sendmail MTA
define BLURB
  XXX anacronism ;-) need text here
endef

MASTER_SITES = ftp://ftp.sendmail.org/pub/sendmail/
DISTFILES  = $(GARNAME).$(GARVERSION).tar.gz
DISTFILES += cswsendmail site.config.m4
DISTFILES += i.sol8 i.sol9 i.sol10 checkinstall
DISTFILES += $(foreach FILE,$(shell cd $(FILEDIR) && ls *.CSW),$(FILE))

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# we require
SPKG_CLASSES = none cswinitsmf
REQUIRED_PKGS = CSWbdb CSWoldaprt CSWosslrt CSWsasl CSWtcpwrap
PROTOTYPE_FILTER = awk '$$$$3 ~/\/init.d\/cswsquid$$$$/ { $$$$2 = "cswinitsmf" } || $$$$3 ~/sol8\./ { $$$$2 = "sol8" } || $$$$3 ~/sol9\./ { $$$$2 = "sol9" } || $$$$3 ~/sol10\./ { $$$$2 = "sol10" } { print }'


# patch away GNUism
PATCHFILES = patch-CC-M.m4

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = custom
TEST_SCRIPTS      = custom
INSTALL_SCRIPTS   = custom

PRESERVECONF  = $(sysconfdir)/mail/aliases.CSW
PRESERVECONF += $(sysconfdir)/mail/sendmail.cf.CSW
PRESERVECONF += $(sysconfdir)/mail/submit.cf.CSW
PRESERVECONF += $(sysconfdir)/mail/local-host-names.CSW
PRESERVECONF += $(sysconfdir)/mail/trusted-users.CSW
PRESERVECONF += $(sysconfdir)/mail/statistics.CSW

include gar/category.mk

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
	( for file in $(LIBFILES) ; do \
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )

	@# install the binaries
	ginstall -m 755 $(OBJDIR)/$(BINFILES) $(DESTDIR)$(bindir)
	( for file in $(SBINFILES) ; do \
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(sbindir) ; \
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
	cp -p $(DOWNLOADDIR)/cswsendmail $(DESTDIR)/etc/opt/csw/init.d

	@# install configurations, XXX missing submit.cf/sendmail.cf
	( for file in `cd $(DOWNLOADDIR) && ls *.CSW`; do \
		ginstall -m 644  $(DOWNLOADDIR)/$$file \
		$(DESTDIR)$(sysconfdir)/mail/$$file; \
		done )

	@$(MAKECOOKIE)

