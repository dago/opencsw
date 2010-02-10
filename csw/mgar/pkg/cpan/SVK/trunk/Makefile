GARNAME = SVK
GARVERSION = 2.2.1
CATEGORIES = cpan
AUTHOR = CLKAO

DESCRIPTION = a distributed version control system
define BLURB
  SVK is a decentralized version control system written in Perl. It uses the
  Subversion filesystem but provides additional features.
endef

REQUIRED_PKGS  = CSWpmalgannotate CSWpmalgdiff CSWpmappcli CSWpmclone CSWpmclsaccessor CSWpmclsautouse
REQUIRED_PKGS += CSWpmclsdtainherit CSWpmcompresszlib CSWpmdatahier CSWpmfiletype CSWpmfreezethaw CSWpmiodigest
REQUIRED_PKGS += CSWpmiopager CSWpmlclemktxtlex CSWpmlclemktxtsimple CSWpmlistmoreut CSWpmlog4perl
REQUIRED_PKGS += CSWpmpathclass CSWpmperlioeol CSWpmperlioviadyn CSWpmperlioviasym CSWpmpodescapes
REQUIRED_PKGS += CSWpmpodsimple CSWpmregexpshellish CSWpmsvn CSWpmsvnmirror CSWpmsvnsimple CSWpmtermreadkey
REQUIRED_PKGS += CSWpmtimedate CSWpmunivrequire CSWpmuri CSWpmyaml CSWpmyamlsyck

MODDIST = $(GARNAME)-v$(GARVERSION).tar.gz
WORKSRC = $(WORKDIR)/$(GARNAME)-v$(GARVERSION)

PACKAGES = CSWsvk
CATALOGNAME = svk

ARCHALL = 1

include gar/category.mk

