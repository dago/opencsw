
# Apply patches from the workdir
PATCHDIR = $(WORKDIR)
PATCHDIRLEVEL = 0

# Disable apache module activation
PATCHFILES += config.diff

# Fix ssl paths for uw-imap c-client
PATCHFILES += imap-ssl.diff

# Don't hardcode $(CC)
PATCHFILES += imap-cc.diff

# Respect my CFLAGS
PATCHFILES += imap-cflags.diff

# Horrible, but necessary due to net-snmp linking with -lwrap
PATCHFILES += snmp-hack.diff

