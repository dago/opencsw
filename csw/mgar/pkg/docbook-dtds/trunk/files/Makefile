prefix = /opt/csw
datadir = $(prefix)/share

INSTALL = /opt/csw/bin/ginstall -c
INSTALL_DATA = $(INSTALL) -m 0644
INSTALL_DIR = $(INSTALL) -m 0755 -d

docbookdir = $(datadir)/sgml/docbook

SGML = $(wildcard *-sgml)
XML = $(wildcard *-xml)

SGMLTARG = $(patsubst %,inst-%,$(SGML))
XMLTARG = $(patsubst %,inst-%,$(XML))

.PHONY: $(SGML) $(XMLT)

all: build

install: $(SGMLTARG) $(XMLTARG)

inst-%-sgml: DD=$(DESTDIR)/$(docbookdir)/sgml-dtd-$*$(GARVERSION)-$(PATCHLEVEL)
inst-%-sgml:
	@echo Installing $*-sgml
	@( cd $*-sgml; \
		gmkdir -p $(DD); \
		$(INSTALL_DATA) *dtd *mod $(DD)/; \
		[ -n "`ls *dcl 2>/dev/null`" ] && $(INSTALL_DATA) *dcl $(DD); \
		$(INSTALL_DATA) docbook.cat $(DD)/; \
		if [ -d ent ]; then \
			$(INSTALL_DIR) $(DD)/ent; \
			$(INSTALL_DATA) ent/* $(DD)/ent/; \
		fi )

inst-%-xml: DD=$(DESTDIR)/$(docbookdir)/xml-dtd-$*$(GARVERSION)-$(PATCHLEVEL)
inst-%-xml:
	@echo Installing $*-xml
	@( cd $*-xml; \
		gmkdir -p $(DD); \
		$(INSTALL_DATA) *dtd *mod $(DD)/; \
		[ -n "`ls *dcl 2>/dev/null`" ] && $(INSTALL_DATA) *dcl $(DD); \
		$(INSTALL_DATA) docbook.cat $(DD)/; \
		if [ -d ent ]; then \
			$(INSTALL_DIR) $(DD)/ent; \
			$(INSTALL_DATA) ent/* $(DD)/ent/; \
		fi )

build:
	@echo Nothing to build...dummy statement in action.

showtarg:
	@echo $(SGMLTARG) $(XMLTARG)
