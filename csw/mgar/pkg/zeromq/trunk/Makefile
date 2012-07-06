NAME = zeromq
VERSION = 2.2.0
GARTYPE = v2
CATEGORIES = lib

DESCRIPTION = Software library for fast, message-based applications
define BLURB
	The 0MQ lightweight messaging kernel is a library which extends the
	standard socket interfaces with features traditionally provided by
	specialized messaging middle-ware products. 0MQ sockets provide an
	abstraction of asynchronous message queues, multiple messaging
	patterns, message filtering (subscriptions), seamless access to
	multiple transport protocols and more.

	This package contains the ZeroMQ shared library.
endef

MASTER_SITES = http://download.zeromq.org/
DISTFILES  += $(DISTNAME).tar.gz
DISTFILES  += set-ulimit-for-build-test

PATCHFILES += 0001-Patching-ltmain.sh-to-prevent-libtool-from-stripping.patch

PACKAGES += CSWlibzmq1
SPKG_DESC_CSWlibzmq1 = Software library for fast, message-based applications
PKGFILES_CSWlibzmq1 += $(call pkgfiles_lib,libzmq.so.1.0.1)
PKGFILES_CSWlibzmq1 += $(call pkgfiles_lib,libzmq.so.1)
PKGFILES_CSWlibzmq1 += $(docdir)/.* 
#CHECKPKG_OVERRIDES_CSWlibzmq1 += pkginfo-opencsw-repository-uncommitted


PACKAGES += CSWlibzmq1-dev
SPKG_DESC_CSWlibzmq1-dev += ZeroMQ development files
PKGFILES_CSWlibzmq1-dev += $(PKGFILES_DEVEL)
PKGFILES_CSWlibzmq1-dev += .*\.7
RUNTIME_DEP_PKGS_CSWlibzmq1-dev += CSWlibzmq1
#CHECKPKG_OVERRIDES_CSWlibzmq1-dev += pkginfo-opencsw-repository-uncommitted

CONFIGURE_ARGS = $(DIRPATHS)

# For tests to succeed on i386 you need to set the ulimit higher than the default of 256.
EXTRA_TEST_ENV += BASH_ENV=$(abspath $(WORKDIR)/set-ulimit-for-build-test)
EXTRA_LINKER_FLAGS = -norunpath

include gar/category.mk

post-install-modulated: DOCDEST = $(DESTDIR)$(docdir)/libzmq1
post-install-modulated: DOCS = AUTHORS ChangeLog COPYING.LESSER MAINTAINERS README  
post-install-modulated:

	# Copy documentation (upstream)
	ginstall -d $(DOCDEST)
	cp $(addprefix $(WORKSRC)/,$(DOCS)) $(DOCDEST)

	@$(MAKECOOKIE)
