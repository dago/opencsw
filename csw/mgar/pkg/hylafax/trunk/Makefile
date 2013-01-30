NAME = hylafax
VERSION = 5.5.2
GARTYPE = v2
CATEGORIES = server

DESCRIPTION = An enterprise-class system for sending and receiving facsimiles and alpha-numeric pages
define ECTBLURB
endef

SF_PROJ = hylafax
MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME# )-$(VERSION).tar.gz
DISTFILES += $(call admfiles,CSWhylafax,prototype depend postinstall preremove postremove)
DISTFILES += config.site.CSW
#DISTFILES += cswhylafax.init cswhylafax.xml svc-cswhylafax

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=148904
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = # PATCHFILES += 0001-Use-relative-path.patch

BUILD_DEP_PKGS += CSWopenldap-devPKGS = CSWoldapdevel

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
#export MANPATH=/usr/share/ma#CONFIGURE_ENV = PATH_GSRIP=$(bindir)/gs PS=gs DIR_MAN=$(mandir)
#BUILD_ENV = PATH_GSRIP=$(bindir)/gs PS=gs DIR_MAN=$(mandir)

#EXTRA_CONFIGURE_EXPORTS += PATH_GSRIP
CONFIGURE_ENV_PATH_GSRIP = $(bindir)/gs
#EXTRA_CONFIGURE_EXPORTS += PS
CONFIGURE_ENV_PS = gs
#EXTRA_CONFIGURE_EXPORTS += DIR_MAN
CONFIGURE_ENV_DIR_MAN = $(mandir)

#EXTRA_BUILD_EXPORTS += PATH_GSRIP
BUILD_ENV_PATH_GSRIP = $(bindir)/gs
#EXTRA_BUILD_EXPORTS += PS
BUILD_ENV_PS = gs
#EXTRA_BUILD_EXPORTS += DIR_MAN
BUILD_ENV_DIR_MAN = $(mandir)

#EXTRA_LINKER_FLAGS += -lsocket -lnsl

CONFIGURE_ARGS += --nointeractive
#CONFIGURE_ARGS += --with-INSTALLROOT=$(DESTDIR)

# Hylafax doesn't have a testsuite
TEST_SCRIPTS =

include gar/category.mk

#CFLAGS := $(CFLAGS) -L$(libdir) -R$(libdir) -lsocket -lnsl
#dir) -lsocket -lnsl
CXXFLAGS := $(CXXFLAGS) -L$(libdir) -R$(libdir) -lsocket -l#cp $(WORKDIR)/config.site.CSW $(WORKSRC)/config.site
	cd $(WORKSRC) && perl -npi -e 's{\$$\{DEPTH\}/\$$\{TOPSRCDIR\}}{\$${TOPSRCDIR}}' `find . -type f`
	banner ex
	@$(MAKECOOKIE)

post-install:
	@echo " ==> Fixing permissions"
	#ixing permissions"
	chown -R uucp:uucp $(addprefix $(DESTDIR)$(localstatedir)/spool/hylafax/,info log recvq status sendq doneq docq tmp p#ollq archive FIFO)
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
# 