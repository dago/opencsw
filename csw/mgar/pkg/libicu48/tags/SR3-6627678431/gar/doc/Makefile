all: diagrams

diagrams: connections.png release-workflow.png

%.png: %.dot
	dot -Tpng -o $@ $<
	if [ -d $(HOME)/public_html ]; \
		then cp $@ $(HOME)/public_html; \
	fi
