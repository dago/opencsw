GARNAME = tuntap
GARVERSION = 1.1
CATEGORIES = net

DESCRIPTION = TUN and TAP virtual network kernel drivers
define BLURB
  TUN (as in network TUNnel) simulates a network layer device and it 
  operates with layer 3 packets such as IP packets.
  TAP (as in network tap) simulates an Ethernet device and it operates 
  with layer 2 packets such as Ethernet frames. TAP is used 
  to create a network bridge, while TUN is used with routing. 
endef

SPKG_SOURCEURL = http://www.whiteboard.ne.jp/~admin2/tuntap/
MASTER_SITES = http://www.whiteboard.ne.jp/~admin2/tuntap/source/tuntap/
# fix Dist
DISTNAME = tuntap
DISTFILES = $(DISTNAME).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

# one Makefile for both packages
PACKAGES = CSWtun CSWtap
CATALOGNAME_CSWtun = tun
SPKG_DESC_CSWtun = tun
CATALOGNAME_CSWtap = tap
SPKG_DESC_CSWtap = tap
# define packagefiles
PKGFILES_CSWtun  = /usr/kernel/drv/tun
PKGFILES_CSWtun += /usr/kernel/drv/tun.conf
PKGFILES_CSWtun += /usr/kernel/drv/sparcv9/tun
PKGFILES_CSWtun += /usr/kernel/drv/amd64/tun
PKGFILES_CSWtun += /usr/include/net/if_tun.h
PKGFILES_CSWtap  = /usr/kernel/drv/tap
PKGFILES_CSWtap += /usr/kernel/drv/tap.conf
PKGFILES_CSWtap += /usr/kernel/drv/sparcv9/tap
PKGFILES_CSWtap += /usr/kernel/drv/amd64/tap
PKGFILES_CSWtap += /usr/include/net/if_tun.h
# prototype group sys directories
PROTOTYPE_FILTER = awk '$$$$3 !~/^\/usr\/include/ && $$$$6 == "bin" { $$$$6 = "sys" } { print }'

# build 64bit modules
BUILD64 = 1
NO_ISAEXEC = 1

# no build tests
SKIPTEST = 1

# we going to use a custom install
INSTALL_SCRIPTS = custom
# extra merging files outside /opt/csw..
EXTRA_MERGE_INCLUDE_FILES  = /usr/kernel/drv/sparcv9/tun
EXTRA_MERGE_INCLUDE_FILES += /usr/kernel/drv/amd64/tun
EXTRA_MERGE_INCLUDE_FILES += /usr/kernel/drv/sparcv9/tap
EXTRA_MERGE_INCLUDE_FILES += /usr/kernel/drv/amd64/tap

# set korrekt module directory
DRV_CONF_DIR = /usr/kernel/drv
ifeq ($(ISA),sparcv9)
        DRV_DIR = /usr/kernel/drv/sparcv9
endif
ifeq ($(ISA),sparcv8)
        DRV_DIR = /usr/kernel/drv
endif
ifeq ($(ISA),amd64)
        DRV_DIR = /usr/kernel/drv/amd64
endif
ifeq ($(ISA),i386)
        DRV_DIR = /usr/kernel/drv
endif

# we will need a postinstall and preremove script
define CSWtun_postinstall
#!/bin/sh
PATH=/usr/bin:/usr/sbin
rem_drv tun > /dev/null 2>&1
echo " ==> Loading tun module"
add_drv tun
endef
define CSWtun_preremove
#!/bin/sh
PATH=/usr/bin:/usr/sbin
echo " ==> Unloading tun module"
rem_drv tun
endef
define CSWtap_postinstall
#!/bin/sh
PATH=/usr/bin:/usr/sbin
rem_drv tap > /dev/null 2>&1
echo " ==> Loading tap module"
add_drv tap
endef
define CSWtap_preremove
#!/bin/sh
PATH=/usr/bin:/usr/sbin
echo " ==> Unloading tap module"
rem_drv tap
endef

include gar/category.mk

# adjust compiler flags
pre-build-modulated:
	perl -pi -e 's@-m64@@' $(WORKSRC)/Makefile
pre-build-isa-amd64:
	perl -pi -e 's@(-D_KERNEL)@$$1 -xmodel=kernel@' $(WORKSRC)/Makefile

# custom install
install-custom:
	@echo " ==> Installing ISA $(ISA)"
	ginstall -d -m 0755 $(DESTDIR)$(DRV_CONF_DIR)
	ginstall -m 644 $(WORKSRC)/tun.conf $(DESTDIR)$(DRV_CONF_DIR)
	ginstall -m 644 $(WORKSRC)/tap.conf $(DESTDIR)$(DRV_CONF_DIR)
	ginstall -d -m 0755 $(DESTDIR)/usr/include/net
	ginstall -m 644 $(WORKSRC)/if_tun.h $(DESTDIR)/usr/include/net
	ginstall -d -m 0755 $(DESTDIR)$(DRV_DIR)
	ginstall -m 644 $(WORKSRC)/tun $(DESTDIR)$(DRV_DIR)
	ginstall -m 644 $(WORKSRC)/tap $(DESTDIR)$(DRV_DIR)
	@$(MAKECOOKIE)
