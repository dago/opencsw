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

NAME = lftp
VERSION = 4.3.1
CATEGORIES = net

DESCRIPTION = A sophisticated command-line ftp/http client
define BLURB
   lftp is a sophisticated command line based file transfer program. Supported protocols include FTP, HTTP, SFTP, and FISH. It has a multithreaded design allowing you to issue and execute multiple commands simultaneously or in the background. It also features mirroring capabilities and will reconnect and continue transfers in the event of a disconnection. Also, if you quit the program while transfers are still in progress, it will switch to nohup mode and finish the transfers in the background. Additional protocols supported: FTP over HTTP proxy, HTTPS and FTP over SSL. There are lots of tunable parameters, including rate limitation, number of connections limitation and more.
endef

PACKAGES = CSWlftp

RUNTIME_DEP_PKGS = CSWexpat
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWlibsocks
RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS += CSWlibreadline6

###### Upstream and opencsw files information #######

MASTER_SITES = http://ftp.yars.free.net/pub/source/lftp/

DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += changelog.CSW

# do some type conversion before munmap call
# so lftp can be compiled with sun cc 
# (patch only mandatory to compile with gnutls)
#PATCHFILES = munmap.patch

# Sun Studio 12 cc supports the __restrict__ keyword
# but CC doesn't, that disturbs autoconf.
# so we have to apply the following modification to 
# lftp-provided autoconf m4 macros
# http://git.savannah.gnu.org/cgit/autoconf.git/commit/?id=aa30765d64d4a50ad7ce83e78b5699223571ef36
PATCHFILES += sun_cc_no_restrict.patch

PATCHFILES += dont_use_csw_getopt_h.patch

# Disable the use of IPV6_V6ONLY function
# It is not mandatory here, lftp uses the option for the torrent listen socket
# it opens a socket first for ipv4 then for ipv6, so the ipv6 one will never
# catch the ipv4 connection even if IPV6_V6ONLY can't be set
PATCHFILES += 0006-no-ipv6_v6only-setsock-option-under-solaris-9.patch

# sun should not be used as a variable as sun is a macro under Solaris
PATCHFILES += do_not_use_sun_as_a_variable.patch

# SUN_LEN macro is not defined under Solaris
PATCHFILES += sun_len_definition.patch

# Update the system-wide lftp.conf path in the man page
PATCHFILES += 0007-update-configuration-files-paths-in-documentation.patch

PRESERVECONF = $(sysconfdir)/lftp.conf
MIGRATE_FILES_CSWlftp = lftp.conf

MERGE_EXCLUDE_FILES  = .*/charset.alias

##### Build and installation information #####

# We don't want Sun Studio RPATH entries
# see http://wiki.opencsw.org/checkpkg-error-tags#bad-rpath-entry
EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS = $(DIRPATHS)

# previous maintainer compiled with openssl
# instead of gnutls, no need to change that
CONFIGURE_ARGS += --without-gnutls --with-openssl=/opt/csw
# Requested see https://www.opencsw.org/mantis/view.php?id=4481
CONFIGURE_ARGS += --with-socksdante

# No test suite here
TEST_SCRIPTS =



include gar/category.mk

# we re-run autoconf because we patched a m4 file
pre-configure-modulated:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

post-merge:
	@ginstall -D $(DOWNLOADDIR)/changelog.CSW $(PKGROOT)/$(docdir)/lftp/changelog.CSW
	@$(MAKECOOKIE)

