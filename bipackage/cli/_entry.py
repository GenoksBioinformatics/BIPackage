import argparse
import importlib.metadata

from bipackage.util._colors import blue, bold


def main():
    parser = argparse.ArgumentParser(description="BIpackage CLI")
    # --version
    parser.add_argument(
        "--version",
        "-v",
        action="version",
        version=f"BIpackage {blue(importlib.metadata.version('bipackage'))}",
        help="Show version",
    )

    # init subparsers
    subparsers = parser.add_subparsers(dest="command")

    # ======================================== BAMTOOLS ========================================

    # ---------------------------------------- bam_counts ----------------------------------------
    bam_counts_subparser = subparsers.add_parser("bam_counts", help="Get counts from BAM file.")
    bam_counts_subparser.add_argument("--input_dir", "-i", help="Input directory.")
    bam_counts_subparser.add_argument("--exome_bait", "-e", help="Exome bait.")
    bam_counts_subparser.add_argument("--num_threads", "-n", type=int, help="Number of threads to use.")

    # ------------------------------------- compile_bam_stats -------------------------------------
    compile_bam_stats_subparser = subparsers.add_parser("compile_bam_stats", help="Complies BAM stats to CSV.")
    compile_bam_stats_subparser.add_argument("--root_directory", "-r", help="Root directory for the operations.")
    compile_bam_stats_subparser.add_argument("--output_csv", "-o", help="Output csv file")

    
