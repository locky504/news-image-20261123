# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/locky504/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/locky504/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A program that draws the world news of Monday 23 November 2026 as a one-page newspaper front page ("The World Today") and writes it to /output/entry.png.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies the finished `entry.png` — drawn by `draw.py` from the verified headlines of 23 November 2026 — to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png` when that is set). Node standard library only; repeated runs write identical bytes.

## The six stories

1. **Climate talks collapse as nations fail to agree** — nearly 200 countries end the COP31 summit in Turkey without a climate declaration.
2. **Democrats clinch 258-seat House majority** — their largest House majority since 1992.
3. **Tankers struck near Strait of Hormuz** — the sharpest run of attacks on shipping there since the war began.
4. **Sea drones hit Russian warship in Libya** — a Russian corvette is struck at the Benghazi naval base.
5. **Russian strikes hit Kyiv region** — the latest round of attacks on the capital's region.
6. **BepiColombo enters orbit around Mercury** — only the second mission ever to do so, after an eight-year journey.

Headlines verified on 23 November 2026 against SCMP, Arab News, The Manila Times and The Economic Times.

---

Entered on [make.fun](https://make.fun/?ref=dvanqqs1&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards
