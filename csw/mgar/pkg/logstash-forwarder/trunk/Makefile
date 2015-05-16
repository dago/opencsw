# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = logstash-forwarder
VERSION = 0.4.0
GARTYPE = v2

DESCRIPTION = Forward Logs for Logstash

MASTER_SITES = https://github.com/elastic/logstash-forwarder/
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += logstash-forwarder.xml

VENDOR_URL = https://github.com/elastic/logstash-forwarder

PACKAGES += CSWlogstash-forwarder
SPKG_DESC_CSWlogstash-forwarder = Forward Logs for Logstash
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWlogstash-forwarder += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlogstash-forwarder += CSWlibgo5

# Due to the way the headers work only 64 bits is supported
CHECKPKG_OVERRIDES_CSWlogstash-forwarder += binary-architecture-does-not-match-placement|file=opt/csw/bin/logstash-forwarder|arch_id=43|arch_name=sparcv9
CHECKPKG_OVERRIDES_CSWlogstash-forwarder += binary-architecture-does-not-match-placement|file=opt/csw/bin/logstash-forwarder|arch_id=62|arch_name=amd64

# This is the DTD for SMF
CHECKPKG_OVERRIDES_CSWlogstash-forwarder += file-with-bad-content|/usr/share|root/var/opt/csw/svc/manifest/logstash-forwarder.xml

LICENSE = LICENSE

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS = custom
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

PRESERVECONF += $(sysconfdir)/logstash-forwarder/logstash-forwarder.conf

PROTOTYPE_MODIFIERS += smf
PROTOTYPE_FILES_smf += /var/opt/csw/svc/manifest/logstash-forwarder.xml
PROTOTYPE_CLASS_smf = manifest

include gar/category.mk

build-custom:
	cd $(WORKSRC) && LD_OPTIONS="$(LD_OPTIONS)" gccgo -o logstash-forwarder -m64 \
		version.go syslog.go config.go prospector.go harvester.go filestate_linux.go filecompare.go \
		event.go spooler.go publisher1.go registrar.go fileinfo_linux.go registrar_other.go logstash-forwarder.go

install-custom:
	ginstall -D -m 0755 $(WORKSRC)/logstash-forwarder $(DESTDIR)$(bindir)/logstash-forwarder
	ginstall -D -m 0644 $(WORKSRC)/logstash-forwarder.conf.example $(DESTDIR)$(sysconfdir)/logstash-forwarder/logstash-forwarder.conf
	ginstall -D -m 0644 $(WORKDIR)/logstash-forwarder.xml $(DESTDIR)/var/opt/csw/svc/manifest/logstash-forwarder.xml
	@$(MAKECOOKIE)
