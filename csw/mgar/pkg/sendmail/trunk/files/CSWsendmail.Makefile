# Simple Makefile to help with updating the databases

all: sendmail.cf virtusertable.db access.db domaintable.db mailertable.db

%.db: %
	/opt/csw/sbin/makemap hash $@ < $<

%.cf: %.mc
	m4 $< > $@;
