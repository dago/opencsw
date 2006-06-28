GARNAME = snort
GARVERSION = 2.6.0
CATEGORIES = net

DESCRIPTION = an open source network intrusion prevention and detection system
define BLURB
Snort® is an open source network intrusion prevention and detection system utilizing a rule-driven language, which combines the benefits of signature, protocol and anomaly based inspection methods. With millions of downloads to date, Snort is the most widely deployed intrusion detection and prevention technology worldwide and has become the de facto standard for the industry.
endef

MASTER_SITES = http://www.snort.org/dl/current/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWsnort, prototype )

CONFIGURE_ARGS = $(DIRPATHS)

ENABLE_TEST = 0

include ../category.mk

pre-install:
	( cp -r $(WORKSRC)/../../../files/etc $(DESTDIR)/opt/csw )
	@$(MAKECOOKIE)
