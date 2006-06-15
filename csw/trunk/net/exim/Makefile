GARNAME = exim
GARVERSION = 4.62
CATEGORIES = net

DESCRIPTION = The Exim Mail Transfer Agent
define BLURB
  Exim is a message transfer agent (MTA) developed at the University of
  Cambridge for use on Unix systems connected to the Internet. It is freely
  available under the terms of the GNU General Public Licence. In style it
  is similar to Smail 3, but its facilities are more general. There is a
  great deal of flexibility in the way mail can be routed, and there are
  extensive facilities for checking incoming mail. Exim can be installed in
  place of sendmail, although the configuration of exim is quite different
  to that of sendmail.
endef

MASTER_SITES = ftp://ftp.exim.org/pub/exim/exim4/
DISTFILES  = $(GARNAME)-$(GARVERSION).tar.bz2
DISTFILES += $(call admfiles,CSWexim,depend)

PATCHFILES = Makefile.patch
PATCHDIRLEVEL = 0

LD_OPTIONS = -R/opt/csw/lib/\$$ISALIST -R/opt/csw/lib

# exim doesn't use configure
CONFIGURE_SCRIPTS =

# exim doesn't have a test target
TEST_TARGET =

include ../category.mk

pre-patch:
	(cd $(WORKSRC); \
	cp -p src/EDITME Local/Makefile; \
	cp -p exim_monitor/EDITME Local/eximon.conf)
post-patch:
	(cd $(WORKSRC); make makefile)
