# : Makefile 9089 2010-03-11 08:34:46Z wahwah $
NAME = amanda
VERSION = 3.2.0
CATEGORIES = apps

DESCRIPTION = The Advanced Maryland Automatic Network Disk Archiver
define BLURB
endef

MASTER_SITES = $(SF_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# File name regex to get notifications about upstream software releases
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

DEP_PKGS = CSWperl CSWreadline CSWlibidn CSWglib2 CSWsasl CSWlibcares CSWggettextrt CSWzlib CSWoldaprt
DEP_PKGS += CSWcurlrt CSWosslrt CSWlibnet

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

include gar/category.mk
