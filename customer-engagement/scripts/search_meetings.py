"""Search meetings via Work IQ CLI."""

import argparse
import subprocess
import sys

from rich.console import Console

console = Console()


def search_meetings(keywords: str):
    """Search calendar meetings using Work IQ CLI."""
    try:
        result = subprocess.run(
            ["workiq", "search", "--type", "meeting", "--query", keywords],
            capture_output=True,
            text=True,
            check=True,
        )
        console.print(result.stdout)
        return result.stdout
    except FileNotFoundError:
        console.print("[red]Work IQ CLI not found. Run: npm install -g @microsoft/workiq[/red]")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Search failed: {e.stderr}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search meetings via Work IQ")
    parser.add_argument("--keywords", required=True, help="Search keywords")
    args = parser.parse_args()
    search_meetings(args.keywords)
