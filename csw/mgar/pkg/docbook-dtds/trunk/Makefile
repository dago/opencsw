# Replicate the RHEL5 docbook-dtds-1.0.30.1 rpm for CSW.  Patches are taken
# from that srpm and modified (so paths work for GAR).

# NOTE NOTE NOTE
# If these version numbers change, you'll need to update the postinstall
# and preremove scripts also.
# 20081204 -bw
# NOTE NOTE NOTE

GARNAME = docbookdtds
GARVERSION = 1.0

PATCHLEVEL = 30.1
CATEGORIES = xtra

REQUIRED_PKGS = CSWsgmlcommon CSWxmlcommon CSWopenjade CSWlibxml2

DESCRIPTION = SGML and XML document type definitions for DocBook.
define BLURB
The DocBook Document Type Definition (DTD) describes the syntax of
technical documentation texts (articles, books and manual pages).
This syntax is XML-compliant and is developed by the OASIS consortium.
This package contains SGML and XML versions of the DocBook DTD.
endef

# The following is from the rhel5 1.0.3.1 docbook-dtds spec file.  Given
# this list, we put together the insane list of master_sites and distfiles
# below...the initial wget kinda stinks, but it gets the job done.

# Source0: http://www.oasis-open.org/docbook/sgml/3.0/docbk30.zip
# Source1: http://www.oasis-open.org/docbook/sgml/3.1/docbk31.zip
# Source2: http://www.oasis-open.org/docbook/sgml/4.0/docbk40.zip
# Source3: http://www.oasis-open.org/docbook/sgml/4.1/docbk41.zip
# Source4: http://www.oasis-open.org/docbook/xml/4.1.2/docbkx412.zip
# Source5: http://www.oasis-open.org/docbook/sgml/4.2/docbook-4.2.zip
# Source6: http://www.oasis-open.org/docbook/xml/4.2/docbook-xml-4.2.zip
# Source7: http://www.docbook.org/sgml/4.3/docbook-4.3.zip
# Source8: http://www.docbook.org/xml/4.3/docbook-xml-4.3.zip
# Source9: http://www.docbook.org/sgml/4.4/docbook-4.4.zip
# Source10: http://www.docbook.org/xml/4.4/docbook-xml-4.4.zip

OASIS = http://www.oasis-open.org/docbook
DOCBOOK = http://www.docbook.org

# based on the above, we'll need to look for files in the following locations
# ...basically one file per url.  that blows, eh?
O_SRC = $(OASIS)/sgml/3.0/ $(OASIS)/sgml/3.1/ $(OASIS)/sgml/4.0/
O_SRC += $(OASIS)/sgml/4.1/ $(OASIS)/xml/4.1.2/ $(OASIS)/sgml/4.2/
O_SRC += $(OASIS)/xml/4.2/
D_SRC = $(DOCBOOK)/sgml/4.3/ $(DOCBOOK)/xml/4.3/ $(DOCBOOK)/sgml/4.4/
D_SRC += $(DOCBOOK)/xml/4.4/

# the various files we'll need to fetch from the various sources
DBFILES = docbk30.zip docbk31.zip docbk40.zip docbk41.zip docbkx412.zip
DBFILES += docbook-4.2.zip docbook-xml-4.2.zip docbook-4.3.zip
DBFILES += docbook-xml-4.3.zip docbook-4.4.zip docbook-xml-4.4.zip

MASTER_SITES = $(O_SRC) $(D_SRC)
DISTFILES  = $(DBFILES)
DISTFILES += $(call admfiles,CSWdocbookdtds,postinstall preremove)

PATCHFILES = docbook-4.2-euro.patch docbook-dtd30-sgml-1.0.catalog.patch
PATCHFILES += docbook-dtd31-sgml-1.0.catalog.patch
PATCHFILES += docbook-dtd40-sgml-1.0.catalog.patch
PATCHFILES += docbook-dtd41-sgml-1.0.catalog.patch
PATCHFILES += docbook-dtd42-sgml-1.0.catalog.patch
PATCHFILES += docbook-dtds-ents.patch
PATCHFILES += add_makefile.patch

# we don't need no stinkin' configure! :)
CONFIGURE_SCRIPTS = 
# no tests either.
TEST_SCRIPTS = 

# nothing to build either...
BUILD_SCRIPTS = 

INSTALL_ARGS = DESTDIR=$(DESTDIR) GARVERSION=$(GARVERSION) PATCHLEVEL=$(PATCHLEVEL)

include gar/category.mk

# ok, for each source, we make an explicit target that overrides the implicit
# zip-extract-% targets in GAR.
zip-extract-docbk30.zip:
	ginstall -d $(WORKSRC)/3.0-sgml
	unzip $(DOWNLOADDIR)/docbk30.zip -d $(WORKSRC)/3.0-sgml
	@$(MAKECOOKIE)

zip-extract-docbk31.zip: 
	ginstall -d $(WORKSRC)/3.1-sgml
	unzip $(DOWNLOADDIR)/docbk31.zip -d $(WORKSRC)/3.1-sgml
	@$(MAKECOOKIE)

zip-extract-docbk40.zip:
	ginstall -d $(WORKSRC)/4.0-sgml
	unzip $(DOWNLOADDIR)/docbk40.zip -d $(WORKSRC)/4.0-sgml
	@$(MAKECOOKIE)

zip-extract-docbk41.zip:
	ginstall -d $(WORKSRC)/4.1-sgml
	unzip $(DOWNLOADDIR)/docbk41.zip -d $(WORKSRC)/4.1-sgml
	@$(MAKECOOKIE)

zip-extract-docbook-4.2.zip:
	ginstall -d $(WORKSRC)/4.2-sgml
	unzip $(DOWNLOADDIR)/docbook-4.2.zip -d $(WORKSRC)/4.2-sgml
	@$(MAKECOOKIE)

zip-extract-docbkx412.zip:
	ginstall -d $(WORKSRC)/4.1.2-xml
	unzip $(DOWNLOADDIR)/docbkx412.zip -d $(WORKSRC)/4.1.2-xml
	@$(MAKECOOKIE)


zip-extract-docbook-4.3.zip:
	ginstall -d $(WORKSRC)/4.3-sgml
	unzip $(DOWNLOADDIR)/docbook-4.3.zip -d $(WORKSRC)/4.3-sgml
	@$(MAKECOOKIE)

zip-extract-docbook-4.4.zip:
	ginstall -d $(WORKSRC)/4.4-sgml
	unzip $(DOWNLOADDIR)/docbook-4.4.zip -d $(WORKSRC)/4.4-sgml
	@$(MAKECOOKIE)

zip-extract-docbook-xml-4.2.zip:
	ginstall -d $(WORKSRC)/4.2-xml
	unzip $(DOWNLOADDIR)/docbook-xml-4.2.zip -d $(WORKSRC)/4.2-xml
	@$(MAKECOOKIE)

zip-extract-docbook-xml-4.3.zip:
	ginstall -d $(WORKSRC)/4.3-xml
	unzip $(DOWNLOADDIR)/docbook-xml-4.3.zip -d $(WORKSRC)/4.3-xml
	@$(MAKECOOKIE)

zip-extract-docbook-xml-4.4.zip:
	ginstall -d $(WORKSRC)/4.4-xml
	unzip $(DOWNLOADDIR)/docbook-xml-4.4.zip -d $(WORKSRC)/4.4-xml
	@$(MAKECOOKIE)

post-extract:
	# Increase NAMELEN (bug #36058, bug #159382). [bug references from
	# rpm .spec file]
	( cd $(WORKSRC_FIRSTMOD); \
		gsed -e's,\(NAMELEN\s\+\)44\(\s\*\)\?,\1256,' -i.namelen \
			*/docbook.dcl )

	@$(MAKECOOKIE)
