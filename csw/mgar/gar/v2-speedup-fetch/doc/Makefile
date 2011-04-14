all: diagrams

diagrams: connections.png

%.png: %.dot
	dot -Tpng -o $@ $<
