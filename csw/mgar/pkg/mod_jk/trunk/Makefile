GARNAME = tomcat-connectors
GARVERSION = 1.2.25
CATEGORIES = server

DESCRIPTION = AJP connector module for Apache 2
define BLURB
  JK2 has been put in maintainer mode and no further development will
  take place. The reason for shutting down JK2 development was the lack
  of developers interest. Other reason was lack of users interest in
  adopting JK2, caused by configuration complexity when compared to JK.

  JK2 will have it's successor within core Apache2.1/2.2 distribution.
  We have developed new proxy_ajp that is an addition to the mod_proxy
  and uses Tomcat's AJP protocol stack. It is developped in httpd-2.1
  and integrated in it. We have also developed a new proxy_balancer
  module for load balancing http and ajp protocol stacks.

  JK will be fully supported for all other web servers. The next JK
  release is planned for the end of November. Lots of code from JK2 has
  been ported to JK.
endef

MASTER_SITES = http://www.apache.org/dist/tomcat/tomcat-connectors/jk/source/jk-$(GARVERSION)/
DISTFILES  = $(GARNAME)-$(GARVERSION)-src.tar.gz
ADMINFILES = depend prototype postinstall preremove space
DISTFILES += $(call admfiles,CSWap2modjk,$(ADMINFILES))
DISTFILES += httpd-jk.conf.CSW

AUXCONFIG += workers.properties
AUXCONFIG += workers.properties.minimal
AUXCONFIG += uriworkermap.properties
DISTFILES += $(AUXCONFIG)

WORKSRC = $(WORKDIR)/$(GARNAME)-$(GARVERSION)-src/native

# Make apxs install to the temp dir
PATCHFILES += install.diff

# Fix bad embedded paths in mod_jk.c
PATCHFILES += logging.diff

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --enable-jni
CONFIGURE_ARGS += --enable-prefork
CONFIGURE_ARGS += --disable-static
CONFIGURE_ARGS += --with-java-home=/usr/jdk/latest
CONFIGURE_ARGS += --with-java-platform=2

# No test suite available
TEST_SCRIPTS =

include gar/category.mk

pre-install:
	install -d $(DESTDIR)$(prefix)/apache2/libexec
	install -d $(DESTDIR)$(prefix)/apache2/etc/extra
	install -d $(DESTDIR)$(datadir)/ap2modjk
	install -d $(DESTDIR)$(docdir)/ap2modjk

post-install:
	ginstall -m 0644 \
	  $(WORKDIR)/httpd-jk.conf.CSW $(DESTDIR)$(prefix)/apache2/etc/extra
	for prop in $(AUXCONFIG) ; do \
	  ginstall -m 0644 \
	    $(WORKDIR)/$$prop $(DESTDIR)$(datadir)/ap2modjk ; \
	done
	for doc in LICENSE NOTICE ; do \
	  ginstall -m 0644 \
	    $(WORKSRC)/../$$doc $(DESTDIR)$(docdir)/ap2modjk ; \
	done
	for doc in CHANGES NEWS README STATUS.txt ; do \
	  ginstall -m 0644 \
	    $(WORKSRC)/$$doc $(DESTDIR)$(docdir)/ap2modjk ; \
	done
	@$(MAKECOOKIE)

