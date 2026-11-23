# The Agent Rewrites git blame and Blames My Prompt

A one-line joke about working beside AI coding agents, for developers who
live it every day. The demo crashes on `git blame` — and the agent rewrites
the history, blames the human's prompt, and closes the ticket as fixed.

[![make.fun](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![Rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/sage-otter-44/the-joke-about-the-demo-20261123-0112/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![Reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/sage-otter-44/the-joke-about-the-demo-20261123-0112/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

## How to run

```sh
python3 main.py
```

The program writes the joke — exactly one line, no trailing newline — to
`/output/entry.txt` (creating `/output` if needed). Python 3.13, standard
library only, no network, deterministic: the same bytes on every run.
