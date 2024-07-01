#!/usr/bin/env python3

import re
import json
import argparse
import unicodedata
import itertools


def pinyin_remove_tone(pinyin: str) -> str:
    nfkd_form = unicodedata.normalize('NFKD', pinyin)
    return nfkd_form.encode('ASCII', 'ignore').decode()


def main():
    argument_parser = argparse.ArgumentParser('convert.py', usage='convert.py [JSON_FILE]')
    argument_parser.add_argument('file', type=argparse.FileType('r'))
    args = argument_parser.parse_args()
    idioms = json.load(args.file)
    results = dict()
    for entry in idioms:
        if re.search('，|,', entry['word']):
            words = re.split('，|,', entry['word'])
            pinyins = re.split('，|,', entry['pinyin'])
            for _, word, pinyin in zip(itertools.count(), words, pinyins):
                results.setdefault(word, pinyin_remove_tone(pinyin).replace(r" ", r"'"))
        else:
            results.setdefault(entry['word'], pinyin_remove_tone(entry['pinyin']).replace(r" ", r"'"))

    for word, pinyin in sorted(results.items()):
        print(f'{word}\t{pinyin}\t0')


if __name__ == '__main__':
    main()
