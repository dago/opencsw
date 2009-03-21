GARNAME = lftp
GARVERSION = 3.7.11
CATEGORIES = net

DESCRIPTION = sophisticated command-line ftp/http client
define BLURB
   lftp is a sophisticated command line based file transfer program. Supported protocols include FTP, HTTP, SFTP, and FISH. It has a multithreaded design allowing you to issue and execute multiple commands simultaneously or in the background. It also features mirroring capabilities and will reconnect and continue transfers in the event of a disconnection. Also, if you quit the program while transfers are still in progress, it will switch to nohup mode and finish the transfers in the background. Additional protocols supported: FTP over HTTP proxy, HTTPS and FTP over SSL. There are lots of tunable parameters, including rate limitation, number of connections limitation and more.
endef

MASTER_SITES = http://ftp.yars.free.net/pub/source/lftp/

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(GARNAME)-(\d+(?:\.\d+)*).tar.gz

DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz
DISTFILES += $(call admfiles,CSWlftp,prototype depend)
DISTFILES += changelog.CSW
DISTFILES += i.conf r.conf

# adding the conf classe for handling configuration files
SPKG_CLASSES = none conf

# do some type conversion before munmap call
# so lftp can be compiled with sun cc 
# (patch only mandatory to compile with gnutls)
#PATCHFILES = munmap.patch

CONFIGURE_ARGS = $(DIRPATHS)
# previous maintainer compiled with openssl
# instead of gnutls, no need to change that
CONFIGURE_ARGS += --without-gnutls --with-openssl=/opt/csw

TEST_SCRIPTS =

include gar/category.mk

post-install:
	# po are not installed correctly (I should find a better fix)
	cd $(WORKSRC)/po && $(MAKE) DESTDIR=$(DESTDIR) install_sh=$(CURDIR)/$(WORKSRC)/install-sh install

