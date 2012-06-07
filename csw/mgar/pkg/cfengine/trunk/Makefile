NAME = cfengine
VERSION = 2.2.10
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = A tool for administering Networks of Diverse Machines
define BLURB
  Cfengine is a tool for setting up and maintaining BSD and System-5-like
  operating system optionally attached to a TCP/IP network. You can think of
  cfengine as a very high level language, much higher level than Perl or shell:
  a single statement can result in many hundreds of operations being performed
  on multiple hosts. Cfengine is good at performing a lot of common system
  administration tasks, and allows you to build on its strengths with your own
  scripts. You can also use it as a netwide front-end for `cron'.
endef

SPKG_SOURCEURL = http://www.cfengine.org
MASTER_SITES   = http://www.cfengine.org/tarballs/
DISTFILES      = $(NAME)-$(VERSION).tar.gz 

PACKAGES                     = CSWcfengine
CATALOGNAME_CSWcfengine      = cfengine
SPKG_DESC_CSWcfengine        = A tool for administering Networks of Diverse Machines
RUNTIME_DEP_PKGS_CSWcfengine = CSWlibssl1-0-0 CSWbdb3

PACKAGES                    += CSWcfengine-doc
CATALOGNAME_CSWcfengine-doc  = cfengine_doc
SPKG_DESC_CSWcfengine-doc    = Cfengine documentation
ARCHALL_CSWcfengine-doc      = 1
PKGFILES_CSWcfengine-doc     = .*/share/info/.*
PKGFILES_CSWcfengine-doc    += .*/share/cfengine/.*
OBSOLETED_BY_CSWcfengine-doc = CSWcfenginedoc

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-DCE
CONFIGURE_ARGS += --with-docs
CONFIGURE_ARGS += --with-berkeleydb=/opt/csw/bdb33

GARCOMPILER = GCC3

CHECKPKG_OVERRIDES += missing-dependency|CSWemacscommon
CHECKPKG_OVERRIDES += file-with-bad-content

include gar/category.mk

post-install-modulated:
	echo post-install $(DESTDIR)
	rm -rf $(DESTDIR)/opt/csw/share/info
	@$(MAKECOOKIE)
