# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = elasticsearch
VERSION = 1.5.2
GARTYPE = v2

DESCRIPTION = Search & Analyze Data in Real Time

MASTER_SITES += https://download.elastic.co/elasticsearch/elasticsearch/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += cswelasticsearch.xml

VENDOR_URL = https://www.elastic.co/products/elasticsearch
LICENSE = LICENSE.txt

PACKAGES += CSWelasticsearch
SPKG_DESC_CSWelasticsearch =
# PKGFILES is catchall

# This is for the SMF DTD
CHECKPKG_OVERRIDES_CSWelasticsearch += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswelasticsearch.xml

CHECKPKG_OVERRIDES_CSWelasticsearch-sparc += binary-architecture-does-not-match-placement|file=opt/csw/lib/elasticsearch/sigar/libsigar-sparc64-solaris.so|arch_id=43|arch_name=sparcv9
CHECKPKG_OVERRIDES_CSWelasticsearch-i386 += binary-architecture-does-not-match-placement|file=opt/csw/lib/elasticsearch/sigar/libsigar-amd64-solaris.so|arch_id=62|arch_name=amd64

CHECKPKG_OVERRIDES_CSWelasticsearch-sparc += no-direct-binding|/opt/csw/lib/elasticsearch/sigar/libsigar-sparc-solaris.so|is|not|directly|bound|to|soname|libkstat.so.1
CHECKPKG_OVERRIDES_CSWelasticsearch-sparc += no-direct-binding|/opt/csw/lib/elasticsearch/sigar/libsigar-sparc64-solaris.so|is|not|directly|bound|to|soname|libkstat.so.1
CHECKPKG_OVERRIDES_CSWelasticsearch-i386 += no-direct-binding|/opt/csw/lib/elasticsearch/sigar/libsigar-x86-solaris.so|is|not|directly|bound|to|soname|libkstat.so.1
CHECKPKG_OVERRIDES_CSWelasticsearch-i386 += no-direct-binding|/opt/csw/lib/elasticsearch/sigar/libsigar-amd64-solaris.so|is|not|directly|bound|to|soname|libkstat.so.1

# Where does this come from?!?
CHECKPKG_OVERRIDES_CSWelasticsearch-i386 += bad-rpath-entry|/usr/sfw/lib|opt/csw/lib/elasticsearch/sigar/libsigar-amd64-solaris.so

CHECKPKG_OVERRIDES_CSWelasticsearch += $(CHECKPKG_OVERRIDES_CSWelasticsearch-$(GARCH))

REINPLACEMENTS += esconfig1
REINPLACE_MATCH_esconfig1 = /usr/share/elasticsearch/elasticsearch.in.sh
REINPLACE_WITH_esconfig1 =
REINPLACE_FILES_esconfig1 += bin/elasticsearch

REINPLACEMENTS += esconfig2
REINPLACE_MATCH_esconfig2 = /usr/local/share/elasticsearch/elasticsearch.in.sh
REINPLACE_WITH_esconfig2 =
REINPLACE_FILES_esconfig2 += bin/elasticsearch

REINPLACEMENTS += esconfig3
REINPLACE_MATCH_esconfig3 = /opt/elasticsearch/elasticsearch.in.sh
REINPLACE_WITH_esconfig3 = $(bindir)/elasticsearch.in.sh
REINPLACE_FILES_esconfig3 += bin/elasticsearch

REINPLACEMENTS += esconfigin
REINPLACE_MATCH_esconfigin = ES_CLASSPATH=.*
REINPLACE_WITH_esconfigin = ES_CLASSPATH=\$$ES_CLASSPATH:\$$ES_HOME/lib/elasticsearch/elasticsearch-1.5.2.jar:\$$ES_HOME/lib/elasticsearch/*:\$$ES_HOME/lib/elasticsearch/sigar/*
REINPLACE_FILES_esconfigin += bin/elasticsearch.in.sh

REINPLACEMENTS += conf
REINPLACE_MATCH_conf = ARGV=""
REINPLACE_WITH_conf = properties=-Des.default.path.conf=/etc/opt/csw/elasticsearch\nARGV=""
REINPLACE_FILES_conf += bin/elasticsearch

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF += $(sysconfdir)/elasticsearch.yml
SIGAR_i386 += libsigar-x86-solaris.so
SIGAR_i386 += libsigar-amd64-solaris.so
SIGAR_sparc += libsigar-sparc-solaris.so
SIGAR_sparc += libsigar-sparc64-solaris.so

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswelasticsearch.xml
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

install-custom:
	ginstall -D -m 0755 $(WORKSRC)/bin/elasticsearch $(DESTDIR)$(bindir)/elasticsearch
	ginstall -D -m 0755 $(WORKSRC)/bin/elasticsearch.in.sh $(DESTDIR)$(bindir)/elasticsearch.in.sh
	ginstall -D -m 0755 $(WORKSRC)/config/elasticsearch.yml $(DESTDIR)$(sysconfdir)/elasticsearch/elasticsearch.yml
	ginstall -D -m 0755 $(WORKSRC)/config/logging.yml $(DESTDIR)$(sysconfdir)/elasticsearch/logging.yml
	ginstall -D -m 0755 $(WORKSRC)/README.textile $(DESTDIR)$(docdir)/elasticsearch/README.textile
	ginstall -d -m 0755 $(DESTDIR)$(libdir)/elasticsearch
	cp -rp $(WORKSRC)/lib/* $(DESTDIR)$(libdir)/elasticsearch/
	cd $(DESTDIR)$(libdir)/elasticsearch/sigar && rm -f *freebsd* *linux* *macosx* *winnt* \
	  $(filter-out $(SIGAR_$(GARCH)),$(SIGAR_sparc) $(SIGAR_i386))
	ginstall -D -m 0644 $(WORKDIR)/cswelasticsearch.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswelasticsearch.xml
	@$(MAKECOOKIE)
