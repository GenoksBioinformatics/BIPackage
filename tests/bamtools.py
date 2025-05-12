from bipackage import bam_counts, compile_bam_stats


def _test_bam_counts():
    # Set parameters
    input_dir = "/home/genwork2/Mert/bwa_dedup/braf-kras-nras"
    exome_bait = "/home/genwork2/Mert/02.BEDS/variousbeds/sorted_braf-kras-nras.bed"
    num_threads = 40
    bam_counts(input_dir=input_dir, exome_bait=exome_bait, num_threads=num_threads)
    return

def _test_compile_bam_stats():
    compile_bam_stats(root_directory="TOBEIMPLEMENTED", output_csv="TOBEIMPLEMENTED")
    return