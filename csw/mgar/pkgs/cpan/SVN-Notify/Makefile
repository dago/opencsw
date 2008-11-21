GARNAME = SVN-Notify
GARVERSION = 2.64
CATEGORIES = cpan
AUTHOR = DWHEELER

DESCRIPTION = Subversion activity notification
define BLURB
	This class may be used for sending email messages for Subversion repository
	activity. There are a number of different modes supported, and SVN::Notify
	is fully subclassable, to easily add new functionality. By default, A list
	of all the files affected by the commit will be assembled and listed in a
	single message.
endef

CONFIGURE_SCRIPTS = $(WORKSRC)/Build.PL
BUILD_SCRIPTS = $(WORKSRC)/Build
TEST_SCRIPTS = $(WORKSRC)/Build
INSTALL_SCRIPTS = $(WORKSRC)/Build

DISTFILES = $(call admfiles,CSWpmsvnnotify,prototype)

#DEPENDS += utils/subversion
#DEPENDS += cpan/Module-Build

include ../category.mk
