# Remove 'fix' from previous runs to prevent duplicates
/^alias_maps =/d
/^alias_database =/d

# These will work as long as the template configuration file doesn't change too much
/alias_maps = netinfo:.aliases/ a\
alias_maps = dbm:/etc/opt/csw/postfix/aliases

/alias_database = .*hash:.opt.majordomo.aliases$/ a\
alias_database = dbm:/etc/opt/csw/postfix/aliases
