

SRC = $(PWD)/cluster-lit-draft.md

PDFS=$(SRC:.md=.pdf)
HTML=$(SRC:.md=.html)
TEX=$(SRC:.md=.tex)


all:	$(PDFS) $(HTML) $(TEX)

pdf:	clean $(PDFS)
html:	clean $(HTML)
tex:	clean $(TEX)

%.html:	%.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -w html --template=meta/html.template --css=$(HOME)/.pandoc/marked/kultiad-serif.css --filter pandoc-citeproc -o $@ $<

%.tex:	%.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -w latex -s --pdf-engine=xelatex --template=meta/xelatex.template  --filter pandoc-citeproc -o $@ $<


%.pdf:	%.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -s --pdf-engine=xelatex --template=meta/xelatex.template --filter pandoc-citeproc -o  $@ $<

clean:
	rm -f *.html *.pdf *.tex

linux:
	cat head.md introduction.md models-of-spatial-structure.md clustering-in-social-sciences.md spatial-clustering.md modeling-neighborhood-dynamics.md conclusion.md tail.md > tmp.md
	pandoc -r markdown+simple_tables+table_captions+yaml_metadata_block+smart -s --pdf-engine=xelatex --template=meta/xelatex.template --filter pandoc-citeproc -o tmp.pdf tmp.md 
