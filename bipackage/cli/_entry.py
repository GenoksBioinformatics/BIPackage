import argparse
import importlib.metadata

from bipackage.constants import PARSED_GTF_PATH_GRCh38, WHOLE_GENE_LOCS_PATH_GRCh38
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
    bam_counts_subparser.add_argument("--input_dir", "-i", required=True, help="Input directory.")
    bam_counts_subparser.add_argument("--exome_bait", "-e", required=True, help="Exome bait.")
    bam_counts_subparser.add_argument("--num_threads", "-n", type=int, default=40, help="Number of threads to use.")

    # ------------------------------------- compile_bam_stats -------------------------------------
    compile_bam_stats_subparser = subparsers.add_parser("compile_bam_stats", help="Complies BAM stats to CSV.")
    compile_bam_stats_subparser.add_argument("--root_directory", "-r", required=True, help="Root directory for the operations.")
    compile_bam_stats_subparser.add_argument("--output_csv", "-o", required=True, help="Output csv file.")

    # ======================================== BEDTOOLS ========================================

    # ------------------------------------- bedfilegenerator -------------------------------------
    bedfilegenerator_subparser = subparsers.add_parser("bedfilegenerator", help="Generate and sort BED files from a parsed GTF file.")
    bedfilegenerator_subparser.add_argument("--gene_list", "-g", nargs="+", required=True, help="Gene names to include.")
    bedfilegenerator_subparser.add_argument("--bed_file_name", "-b", required=True, help="Name of the output BED file.")
    bedfilegenerator_subparser.add_argument("--output_folder", "-o", required=True, help="Folder to save the output BED file.")
    bedfilegenerator_subparser.add_argument("--whole_gene_list", "-w", nargs="+", required=True, help="Whole gene names to include.")
    bedfilegenerator_subparser.add_argument(
        "--parsed_gtf_path", "-p", default=PARSED_GTF_PATH_GRCh38, help="Path to Parsed GTF file."
    )
    bedfilegenerator_subparser.add_argument(
        "--whole_gene_locs_path", "-wglp", default=WHOLE_GENE_LOCS_PATH_GRCh38, help="Path to whole gene locs file."
    )
    bedfilegenerator_subparser.add_argument(
        "--cds", "-c", action="store_true", help="If used, use CDS features; otherwise use exon features."
    )
    # ======================================== FASTQTOOLS ========================================

    # ------------------------------------- downsample -------------------------------------
    downsample_subparser = subparsers.add_parser("downsample",help="Pipeline to map, deduplicate, and downsample sequencing reads.")
    downsample_subparser.add_argument("--sample_id", "-s", required=True, help="Sample ID.")
    downsample_subparser.add_argument("--r1", "-r1", required=True, help="Path to R1 fastq file.")
    downsample_subparser.add_argument("--r2", "-r2", required=True, help="Path to R2 fastq file.")
    downsample_subparser.add_argument("--out_path", "-o", required=True, help="Output path for the results.")
    downsample_subparser.add_argument("--reference", "-r", required=True, help="Path to the reference genome.")
    downsample_subparser.add_argument("--threads", "-t", type=int, default=40, help="Number of threads to use.")
    downsample_subparser.add_argument("--remove_all_dups", "-ra", action="store_true", help="Remove all duplicates")
    downsample_subparser.add_argument("--remove_seq_dups", "-rs", action="store_true", help="Remove sequencing duplicates")
    downsample_subparser.add_argument("--use_gatk_md", "-ug", action="store_true", help="Use GATK MarkDuplicatesSpark")
    downsample_subparser.add_argument("--strategy", "-st", default="HighAccuracy", help="Downsampling strategy")
    downsample_subparser.add_argument("--keep", "-k", type=float, default=0.5, help="How much read to keep? Give a ratio")

    # ------------------------------------- fastq_read_counter -------------------------------------
    fastq_read_counter_subparser = subparsers.add_parser("fastq_read_counter", help="Count reads from FASTQ file.")
    fastq_read_counter_subparser.add_argument("--directory", "-d", required=True, help="Path to directory.")
    fastq_read_counter_subparser.add_argument("--output_path", "-o", required=True, help="Path to save csv file.")


    # ------------------------------------- fastqvalidate -------------------------------------
    fastqvalidate_subparser = subparsers.add_parser("fastqvalidate", help="Validate fastq files in a given directory using`fastQValidator`.")
    fastqvalidate_subparser.add_argument("--directory", "-d", required=True, help="Directory to perform the validation of fasq files.")

    # ------------------------------------- merge_it -------------------------------------
    merge_it_subparser = subparsers.add_parser("merge_it", help="Merge fastq files.")
    merge_it_subparser.add_argument("--folder_paths", "-f", nargs="+", required=True, help="List of paths to folders.")
    merge_it_subparser.add_argument("--sample_names", "-s", nargs="+", required=True, help="List of name of the files.")
    merge_it_subparser.add_argument("--output_path", "-o", required=True, help="Path to the output directory.")

    # ------------------------------------- undetermined_demultiplexer -------------------------------------
    undetermined_demultiplexer_subparser = subparsers.add_parser("undetermined_demultiplexer", help="Filter undetermined FASTQ files for multiple samples using index information.")
    undetermined_demultiplexer_subparser.add_argument("--sample_sheet", "-s", required=True, help="Path to the sample sheet CSV file.")
    undetermined_demultiplexer_subparser.add_argument("--input_r1", "-r1", required=True, help="Path to the undetermined R1 FASTQ.gz file.")
    undetermined_demultiplexer_subparser.add_argument("--input_r2", "-r2", required=True, help="Path to the undetermined R2 FASTQ.gz file.")
    undetermined_demultiplexer_subparser.add_argument("--output_dir", "-o", required=True, help="Directory to store the filtered FASTQ files.")
    undetermined_demultiplexer_subparser.add_argument("--json_output", "-j", required=True, help="Path to output JSON file for sample target indices.")
    undetermined_demultiplexer_subparser.add_argument("--threads", "-t", type=int, default=4, help="Number of threads to use (default: 4).")

