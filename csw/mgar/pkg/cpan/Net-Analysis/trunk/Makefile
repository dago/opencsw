NAME = Net-Analysis
VERSION = 0.40
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = WORRALL

DESCRIPTION = Modules for analysing network traffic
define BLURB
  Net::Analysis is a suite of modules that parse tcpdump files, 
  reconstruct TCP sessions from the packets, and provide a very 
  lightweight framework for writing protocol anaylsers.
endef

PACKAGES = CSWpmnetanalysis
CATALOGNAME = pm_netanalysis

# depends
DEP_PKGS = CSWpmnetpcap CSWpmnetpacket CSWpmtstmockobject

LICENSE = $(FILEDIR)/LICENSE

ARCHALL = 1

CHECKPKG_OVERRIDES_CSWpmnetanalysis += surplus-dependency|CSWpmtstmockobject
CHECKPKG_OVERRIDES_CSWpmnetanalysis += surplus-dependency|CSWpmnetpcap
CHECKPKG_OVERRIDES_CSWpmnetanalysis += surplus-dependency|CSWpmnetpacket

include gar/category.mk
