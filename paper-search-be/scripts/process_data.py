import json
import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-path", type=Path, required=True)
    parser.add_argument("--save-path", type=Path, required=True)
    args = parser.parse_args()

    with open(args.data_path, "r") as f:
        papers = json.load(f)
    results = []
    papers = list(filter(lambda p : p["abstract"], papers))
    for i in range(len(papers)):
        results.append(
            {
                "id": i,
                "title": papers[i]["title"],
                "abstract": papers[i]["abstract"],
                "authors": papers[i]["authors"],
            }
        )

    with open(args.save_path, "w") as f:
        json.dump(results, f)


if __name__ == "__main__":
    main()
