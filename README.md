# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Kodoku05/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Kodoku05/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

The World Today — Monday 23 November 2026: a program that sums up the
world news of Monday 23 November 2026 as a one-page newspaper front page
(a 1024×1024 PNG). Lead stories: COP31 collapses with no deal; a 14-tanker
Iranian convoy sets out to break the US blockade; the Democrats win 258
House seats, the largest majority since 1992; and Verstappen wins a wild
Las Vegas Grand Prix. 50 stories across 7 regions and 18 fields, every one
dated 23 November 2026.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=./out node main.ts
```

Writes `entry.png` to `$MAKEFUN_OUTPUT_DIR` (default `/output`). Node 22,
standard library only — the program just copies the image.

## How the image was made

`draw_poster.py` (Python + Pillow, run locally) draws the front page from
the verified story data in `stories.py`: four illustrated leads, a "Why
the Gulf is burning" explainer, a UTC timeline of how the weekend
unfolded, a 46-story grid with spot illustrations, a dotted world map with
numbered story pins, and a date-check box listing the big stories
deliberately left out because they belong to earlier days. The output is
deterministic — two runs produce byte-identical PNGs.

## Sources

Reuters, AP, AFP, UKMTO, BBC, ESPN/Formula1 and wire pickups, checked on
the morning of 23 November 2026. Every story happened, or was first
reported, on Monday 23 November 2026. Illustrations are original
flat-vector drawings, not photographs.
