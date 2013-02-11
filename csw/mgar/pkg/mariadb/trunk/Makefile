# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = mariadb
VERSION = 5.5.29
GARTYPE = v2

DESCRIPTION = Robust, scalable, and reliable SQL server
define BLURB
endef

MASTER_SITES = http://ftp.heanet.ie/mirrors/mariadb/$(DISTNAME)/kvm-tarbake-jaunty-x86/
#                   https://downloads.mariadb.org/f/mariadb-5.5.29/kvm-tarbake-jaunty-x86/mariadb-5.5.29.tar.gz/from/http:/ftp.heanet.ie/mirrors/mariadb
DISTFILES  = $(DISTNAME).tar.gz
DISTFILES += map.mysql

CONFIGURE_SCRIPTS = custom

GARCOMPILER = GNU
BUILD64 = 1

LINKER_MAPS ?= -M "$(abspath $(WORKDIR)/map.mysql)"

TEST_TARGET =

BUILD_DEP_PKGS += CSWcmake
BUILD_DEP_PKGS += CSWbison
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/mysql-test.*
EXTRA_MERGE_EXCLUDE_FILES += $(prefix)/sql-bench.*
EXTRA_MERGE_EXCLUDE_FILES += $(datadir)/mysql-test.*
# http://forge.mysql.com/wiki/Autotools_to_CMake_Transition_Guide
CMAKE_ARGS += -DCMAKE_INSTALL_PREFIX=$(prefix)
CMAKE_ARGS += -DINSTALL_LAYOUT=RPM
CMAKE_ARGS += -DMYSQL_DATADIR=$(localstatedir)
CMAKE_ARGS += -DSYSCONFDIR=$(sysconfdir)
CMAKE_ARGS += -DINSTALL_BINDIR=$(subst $(prefix)/,,$(bindir))
CMAKE_ARGS += -DINSTALL_SBINDIR=$(subst $(prefix)/,,$(libexecdir))
# CMAKE_ARGS += -DINSTALL_MANDIR=$(subst $(prefix)/,,$(mandir))
CMAKE_ARGS += -DINSTALL_LIBDIR=$(subst $(prefix)/,,$(libdir))
CMAKE_ARGS += -DINSTALL_PLUGINDIR=$(subst $(prefix)/,,$(libdir))/$(NAME)/plugin
CMAKE_ARGS += -DWITH_READLINE=1
CMAKE_ARGS += -DWITH_LIBWRAP=1
CMAKE_ARGS += -DWITH_SSL=system
CMAKE_ARGS += -DWITH_ZLIB=system
CMAKE_ARGS += -DDEFAULT_CHARSET=utf8
CMAKE_ARGS += -DDEFAULT_COLLATION=utf8_general_ci
CMAKE_ARGS += -DWITH_COMMENT='OpenCSW'
CMAKE_ARGS += -DCMAKE_C_FLAGS="$(CFLAGS)"
CMAKE_ARGS += -DCMAKE_CXX_FLAGS="$(CXXFLAGS)"
CMAKE_ARGS += -DBUILD_CONFIG=mysql_release
# CMAKE_ARGS += -DOPENSSL_INCLUDE_DIR="$(includedir)"
# CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
# CMAKE_ARGS += -DCMAKE_PREFIX_PATH="$(prefix)"
CMAKE_ARGS += -DOPENSSL_ROOT_DIR=$(prefix)
# CMAKE_ARGS += -DOPENSSL_SSL_LIBRARIES=$(libdir)/libssl.so
# CMAKE_ARGS += -DOPENSSL_CRYPTO_LIBRARIES=$(libdir)/libcrypto.so
CMAKE_ARGS += -DCMAKE_INCLUDE_PATH="$(includedir)"
CMAKE_ARGS += -DCMAKE_LIBRARY_PATH="$(libdir)"
CMAKE_ARGS += "-DCMAKE_C_FLAGS=$(CFLAGS)"
CMAKE_ARGS += "-DCMAKE_CXX_FLAGS=$(CXXFLAGS)"
CMAKE_ARGS += -DCMAKE_VERBOSE_MAKEFILE=ON

include gar/category.mk

configure-custom:
	(cd $(WORKSRC) && \
	 	/usr/bin/env -i \
		  $(CONFIGURE_ENV) \
			cmake \
			. \
			$(CMAKE_ARGS))
	@$(MAKECOOKIE)
