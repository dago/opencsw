# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = logstash-contrib
VERSION = 1.4.2
GARTYPE = v2

DESCRIPTION = A tool for managing events and logs

MASTER_SITES = https://download.elasticsearch.org/logstash/logstash/
DISTFILES += $(DISTNAME).tar.gz
# Taken from logstash
DISTFILES += LICENSE

NOGITPATCH = 1

VENDOR_URL = http://www.logstash.net

PACKAGES += CSWlogstash-contrib
SPKG_DESC_CSWlogstash = A tool for managing events and logs, contributed plugins
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlogstash-contrib += CSWlogstash

# Reorganizing is difficult, delay for now
CHECKPKG_OVERRIDES_CSWlogstash-contrib += discouraged-path-in-pkgmap

# We use JRuby, so this is ok
CHECKPKG_OVERRIDES_CSWlogstash-contrib += missing-dependency|CSWlibruby1-9-1-1|or|CSWruby|or|CSWruby18|or|CSWruby191

# This can not be tracked with checkpkg
CHECKPKG_OVERRIDES_CSWlogstash-contrib += surplus-dependency|CSWlogstash

LICENSE = LICENSE

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	ginstall -d -m 0755 $(DESTDIR)$(sharedstatedir)/logstash
	cd $(WORKSRC) && tar cf - . | (cd $(DESTDIR)$(sharedstatedir)/logstash; tar xf -)
	@$(MAKECOOKIE)
