all: diagrams

diagrams: connections.png

%.png: %.dot
	dot -Tpng -o $@ $<
	if [ -d $(HOME)/public_html ]; \
		then cp $@ $(HOME)/public_html; \
	fi
