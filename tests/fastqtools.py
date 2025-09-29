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
    directory = ("/home/genwork2/03.Fastq_Output/R208genklimerged",)
    output_path = ("/home/genwork2/03.Fastq_Output/R208genklimerged/R208genklimerged-stats.csv",)
    fastq_read_counter(directory=directory, output_path=output_path)
    return


def _test_fastq_validate():
    directory_path = "/home/genwork2/Mert/fastqfix/DS2/2773"
    fastqvalidate(directory_path)
    return


# ON THE SERVER
def _test_merge_it():
    folder_paths = [
        "/mnt/gen100/01.fastq_files/213.TWIST-ExoV2-DNAPrepWithExomePlus-NovaSeq-RUN203_fastq_files/RUN203-ILLM-DNAprep-RNA/PRJ25-1/",
        "/mnt/gen100/01.fastq_files/217.TWIST-ExoV2-DNAPrepWithExomePlus-NovaSeq-RUN207_fastq_files/RUN207-ILLM-RiboZero-PolyA-DNAprep-Poollar-WGS/PRJ25-1/",
        "/mnt/gen100/01.fastq_files/219.TWIST-ExoV2-DNAPrepWithExomePlus-NovaSeq-RUN209_fastq_files/R209-Filtered/",
        "/mnt/gen100/01.fastq_files/223.TWIST-RUN213-DNBSEQT7_fastq_files/PRJ25-1/",
    ]

    sample_names = [
        "KRNA10",
        "KRNA11",
        "KRNA12",
        "KRNA13",
        "KRNA14",
        "KRNA15",
        "KRNA31",
        "KRNA22",
    ]

    output_path = "/home/genwork2/03.Fastq_Output/PRJ25-1-merged"

    merge_it(folder_paths=folder_paths, sample_names=sample_names, output_path=output_path)

    return


def _test_undetermined_demultiplexer():
    undetermined_demultiplexer()
    return
