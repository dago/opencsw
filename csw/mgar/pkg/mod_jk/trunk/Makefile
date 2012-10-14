NAME = tomcat-connectors
VERSION = 1.2.37
CATEGORIES = lib
GARTYPE = v2

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

MASTER_SITES = http://www.apache.org/dist/tomcat/tomcat-connectors/jk/
DISTFILES  = $(NAME)-$(VERSION)-src.tar.gz
DISTFILES += httpd-jk.conf.CSW
PACKAGING_PLATFORMS = solaris10-i386
WORKSRC = $(WORKDIR)/$(DISTNAME)-src/native
PATCHDIR = $(WORKDIR)/$(DISTNAME)-src

# Apache paths
AP2_ROOT      = $(prefix)/apache2
AP2_LIBEXEC   = $(DESTDIR)$(AP2_ROOT)/libexec
AP2_APXS      = $(AP2_ROOT)/sbin/apxs
AP2_MODS = 1
AP2_MODFILES += mod_jk.so

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*)-src.tar.gz

AUXCONFIG += workers.properties
AUXCONFIG += workers.properties.minimal
AUXCONFIG += uriworkermap.properties
DISTFILES += $(AUXCONFIG)

PATCHFILES += 0001-Use-correct-paths-for-install-and-logging.patch

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

post-extract-modulated:
	echo $(WORKDIR)
	echo $(WORKSRC)
	@$(MAKECOOKIE)

pre-install:
	install -d $(DESTDIR)$(prefix)/apache2/libexec
	install -d $(DESTDIR)$(prefix)/apache2/etc/extra
	install -d $(DESTDIR)$(datadir)/ap2modjk
	install -d $(DESTDIR)$(docdir)/ap2modjk
	@$(MAKECOOKIE)

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

