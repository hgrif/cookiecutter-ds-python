"""Utility functions for writing papers."""

import sys

import pandas as pd
from tabulate import tabulate


def save_table(
    df,
    path=None,
    type="latex",
    landscape=False,
    caption=None,
    ref=None,
    resize=True,
    tabulate_kws=None,
):
    """Save a pandas dataframe as a markdown table.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe to save
    path : str
        path to output file
    type : str {'latex', 'pipe'}
        the type of table to output. Can by "pipe" for a markdown table, or "latex" for latex
    landscape: bool
        whether to print the table on its own page in landscape orientation
        (useful for wide tables)
    caption : str
        the table's caption
    ref : str
        short name used to reference the table with pandoc-crossref
    resize: bool
        whether the table should be resized to fit on a single page
    tabulate_kws : dict
        additional keyword arguments passed to tabulate

    """
    original = sys.stdout
    sys.stdout = open(path, "w")
    if not tabulate_kws:
        tabulate_kws = {}

    if landscape:
        print("\\begin{landscape}\n")

    if "latex" or "booktabs" in type:
        print("\\begin{table}[h]\n")
        print("\\begin{center}")
        if resize:
            print("\\resizebox{\\linewidth}{!}{")
            print(tabulate(df, tablefmt=type, headers="keys", **tabulate_kws) + "\n" + "}")
        else:
            print(tabulate(df, tablefmt=type, headers="keys", **tabulate_kws) + "\n")

    else:
        print(tabulate(df, tablefmt=type, headers="keys"))
    if caption and "latex" or "booktabs" in type:
        print(
            "\n\\caption{" + f"{caption}" + "}" + "\n" + "\\label{tbl:" + f"{ref}" + "}"
        )
    elif caption:
        print(f"\n: {caption}" + " {#tbl:" + f"{ref}" + "}")

    if "latex" or "booktabs" in type:
        print("\\end{center}\n" "\\end{table}\n")

    if landscape:
        print("\\end{landscape}")

    sys.stdout = original


def break_string(string, length):
    prestr = "\makecell*[{{p{%s}}}]{" % length
    return prestr + string + "}"


def resize_table_cols(df, length):
    df = df.copy()
    strcols = df.columns[df.columns.dtype=="O"].tolist()[0]
    if isinstance(length, str):
        length = {col: length for col in strcols}
    for i in length:
        df[i] = df[i].apply(lambda x: break_string(x, length[i]))
    return df