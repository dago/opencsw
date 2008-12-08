prefix = /opt/csw
sysconfdir = $(prefix)/etc
datadir = $(prefix)/share


INSTALL = /opt/csw/bin/ginstall -c
INSTALL_DATA = $(INSTALL) -m 0644
INSTALL_DIR = $(INSTALL) -m 0755 -d

docbookdir = $(datadir)/sgml/docbook
docdir = $(datadir)/doc/docbookdtds

SGML = $(wildcard *-sgml)
XML = $(wildcard *-xml)

SGMLTARG = $(patsubst %,inst-%,$(SGML))
XMLTARG = $(patsubst %,inst-%,$(XML))

.PHONY: $(SGML) $(XMLT)

all: build

install: $(SGMLTARG) $(XMLTARG) links docs

links: $(SGMLTARG) $(XMLTARG)
	@echo Installing links to most current SGML and XML catalogs
	@( $(INSTALL_DIR) $(DESTDIR)/$(sysconfdir)/sgml; \
		cd $(DESTDIR)/$(sysconfdir)/sgml; \
		[ -h $(DESTDIR)/$(sysconfdir)/sgml/sgml-docbook.cat ] || \
		ln -s sgml-docbook-4.4-$(GARVERSION)-$(PATCHLEVEL).cat \
			$(DESTDIR)/$(sysconfdir)/sgml/sgml-docbook.cat; \
		[ -h $(DESTDIR)/$(sysconfdir)/sgml/xml-docbook.cat ] || \
		ln -s xml-docbook-4.4-$(GARVERSION)-$(PATCHLEVEL).cat \
			$(DESTDIR)/$(sysconfdir)/sgml/xml-docbook.cat )

docs:
	@echo Installing docs
	$(INSTALL_DIR) $(DESTDIR)/$(docdir)/
	for d in *; do \
		if [  "`echo $$d/*txt`" != "$$d/*txt" ]; then \
			$(INSTALL_DIR) $(DESTDIR)/$(docdir)/$$d; \
			$(INSTALL_DATA) $$d/*txt $(DESTDIR)/$(docdir)/$$d/; \
		fi \
	done
	for x in 3 4; do \
		dir=$(DESTDIR)/$(docdir)/$$x.1-sgml; \
		[ -d $$dir ] || $(INSTALL_DIR) $$dir; \
		$(INSTALL_DATA) $$x.1-sgml/ChangeLog $$dir/; \
	done

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
