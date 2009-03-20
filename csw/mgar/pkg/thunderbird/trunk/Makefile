GARNAME = thunderbird
GARVERSION = 2.0.0.21
CATEGORIES = apps
DISTNAME = $(GARNAME)

DESCRIPTION =  Mozilla Thunderbird Mail Client
define BLURB
 Thunderbird 2 is the next generation release of the award-winning Thunderbird email client from Mozilla.
endef

MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/$(GARVERSION)/source/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWthunderbird, )

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = (\d+(?:\.\d+)*)
UPSTREAM_MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/thunderbird/releases/

CONFIGURE_ARGS = --prefix=/opt/csw/mozilla/thunderbird

CFLAGS+= -DG_HAVE_ISO_VARARGS
CXXFLAGS+= -DG_HAVE_ISO_VARARGS
LDFLAGS+=-L/usr/lib/lwp -L/opt/csw/mozilla/thunderbird/lib -R/opt/csw/mozilla/thunderbird/lib -L/opt/csw/lib -R/opt/csw/lib

export PERL CFLAGS CXXFLAGS LDFLAGS

PKGS_REQUIRED_CSWthunderbird  = CSWbonobo2 CSWfconfig CSWftype2 CSWgconf2 CSWggettextrt CSWglib2 CSWgnomekeyring CSWgnomevfs2
PKGS_REQUIRED_CSWthunderbird += CSWgtk2 CSWlibart CSWlibatk CSWlibbonoboui CSWlibcairo CSWlibgnome CSWlibgnomecanvas
PKGS_REQUIRED_CSWthunderbird += CSWlibgnomeui CSWlibidl CSWlibpopt CSWlibxft2 CSWlibxrender CSWorbit2 CSWpango CSWzlib

#PATCHFILES = autoconf.mk.in.diff

TEST_SCRIPTS = 

post-extract:
	@mv $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/mozilla $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)
	@$(MAKECOOKIE)

pre-configure:
	@cp $(FILEDIR)/.mozconfig  $(WORKROOTDIR)/build-$(firstword $(MODULATIONS))/$(GARNAME)/.mozconfig

pre-install:
	( if [ ! -d $(DESTDIR)/opt/csw/bin ] ; then mkdir -p $(DESTDIR)/opt/csw/bin ; fi )
	( cd $(DESTDIR)/opt/csw/bin && rm -f thunderbird  && ln -s ../mozilla/thunderbird/bin/thunderbird . )
	( mkdir -p $(DESTDIR)/opt/csw/share/pixmaps )
#	( cp $(WORKDIR)/$(DISTNAME)/other-licenses/branding/thunderbird/mozicon128.png $(DESTDIR)/opt/csw/share/pixmaps/thunderbird.png )
	( mkdir -p $(DESTDIR)/opt/csw/share/applications )
	( cp $(FILEDIR)/thunderbird.desktop $(DESTDIR)/opt/csw/share/applications/thunderbird.desktop )
	( mkdir -p $(DESTDIR)/opt/csw/share/gnome/mime-info )
	( cp $(FILEDIR)/thunderbird.keys $(DESTDIR)/opt/csw/share/gnome/mime-info/thunderbird.keys )

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
#	( gfind $(DESTDIR)/opt/csw -name chromelist.txt -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKDIR)/$(DISTNAME)/\_\_g {}.temp > {} && rm {}.temp"  \; )
#	( gfind $(DESTDIR)/opt/csw/mozilla/thunderbird -name "*.js" -exec bash -c " mv {} {}.temp && gsed -e  s\_`pwd`/$(WORKDIR)/$(DISTNAME)/\_\_g {}.temp > {} && rm {}.temp"  \; )
#	( gfind $(DESTDIR)/opt/csw/mozilla/thunderbird -name "*.jar" -exec bash -c "`pwd`/removeBuildPathFromJar.sh {} `pwd` $(WORKDIR) $(DISTNAME)" \; )

include gar/category.mk

