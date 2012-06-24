# $Id$
NAME = amanda
VERSION = 3.3.1
CATEGORIES = apps
GARTYPE = v2

DESCRIPTION = The Advanced Maryland Automatic Network Disk Archiver
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

BUILD_DEP_PKGS = CSWlibcares-dev
# libcares?
# DEP_PKGS = CSWperl CSWreadline CSWlibidn CSWglib2 CSWsasl CSWggettextrt CSWzlib CSWoldaprt
# DEP_PKGS += CSWcurlrt CSWosslrt CSWlibnet

VENDOR_URL = http://www.amanda.org

LICENSE = COPYRIGHT

# From packaging/rpm/amanda.spec for reference:

#        --quiet \
#        --prefix=%{PREFIX} \
#        --sysconfdir=%{SYSCONFDIR} \
#        --sharedstatedir=%{LOCALSTATEDIR} \
#        --localstatedir=%{LOCALSTATEDIR} \
#        --libdir=%{LIBDIR} \
#        --includedir=%{INCLUDEDIR} \
#        --with-amdatadir=%{AMDATADIR} \
#        --with-gnuplot=/usr/bin/gnuplot \
#        --with-gnutar=/bin/tar \
#        --with-gnutar-listdir=%{AMANDAHOMEDIR}/gnutar-lists \
#        --with-index-server=localhost \
#        --with-tape-server=localhost \
#        --with-user=%{config_user} \
#        --with-group=%{config_group} \
#        --with-owner=%{packer} \
#        --with-fqdn \
#        --with-bsd-security \
#        --with-bsdtcp-security \
#        --with-bsdudp-security \
#        --with-ssh-security \
#        --with-udpportrange=%{udpportrange} \
#        --with-tcpportrange=%{tcpportrange} \
#        --with-low-tcpportrange=%{low_tcpportrange} \
#        --with-debugging=%{LOGDIR} \
#        --with-assertions \
#        --disable-installperms \
#        %{?without_ipv6}

# Configure a target using Makefile.PL
# _CATEGORY_LD_OPTIONS ?= -L$(libdir) -lperl
# PERL_CONFIGURE_ARGS ?= INSTALLDIRS=vendor $(EXTRA_PERL_CONFIGURE_ARGS)

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-gnuplot=/opt/csw/bin/gnuplot
CONFIGURE_ARGS += --with-gnutar=/opt/csw/bin/gtar
CONFIGURE_ARGS += --disable-installperms
CONFIGURE_ARGS += --with-amperldir=/opt/csw/lib/perl/csw

RUNTIME_DEP_PKGS_CSWamanda += CSWlibcurl4
RUNTIME_DEP_PKGS_CSWamanda += CSWlibglib2-0-0
RUNTIME_DEP_PKGS_CSWamanda += CSWlibgmodule2-0-0
RUNTIME_DEP_PKGS_CSWamanda += CSWlibgobject2-0-0
RUNTIME_DEP_PKGS_CSWamanda += CSWlibgthread2-0-0
RUNTIME_DEP_PKGS_CSWamanda += CSWlibidn11
RUNTIME_DEP_PKGS_CSWamanda += CSWlibintl8
RUNTIME_DEP_PKGS_CSWamanda += CSWlibreadline6
RUNTIME_DEP_PKGS_CSWamanda += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWamanda += CSWlibz1
RUNTIME_DEP_PKGS_CSWamanda += CSWperl

# for opt/csw/lib/charset.alias
RUNTIME_DEP_PKGS_CSWamanda += CSWlibcharset1
CHECKPKG_OVERRIDES_CSWamanda += surplus-dependency|CSWlibcharset1

# man pages
CHECKPKG_OVERRIDES_CSWamanda += file-with-bad-content

include gar/category.mk

post-install-modulated:
	# It belongs to CSWlibcharset1
	rm $(DESTDIR)/opt/csw/lib/charset.alias
	@$(MAKECOOKIE)
