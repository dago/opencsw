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
CATALOGNAME_CSWlftp = lftp

RUNTIME_DEP_PKGS = CSWexpat
RUNTIME_DEP_PKGS += CSWiconv
RUNTIME_DEP_PKGS += CSWosslrt
RUNTIME_DEP_PKGS += CSWlibsocks
RUNTIME_DEP_PKGS += CSWlibintl8
RUNTIME_DEP_PKGS += CSWlibreadline6


# Reference to configuration file default path for configure, can be safely ignored
CHECKPKG_OVERRIDES_CSWlftp += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/lftp.1


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

# Add a --disable-ipv6 option to configure so we can disable ipv6 support
# under Solaris 9 and workaround "IPV6_V6ONLY symbole missing" issue
# see http://wiki.opencsw.org/porting-faq#toc14
#PATCHFILES += disable_ipv6_configure_option.patch

# Disable the use of IPV6_V6ONLY
PATCHFILES += 0006-no-ipv6_v6only-setsock-option-under-solaris-9.patch

# sun should not be used as a variable as sun is a macro under Solaris
PATCHFILES += do_not_use_sun_as_a_variable.patch

# SUN_LEN macro is not defined under Solaris
PATCHFILES += sun_len_definition.patch

PRESERVECONF = $(sysconfdir)/lftp.conf

MIGRATE_FILES_CSWlftp = lftp.conf

##### Build and installation information #####

# We build solaris 10 specific version to be able to enable
# ipv6 support on these platforms
# see http://wiki.opencsw.org/porting-faq#toc14
#PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386                                        
#PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# to support shared /opt/csw setup
# see http://wiki.opencsw.org/shared-opt-csw-setup
localstatedir   = /var$(prefix)
sysconfdir      = /etc$(prefix)

# We don't want Sun Studio RPATH entries
# see http://wiki.opencsw.org/checkpkg-error-tags#bad-rpath-entry
EXTRA_LINKER_FLAGS = -norunpath

CONFIGURE_ARGS = $(DIRPATHS)

# Solaris 9 does not have IPV6_V6ONLY.
# IPv6 support only works on Solaris 10.
CONFIGURE_ARGS_5.9 = --disable-ipv6
CONFIGURE_ARGS_5.10 = --enable-ipv6
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GAROSREL))

# previous maintainer compiled with openssl
# instead of gnutls, no need to change that
CONFIGURE_ARGS += --without-gnutls --with-openssl=/opt/csw
# Requested see https://www.opencsw.org/mantis/view.php?id=4481
CONFIGURE_ARGS += --with-socksdante

TEST_SCRIPTS =

include gar/category.mk

# we re-run autoconf because we patched a m4 file
pre-configure-modulated:
	cd $(WORKSRC) && autoconf
	@$(MAKECOOKIE)

post-merge:
	@ginstall -D $(DOWNLOADDIR)/changelog.CSW $(PKGROOT)/$(docdir)/lftp/changelog.CSW
	@rm $(PKGROOT)/$(libdir)/charset.alias
	@$(MAKECOOKIE)

