# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = logstash
VERSION = 1.5.1
GARTYPE = v2

DESCRIPTION = A tool for managing events and logs

MASTER_SITES = https://download.elasticsearch.org/logstash/logstash/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += logstash
DISTFILES += cswlogstash.xml

PATCHFILES += 0001-Use-correct-grep.patch

NOGITPATCH = 1

VENDOR_URL = http://www.logstash.net

PACKAGES += CSWlogstash
SPKG_DESC_CSWlogstash = A tool for managing events and logs
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlogstash += CSWjre8
# This can not be tracked with checkpkg
CHECKPKG_OVERRIDES_CSWlogstash += surplus-dependency|CSWjre8

# Reorganizing is difficult, delay for now
CHECKPKG_OVERRIDES_CSWlogstash += discouraged-path-in-pkgmap
CHECKPKG_OVERRIDES_CSWlogstash += binary-architecture-does-not-match-placement

# We use JRuby, so this is ok
CHECKPKG_OVERRIDES_CSWlogstash += missing-dependency|CSWlibruby1-9-1-1|or|CSWruby|or|CSWruby18|or|CSWruby191

# We don't control the binaries
CHECKPKG_OVERRIDES_CSWlogstash += bad-rpath-entry

# This is the DTD for SMF
CHECKPKG_OVERRIDES_CSWlogstash += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/cswlogstash.xml

LICENSE = LICENSE

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/cswlogstash.xml
PROTOTYPE_CLASS_smf = manifest

REMOVE_FILES-sparc += i386-SunOS
REMOVE_FILES-sparc += x86_64-SunOS
REMOVE_FILES-i386 += sparcv9-SunOS

CHECKPKG_OVERRIDES_CSWlogstash += binary-wrong-architecture|file=opt/csw/share/logstash/vendor/jruby/lib/jni/x86_64-SunOS/libjffi-1.2.so|pkginfo-says=sparc|actual-binary=i386


include gar/category.mk

install-custom:
	ginstall -D -m 0755 $(WORKDIR)/logstash $(DESTDIR)$(bindir)/logstash
	ginstall -d -m 0755 $(DESTDIR)$(sharedstatedir)/logstash
	cd $(WORKSRC) && tar cf - . | (cd $(DESTDIR)$(sharedstatedir)/logstash; tar xf -)
	@# Having PPC code in the package confuses checkpkg
	rm -rf $(DESTDIR)$(sharedstatedir)/logstash/vendor/jruby/lib/jni/Darwin
	rm -rf $(DESTDIR)$(sharedstatedir)/logstash/vendor/jruby/lib/jni/*-Linux
	rm -rf $(DESTDIR)$(sharedstatedir)/logstash/vendor/jruby/lib/jni/*-Windows
	rm -rf $(DESTDIR)$(sharedstatedir)/logstash/vendor/jruby/lib/jni/*-AIX
	rm -rf $(DESTDIR)$(sharedstatedir)/logstash/vendor/jruby/lib/jni/*-FreeBSD
	rm -rf $(foreach F,$(REMOVE_FILES-$(GARCH)),$(DESTDIR)$(sharedstatedir)/logstash/vendor/jruby/lib/jni/$$F)
	ginstall -d -m 0755 $(DESTDIR)$(sysconfdir)/logstash/conf.d
	ginstall -D -m 0644 $(WORKDIR)/cswlogstash.xml $(DESTDIR)/var/opt/csw/svc/manifest/cswlogstash.xml
	@$(MAKECOOKIE)
