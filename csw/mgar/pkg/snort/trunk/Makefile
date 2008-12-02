GARNAME = snort
GARVERSION = 2.6.0.2
CATEGORIES = net

DESCRIPTION = The open source Network Intrusion Detection System
define BLURB
Snort® is an open source network intrusion prevention and detection system utilizing a rule-driven language, which combines the benefits of signature, protocol and anomaly based inspection methods. With millions of downloads to date, Snort is the most widely deployed intrusion detection and prevention technology worldwide and has become the de facto standard for the industry.
endef

MASTER_SITES = http://www.snort.org/dl/current/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsnort, depend )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_ARGS = $(DIRPATHS) --libdir=/opt/csw/lib
CONFIGURE_ARGS += --enable-dynamicplugin

TEST_SCRIPTS =

include gar/category.mk

pre-install:
	( mkdir -p $(DESTDIR)/opt/csw/etc )
	( cp $(WORKSRC)/etc/snort.conf $(DESTDIR)/opt/csw/etc/snort.conf.CSW )
	( cp $(WORKSRC)/etc/unicode.map $(DESTDIR)/opt/csw/etc/unicode.map )
	( cp $(WORKSRC)/etc/sid-msg.map $(DESTDIR)/opt/csw/etc/sid-msg.map )
	( cp $(WORKSRC)/etc/gen-msg.map $(DESTDIR)/opt/csw/etc/gen-msg.map )
	( cp $(WORKSRC)/etc/classification.config $(DESTDIR)/opt/csw/etc/classification.config )
	( cp $(WORKSRC)/etc/reference.config $(DESTDIR)/opt/csw/etc/reference.config )
	( cp $(WORKSRC)/etc/generators $(DESTDIR)/opt/csw/etc/generators )
	@$(MAKECOOKIE)

post-install:
	( rm -rf $(DESTDIR)/opt/csw/src )
