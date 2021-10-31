import os
import tarfile
import zlib
from tqdm import tqdm

FILE_INPUT_PATH = 'data/sample_dicom'
ZIP_OUTPUT_PATH = 'data/output'
ZIP_FILE_NAME = 'sample_dicom'

def _yield_file_paths(file_input_path=FILE_INPUT_PATH):
    file_paths = []
    for base, _, files in os.walk(file_input_path):
        for file in files:
            file_paths.append(os.path.join(base, file))
    return file_paths

def zip1(file_paths):
    with tarfile.open(f'{ZIP_OUTPUT_PATH}/{ZIP_FILE_NAME}.tar.bz2', 'w:bz2') as tar:
        for file in tqdm(file_paths):
            tar.add(file)


if __name__ == '__main__':
    zip1(_yield_file_paths())
