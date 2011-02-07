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

NAME = cyrus_imapd
VERSION = 2.4.6
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
RUNTIME_DEP_PKGS_CSWcyrusimapd = CSWosslrt CSWsasl CSWbdb42 CSWkrb5lib CSWnetsnmp CSWzlib CSWtcpwrap
#SPKG_CLASSES_CSWcyrusimapd = none services cswpreserveconf cswinitsmf

SPKG_DESC_CSWcyrusimapdutils = Various admin utilities for Cyrus Imapd/Popd
CATALOGNAME_CSWcyrusimapdutils = cyrus_imapd_utils
RUNTIME_DEP_PKGS_CSWcyrusimapdutils = CSWpmcyrus CSWosslrt CSWsasl CSWbdb42 CSWkrb5lib CSWzlib
#SPKG_CLASSES_CSWcyrusimapdutils = none 

SPKG_DESC_CSWpmcyrus = Perl interface to Cyrus Imap functions
CATALOGNAME_CSWpmcyrus = pm_cyrus
RUNTIME_DEP_PKGS_CSWpmcyrus = CSWperl CSWbdb42 CSWosslrt CSWsasl CSWzlib
#SPKG_CLASSES_CSWpmcyrus = none

PKGFILES_CSWcyrusimapd = $(sbindir)/.*
PKGFILES_CSWcyrusimapd += $(sysconfdir)/cyrus
PKGFILES_CSWcyrusimapd += $(docdir)/cyrus_imapd/.*
PKGFILES_CSWcyrusimapd += $(mandir)/man5/.*
PKGFILES_CSWcyrusimapd += $(mandir)/man8/.*
PKGFILES_CSWcyrusimapd += $(libexecdir)/cyrus.*
PKGFILES_CSWcyrusimapd += $(sysconfdir)/cyrus/imapd.conf.CSW
PKGFILES_CSWcyrusimapd += $(sysconfdir)/cyrus/cyrus.conf.CSW
PKGFILES_CSWcyrusimapd += /etc$(prefix)/init.d/cswcyrus
PKGFILES_CSWcyrusimapd += /var$(prefix)/svc/manifest/network/cswcyrus\.xml
PKGFILES_CSWcyrusimapd += $(localstatedir)/cyrus.*

PROTOTYPE_MODIFIERS = cyrusdir
PROTOTYPE_FILES_cyrusdir = $(localstatedir)/cyrus.*
PROTOTYPE_USER_cyrusdir = cyrus
PROTOTYPE_GROUP_cyrusdir = mail

PRESERVECONF = $(sysconfdir)/cyrus/imapd.conf
PRESERVECONF += $(sysconfdir)/cyrus/cyrus.conf
INITSMF = /etc$(prefix)/init.d/cswcyrus
ETCSERVICES = /etc/$(prefix)/pkg/CSWcyrusimapd/services

LICENSE = COPYRIGHT

PKGFILES_CSWcyrusimapdutils = $(bindir)/.*
PKGFILES_CSWcyrusimapdutils += $(mandir)/man1/.*
PKGFILES_CSWcyrusimapdutils += $(docdir)/cyrus_imapd_utils/.*

PKGFILES_CSWpmcyrus = $(perllib)/.*
PKGFILES_CSWpmcyrus += $(mandir)/man3/Cyrus::.*
PKGFILES_CSWpmcyrus += $(docdir)/pm_cyrus/.*


CHECKPKG_OVERRIDES_CSWcyrusimapdutils += surplus-dependency|CSWpmcyrus

# Don't how to properly solve this now
CHECKPKG_OVERRIDES_CSWcyrusimapd += file-collision|/opt/csw/share/man/man8/imapd.8|CSWcourierimap|CSWcyrusimapd


###### Upstream and opencsw files information #######

MASTER_SITES = ftp://ftp.cyrusimap.org/cyrus-imapd/ http://email.uoa.gr/download/cyrus/cyrus-imapd-$(VERSION)/ http://www.vx.sk/download/patches/cyrus-imapd/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(shell echo $(NAME) | tr '_' '-')-(\d+(?:\.\d+)*).tar.gz

DISTNAME = $(shell echo $(NAME) | tr '_' '-')-$(VERSION)

DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += CSWcyrusimapd.preinstall CSWcyrusimapd.checkinstall
DISTFILES += cyrus_imapd.changelog.CSW README.CSW
DISTFILES += services
DISTFILES += cswcyrus cswcyrus.xml
DISTFILES += imapd.conf cyrus.conf

DISTFILES += cyrus_imapd_utils.changelog.CSW
DISTFILES += pm_cyrus.changelog.CSW

# We move from /opt/csw/{etc,var} to /{etc,var}/opt/csw
MIGRATE_FILES_CSWcyrusimapd = cyrus.conf imapd.conf
MIGRATE_SOURCE_DIR = $(prefix)/etc/cyrus
MIGRATE_DEST_DIR = $(sysconfdir)/cyrus



# compile_et is not provided by krb5lib_dev so we must provide our own version
# taken from the krb5 source.
DISTFILES += compile_et et_c.awk et_h.awk

# University of Athens patchs to allow autocreation of mailboxes
# and autocreation of sub-lolders for filter rules
#PATCHFILES = cyrus-imapd-$(VERSION)-autocreate-0.10-0.diff cyrus-imapd-$(VERSION)-autosieve-0.6.0.diff 
PATCHFILES = cyrus-imapd-2.4.4-autocreate-0.10-0.patch cyrus-imapd-2.4.4-autosieve-0.6.0.patch 
 
# This patch makes cyrus more tolerant with mails containing
# invalid From headers 
# This avoids "Invalid Message header" error messages
#PATCHFILES += cyrus-imapd-acceptinvalidfrom.patch

# This patch makes cyrus more tolerant with mails containing
# contains bare newlines
PATCHFILES += cyrus-imapd-2.3.7-nobarenewlinescheck.patch 

# the default value for allowplaintext changed since 2.3.9
# we restore the previous default value to avoid upgrade problem
PATCHFILES += restore_allowplaintext_default.patch

# Make sure the module is self contained. This fixes bug
#   <http://www.opencsw.org/mantis/view.php?id=3766>
PATCHFILES += 0001-Force-linkage-to-libperl.so.patch

# Fix config2header so it works with argument like
# "CC=/path/to/CC arg1 arg2"
# mandatory to work with assignment like
# "CC="/opt/SUNWspro/bin/cc -xrunpath"
PATCHFILES += 0002-fix-config2header.patch

#GARCOMPILER = GNU
#GNU_CC_OPT = -g
#GNU_LD_OPT = -g

##### Build and installation information #####

# to support shared /opt/csw setup
# see http://wiki.opencsw.org/shared-opt-csw-setup
localstatedir   = /var$(prefix)
sysconfdir      = /etc$(prefix)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-cyrus-prefix=$(prefix)
CONFIGURE_ARGS += --with-service-path=$(libexecdir)/cyrus 
CONFIGURE_ARGS += --sysconfdir=$(sysconfdir)/cyrus 
CONFIGURE_ARGS += --with-bdb=db-4.2
CONFIGURE_ARGS += --with-bdb-libdir=$(prefix)/bdb42/lib 
CONFIGURE_ARGS += --with-bdb-incdir=$(prefix)/bdb42/include 
CONFIGURE_ARGS += --with-openssl=$(prefix)
CONFIGURE_ARGS += --with-sasl=$(prefix)
CONFIGURE_ARGS += --with-perl=$(prefix)/bin/perl 
CONFIGURE_ARGS += --enable-idled 
CONFIGURE_ARGS += --enable-murder 
CONFIGURE_ARGS += --enable-replication
CONFIGURE_ARGS += --with-snmp=$(prefix)
CONFIGURE_ARGS += --with-libwrap=$(prefix)
CONFIGURE_ARGS += --disable-nntp

# we add the args so perl libraries are installed
# in the correct path
INSTALL_ARGS = INSTALLDIRS=vendor

TEST_SCRIPTS = 

CYRUS_DAEMONS = fud idled imapd lmtpd lmtpproxyd mupdate notifyd pop3d pop3proxyd proxyd sieved smmapd timsieved

include gar/category.mk

# compile_et is missing so we want our to be used
CONFIGURE_ENV += COMPILE_ET="$(CURDIR)/files/compile_et -d $(CURDIR)/files/"

pre-configure-modulated:
	# master is a too common name, so we rename it cyrus-master
	cp $(WORKSRC)/man/master.8 $(WORKSRC)/man/cyrus-master.8
	cp $(WORKSRC)/doc/man/master.8.html $(WORKSRC)/doc/man/cyrus-master.8.html
	find $(WORKSRC)/doc/ -type f -exec perl -pi -e 's/(cyrus-)?master/cyrus-master/g' '{}' ';'
	find $(WORKSRC)/man/ -type f -exec perl -pi -e 's/(cyrus-)?master/cyrus-master/g' '{}' ';'
	perl -pi -e 's/(cyrus-)?master/cyrus-master/' $(WORKSRC)/master/Makefile.in

	#  we delete autogenerated error files to force regeneration
	# find $(WORKSRC) \( -name "*_err.c" -o -name "*_err.h" \) ! -name "com_err.*" -exec rm {} \;

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

post-merge: fix2build install-tools cyrus-rename install-docs libexec-in-sbin install-cyrus-directory install-additional-files 


# Let's install the files 
install-additional-files:
	# we provide our class action scripts to modify /etc/inet/services
	ginstall -D $(WORKDIR_FIRSTMOD)/services $(PKGROOT)/etc/opt/csw/pkg/CSWcyrusimapd/services
	
	# configuration and init file installation
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswcyrus" "$(PKGROOT)/etc/opt/csw/init.d/cswcyrus"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cswcyrus.xml" "$(PKGROOT)/var/opt/csw/svc/manifest/network/cswcyrus.xml"
	ginstall -D "$(WORKDIR_FIRSTMOD)/imapd.conf" "$(PKGROOT)/$(sysconfdir)/cyrus/imapd.conf.CSW"
	ginstall -D "$(WORKDIR_FIRSTMOD)/cyrus.conf" "$(PKGROOT)/$(sysconfdir)/cyrus/cyrus.conf.CSW"

	@$(MAKECOOKIE)


# Some binaries put under libexec/cyrus should be put under sbin
# to be more easily used
libexec-in-sbin:
	( cd "$(PKGROOT)$(libexecdir)/cyrus/" && \
		for E in *; do \
			echo $(CYRUS_DAEMONS) | grep -w $$E >/dev/null && continue; \
			[ -L $$E ] || ( mv -f $$E ../../sbin/$$E && ln -sf ../../sbin/$$E ); \
		done )
	@$(MAKECOOKIE)
	

# let's create the directory structure where mails 
# and other cyrus stuffs will be stored
install-cyrus-directory:
	for D in sieve config/proc config/db config/socket config/log \
		config/msg config/ptclient mail mail/stage.; do \
		mkdir -p "$(PKGROOT)/$(localstatedir)/cyrus/$$D"; \
	done
	@$(MAKECOOKIE)
	


# Some fixes and cleaning to correctly build the package
fix2build:
	# we fix some permission problems
	chmod -R u+w "$(PKGROOT)/"

	# let's remove pod files
	gfind $(PKGROOT) -name "perllocal.pod" -exec rm '{}' ';'
	# and CVS directories
	gfind $(PKGROOT) -depth -type d -name "CVS" -exec rm -rf '{}' ';'

	# We remove fetchnews man and doc page as we did not build nntp support
	# and as it clashes with leafnode
	rm -f $(PKGROOT)$(mandir)/man8/fetchnews.8
	rm -f $(PKGROOT)$(docdir)/cyrus_imapd/man/fetchnews.8.html
	
	@$(MAKECOOKIE)


# we rename some tools with too generic names
cyrus-rename:
	mv $(PKGROOT)/$(sbindir)/mkimap $(PKGROOT)/$(sbindir)/mkdirs
	( for FILE in mkdirs mknewsgroups dohash undohash rehash; do \
		mv $(PKGROOT)/$(sbindir)/$$FILE $(PKGROOT)/$(sbindir)/cyrus-$$FILE; \
	  done )
	@$(MAKECOOKIE)


# we install the documentation
install-docs:
	cp -r $(WORKSRC_FIRSTMOD)/doc/* $(PKGROOT)/$(docdir)/cyrus_imapd
	( for PKG in cyrus_imapd cyrus_imapd_utils pm_cyrus; do \
		ginstall -D $(WORKDIR_FIRSTMOD)/$$PKG.changelog.CSW $(PKGROOT)/$(docdir)/$$PKG/changelog.CSW; \
		ginstall -D $(WORKDIR_FIRSTMOD)/README.CSW $(PKGROOT)/$(docdir)/$$PKG/README.CSW; \
	  done )
	@$(MAKECOOKIE)

# we install binary under tools as part of the package
install-tools:
	cp -r $(WORKSRC_FIRSTMOD)/tools/* $(PKGROOT)$(sbindir)
	[ -f "$(PKGROOT)$(sbindir)/arbitronsort.pl" ] && mv "$(PKGROOT)$(sbindir)/arbitronsort.pl" "$(PKGROOT)$(sbindir)/arbitronsort"
	for F in config2header config2man not-mkdep migrate-metadata mupdate-loadgen.pl upgradesieve convert-sieve.pl; do \
		rm -f $(PKGROOT)$(sbindir)/$$F; \
	done
	
	# we want perl scripts to use opencsw perl
	perl -pi -e 's/exec\s+perl/exec \/opt\/csw\/bin\/perl/g' $(PKGROOT)$(sbindir)/* $(PKGROOT)$(bindir)/*
	( for FILE in translatesieve undohash arbitronsort; do \
	    perl -pi -e 's/^#!\/usr\/(local\/)?bin\/perl/#!\/usr\/bin\/perl/' $(PKGROOT)$(sbindir)/$$FILE; \
	    done )
	@$(MAKECOOKIE)
