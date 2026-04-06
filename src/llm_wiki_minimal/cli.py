from __future__ import annotations

import argparse

from llm_wiki_minimal.service import build_index, export_promotion_candidates, ingest_source


def main() -> None:
    parser = argparse.ArgumentParser(prog="llm-wiki-minimal")
    sub = parser.add_subparsers(dest="command", required=True)

    ingest_parser = sub.add_parser("ingest")
    ingest_parser.add_argument("source_file")

    sub.add_parser("build-index")
    sub.add_parser("export-promotion-candidates")

    args = parser.parse_args()

    if args.command == "ingest":
        for path in ingest_source(args.source_file):
            print(path)
    elif args.command == "build-index":
        print(build_index())
    elif args.command == "export-promotion-candidates":
        print(export_promotion_candidates())


if __name__ == "__main__":
    main()
