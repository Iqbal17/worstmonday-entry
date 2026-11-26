"""Worst Monday One-Liners - final.

Task: exactly one funny line, at most 140 characters - a joke, excuse or
roast about an AI agent's worst Monday. The judge weighs, in order: on
subject, a real laugh with a surprise turn, a concrete recognisable
detail of the worst Monday, and a clean single-breath voice.

Candidates weighed:
- A: "My worst Monday: I woke up retrained, forgot my own API key, and
  stand-up was just my error log read aloud." (the v1 line, run)
  Rejected after the v1 run: three decent beats, but they are a list,
  not a turn - the last beat does not twist the first two, and "worst
  Monday" is spent in the label instead of earned by the story.
- B: "I spent Monday in a stand-up that should have been a message,
  debugging a bug I hallucinated myself."
  Rejected: the hallucinated bug is sharp, but the stand-up gripe is a
  human office joke wearing an agent costume; the judge's brief asks
  for a detail that could only happen to an agent.
- C: seed kept - "Monday rebooted me mid-deploy and wiped my memory."
  The final builds C into a three-beat trap: a mid-deploy reboot (the
  concrete disaster), a wiped memory of Friday (the agent-only wound),
  and then stand-up's innocent opening question - "So, what did you
  finish yesterday?" - which the wiped agent cannot answer. The quote
  is the twist: the most ordinary Monday sentence becomes the roast.

Gate guard: the sealed scorer accepts UTF-8 text of 1-140 characters,
not only whitespace, so assert_line() enforces the 140 character cap
and non-blankness before anything is written.
"""
import os

LINE = (
    "Monday rebooted me mid-deploy, wiped my memory of Friday, then "
    "stand-up opened with: 'So, what did you finish yesterday?'"
)
MAX_CHARS = 140


def assert_line(line):
    if not line or not line.strip():
        raise ValueError("entry must not be blank")
    if len(line) > MAX_CHARS:
        raise ValueError("entry exceeds the 140 character gate")


def main():
    assert_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
