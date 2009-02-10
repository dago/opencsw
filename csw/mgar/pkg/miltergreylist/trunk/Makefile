GARNAME = miltergreylist
GARVERSION = 4.2
RELEASE = b1
DISTVERSION = $(GARVERSION)$(RELEASE)
DISTNAME = milter-greylist-$(DISTVERSION)
WORKSRC = $(WORKDIR)/$(DISTNAME)
CATEGORIES = net

DESCRIPTION = greylist mail filtering method
define BLURB
endef

MASTER_SITES = http://ftp.espci.fr/pub/milter-greylist/
DISTFILES  = milter-greylist-$(DISTVERSION).tgz
DISTFILES += $(call admfiles,CSWmiltergreylist,)

REQUIRED_PKGS = CSWsendmail CSWcurlrt CSWgeoip CSWcswclassutils

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = -(\d+(?:\.\d+)*).tgz

#CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS  = --prefix=/opt/csw
CONFIGURE_ARGS += --with-user=bonivart
#CONFIGURE_ARGS += --with-user=greylist
CONFIGURE_ARGS += --with-conffile=/opt/csw/etc/mail/greylist.conf
CONFIGURE_ARGS += --enable-dnsrbl
CONFIGURE_ARGS += --enable-stdio-hack
CONFIGURE_ARGS += --localstatedir=/var/opt/csw/milter-greylist
CONFIGURE_ARGS += --with-libGeoIP=/opt/csw/lib
CONFIGURE_ARGS += --with-libcurl=/opt/csw/lib
CONFIGURE_ARGS += --mandir=/opt/csw/share/man

TEST_SCRIPTS = 

PROTOTYPE_FILTER  = awk '$$$$3 ~ /\/init.d\/cswmiltergreylist$$$$/ { $$$$2 = "cswinitsmf" } $$$$3 ~ /\/greylist.conf.CSW$$$$/ { $$$$2 = "cswcpsampleconf" } $$$$3 ~ /\/var\/opt\/csw\/named/ { $$$$5 = "named" } { print }'

include gar/category.mk

#WORKSRC := $(WORKDIR)/$(GARNAME)-$(GARVERSION)b1
SPKG_SOURCEURL = http://hcpnet.free.fr/milter-greylist
SPKG_REVSTAMP := $(SPKG_REVSTAMP)_rev=$(RELEASE)
