import sys
import argparse
from collections import defaultdict

KEYS_TO_CHANGE = {
    "Dungeon Injection Settings - Manual Level Names List",
}

def main():
    ap = argparse.ArgumentParser(description="Set custom dungeon values to be equal")
    ap.add_argument("-i", "--infile", required=True, help="Configfile")
    ap.add_argument("-o", "--outfile", help="Output configfile")
    args = ap.parse_args()

    infile = args.infile
    outfile = args.outfile 

    level_cfg = defaultdict(dict)
    with (
        open(infile) as fh,
        open(outfile, "wt") if args.outfile else sys.stdout as ofh
    ):
        curr_level = None
        for line in fh:
            line = line.strip()

            if line.startswith("["):
                curr_level = line.strip("[]").replace(u"\u200b", "")
                print(line, file=ofh)
                continue

            if "Custom Dungeon" not in curr_level or line.startswith("#") or not line:
                print(line, file=ofh)
                continue

            k, v = line.split(" = ")
            if k in KEYS_TO_CHANGE:
                level_wts = {}
                for level_wt in v.split(","):
                    level, wt = level_wt.split(":")
                    level_wts[level] = int(wt)
                max_val = max(level_wts.values())
                updated_level_wts = {k: max_val for k, v in level_wts.items()}

                updated_v = ",".join(f"{k}:{v}" for k,v in updated_level_wts.items())
                print(f"'{curr_level}': '{k}'", file=sys.stderr)
                print(f"\tbefore: {v}", file=sys.stderr)
                print(f"\tafter: {updated_v}", file=sys.stderr)

                new_line = f"{k} = {updated_v}"
                print(new_line, file=ofh)
            else:
                print(line, file=ofh)


if __name__ == "__main__":
    raise SystemExit(main())
