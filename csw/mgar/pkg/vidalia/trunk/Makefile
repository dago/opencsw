NAME = vidalia
VERSION = 0.2.19
GARTYPE = v2
CATEGORIES = net

DESCRIPTION = Controller GUI for Tor
define BLURB
Vidalia lets you start and stop Tor, see how much bandwidth you are consuming, see how many circuits you currently have active, see where these circuits are connected on a global map, view messages from Tor about its progress and current state, and let you configure your Tor client, bridge, or relay with a simple interface. Included in Vidalia is an extensive help system which helps you understand all of the options available to you. All of these features are translated into a large number of languages.
endef

MASTER_SITES = https://www.torproject.org/dist/vidalia/
DISTFILES  = $(DISTNAME).tar.gz

LICENSE = LICENSE

# no patches so lets skip this to save a little time
NOGITPATCH = 1

GARCOMPILER = GNU

TEST_SCRIPTS =

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom
INSTALL_SCRIPTS = custom

PACKAGING_PLATFORMS = solaris10-sparc solaris10-i386

include gar/category.mk

configure-custom:
	mkdir $(WORKSRC)/build
	cd $(WORKSRC)/build && /opt/csw/bin/cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=/opt/csw \
	-DCMAKE_EXE_LINKER_FLAGS:STRING='-lsocket -lnsl' \
	-DQT_QMAKE_EXECUTABLE=/opt/csw/gxx/bin/qmake ..
	@$(MAKECOOKIE)

build-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake
	@$(MAKECOOKIE)

install-custom:
	cd $(WORKSRC)/build && /opt/csw/bin/gmake install DESTDIR=$(DESTDIR)
	@$(MAKECOOKIE)
