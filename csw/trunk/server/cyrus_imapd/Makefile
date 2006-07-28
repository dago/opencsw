GARNAME = cyrus_imapd
GARVERSION = 2.3.3
CATEGORIES = server

DESCRIPTION = Pop and Imap server from the Cyrus mail system
define BLURB
  The Cyrus IMAP server is generally intended to be run on sealed systems, 
  where normal users are not permitted to log in. The mailbox database is 
  stored in parts of the filesystem that are private to Cyrus. All user 
  access to mail is through the IMAP, POP3, or KPOP protocols. The private 
  mailbox database design gives the server large advantages in efficiency, 
  scalability, and administratability. Multiple concurrent read/write 
  connections to the same mailbox are permitted. The server supports access 
  control lists on mailboxes and storage quotas on mailbox hierarchies, 
  multiple SASL mechanisms, and the Sieve mail filtering language.
endef

MASTER_SITES = ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/
DISTFILES  = $(shell echo $(GARNAME) | tr '_' '-')-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWcyrusimapd,prototype preinstall depend)
DISTFILES += cyrus_imapd.changelog.CSW README.CSW
DISTFILES += i.services r.services services
DISTFILES += i.init r.init i.smf r.smf i.conf r.conf
DISTFILES += cswcyrus cyrus_imapd.xml
DISTFILES += imapd.conf cyrus.conf

DISTFILES += $(call admfiles,CSWpmcyrus,prototype,depend)
DISTFILES += $(call admfiles,CSWcyrusimapdutils,prototype depend)
DISTFILES += cyrus_imapd_utils.changelog.CSW

SPKG_CLASSES = none services conf

# University of Athens patchs to allow autocreation of mailboxes
# and autocreation of sub-lolders for filter rules
PATCHFILES = cyrus-imapd-2.3.3-autocreate-0.10-1.diff cyrus-imapd-2.3.3-autosieve-0.6.0.diff 
 
# This patch adds a new option which allows cyrus to
# accept mails with 8bits characters in header
# PATCHFILES += cyrus-imapd-2.2.7-munge8bit.patch

# This patch makes cyrus more tolerant with mails containing
# invalid From headers 
# This avoids "Invalid Message header" error messages
PATCHFILES += cyrus-imapd-acceptinvalidfrom.patch

# This patch makes cyrus more tolerant with mails containing
# contains bare newlines
PATCHFILES += cyrus-imapd-2.1.15-nobarenewlinescheck.patch 

# master is a too common name, so we rename it cyrus-master
# this patch does a part of this job
PATCHFILES += master-rename.patch 

# files are extracted in cyrus_imapd not cyrus-imapd
WORKSRC = $(WORKDIR)/$(shell echo $(GARNAME) | tr '_' '-')-$(GARVERSION)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-cyrus-prefix=$(prefix)
CONFIGURE_ARGS += --with-service-path=$(libexecdir)/cyrus 
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/cyrus 
CONFIGURE_ARGS += --with-bdb-libdir=$(prefix)/bdb4/lib 
CONFIGURE_ARGS += --with-bdb-incdir=$(prefix)/bdb4/include 
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-sasl=$(prefix)
CONFIGURE_ARGS += --with-perl=$(prefix)/bin/perl 
CONFIGURE_ARGS += --enable-idled 
CONFIGURE_ARGS += --enable-murder 
CONFIGURE_ARGS += --enable-replication
CONFIGURE_ARGS += --without-snmp

# we add the args so perl libraries are installed
# in the correct path
INSTALL_ARGS = INSTALLDIRS=vendor

ENABLE_TEST = 0


include ../category.mk

pre-build:
	# master is a too common name, so we rename it cyrus-master
	cp $(WORKSRC)/man/master.8 $(WORKSRC)/man/cyrus-master.8
	cp $(WORKSRC)/doc/man/master.8.html $(WORKSRC)/doc/man/cyrus-master.8.html
	@$(MAKECOOKIE)

post-build:
	# we change /etc reference to /opt/csw/etc in doc and scripts
	( cd $(WORKSRC); \
	find man doc tools -type f -exec perl -pi -e 's/\/etc\//\/opt\/csw\/etc\/cyrus\//g' '{}' ';')
	@$(MAKECOOKIE)

pre-install:
	# we must create the directory where perl libraries will be installed
	mkdir -p $(DESTDIR)/$(prefix)/lib/perl
	mkdir -p $(DESTDIR)/$(sbindir)
	mkdir -p $(DESTDIR)/$(sysconfdir)/cyrus
	mkdir -p $(DESTDIR)/$(prefix)/share/doc/cyrus_imapd
	@$(MAKECOOKIE)

post-install:
	# we install binary under tools as part of the package
	cp -r $(WORKSRC)/tools/* $(DESTDIR)$(sbindir)
	ginstall -D $(DESTDIR)$(sbindir)/arbitronsort.pl $(DESTDIR)$(sbindir)/arbitronsort

	# we want perl script to use blastwave perl
	perl -pi -e 's/exec\s+perl/exec \/opt\/csw\/bin\/perl/g' $(DESTDIR)$(sbindir)/*
	( for FILE in convert-sieve.pl mupdate-loadgen.pl translatesieve undohash upgradesieve arbitronsort; do \
	    perl -pi -e 's/^#!\/usr\/(local\/)?bin\/perl/#!\/usr\/bin\/perl/' $(DESTDIR)$(sbindir)/$$FILE; \
	    done )

	# we install the documentation
	cp -r $(WORKSRC)/doc/* $(DESTDIR)/$(docdir)/cyrus_imapd
	( for PKG in cyrus_imapd cyrus_imapd_utils; do \
		ginstall -D $(WORKDIR)/$$PKG.changelog.CSW $(DESTDIR)/$(docdir)/$$PKG/changelog.CSW; \
	  done )
	ginstall -D $(WORKDIR)/README.CSW $(DESTDIR)/$(docdir)/cyrus_imapd/README.CSW

	ginstall -D $(WORKDIR)/i.conf $(DESTDIR)/i.conf
	ginstall -D $(WORKDIR)/r.conf $(DESTDIR)/r.conf
	
	ginstall -D $(WORKDIR)/i.init $(DESTDIR)/i.init
	ginstall -D $(WORKDIR)/r.init $(DESTDIR)/r.init
	ginstall -D $(WORKDIR)/i.smf $(DESTDIR)/i.smf
	ginstall -D $(WORKDIR)/r.smf $(DESTDIR)/r.smf
	ginstall -D $(WORKDIR)/cswcyrus $(DESTDIR)/etc/init.d/cswcyrus

	#ginstall -D $(WORKDIR)/cyrus_imapd.xml $(DESTDIR)/$(prefix)/svc/manifest/network/cyrus_imapd.xml

	# the services file containg cyrus service definition
	ginstall -D $(WORKDIR)/i.services $(DESTDIR)/i.services
	ginstall -D $(WORKDIR)/r.services $(DESTDIR)/r.services
	ginstall -D $(WORKDIR)/services $(DESTDIR)/etc/inet/services

	# we rename some tools with too generic names
	ginstall -D $(DESTDIR)/$(sbindir)/mkimap $(DESTDIR)/$(sbindir)/mkdirs
	( for FILE in mkdirs mknewsgroups dohash undohash rehash; do \
		ginstall -D $(DESTDIR)/$(sbindir)/$$FILE $(DESTDIR)/$(sbindir)/cyrus-$$FILE; \
	  done )
	
	# we install the default config files
	ginstall -D $(WORKDIR)/imapd.conf $(DESTDIR)/$(sysconfdir)/cyrus/imapd.conf
	ginstall -D $(WORKDIR)/cyrus.conf $(DESTDIR)/$(sysconfdir)/cyrus/cyrus.conf.CSW

	@$(MAKECOOKIE)
