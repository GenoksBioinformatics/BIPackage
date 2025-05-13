from bipackage import nipt_bcl2fastq

source_path = "/mnt/nextseq"
bcl_path = "/home/genwork2/06.BCLs"

FTP_SERVER = "transfer.ctit.eurofinseu.com"
FTP_USER = "tr_genoks"
FTP_PASSWORD = "N:If&iZR4cxPg2"

def _test_nipt_bcl2fastq():

    nipt_bcl2fastq(
        nipt_part="",
        nipt_folders="",
        fastq_names="",
        output_folder="",
        num_readers=10,
        num_writers=10,
        num_processors=40,
        compression_level=8,
        source_path=source_path,
        bcl_path=bcl_path,
        ftp_server=FTP_SERVER,
        ftp_user=FTP_USER,
        ftp_password=FTP_PASSWORD,
    )
    return
