NAME = Log-Dispatch
VERSION = 2.29
CATEGORIES = cpan
GARTYPE = v2
AUTHOR = DROLSKY

DESCRIPTION = Dispatches messages to one or more outputs
define BLURB
endef

CATALOG_RELEASE = unstable

LICENSE = LICENSE

PACKAGES += CSWpm-log-dispatch-syslog
CATALOGNAME_CSWpm-log-dispatch-syslog = pm_log_dispatch_syslog
SPKG_DESC_CSWpm-log-dispatch-syslog = Dispatches messages to one or more outputs
# There was no information if this is pure Perl or not. Please remove if necessary.
ARCHALL_CSWpm-log-dispatch-syslog = 1
RUNTIME_DEP_PKGS_CSWpm-log-dispatch-syslog += CSWpm-params-validate
OBSOLETED_BY_CSWpm-log-dispatch-syslog += CSWpmlogdispatch
CATALOGNAME_CSWpmlogdispatch = pm_logdispatch_stub

include gar/category.mk
