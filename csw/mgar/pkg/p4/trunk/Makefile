# Copyright 2009 OpenCSW
# Distributed under the terms of the GNU General Public License v2
# $Id$

GARNAME = p4
GARVERSION = 09.1
CATEGORIES = utils
DESCRIPTION = Perforce command-line client
define BLURB
  The purpose of this build to be able to easily package it up for in-house
  distribution.  It's not intended to be used to distribute p4 client as part
  of the OpenCSW catalog.
endef
SPKG_SOURCEURL = http://www.perforce.com
P4OS_5.8 = solaris8
P4OS_5.9 = solaris9
P4OS_5.10 = solaris10
P4OS = $(P4OS_$(GAROSREL))

P4ARCH_i386 = x86
P4ARCH_amd64 = x86_64
P4ARCH_sparcv8 = sparc
P4ARCH_sparcv9 = sparc64
P4ARCH = $(P4ARCH_$(KERNELISA))
# MASTER_SITES  = http://www.perforce.com/downloads/perforce/r$(GARVERSION)/bin.$(P4OS)$(P4ARCH)/
MASTER_SITES += http://www.perforce.com/perforce/contracts/
PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

DISTFILES  =
DISTFILES += p4-$(GARVERSION)-solaris10x86
DISTFILES += p4-$(GARVERSION)-solaris10x86_64
DISTFILES += p4-$(GARVERSION)-solaris10sparc
DISTFILES += p4-$(GARVERSION)-solaris10sparc64
DISTFILES += commercial.pdf

work/solaris%/download/p4-$(GARVERSION)-solaris10x86:
	wget http://www.perforce.com/downloads/perforce/r$(GARVERSION)/bin.solaris10x86/p4 \
		-P $(PARTIALDIR) \
		-O $@

work/solaris%/download/p4-$(GARVERSION)-solaris10x86_64:
	wget http://www.perforce.com/downloads/perforce/r$(GARVERSION)/bin.solaris10x86_64/p4 \
		-P $(PARTIALDIR) \
		-O $@

work/solaris%/download/p4-$(GARVERSION)-solaris10sparc:
	wget http://www.perforce.com/downloads/perforce/r$(GARVERSION)/bin.solaris10sparc/p4 \
		-P $(PARTIALDIR) \
		-O $@

work/solaris%/download/p4-$(GARVERSION)-solaris10sparc64:
	wget http://www.perforce.com/downloads/perforce/r$(GARVERSION)/bin.solaris10sparc64/p4 \
		-P $(PARTIALDIR) \
		-O $@

LICENSE = commercial.txt
CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = p4
INSTALL_SCRIPTS = p4
TEST_SCRIPTS =
BUILD64 = 1
include gar/category.mk

build-p4:
	pdftotext $(WORKDIR)/commercial.pdf
	@$(MAKECOOKIE)

install-p4:
	ginstall -m 755 -d $(DESTDIR)$(bindir)
	ginstall -m 755 $(WORKDIR)/p4-$(GARVERSION)-solaris10$(P4ARCH) $(DESTDIR)$(bindir)/p4
	ginstall -m 755 -d $(DESTDIR)$(docdir)/p4
	ginstall -m 644 $(DOWNLOADDIR)/commercial.pdf $(DESTDIR)$(docdir)/p4
	@$(MAKECOOKIE)
