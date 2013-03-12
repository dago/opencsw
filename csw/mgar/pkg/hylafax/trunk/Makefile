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
DIST
EXPANDVARS += config.siteS += config.site.CSW
#DISTFILES += cswhylafax.init cswhylafax.xml svc-cswhylafax

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=148904
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = # PATCHFILES += 0001-Use-relative-path.patch
PATCHFILES += 0002-Return-value-if-function-requires-it.patch

BUILD_DEP_PKGS += CSWlibjbig-dev
BUILD_DEP_PKGS += CSWliblcms2-dev
BUILD_DEP_PKGS += CSWopenldap-dev

PACKAGES += CSWhylafax
SPKG_DESC_CSWhylafax server

DESCRIPTION = An enterprise-class system for sending and receiving facsimiles and # PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWhylafax += CSWlibjbig2
RUNTIME_DEP_PKGS_CSWhylafax += CSWliblcms2-2
RUNTIME_DEP_PKGS_CSWhylafax += CSWlibldap2-4-2
RUNTIME_DEP_PKGS_CSWhylafax += CSWlibz1
RUNTIME_DEP_PKGS_CSWhylafax += CSWlibjpeg7
RUNTIME_DEP_PKGS_CSWhylafax += CSWlibtiff3

INITSMF += /etc/opt/csw/init.d/hylafaxPKGS = CSWoldapdevel

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
#export MANPATH=/usr/share/maEXTRA_CXXFLAGS += -norunpath
# Why does LD_OPTIONS does not work???
# EXTRA_CXXFLAGS += $(LINKER_IGNORE)

# EXTRA_CFLAGS += $(LINKER_IGNORE)

EXTRA_LDFLAGS += $(LD_OPTIONS)

#EXTRA_CXXFLAGS += $(LINKER_DIRECT)
#EXTRA_CXXFLAGS += $(LINKER_IGNORE)ma#CONFIGURE_ENV = PATH_GSRIP=$(bindir)/gs PS=gs DIR_MAN=$(mandir)
#BUILD_ENV = PATH_GSRIP=$(bindir)/gs PS=gs DIR_MAN=$(mandir)

EXTRA_CONFIGURE_EXPORTS += PATH_GSRIP
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

CONFIGURE_ARGS += --nointeractive
CONFIGURE_ARGS += --with-INSTALLROOT=$(DESTDIR)

# Hylafax doesn't have a testsuite
TEST_SCRIPTS =

EXTRA_MERGE_EXCLUDE_FILES += /etc/opt/csw/rc.*
# EXTRA_PAX_ARGS += -s '(/etc/init.d)(/etc/opt/csw/init.d)'

include gar/category.mk

#CFLAGS := $(CFLAGS) -L$(libdir) -R$(libdir) -lsocket -lnsl
#dir) -lsocket -lnsl
CXXFLAGS := $(CXXFLAGS) -L$(libdir) -R$(libdir) -lsocket -lcd $(WORKSRC) && perl -npi -e 's{\$$\{DEPTH\}/\$$\{TOPSRCDIR\}}{\$${TOPSRCDIR}}' `find . -type f`
	@$(MAKECOOKIE)

pre-configure:
	cp $(WORKDIR)/config.site $(WORKSRC)/config.site
	@$(MAKECOOKIE)

post-install:
	@echo " ==> Fixing permissions"
	#ixing permissions"
	chown -R uucp:uucp $(addprefix $(DESTDIR)$(localstatedir)/spool/hylafax/,info log recvq status sendq doneq docq tmp p#ollq archive FIFO)
	@echo " ==> Adinit.d/cswhylafax
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