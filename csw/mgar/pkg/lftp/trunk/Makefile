#####################################################################
# OpenCSW build recipe for lftp
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

GARNAME = lftp
GARVERSION = 4.0.2
CATEGORIES = net

DESCRIPTION = sophisticated command-line ftp/http client
define BLURB
   lftp is a sophisticated command line based file transfer program. Supported protocols include FTP, HTTP, SFTP, and FISH. It has a multithreaded design allowing you to issue and execute multiple commands simultaneously or in the background. It also features mirroring capabilities and will reconnect and continue transfers in the event of a disconnection. Also, if you quit the program while transfers are still in progress, it will switch to nohup mode and finish the transfers in the background. Additional protocols supported: FTP over HTTP proxy, HTTPS and FTP over SSL. There are lots of tunable parameters, including rate limitation, number of connections limitation and more.
endef

PACKAGES = CSWlftp
CATALOGNAME_CSWlftp = lftp

REQUIRED_PKGS = CSWexpat CSWggettextrt CSWiconv CSWosslrt CSWreadline 

# we're using conf handling class from the cswclassutils package
REQUIRED_PKGS += CSWcswclassutils
SPKG_CLASSES = none cswpreserveconf


###### Upstream and opencsw files information #######

MASTER_SITES = http://ftp.yars.free.net/pub/source/lftp/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += CSWlftp.prototype
DISTFILES += changelog.CSW


##### Build and installation information #####

# do some type conversion before munmap call
# so lftp can be compiled with sun cc 
# (patch only mandatory to compile with gnutls)
#PATCHFILES = munmap.patch

CONFIGURE_ARGS = $(DIRPATHS)
# previous maintainer compiled with openssl
# instead of gnutls, no need to change that
CONFIGURE_ARGS += --without-gnutls --with-openssl=/opt/csw

TEST_SCRIPTS =

include gar/category.mk

post-merge:
	@ginstall -D $(PKGROOT)/$(sysconfdir)/lftp.conf $(PKGROOT)/$(sysconfdir)/lftp.conf.CSW
	@ginstall -D $(DOWNLOADDIR)/changelog.CSW $(PKGROOT)/$(docdir)/lftp/changelog.CSW
	@$(MAKECOOKIE)

