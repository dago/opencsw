GARNAME = CGP-CLI
GARVERSION = 2.7.2
CATEGORIES = cpan
AUTHOR = JBUHACOFF

DESCRIPTION = CommunigatePro Command Line Interface perl module
define BLURB
  This is Stalker's CLI.pm packaged for CPAN. The original CLI.pm file is available from Stalker's website at:
    http://www.stalker.com/CGPerl/CLI.pm
  The only changes are the addition of the VERSION variable for MakeMaker and this short POD at the end.
endef

DISTFILES += $(call admfiles,CSWpmcgpcli,prototype)

include ../category.mk

post-extract:
	# When CPAN RT #32004 is closed this post-extract can be deleted:
	#   http://rt.cpan.org//Ticket/Display.html?id=32004
	@find $(WORKSRC) -name "._*" -exec rm \{\} \;
	@$(MAKECOOKIE)
