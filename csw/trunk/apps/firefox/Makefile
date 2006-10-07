GARNAME = firefox
GARVERSION = 1.5.0.7
CATEGORIES = apps

DESCRIPTION = Firefox Community Edition
define BLURB
 The award-winning, free Web browser is better than ever. Browse the Web with confidence - Firefox protects you from viruses, spyware and pop-ups. Enjoy improvements to performance, ease of use and privacy. It's easy to import your favorites and settings and get started. Download Firefox now and get the most out of the Web. 
endef

MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/$(GARVERSION)/source/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWfirefox, depend postinstall preremove )

PERL="/opt/csw/bin/perl"
CFLAGS=-xlibmil
CXXFLAGS="-xlibmil -xlibmopt -features=tmplife -norunpath"
LDFLAGS="-R'\$\$ORIGIN:\$\$ORIGIN/..' -L/opt/csw/lib -R/opt/csw/lib"

export PERL CFLAGS CXXFLAGS LDFLAGS

CONFIGURE_ARGS = --prefix=/opt/csw/libexec/firefox

TEST_SCRIPTS =

include ../category.mk

post-extract:
	( mv $(WORKDIR)/mozilla $(WORKDIR)/$(GARNAME)-$(GARVERSION) )
	@$(MAKECOOKIE)

pre-configure:
	( mv $(HOME)/.mozconfig $(HOME)/.mozconfig.pre-CSWfirefox-build )
	( cp $(FILEDIR)/.mozconfig $(HOME)/.mozconfig )

pre-install:
	( mkdir -p $(DESTDIR)/opt/csw/bin )
	( cd $(DESTDIR)/opt/csw/bin && ln -s ../libexec/firefox/bin/firefox )
	( mkdir -p $(DESTDIR)/opt/csw/share/pixmaps )
	( cp $(WORKDIR)/$(GARNAME)-$(GARVERSION)/other-licenses/branding/firefox/mozicon128.png $(DESTDIR)/opt/csw/share/pixmaps/firefox.png )
	( mkdir -p $(DESTDIR)/opt/csw/share/applications )
	( cp $(FILEDIR)/firefox.desktop $(DESTDIR)/opt/csw/share/applications/firefox.desktop )
	( mkdir -p $(DESTDIR)/opt/csw/share/gnome/mime-info )
	( cp $(FILEDIR)/firefox.keys $(DESTDIR)/opt/csw/share/gnome/mime-info/firefox.keys )
post-install:
	( rm -rf $(DESTDIR)/opt/csw/libexec/firefox/include )
