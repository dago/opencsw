GARNAME = firefox
GARVERSION = 1.5.0.3
CATEGORIES = apps

DESCRIPTION = mozilla.org browser
define BLURB
  LONG DESCRIPTION
endef

MASTER_SITES = http://releases.mozilla.org/pub/mozilla.org/firefox/releases/1.5.0.3/source/
DISTFILES  = $(GARNAME)-$(GARVERSION)-source.tar.bz2
DISTFILES += $(call admfiles,CSWfirefox,)

PERL="/opt/csw/bin/perl"
PERL5"=/opt/csw/bin/perl"
CFLAGS=-xlibmil
CXXFLAGS="-xlibmil -xlibmopt -features=tmplife -norunpath"
LDFLAGS="-R'\$\$ORIGIN:\$\$ORIGIN/..' -L/opt/csw/lib -R/opt/csw/lib"

export PERL PERL5

CONFIGURE_ARGS = --prefix=$(prefix)
#CONFIGURE_ARGS += PERL='/opt/csw/bin/perl'
#CONFIGURE_ARGS += PERL5='/opt/csw/bin/perl'
#CONFIGURE_ARGS += CFLAGS="-xlibmil"
#CONFIGURE_ARGS += CXXFLAGS="-xlibmil -xlibmopt -features=tmplife -norunpath"
#CONFIGURE_ARGS += LDFLAGS="-R'\$\$ORIGIN:\$\$ORIGIN/..' -R/opt/csw/lib"

ENABLE_TEST = 0

include ../category.mk
