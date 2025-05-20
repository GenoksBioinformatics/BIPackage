from bipackage import bedfilegenerator
from bipackage.constants import (
    PARSED_GTF_PATH_GRCh38,
    WHOLE_GENE_LOCS_PATH_GRCh38,
)


def _test_bedfilegenerator():
    bedfilegenerator()
    return


kwargs = {}


# TO BE IMPLEMENTED
def _test_bedfilegenerator():
    bedfilegenerator(
        parsed_gtf_path=PARSED_GTF_PATH_GRCh38,
        whole_gene_locs_path=WHOLE_GENE_LOCS_PATH_GRCh38,
        **kwargs,
    )
    return
