# 🤞 Random Luck

[![Build](https://github.com/Spico197/random-luck/workflows/BuildRandLuck/badge.svg?branch=main)](https://github.com/Spico197/random-luck/actions/workflows/build.yml)
[![codecov](https://codecov.io/gh/Spico197/random-luck/branch/main/graph/badge.svg?token=EXQFxLr1ZC)](https://codecov.io/gh/Spico197/random-luck)


> Deep learning is acturally the alchemy.

This repo provides a package to automatically select a random seed based on ancient Chinese Xuanxue.

Good luck and best wishes!

## 🚀QuickStart

```bash
# installation
$ pip install git+https://github.com/Spico197/random-luck.git
# usage
$ python
>>> import randluck
>>> random_seed = randluck.get_random_seed(strategy="bazi")
>>> print(random_seed)
1234
>>> from datetime import datetime
# be sure to use the UTC time, and the offset is calculated automatically in the background
>>> random_seed = randuck.get_random_seed(utc_datetime=datetime.utcnow(), strategy="bazi")
>>> print(random_seed)
1234
>>> random_seed = randuck.get_random_seed(utc_datetime=datetime.date(year=1997, month=1, day=1), strategy="lucky_num_by_year")
>>> print(random_seed)
5430
```

## 📐Strategies & Principles

Random seed is selected by the time that experiments starts.

UTC datetime is first converted to Chinese time (UTC+8), and then the datetime is converted to Chinese Lunar calendar to calculate the suitable random seed.

Here are different strategies this repo contains.
New strategies may be updated in the future.

- ***bazi***
  - Ganzhi number converted from Lunar datetime
- ***lucky_num_by_year***
  - Calculate your lucky number by your birth date

## 🤝Contributions

- Bug reports and patch PRs are welcome, please open an issue directly.
- New strategies are welcome, please open an issue first providing the strategy details and new ideas, then make a PR.
- Tarot cards and constellation strategies are welcome, but I'm not familiar with them, please open new issues to discuss if it is OK to make a PR.

## 🔑License

This repo is under the MIT license.
