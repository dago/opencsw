NAME = scrollkeeper
VERSION = 0.3.14
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Cataloging system for documentation on open systems
define BLURB
 ScrollKeeper is a cataloging system for documentation on open systems. It
 manages documentation metadata (as specified by the Open Source Metadata
 Framework(OMF)) and provides a simple API to allow help browsers to find,
 sort, and search the document catalog. It will also be able to communicate
 with catalog servers on the Net to search for documents which are not on the
 local system. 
endef

MASTER_SITES = $(SF_MIRRORS)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

SPKG_SOURCEURL = http://scrollkeeper.sourceforge.net/

LICENSE = COPYING

RUNTIME_DEP_PKGS = CSWggettextrt CSWiconv CSWlibxml2 CSWlibxslt CSWzlib

# We define upstream file regex so we can be notifed of new upstream software release
UPSTREAM_MASTER_SITES = $(SF_PROJECT_SHOWFILE)=11543
UPSTREAM_USE_SF = 1
UFILES_REGEX = (\d+(?:\.\d+)*)

PATCHFILES = Makefile.in.diff

RUNTIME_DEP_PKGS_CSWscrollkeeper += CSWlibintl8
RUNTIME_DEP_PKGS_CSWscrollkeeper += CSWlibxslt1
RUNTIME_DEP_PKGS_CSWscrollkeeper += CSWlibiconv2
RUNTIME_DEP_PKGS_CSWscrollkeeper += CSWlibxml2-2
RUNTIME_DEP_PKGS_CSWscrollkeeper += CSWlibz1

PRESERVECONF = $(sysconfdir)/scrollkeeper.conf

CHECKPKG_OVERRIDES_CSWscrollkeeper += file-with-bad-content|/usr/local|root/opt/csw/share/doc/scrollkeeper-0.3.14/scrollkeeper-spec.txt
CHECKPKG_OVERRIDES_CSWscrollkeeper += file-with-bad-content|/usr/local|root/opt/csw/share/man/man5/scrollkeeper.conf.5
CHECKPKG_OVERRIDES_CSWscrollkeeper += file-with-bad-content|/usr/share|root/opt/csw/share/doc/scrollkeeper-0.3.14/scrollkeeper-spec.txt
CHECKPKG_OVERRIDES_CSWscrollkeeper += file-with-bad-content|/usr/share|root/opt/csw/share/man/man5/scrollkeeper.conf.5
CHECKPKG_OVERRIDES_CSWscrollkeeper += file-with-bad-content|/usr/share|root/opt/csw/share/scrollkeeper/doc/writing_scrollkeeper_omf_files/C/writing_scrollkeeper_omf_files.xml
# path /usr/share/omf is not bad in general
CHECKPKG_OVERRIDES_CSWscrollkeeper += file-with-bad-content|/usr/share|root/etc/opt/csw/scrollkeeper.conf.CSW

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-omfdirs=/opt/csw/share/omf:/usr/share/omf

TEST_SCRIPTS =

include gar/category.mk

localstatedir = /var/$(prefix)
