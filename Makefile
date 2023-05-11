all: build/US3.pdf

build/US3.pdf: US3.tex aufbau.tex auswertung.tex diskussion.tex durchfuehrung.tex fehlerrechnung.tex lit.bib theorie.tex ziel.tex | build
	lualatex  --output-directory=build US3.tex
	lualatex  --output-directory=build US3.tex
	biber build/US3.bcf
	lualatex  --output-directory=build US3.tex


build: 
	mkdir -p build

clean:
	rm -rf build

.PHONY: clean all
