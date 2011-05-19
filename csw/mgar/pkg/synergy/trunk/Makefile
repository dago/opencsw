# TODO (release-critical prefixed with !, non release-critical with *)
#
# ! Doesn't yet build
# "../../lib/server/CConfig.h", line 145: Error: "," expected instead of "<".
# "../../lib/server/CConfig.h", line 145: Error: Use ";" to terminate declarations.
# "../../lib/server/CConfig.h", line 145: Error: "}" expected instead of "<".
# "../../lib/server/CConfig.h", line 145: Error: Use ";" to terminate declarations.
# "../../lib/server/CConfig.h", line 145: Error: A declaration was expected instead of "<".
# "../../lib/server/CConfig.h", line 145: Warning: declarator required in declaration.
# "../../lib/server/CConfig.h", line 145: Error: Use ";" to terminate declarations.
# "../../lib/server/CConfig.h", line 145: Error: A declaration was expected instead of ">"
#
NAME = synergy
VERSION = 1.4.2
CATEGORIES = apps

DESCRIPTION = Software-based TCP/IP "KVM" switch
define BLURB
 Synergy lets you easily share a single mouse and keyboard between multiple
 computers with different operating systems, each with its own display, 
 without special hardware. It's intended for users with multiple computers 
 on their desk since each system uses its own monitor(s). 
endef

MASTER_SITES = $(GOOGLE_MIRROR)
DISTNAME = synergy-$(VERSION)-Source
DISTFILES += $(DISTNAME).tar.gz

VENDOR_URL = http://synergy-foss.org/

# Was required with synergy 1.3.1, still required?
# Adjust code so that it compiles with Sun Studio Compiler
# https://sourceforge.net/tracker/index.php?func=detail&aid=1574331&group_id=59275&atid=490469
#PATCHFILES = suncc.diff

# Was required with synergy 1.3.1, still required?
# Adjust configure.in to properly use --x-libraries option
# http://sf.net/tracker/index.php?func=detail&aid=2359359&group_id=59275&atid=490469
#PATCHFILES += link-xlibs.diff

# TEST_SCRIPTS =

#pre-configure:
#	cd $(WORKSRC) && autoreconf
#	@$(MAKECOOKIE)

CONFIGURE_SCRIPTS = custom
BUILD_SCRIPTS = custom

include gar/category.mk

configure-custom:
	cd $(WORKSRC) && ./hm.sh configure

build-custom:
	cd $(WORKSRC) && ./hm.sh build

post-install:
	ginstall -d $(DESTDIR)$(sysconfdir)
	ginstall -d $(DESTDIR)$(docdir)/$(NAME)/images
	ginstall -m 644 \
		$(WORKSRC)/examples/synergy.conf \
		$(DESTDIR)$(sysconfdir)/synergy.conf.example
	ginstall -m 644 \
		$(WORKSRC)/README \
		$(WORKSRC)/AUTHORS \
		$(WORKSRC)/NEWS \
		$(WORKSRC)/doc/*.html \
		$(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 644 \
		$(WORKSRC)/doc/images/* \
		$(DESTDIR)$(docdir)/$(NAME)/images
	@$(MAKECOOKIE)
