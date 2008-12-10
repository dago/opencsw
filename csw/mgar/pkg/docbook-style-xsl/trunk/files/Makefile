
DESTDIR ?= ... should be overridden by GAR ...
GARVERSION ?= ... should be overridden by GAR ...
PATCHLEVEL ?= ... should be overridden by GAR ...

SHELL = /opt/csw/bin/bash

prefix = $(DESTDIR)/opt/csw
bindir = $(prefix)/bin
datadir = $(prefix)/share

instdir = $(datadir)/sgml/docbook/xsl-stylesheets-$(GARVERSION)-$(PATCHLEVEL)
docdir = $(datadir)/doc/docbookxsl-$(GARVERSION)-$(PATCHLEVEL)

all: install

install: install-xsl install-img install-misc install-docs

install-xsl:
	gmkdir -p $(instdir)/{common,fo,html,htmlhelp/doc,javahelp,lib,template,xhtml,manpages,profiling}
	cp common/*.dtd $(instdir)/common
	cp common/*.xml $(instdir)/common
	cp common/*.xsl $(instdir)/common
	cp fo/*.xml $(instdir)/fo
	cp fo/*.xsl $(instdir)/fo
	cp html/*.xml $(instdir)/html
	cp html/*.xsl $(instdir)/html
	cp htmlhelp/*.xsl $(instdir)/htmlhelp
	cp javahelp/*.xsl $(instdir)/javahelp
	cp lib/lib.xsl $(instdir)/lib
	cp template/README $(instdir)/template
	cp template/*.xml $(instdir)/template
	cp template/*.xsl $(instdir)/template
	cp xhtml/*.xsl $(instdir)/xhtml
	cp manpages/README $(instdir)/manpages
	cp manpages/*.xsl $(instdir)/manpages
	cp profiling/*.xsl $(instdir)/profiling

install-img:
	gmkdir -p $(instdir)/images/callouts
	cp images/*.gif $(instdir)/images
	cp images/*.png $(instdir)/images
	cp images/callouts/*.png $(instdir)/images/callouts

install-misc:
	cp VERSION $(instdir)

install-docs:
	gmkdir -p $(docdir)
	cp BUGS ChangeLog README TODO $(docdir)/
	cp -R doc $(docdir)/