import argparse
import logging
import os
import shutil
import time
from filecmp import dircmp
from pathlib import Path

CACHE_FOLDER = os.path.join(os.path.dirname(__file__), './cache')

def copyfolder(folderPath):
    shutil.rmtree(CACHE_FOLDER, True)
    shutil.copytree(folderPath, CACHE_FOLDER)

def diff(dcmp, logger):
    for file in dcmp.left_only:
        logger.info("DELETE: " + dcmp.right + "/" + file)

    for file in dcmp.right_only:
        logger.info("NEW: " + dcmp.right + "/" + file)

    for file in dcmp.diff_files:
        logger.info("UPDATE: " + dcmp.right + "/" + file)

    for sub_dcmp in dcmp.subdirs.values():
        diff(sub_dcmp, logger)

def main():
    #Parsing Arguments
    parser = argparse.ArgumentParser(description="Check periodicly the chagements in a folder")
    parser.add_argument("folder", type=str, help="The folder to check")
    parser.add_argument("log", type=str, help="The log file")
    parser.add_argument("-i", "--interval", type=int, help="Interval in seconde between comparaisons", default=15)
    parser.add_argument("-d", "--depth", type=int, help="Depth")
    parser.add_argument("-v", "--verbose", help="Verbose mode", action="store_true")
    args = parser.parse_args()

    #Check arguments validity
    if not os.path.isdir(args.folder):
        raise NotADirectoryError("'"+args.folder+"'"+' is not a directory')

    #Logging Configuration
    logging.basicConfig(filename=args.log, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    logger = logging.getLogger()
    if args.verbose:
        logger.addHandler(logging.StreamHandler())

    #Check cache folder
    if not os.path.isdir(CACHE_FOLDER):
        os.makedirs(CACHE_FOLDER)


    while True:
        dcmp = dircmp(CACHE_FOLDER, args.folder) 
        diff(dcmp, logger)
        copyfolder(args.folder)
        time.sleep(args.interval)

if __name__ == '__main__':
    main()
