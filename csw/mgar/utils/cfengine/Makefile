GARNAME = cfengine
GARVERSION = 2.1.20
CATEGORIES = utils

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

MASTER_SITES = ftp://ftp.iu.hio.no/pub/$(GARNAME)/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.gz 
DISTFILES += $(call admfiles,CSWcfengine,)

# Requires GNU texi
PATCHFILES = nodoc.diff

CONFIGURE_ARGS  = $(DIRPATHS)
CONFIGURE_ARGS += --enable-DCE
CONFIGURE_ARGS += --with-berkeleydb=$(tool_prefix)
CONFIGURE_ARGS += --with-openssl=$(tool_prefix)

TEST_TARGET = check

include ../category.mk
