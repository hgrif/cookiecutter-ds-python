"""Utility functions for writing papers."""

import sys

import pandas as pd
from tabulate import tabulate


def save_table(df, path=None, type="pipe", landscape=False, caption=None, ref=None):
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

    """
    original = sys.stdout
    sys.stdout = open(path, "w")

    if landscape:
        print("\\begin{landscape}\n")
    if type == "latex":
        print(
            "\\begin{table}[h]\n"
            "\\begin{center}" + tabulate(df, tablefmt=type, headers="keys") + "\n"
        )
    else: 
        print(tabulate(df, tablefmt=type, headers="keys"))
        
    if caption and type == "latex":
        print("\n\\caption{"+f"{caption}"+"}" +"\n" + "\label{tbl:"+f"{ref}"+"}"
)
    elif caption:
        print(f"\n: {caption}" + " {#tbl:" + f"{ref}" + "}")
    if type=='latex':
        print("\\end{center}\n" "\\end{table}\n")

    if landscape:
        print("\\end{landscape}")

    sys.stdout = original
