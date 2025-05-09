import os

from bipackage.util.utilities import timer


def check_files(directory: str):
    for filename in os.listdir(directory):
        if filename.endswith("fastq.gz") or filename.endswith("fq.gz"):
            if os.path.isfile(os.path.join(directory, filename)):
                print("Checking file:", os.path.join(directory, filename))
                print("Performing validation for file:", filename)
                command = f"fastQValidator --file {os.path.join(directory, filename)} --noeof"
                print("Command:", command)
                os.system(command)
        else:
            pass


def _test_fastq_validate():
    directory_path = "/home/genwork2/Mert/fastqfix/DS2/2773"
    check_files(directory_path)
    return


@timer
def fastqvalidate(directory: str) -> None:
    """
    Validate fastq files in a given directory using`fastQValidator`.

    Parameters
    ----------
    directory
        Directory to perform the validation of fasq files.

    Returns
    -------
    None
    """
    check_files(directory=directory)
    return


if __name__ == "__main__":
    _test_fastq_validate()
