# TODO: Add run.sh for cron update
# TODO: Repository under /var/opt/csw/repos

NAME = opengrok
VERSION = 0.12.1
CATEGORIES = devel

DESCRIPTION = A wicked fast source browser
define BLURB
  OpenGrok is a fast and usable source code search and
  cross reference engine. It helps you search, cross-reference
  and navigate your source tree. It can understand various
  program file formats and version control histories like SCCS,
  RCS, CVS, Subversion and Mercurial. In other words it lets
  you grok (profoundly understand) the open source, hence
  the name OpenGrok. It is written in Java.
endef

MASjava.net/projects/opengrok/downloads/download/
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://opengrok.github.io/OpenGrok/

PACKAGES += CSWopengrok
SPKG_DESC_CSWopengrok = A wicked fast source browser
# PKGFILES is catchall
ARCHALL_CSWopengrok = 1
RUNTIME_DEP_PKGS_CSWopengrok += CSWectags
RUNTIME_DEP_PKGS_CSWopengrok += CSWtomcat8

# The binaries are used from within scripts
CHECKPKG_OVERRIDES_CSWopengrok += surplus-dependency|CSWectags
CHECKPKG_OVERRIDES_CSWopengrok += surplus-dependency|CSWtomcat8

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =
INSTALL_SCRIPTS = custom

include gar/category.mk

install-custom:
	@echo " ==> Installing files"
	rm -rf $(DESTDIR)$(prefix)/share/tomcat8/webapps/source
	ginstall -d $(DESTDIR)$(prefix)/share/tomcat8/webapps/source
	(cat $(WORKSRC)/lib/source.war | \
		(cd $(DESTDIR)$(prefix)/share/tomcat8efix)/share/tomcat5/webapps/source; \
		jar xf /dev/fd/0) \
	)
	@# For Indexing. Structure of opengrok is opengrok in application root
	@# directory and all libs in lib/. We use only WEB-INF whose rectory structure \
	@# is sl#gln -s $(DESTDIR)$(prefix)/share/tomcat8/webapps/source/WEB-INF/lib/. \
	#	$(DESTDIR)$(prefix)/share/tomcat8/webapps/source/WEB-INF/lib/lib

	ginstall -d $(DESTDIR)$(prefix)/share/doc/opengrok
	mv $(DESTDIR)$(prefix)/share/tomcat8/webapps/source/WEB-INF/web.xml \
		$(DESTDIR)$(prefix)/share/tomcat8/webapps/source/WEB-INF/web.xml.CSW
	@# TODO: Apply XML-Starlet to web.xml
	rm -rf $(DESTDIR)$(prefix)/share/doc/opengrok
	ginstall -d $(DESTDIR)$(prefix)/share/doc/opengrok
	@$(MAKECOOKIE)
	

