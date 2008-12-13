GARNAME = opengrok
GARVERSION = 0.7
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

MASTER_SITES = http://www.opensolaris.org/os/project/opengrok/files/
DISTFILES = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWopengrok,postinstall preremove)

REQUIRED_PKGS = CSWectags CSWjavasvn CSWtomcat5 CSWmercurial

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS =
BUILD_SCRIPTS =
TEST_SCRIPTS =

INSTALL_SCRIPTS = custom
install-custom:
	@echo " ==> Installing files"
	@rm -rf $(DESTDIR)$(prefix)/share/tomcat5/webapps/source
	@ginstall -d $(DESTDIR)$(prefix)/share/tomcat5/webapps/source
	@(cat $(WORKSRC)/source.war | \
		(cd $(DESTDIR)$(prefix)/share/tomcat5/webapps/source; \
		jar xf /dev/fd/0) \
	)
	@# For Indexing. Structure of opengrok is opengrok in application root
	@# directory and all libs in lib/. We use only WEB-INF whose directory structure \
	@# is slightly different.
	@gln -s $(DESTDIR)$(prefix)/share/tomcat5/webapps/source/WEB-INF/lib/. \
		$(DESTDIR)$(prefix)/share/tomcat5/webapps/source/WEB-INF/lib/lib

	@ginstall -d $(DESTDIR)$(prefix)/share/doc/opengrok
	@ginstall $(WORKSRC)/*.txt \
		$(DESTDIR)$(prefix)/share/doc/opengrok/
	@mv $(DESTDIR)$(prefix)/share/tomcat5/webapps/source/WEB-INF/web.xml \
		$(DESTDIR)$(prefix)/share/tomcat5/webapps/source/WEB-INF/web.xml.CSW
	@# TODO: Apply XML-Starlet to web.xml
	@rm -rf $(DESTDIR)$(prefix)/share/doc/opengrok
	@ginstall -d $(DESTDIR)$(prefix)/share/doc/opengrok
	@ginstall $(WORKSRC)/*.txt \
		$(DESTDIR)$(prefix)/share/doc/opengrok/
	@$(MAKECOOKIE)
	

include gar/category.mk

# TODO: Add run.sh for cron update
# TODO: Repository under /var/opt/csw/repos
