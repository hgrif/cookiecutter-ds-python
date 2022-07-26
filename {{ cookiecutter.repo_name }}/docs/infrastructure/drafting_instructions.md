# Drafting the paper

The paper is compiled with pandoc and tectonic so you are free to mix and match markdown with latex as you see fit.

## Drafting

- The `paper` directory contains source files for the manuscript
- The "main" file, usually called `draft.md` contains the pandoc yaml structure for the document
  - you can write directly in `draft.md` but it is usually easier to break the draft into separate files for each of the top-level sections. You can then include these sections in the draft using pandoc-include syntax: `!include {filename}`  (with each additional file spearated by a newline). 
  - Included files can contain text beyond markdown, so this can be used, e.g. to split a long table defined in latex into a separate file, which makes the source easier to read
- LaTeX styling files are located in `paper/.pandoc/`. These include any `.template` file that pandoc uses to dispatch data into latex. If you want to add a latex package or format the paper differently, you can edit the template files here or create a new one (and point to it in the makefile). You can also swap out citation style (CSL) or font files here, if you like. (note that if you make any edits, you dont need to make any changes to the build system (e.g. tlmgr). Tectonic will pick them up automatically)
- the paper is compiled from inside the `paper` directory, so any file paths (figures, included files, etc.) should be relative to the `paper` directory.


## Citations

Citations are handled with bibtex, zotero, and better-bibtex. 

- any works cited should be added to the shared Zotero library collection
  - ensure the shared bib stays up to date with the local bibfile by:
    - open zotero
    - right click on the shared library
    - click "Export Library"
    - click the checkbox for "keep updated"
    - navigate to the project/paper directory to save the bib file
- see [this post](https://github.com/sjsrey/til/blob/main/zotero/export_fields.md) for instructions on how to setup betterbibtex to avoid git clashes when multiple authors share a bibtex file

## Compiling the manuscript

- use the makefile commands to build the manuscript into different output formats or use `make paper` to generate them all
- the built versions will be placed inside `paper/compiled/`
- the `make latex` command will generate a standalone tex document that only needs the files relative to `paper`. That means if you move the generated tex file up a directory (out of `compiled` and into `paper`) you should be able to build the paper directly using your latex installation of choice

