import os
import tarfile
from multiprocessing.pool import ThreadPool, Pool
import numpy as np
from tqdm import tqdm

DATA_INPUT_PATH = '/home/twkim/toy/python/data/dicom'
ZIP_OUTPUT_PATH = 'data/output'
ZIP_FILE_NAME = 'sample_dicom'


def _divide_subdirs_by_n(dir: str, n: int):
    subdirs = [dir.path for dir in os.scandir(dir) if dir.is_dir()]
    subdirs_splitted_by_n = np.array_split(subdirs, n)
    return [subdirs.tolist() for subdirs in subdirs_splitted_by_n]

def _get_file_paths(data_input_path=DATA_INPUT_PATH):
    file_paths = []
    for base, _, files in os.walk(data_input_path):
        for file in files:
            file_paths.append(os.path.join(base, file))
    return file_paths

def compress(file_paths, id):
    with tarfile.open(f'{ZIP_OUTPUT_PATH}/{ZIP_FILE_NAME}_{id}.tar.bz2', 'w:bz2') as tar:
        for file in tqdm(file_paths):
            tar.add(file)

def multi_process_compress(dicom_subdirs_list):
    dicom_file_paths_groups = [[_get_file_paths(dicom_subdir) for dicom_subdir in dicom_subdirs] for dicom_subdirs in dicom_subdirs_list]
    for dicom_file_paths_group in dicom_file_paths_groups:
        return
    # pool = Pool(processes=3)
    # print([_get_file_paths(dicom_subdir) for dicom_subdir in dicom_subdirs_list])
    # pool.map(compress, [_get_file_paths(dicom_subdir) for dicom_subdir in dicom_subdirs_list])


if __name__ == '__main__':
    dicom_subdirs_list = (_divide_subdirs_by_n(DATA_INPUT_PATH, 2))
    multi_process_compress(dicom_subdirs_list)
