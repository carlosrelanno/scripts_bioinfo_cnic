# import pandas as pd
# import sys
# import os
from cellphonedb.src.core.methods import cpdb_degs_analysis_method
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-D", "--cpdb_file_path", dest="cpdb_file_path")
parser.add_option("-m", "--meta_file_path", dest="meta_file_path")
parser.add_option("-c", "--counts_file_path", dest="counts_file_path")
parser.add_option("-d", "--degs_file_path", dest="degs_file_path")
parser.add_option("-o", "--out_path", dest="out_path")

options, remainder = parser.parse_args()

# deconvoluted, means, relevant_interactions, significant_means = 

cpdb_degs_analysis_method.call(
    cpdb_file_path = options.cpdb_file_path,                            # mandatory: CellPhoneDB database zip file.
    meta_file_path = options.meta_file_path,                            # mandatory: tsv file defining barcodes to cell label.
    counts_file_path = options.counts_file_path,                        # mandatory: normalized count matrix.
    degs_file_path = options.degs_file_path,                            # mandatory: tsv file with DEG to account.
    counts_data = 'hgnc_symbol',                                # defines the gene annotation in counts matrix.
    # microenvs_file_path = microenvs_file_path,                  # optional (default: None): defines cells per microenvironment.
    threshold = 0.1,                                            # defines the min % of cells expressing a gene for this to be employed in the analysis.
    result_precision = 3,                                       # Sets the rounding for the mean values in significan_means.
    separator = '|',                                            # Sets the string to employ to separate cells in the results dataframes "cellA|CellB".
    debug = False,                                              # Saves all intermediate tables emplyed during the analysis in pkl format.
    output_path = options.out_path,                                     # Path to save results
    output_suffix = None                                        # Replaces the timestamp in the output files by a user defined string in the  (default: None)
    )