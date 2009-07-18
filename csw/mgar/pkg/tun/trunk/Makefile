GARNAME = tun
GARVERSION = 1.1
CATEGORIES = net

DESCRIPTION = Tunnel software network interface
define BLURB
  TUN (as in network TUNnel) simulates a network layer device and it 
  operates with layer 3 packets such as IP packets. TAP is used 
  to create a network bridge, while TUN is used with routing. 
endef

MASTER_SITES = http://www.whiteboard.ne.jp/~admin2/tuntap/source/tuntap/
DISTFILES = tuntap.tar.gz
# fix distname
DISTNAME = tuntap

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS)

TEST_SCRIPTS =

INSTALL_SCRIPTS = custom

# we will need a postinstall and preremove script
define CSWtun_postinstall
#!/bin/sh

$(REM_DRV) tun > /dev/null 2>&1
echo loading tun module
$(ADD_DRV) tun
endef

define CSWtun_preremove
#!/bin/sh

echo unloading tun module
$(REM_DRV) tun > /dev/null 2>&1
endef

include gar/category.mk

# custom install
INSTALL = /opt/csw/bin/ginstall
ADD_DRV = /usr/sbin/add_drv
REM_DRV = /usr/sbin/rem_drv
DRV_DIR = /usr/kernel/drv
DRV_CONF_DIR = /usr/kernel/drv
install-custom:
	@$(INSTALL) -d -m 0755 $(DESTDIR)/usr/include/net
	@$(INSTALL) -d -m 0755 $(DESTDIR)$(DRV_DIR)
	@$(INSTALL) -m 644 $(WORKSRC)/if_tun.h $(DESTDIR)/usr/include/net
	@$(INSTALL) -m 644 $(WORKSRC)/tun $(DESTDIR)$(DRV_DIR)
	@$(INSTALL) -m 644 $(WORKSRC)/tun.conf $(DESTDIR)$(DRV_CONF_DIR)
	@$(MAKECOOKIE)
