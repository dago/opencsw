GARNAME = opengrok
GARVERSION = 0.4
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
DISTFILES += $(call admfiles,CSWopengrok,depend)

CONFIGURE_SCRIPTS =

BUILD_SCRIPTS =

INSTALL_SCRIPTS = custom
install-custom:
	@echo " ==> Installing files"
	@ginstall -d $(DESTDIR)$(prefix)/share/tomcat5/webapps/source
	@SOURCE=`pwd`/$(WORKSRC)/source.war
	(cat $(WORKSRC)/source.war | \
		(cd $(DESTDIR)$(prefix)/share/tomcat5/webapps/source; \
		jar xf /dev/fd/0) \
	)
	# XML-Starlet auf web.xml
	@$(MAKECOOKIE)
	

include ../category.mk
