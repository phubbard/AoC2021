
sourcefiles := $(wildcard *.msc)
svgs := $(patsubst %.msc,%.svg,$(sourcefiles))
dotsourcefiles := $(wildcard *.dot)
dotsvgs := $(patsubst %.dot,%.svg,$(dotsourcefiles))

all: $(svgs) $(dotsvgs)

$(svgs): %.svg: %.msc
	mscgen -i $< -T svg -o $@

$(dotsvgs): %.svg: %.dot
	dot $< -Tsvg -o$@
	
clean:
	-rm *.svg

