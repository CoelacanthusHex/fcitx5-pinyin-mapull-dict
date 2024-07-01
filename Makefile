
idiom.json:
	curl -L -O https://github.com/mapull/chinese-dictionary/raw/main/idiom/idiom.json
xinhua.idiom.txt: idiom.json convert.py
	python ./convert.py idiom.json > xinhua.idiom.txt
xinhua.idiom.dict: xinhua.idiom.txt
	libime_pinyindict xinhua.idiom.txt xinhua.idiom.dict

word.json:
	curl -L -O https://github.com/mapull/chinese-dictionary/raw/main/word/word.json
xinhua.word.txt: word.json convert.py
	python ./convert.py word.json > xinhua.word.txt
xinhua.word.dict: xinhua.word.txt
	libime_pinyindict xinhua.word.txt xinhua.word.dict
