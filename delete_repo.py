#!/usr/bin/env python3
"""Script to delete a GitHub repository via the GitHub API."""

import argparse
import os
import sys
import urllib.request
import urllib.error
import json


def delete_repository(owner: str, repo: str, token: str) -> None:
    """Delete a GitHub repository.

    Args:
        owner: The repository owner (user or organization).
        repo: The repository name.
        token: A GitHub personal access token with delete_repo scope.

    Raises:
        SystemExit: If the deletion fails.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    req = urllib.request.Request(
        url,
        method="DELETE",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            if response.status == 204:
                print(f"Repository '{owner}/{repo}' deleted successfully.")
            else:
                print(f"Unexpected response status: {response.status}", file=sys.stderr)
                sys.exit(1)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        try:
            message = json.loads(body).get("message", body)
        except json.JSONDecodeError:
            message = body
        print(f"Failed to delete repository '{owner}/{repo}': {message}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Delete a GitHub repository via the GitHub API."
    )
    parser.add_argument("owner", help="Repository owner (user or organization)")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument(
        "--token",
        default=os.environ.get("GITHUB_TOKEN"),
        help=(
            "GitHub personal access token with delete_repo scope. "
            "Defaults to the GITHUB_TOKEN environment variable."
        ),
    )
    args = parser.parse_args()
    if not args.token:
        parser.error(
            "A GitHub token is required. Provide --token or set the GITHUB_TOKEN environment variable."
        )
    delete_repository(args.owner, args.repo, args.token)


if __name__ == "__main__":
    main()
