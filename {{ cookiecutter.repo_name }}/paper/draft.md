---
title: A Template for Data-Centric Manuscripting in Markdown
author:
- name: Elijah Knaap
  affiliation: University of California-Riverside
  email: knaap@ucr.edu
- name: Someone Else
  affiliation: University of Neverland
  email: someone@neverland.edu
date: August 2019
abstract: >-
    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco
    laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in
    voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
keywords: "reproducibility, data, computational infrastructure"
bibliography: references.bib
nocite: |
  @Knaap2019
crossrefYaml: .pandoc/crossref_opts.yaml
csl: .pandoc/csl/apa-custom.csl  # apa without name disambiguation
# these do not work for fancy_article
sansitup: True
linestretch: 1.25
geometry: margin=1in
fontsize: 11pt
thanks: "This work is supported by NSF Grant XXXXXX"
anonymous: False
---

# Introduction

## Hook

(note this section heading goes away once we write out the hook same for all subsubsections under Introduction)

Get reader's attention by telling them the paper relates to something interesting. 
    - Y matters: when Y rises or falls, people are hurt or helped
    - Y is controversial: some say it matters, some say it doesnt. Some say it is bad, some good
    - Y is big (affects many people)

## Question

Tell the reader what this paper actually does. Think of this as the point in a trial where having
detailed the crime, you now identify a perpetrator and promise to provide a persuasive case. The
reader should have an idea of a clean research question that will have a more or less satisfactory
answer by the end of the paper. Examples follow below. The question may take two paragraphs. At the
end of the first (2nd paragraph of the paper) or possibly beginning of the second (3rd paragraph
overall) you should have the “This paper addresses the question” sentence.

## Antecedents

Identify the prior work that is critical for understanding the contribution this paper will make.
The key mistake to avoid here are discussing papers that are not essential parts of the intellectual
narrative leading up to your own paper. Give credit where due but establish, in a non-insulting way,
that the prior work is incomplete or otherwise deficient in some important way.

## Value-Added

Describe approximately 3 contributions this paper will make relative to the antecedents. This
paragraph might be the most important one for convincing referees not to reject your paper. A big
difference between it and the earlier “question” paragraph is that the contributions should make
sense only in light of prior work whereas the basic research question of the paper should be
understandable simply in terms of knowing the topic (from the hook paragraph). John suggests that
“Antecedents” and “Value-added” may be intertwined. They may also take up to 3 paragraphs.

## Road-map

Outline the organization of the paper. Avoid writing an outline so generic that it could apply to
any paper (“the next section is the middle of the paper and then we have the end”). Instead
customize the road map to the project and possibly mention pivotal “landmarks” (problems, solutions,
results…) that will be seen along the way. But keep this short because many readers will now be
eager to get to the heart of the paper.

# Theory

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

# Conclusion

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquip ex ea commodo consequat. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Lorem ipsum dolor sit
amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enimad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
commodo consequat. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enimad minim veniam, quis nostrud exercitation
ullamco laboris nisi ut aliquip ex ea commodo consequat.

Make sure you include the final `#References` tag at the end of the document to ensure that the references section has a header

# References
