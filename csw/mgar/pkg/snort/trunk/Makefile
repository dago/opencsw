GARNAME = snort
GARVERSION = 2.8.5
CATEGORIES = net

DESCRIPTION = The open source Network Intrusion Detection System
define BLURB
   Snort is an open source network intrusion prevention and detection
   system utilizing a rule-driven language, which combines the benefits
   of signature, protocol and anomaly based inspection methods. With
   millions of downloads to date, Snort is the most widely deployed
   intrusion detection and prevention technology worldwide and has
   become the de facto standard for the industry.
endef

MASTER_SITES = http://dl.snort.org/snort-current/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz

REQUIRED_PKGS  = CSWpcrert CSWlibpcap CSWgcc4corert
#REQUIRED_PKGS += CSWosslrt CSWmysql4rt CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

GARCOMPILER = GNU

CONFIGURE_ARGS  = $(DIRPATHS) --libdir=/opt/csw/lib
CONFIGURE_ARGS += --enable-dynamicplugin

TEST_TARGET = check

SAMPLECONF = /etc/opt/csw/snort/snort.conf

include gar/category.mk

post-install-modulated:
	@ginstall -d -m 755 $(DESTDIR)/etc/opt/csw/snort
	@cp $(WORKSRC)/etc/snort.conf $(DESTDIR)/etc/opt/csw/snort/snort.conf
	@cp $(WORKSRC)/etc/unicode.map $(DESTDIR)/etc/opt/csw/snort/unicode.map
	@cp $(WORKSRC)/etc/sid-msg.map $(DESTDIR)/etc/opt/csw/snort/sid-msg.map
	@cp $(WORKSRC)/etc/gen-msg.map $(DESTDIR)/etc/opt/csw/snort/gen-msg.map
	@cp $(WORKSRC)/etc/classification.config $(DESTDIR)/etc/opt/csw/snort/classification.config
	@cp $(WORKSRC)/etc/reference.config $(DESTDIR)/etc/opt/csw/snort/reference.config
#	@cp $(WORKSRC)/etc/generators $(DESTDIR)/etc/opt/csw/snort/generators
	@$(MAKECOOKIE)
