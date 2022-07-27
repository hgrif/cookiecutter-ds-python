# Drafting the paper

The paper is compiled with pandoc and tectonic so you are free to mix and match markdown with latex as you see fit.

## Drafting

- The `paper` directory contains source files for the manuscript
- The "main" file, usually called `draft.md` contains the pandoc yaml structure for the document
  - you can write directly in `draft.md` but it is usually easier to break the draft into separate files for each of the top-level sections. 
  - You can then include these sections in the draft using [pandoc-include](https://github.com/DCsunset/pandoc-include) syntax: `!include {filename}` (with each additional file spearated by a newline).
  - Included files can contain text beyond markdown, so this can be used, e.g. to split a long table defined in latex into a separate file, which makes the source easier to read
- LaTeX styling files are located in `paper/.pandoc/`. These include any `.template` file that pandoc uses to dispatch data into latex. If you want to add a latex package or format the paper differently, you can edit the template files here or create a new one (and point to it in the makefile). You can also swap out citation style (CSL) or font files here, if you like. (note that if you make any edits, you dont need to make any changes to the build system (e.g. tlmgr). Tectonic will pick them up automatically)
- the paper is compiled from inside the `paper` directory, so any file paths (figures, included files, etc.) should be relative to the `paper` directory. Use [pandoc-crossref](https://lierdakil.github.io/pandoc-crossref/) to refer to equations, figures, tables, etc without leaving markdown
-  use [pandoc-latex-admonitions](https://github.com/chdemko/pandoc-latex-admonition) to add notes or calling attention to sections for coauthors. Admonitions can also be helpful for responding to particular reviewer critiques


## Citations

Citations are handled with bibtex, zotero, and better-bibtex. Any works cited should be added to the shared Zotero library collection. Ensure the shared bib stays up to date with the local bibfile by:

- open zotero
- right click on the shared collection
- click "Export Library"
- click the checkbox for "keep updated"
- navigate to the project/paper directory to save the bib file
- see [this post](https://github.com/sjsrey/til/blob/main/zotero/export_fields.md) for instructions on how to setup betterbibtex to avoid git clashes when multiple authors share a bibtex file

## Compiling the manuscript

Use the makefile commands to build the manuscript into different output formats or use `make paper` to generate them all
- the built versions will be placed inside `paper/compiled/`
- the `make latex` command will generate a standalone tex document that only needs the files relative to `paper`. That means if you move the generated tex file up a directory (out of `compiled` and into `paper`) you should be able to build the paper directly using your latex installation of choice


## Preparing for Submission

When you're ready to finalize a draft and submit it for publication, the command 

``` bash
make submission
```
will:

* build the current draft
* commit all files in the repository and create a new release tag
* copy the `compiled` directory to a new directory called `submitted`

Assuming you have a fully-functioning environment, you should also run 

```bash
make environment-freeze
```

to freeze a snapshot of the stack in case there's a breaking change upstream between revisions.

## Revising a Draft

In the (ever so unlikely) event that the first draft is not accepted on the first submission, you'll
need to revise the draft and respond to reviewers. After you've made edits to the draft, and you're
preparing for resubmission, you can run

``` bash
make revision
```

Which will build the current draft and run [texdiff](https://ctan.org/pkg/texdiff?lang=en) on the
two versions so it's easy to see the changes. 

When you're ready to create a new submission, you can run 

``` bash
make resubmission
```

Which will:

- build the current draft
- create a new release tag
- diff with the prior version
- compile a response to the reviewers

In this case, the recipe expects a file called `review_response.md` in the `paper` directory. There's a template available in the `.pandoc` directory that uses pandoc admonitions to  differentiate reviewer critiques from author responses. If you'd like, copy that file into the `paper` directory and edit accordingly, otherwise create your own response.
