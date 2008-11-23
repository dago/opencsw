GARNAME = hylafax
GARVERSION = 5.2.5
CATEGORIES = server

DESCRIPTION = An enterprise-class system for sending and receiving facsimiles and alpha-numeric pages
define BLURB
endef

SF_PROJ = hylafax
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWhylafax,prototype depend postinstall preremove postremove)
DISTFILES += config.site.CSW
#DISTFILES += cswhylafax.init cswhylafax.xml svc-cswhylafax

PATCHFILES = patch-hylafax.diff

PREREQUISITE_PKGS = CSWoldapdevel

#export CC=/opt/SUNWspro/bin/cc
#export CXX=/opt/SUNWspro/bin/CC
#export CFLAGS="-I/opt/csw/include -L/opt/csw/lib -lsocket -lnsl"
#export CXXFLAGS="-I/opt/csw/include -L/opt/csw/lib -lsocket -lnsl"
#export PATH_GSRIP=/opt/csw/bin/gs
#export PS=gs
#export DIR_MAN=/opt/hylafax/man
#export LDFLAGS="-L/opt/csw/lib -R/opt/csw/lib"
#export PATH=$PATH:/opt/hylafax/sbin:/opt/hylafax/bin
#export LD_LIBRARY_PATH=/opt/csw/lib:/opt/hylafax/lib
#export MANPATH=/usr/share/man:/opt/hylafax/man

CONFIGURE_ENV = PATH_GSRIP=$(bindir)/gs PS=gs DIR_MAN=$(mandir)
BUILD_ENV = PATH_GSRIP=$(bindir)/gs PS=gs DIR_MAN=$(mandir)

CONFIGURE_ARGS = --nointeractive --with-INSTALLROOT=$(DESTDIR)

# Hylafax doesn't has a testsuite
TEST_SCRIPTS =

SPKG_CLASSES = none cswinitsmf

include gar/category.mk

CFLAGS := $(CFLAGS) -L$(libdir) -R$(libdir) -lsocket -lnsl
CXXFLAGS := $(CXXFLAGS) -L$(libdir) -R$(libdir) -lsocket -lnsl

post-extract:
	@echo " ==> Putting config.site in place"
	@cp $(WORKDIR)/config.site.CSW $(WORKSRC)/config.site
	@$(MAKECOOKIE)

post-install:
	@echo " ==> Fixing permissions"
	chown -R uucp:uucp $(addprefix $(DESTDIR)$(localstatedir)/spool/hylafax/,info log recvq status sendq doneq docq tmp pollq archive FIFO)
	@echo " ==> Adding RC-Scripts"
	#-ginstall $(WORKSRC)/etc/hylafax $(DESTDIR)/etc/init.d/cswhylafax
	#-gln -s ../init.d/cswhylafax $(DESTDIR)/etc/rc2.d/S80cswhylafax
	#-$(foreach D,rc0.d rc1.d rcS.d,gln -s ../init.d/hylafax $(DESTDIR)/etc/$D/K20cswhylafax;)
	#ginstall $(WORKSRC)/etc/hylafax $(DESTDIR)/opt/csw/etc/init.d/cswhylafax
	-mkdir -p $(DESTDIR)$(sharedstatedir)/hylafax
	#@$(MAKECOOKIE)

# 1. rmdir /opt/csw/var/spool/hylafax/dev
#    ln -s /dev /opt/csw/var/spool/hylafax/dev
# 2. chown uucp:uucp /opt/csw/var/spool/hylafax 
# 3. chown uucp:uucp /opt/csw/var/spool/hylafax/*
# 4. chown uucp:uucp /opt/csw/var/spool/hylafax/etc/xferfaxlog 


# Modem hinzufuegen und Steuerdateien anlegen:
#   faxaddmodem cua/a001 -> erzeugt /opt/csw/var/spool/hylafax/FIFO.cua_a001
# -> (muss fuer uucp:uucp schreibbar sein!)
# Danach  muss das Modem noch aktiv geschaltet werden:
#   faxmodem cua/a001
