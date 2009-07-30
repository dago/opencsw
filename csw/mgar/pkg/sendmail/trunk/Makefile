GARNAME = sendmail
GARVERSION = 8.14.3
CATEGORIES = server

DESCRIPTION = Sendmail MTA
define BLURB
  XXX anacronism ;-) need text here
endef

MASTER_SITES = ftp://ftp.sendmail.org/pub/sendmail/
DISTFILES  = $(GARNAME).$(GARVERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

# If the url used to check for software update is different of MASTER_SITES, then 
# uncomment the next line. Otherwise it is set by default to the value of MASTER_SITES
# UPSTREAM_MASTER_SITES = 

# we require
REQUIRED_PKGS = CSWbdb CSWoldaprt CSWosslrt CSWsasl CSWtcpwrap

# patch away GNUism
PATCHFILES = patch-CC-M.m4

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS     = custom
TEST_SCRIPTS      = custom
#INSTALL_SCRIPTS   = custom

PRESERVECONF  = $(sysconfdir)/mail/aliases.CSW
PRESERVECONF += $(sysconfdir)/mail/sendmail.cf.CSW
PRESERVECONF += $(sysconfdir)/mail/submit.cf.CSW
PRESERVECONF += $(sysconfdir)/mail/local-host-names.CSW
PRESERVECONF += $(sysconfdir)/mail/trusted-users.CSW
PRESERVECONF += $(sysconfdir)/mail/statistics.CSW

include gar/category.mk

OBJDIR    = $(WORKDIR)/$(DISTNAME)/obj.SunOS.`uname -r`.`uname -i`
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
		$(FILEDIR)/site.config.m4 > \
		$(WORKDIR)/$(DISTNAME)/devtools/Site/site.config.m4
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKDIR)/$(DISTNAME) && ./Build
	@$(MAKECOOKIE)

test-custom:
	@$(MAKECOOKIE)

install-custom:
	@# install the binaries
	ginstall -d -m 755 $(DESTDIR)$(libdir)
	( for file in $(LIBFILES) ; do \
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )
	ginstall -d -m 755 $(DESTDIR)$(bindir)
	ginstall -m 755 $(OBJDIR)/$(BINFILES) $(DESTDIR)$(bindir)
	ginstall -d -m 755 $(DESTDIR)$(sbindir)
	ginstall -d -m 755 $(DESTDIR)$(mandir)
	( for file in $(SBINFILES) ; do \
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(sbindir) ; \
		done )
	@# install manpages
	( for file in $(MANFILES1) ; do \
		ginstall -d -m 755 $(DESTDIR)$(mandir)/1 ; \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/1 ; \
		done )
	( for file in $(MANFILES5) ; do \
		ginstall -d -m 755 $(DESTDIR)$(mandir)/5 ; \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/5 ; \
		done )
	( for file in $(MANFILES8) ; do \
		ginstall -d -m 755 $(DESTDIR)$(mandir)/8 ; \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/8 ; \
		done )
	@# install m4/cf macros
	ginstall -d -m 755 $(DESTDIR)$(sharedstatedir)/mail
	find $(WORKDIR)/$(DISTNAME)/cf -type f -exec chmod 644 {} +
	cp -r $(WORKDIR)/$(DISTNAME)/cf $(DESTDIR)$(sharedstatedir)/mail
	@# install startup script
	ginstall -d -m 0755 $(DESTDIR)/etc/opt/csw/init.d
	cp -p $(FILEDIR)/cswsendmail $(DESTDIR)/etc/opt/csw/init.d
	@# install configurations, XXX missing submit.cf/sendmail.cf
	ginstall -d -m 0755 $(DESTDIR)$(etcdir)/mail
	ginstall -m 644 $(WORKDIR)/$(DISTNAME)/sendmail/aliases \
		$(DESTDIR)$(etcdir)/mail/aliases.CSW
	ginstall -m 644 $(OBJDIR)/sendmail/statistics \
		$(DESTDIR)$(etcdir)/mail/statistics.CSW
	ginstall -m 644 $(OBJDIR)/sendmail/helpfile \
		$(DESTDIR)$(etcdir)/mail/helpfile.CSW
	touch $(DESTDIR)$(etcdir)/mail/trusted-users.CSW \
		$(DESTDIR)$(etcdir)/mail/local-host-names.CSW
	@$(MAKECOOKIE)
