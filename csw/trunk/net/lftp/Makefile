GARNAME = lftp
GARVERSION = 3.5.11
CATEGORIES = net

DESCRIPTION = sophisticated command-line ftp/http client
define BLURB
   lftp is a sophisticated command line based file transfer program. Supported protocols include FTP, HTTP, SFTP, and FISH. It has a multithreaded design allowing you to issue and execute multiple commands simultaneously or in the background. It also features mirroring capabilities and will reconnect and continue transfers in the event of a disconnection. Also, if you quit the program while transfers are still in progress, it will switch to nohup mode and finish the transfers in the background. Additional protocols supported: FTP over HTTP proxy, HTTPS and FTP over SSL. There are lots of tunable parameters, including rate limitation, number of connections limitation and more.
endef

MASTER_SITES = http://ftp.yars.free.net/pub/source/lftp/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlftp,prototype depend)
DISTFILES += changelog.CSW
DISTFILES += i.conf r.conf

# adding the conf classe for handling configuration files
SPKG_CLASSES = none conf

# NOT NECESSARY ANYMORE: patch accepted upstream
# correct some bugs preventing compilation
# with sun cc
#PATCHFILES += sun_cc_bool_compilation_fix.patch
# this patch need autoconf >= 2.60 not available
# on blastave machines so we will regenerate 
# configure on another machine and copy it during
# the pre-configure.
#DISTFILES += configure config.h.in

# do some type conversion before munmap call
# so lftp can be compiled with sun cc 
# (patch only mandatory to compile with gnutls)
#PATCHFILES = munmap.patch

CONFIGURE_ARGS = $(DIRPATHS)
# previous maintainer compiled with openssl
# instead of gnutls, no need to change that
CONFIGURE_ARGS += --without-gnutls --with-openssl=/opt/csw
#
# for debug build
#GARCOMPILER = GNU
#CONFIGURE_ARGS += --with-debug
#SUN_CC_OPT=-g
#SUN_CXX_OPT=-g
#GNU_CC_OPT = -g
#GNU_CXX_OPT = -g

TEST_SCRIPTS =

include ../category.mk

# NOT NECESSARY ANYMORE: patch accepted upstream
#pre-configure: 
	#cp $(WORKDIR)/configure $(WORKSRC)/configure
	#cp $(WORKDIR)/config.h.in $(WORKSRC)/include/config.h.in

post-install:
	# po are not installed correctly (I should find a better fix)
	cd $(WORKSRC)/po && $(MAKE) DESTDIR=$(DESTDIR) install_sh=$(CURDIR)/$(WORKSRC)/install-sh install
	@ginstall -D $(WORKDIR)/changelog.CSW $(DESTDIR)$(docdir)/$(GARNAME)/changelog.CSW
	@ginstall $(WORKDIR)/i.conf $(WORKDIR)/r.conf $(DESTDIR)

