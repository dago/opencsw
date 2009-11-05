#####################################################################
# OpenCSW build recipe for Cyrus Imap
#
# Copyright 2009 Yann Rouillard <yann@pleiades.fr.eu.org>
# All rights reserved.  Use is subject to license terms.
#
# Redistribution and/or use, with or without modification, is
# permitted.  This software is without warranty of any kind.  The
# author(s) shall not be liable in the event that use of the
# software causes damage.
#####################################################################

###### Package information #######

GARNAME = cyrus_imapd
GARVERSION = 2.3.15
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

PACKAGES = CSWcyrusimapd CSWcyrusimapdutils CSWpmcyrus

SPKG_DESC_CSWcyrusimapd = Pop and Imap server from the Cyrus mail system
CATALOGNAME_CSWcyrusimapd = cyrus_imapd
REQUIRED_PKGS_CSWcyrusimapd = CSWosslrt CSWsasl CSWbdb42 CSWkrb5lib CSWtcpwrap CSWnetsnmp CSWpcrert
SPKG_CLASSES_CSWcyrusimapd = none services cswpreserveconf cswinitsmf

SPKG_DESC_CSWcyrusimapdutils = Various admin utilities for Cyrus Imapd/Popd
CATALOGNAME_CSWcyrusimapdutils = cyrus_imapd_utils
REQUIRED_PKGS_CSWcyrusimapdutils = CSWpmcyrus CSWosslrt CSWsasl CSWbdb42 CSWkrb5lib CSWpcrert
SPKG_CLASSES_CSWcyrusimapdutils = none 

SPKG_DESC_CSWpmcyrus = Perl interface to Cyrus Imap functions
CATALOGNAME_CSWpmcyrus = pm_cyrus
REQUIRED_PKGS_CSWpmcyrus = CSWperl CSWbdb42 CSWosslrt CSWsasl
SPKG_CLASSES_CSWpmcyrus = none


###### Upstream and opencsw files information #######

#MASTER_SITES = ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/ http://email.uoa.gr/download/cyrus/cyrus-imapd-$(GARVERSION)/
MASTER_SITES = ftp://ftp.andrew.cmu.edu/pub/cyrus-mail/ http://email.uoa.gr/download/cyrus/cyrus-imapd-2.3.14/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(shell echo $(GARNAME) | tr '_' '-')-(\d+(?:\.\d+)*).tar.gz

DISTNAME = $(shell echo $(GARNAME) | tr '_' '-')-$(GARVERSION)

DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWcyrusimapd.prototype CSWcyrusimapd.preinstall CSWcyrusimapd.checkinstall
DISTFILES += cyrus_imapd.changelog.CSW README.CSW
DISTFILES += i.services r.services services
DISTFILES += cswcyrus cswcyrus.xml
DISTFILES += imapd.conf cyrus.conf

DISTFILES += CSWpmcyrus.prototype
DISTFILES += CSWcyrusimapdutils.prototype
DISTFILES += cyrus_imapd_utils.changelog.CSW
DISTFILES += pm_cyrus.changelog.CSW

# compile_et is not provided by krb5lib_dev so we must provide our own version
# taken from the krb5 source.
DISTFILES += compile_et et_c.awk et_h.awk

# le fichier install-upgrade de cyrus 2.3.11 est incomplet
DISTFILES += install-upgrade

# University of Athens patchs to allow autocreation of mailboxes
# and autocreation of sub-lolders for filter rules
#PATCHFILES = cyrus-imapd-$(GARVERSION)-autocreate-0.10-0.diff cyrus-imapd-$(GARVERSION)-autosieve-0.6.0.diff 
PATCHFILES = cyrus-imapd-2.3.15-autocreate-0.10-0.diff cyrus-imapd-2.3.14-autosieve-0.6.0.diff 
 
# This patch makes cyrus more tolerant with mails containing
# invalid From headers 
# This avoids "Invalid Message header" error messages
PATCHFILES += cyrus-imapd-acceptinvalidfrom.patch

# This patch makes cyrus more tolerant with mails containing
# contains bare newlines
PATCHFILES += cyrus-imapd-2.3.7-nobarenewlinescheck.patch 

# the default value for allowplaintext changed since 2.3.9
# we restore the previous default value to avoid upgrade problem
PATCHFILES += restore_allowplaintext_default.patch

#GARCOMPILER = GNU
#GNU_CC_OPT = -g
#GNU_LD_OPT = -g

##### Build and installation information #####

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-cyrus-prefix=$(prefix)
CONFIGURE_ARGS += --with-service-path=$(libexecdir)/cyrus 
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/cyrus 
CONFIGURE_ARGS += --with-bdb-libdir=$(prefix)/bdb42/lib 
CONFIGURE_ARGS += --with-bdb-incdir=$(prefix)/bdb42/include 
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-sasl=$(prefix)
CONFIGURE_ARGS += --with-perl=$(prefix)/bin/perl 
CONFIGURE_ARGS += --enable-idled 
CONFIGURE_ARGS += --enable-murder 
CONFIGURE_ARGS += --enable-replication
CONFIGURE_ARGS += --with-snmp=$(prefix)

# we add the args so perl libraries are installed
# in the correct path
INSTALL_ARGS = INSTALLDIRS=vendor

TEST_SCRIPTS = 

include gar/category.mk

# compile_et is missing so we want our to be used
CONFIGURE_ENV += COMPILE_ET="$(CURDIR)/files/compile_et -d $(CURDIR)/files/"

pre-patch:
	cp $(WORKDIR)/install-upgrade $(WORKSRC)/doc/text

pre-configure-modulated:
	# master is a too common name, so we rename it cyrus-master
	cp $(WORKSRC)/man/master.8 $(WORKSRC)/man/cyrus-master.8
	cp $(WORKSRC)/doc/man/master.8.html $(WORKSRC)/doc/man/cyrus-master.8.html
	find $(WORKSRC)/doc/ -type f -exec perl -pi -e 's/(cyrus-)?master/cyrus-master/g' '{}' ';'
	find $(WORKSRC)/man/ -type f -exec perl -pi -e 's/(cyrus-)?master/cyrus-master/g' '{}' ';'
	perl -pi -e 's/(cyrus-)?master/cyrus-master/' $(WORKSRC)/master/Makefile.in

	#  we delete autogenerated error files to force regeneration
	find $(WORKSRC) \( -name "*_err.c" -o -name "*_err.h" \) ! -name "com_err.*" -exec rm {} \;

	@$(MAKECOOKIE)

post-build:
	# we change /etc reference to /opt/csw/etc in doc and scripts,
	# except the sasldb2 path
	( cd $(WORKSRC); \
	find man doc tools -type f -exec perl -pi -e 's/\/etc\//\/opt\/csw\/etc\/cyrus\//g' '{}' ';'; \
	find doc -type f -exec perl -pi -e 's/\/opt\/csw\/etc\/cyrus\/sasldb2/\/opt\/csw\/etc\/sasldb2/g' '{}' ';')
	@$(MAKECOOKIE)

pre-merge:
	# we must create the directory where perl libraries will be installed
	mkdir -p $(PKGROOT)/$(prefix)/lib/perl
	mkdir -p $(PKGROOT)/$(sbindir)
	mkdir -p $(PKGROOT)/$(sysconfdir)/cyrus
	mkdir -p $(PKGROOT)/$(prefix)/share/doc/cyrus_imapd
	@$(MAKECOOKIE)

post-merge:
	# we provide our class action scripts to modify /etc/inet/services
	ginstall $(WORKDIR_FIRSTMOD)/*.services $(WORKDIR)/
	ginstall -D $(WORKDIR_FIRSTMOD)/services $(PKGROOT)/etc/inet/services
	
	# configuration and init file installation
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswcyrus" "$(PKGROOT)/etc/opt/csw/init.d/cswcyrus"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswcyrus.xml" "$(PKGROOT)/var/opt/csw/svc/manifest/network/cswcyrus.xml"
	ginstall -D "$(WORKDIR_FIRSTMOD)/imapd.conf" "$(PKGROOT)/$(sysconfdir)/cyrus/imapd.conf.CSW"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cyrus.conf" "$(PKGROOT)/$(sysconfdir)/cyrus/cyrus.conf.CSW"


	# we install binary under tools as part of the package
	cp -r $(WORKSRC_FIRSTMOD)/tools/* $(PKGROOT)$(sbindir)
	ginstall -D $(PKGROOT)$(sbindir)/arbitronsort.pl $(PKGROOT)$(sbindir)/arbitronsort

	# we want perl script to use opencsw perl
	perl -pi -e 's/exec\s+perl/exec \/opt\/csw\/bin\/perl/g' $(PKGROOT)$(sbindir)/* $(PKGROOT)$(bindir)/*
	( for FILE in convert-sieve.pl mupdate-loadgen.pl translatesieve undohash upgradesieve arbitronsort; do \
	    perl -pi -e 's/^#!\/usr\/(local\/)?bin\/perl/#!\/usr\/bin\/perl/' $(PKGROOT)$(sbindir)/$$FILE; \
	    done )

	# we install the documentation
	cp -r $(WORKSRC_FIRSTMOD)/doc/* $(PKGROOT)/$(docdir)/cyrus_imapd
	( for PKG in cyrus_imapd cyrus_imapd_utils pm_cyrus; do \
		ginstall -D $(WORKDIR_FIRSTMOD)/$$PKG.changelog.CSW $(PKGROOT)/$(docdir)/$$PKG/changelog.CSW; \
		ginstall -D $(WORKDIR_FIRSTMOD)/README.CSW $(PKGROOT)/$(docdir)/$$PKG/README.CSW; \
	  done )

	# we rename some tools with too generic names
	ginstall -D $(PKGROOT)/$(sbindir)/mkimap $(PKGROOT)/$(sbindir)/mkdirs
	( for FILE in mkdirs mknewsgroups dohash undohash rehash; do \
		ginstall -D $(PKGROOT)/$(sbindir)/$$FILE $(PKGROOT)/$(sbindir)/cyrus-$$FILE; \
	  done )
	
	# we fix some permission problems
	chmod -R u+w "$(PKGROOT)/"

	@$(MAKECOOKIE)
