import os
from concurrent.futures import ThreadPoolExecutor

from bipackage import downsample, fastq_read_counter, fastqvalidate, merge_it, undetermined_demultiplexer


def _test_downsample():
    downsample()
    return

def _test_fastq_read_counter():
    fastq_read_counter()

    return

def _test_fastq_read_counter():
    directory="/home/genwork2/03.Fastq_Output/R208genklimerged",
    output_path="/home/genwork2/03.Fastq_Output/R208genklimerged/R208genklimerged-stats.csv",
    fastq_read_counter(directory=directory, output_path=output_path)
    return

def _test_fastq_validate():
    directory_path = "/home/genwork2/Mert/fastqfix/DS2/2773"
    fastqvalidate(directory_path)
    return

def _test_merge_it():
    merge_it()
    return

def _test_undetermined_demultiplexer():
    undetermined_demultiplexer()
    return