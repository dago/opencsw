# $Id$
# TODO (release-critical prefixed with !, non release-critical with *)
#
NAME = sphinx
VERSION = 2.0.6
GARTYPE = v2

DESCRIPTION = An open source full text search server

MASTER_SITES += http://sphinxsearch.com/files/
MASTER_SITES += http://snowball.tartarus.org/dist/
DISTNAME = $(NAME)-$(VERSION)-release
DISTFILES += $(DISTNAME).tar.gz
DISTFILES += libstemmer_c.tgz

PACKAGES += CSWsphinx-search
SPKG_DESC_CSWsphinx-search = An open source full text search server
# PKGFILES is catchall
RUNTIME_DEP_PKGS_CSWsphinx-search += CSWlibiconv2  
RUNTIME_DEP_PKGS_CSWsphinx-search += CSWlibexpat1  
RUNTIME_DEP_PKGS_CSWsphinx-search += CSWlibz1  
RUNTIME_DEP_PKGS_CSWsphinx-search += CSWlibmysqlclient18  
RUNTIME_DEP_PKGS_CSWsphinx-search += CSWlibstdc++6  
RUNTIME_DEP_PKGS_CSWsphinx-search += CSWlibodbc2  
RUNTIME_DEP_PKGS_CSWsphinx-search += CSWlibgcc-s1  

# These are just examples
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/local|root/opt/csw/bin/pentium_pro/searchd
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/local|root/opt/csw/bin/amd64/searchd
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv8plus/searchd
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/local|root/opt/csw/bin/sparcv9/searchd
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/local|root/opt/csw/share/man/man1/indexer.1
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/local|root/etc/opt/csw/sphinx.conf.CSW
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/indextool.1
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/indexer.1
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/search.1
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/searchd.1
CHECKPKG_OVERRIDES_CSWsphinx-search += file-with-bad-content|/usr/share|root/opt/csw/share/man/man1/spelldump.1

GARCOMPILER = GCC4

EXTRA_LINKER_FLAGS += -liconv

BUILD64 = 1
ISAEXEC = 1

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-id64
CONFIGURE_ARGS += --with-libstemmer

# Lets do MySQL first
#CONFIGURE_ARHS += --with-pgsql
#  --with-pgsql-includes   path to PostgreSQL header files
#  --with-pgsql-libs       path to PostgreSQL libraries

CONFIGURE_ARGS += --with-libexpat
CONFIGURE_ARGS += --with-iconv
CONFIGURE_ARGS += --with-syslog

# UnixODBC can't be enabled right now as 64 bit has different type in include, this needs to be fixed first
CONFIGURE_ARGS += --with-unixodbc

# Make sure we find GNU grep before Solaris grep as "grep -q" is uesd to detect postgres presence
CONFIGURE_ENV_PATH = $(prefix)/gnu:$(PATH)

# Test needs a running SQL server
SKIPTEST ?= 1

EXTRA_PAX_ARGS += -s ",$(sysconfdir)/(example.sql),$(docdir)/$(CATALOGNAME)/\$$1,"
EXTRA_PAX_ARGS += -s ",$(sysconfdir)/(sphinx-min\.conf\.dist),$(docdir)/$(CATALOGNAME)/\$$1,"
EXTRA_PAX_ARGS += -s ",($(sysconfdir)/sphinx\.conf)\.dist,\$$1.CSW,"

PRESERVECONF += sphinx.conf

include gar/category.mk

post-extract:
	cp -rp $(WORKDIR)/libstemmer_c/* $(WORKSRC)/libstemmer_c/
	@$(MAKECOOKIE)
