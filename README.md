# Delete Repositories

A Python script to delete a GitHub repository via the [GitHub REST API](https://docs.github.com/en/rest/repos/repos#delete-a-repository).

## Prerequisites

- Python 3.6+
- A GitHub [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) with the **`delete_repo`** scope

## Usage

```bash
python delete_repo.py <owner> <repo> --token <your_github_token>
```

### Arguments

| Argument | Description |
|----------|-------------|
| `owner`  | Repository owner (GitHub username or organization name) |
| `repo`   | Repository name |
| `--token`| GitHub personal access token with `delete_repo` scope (or set `GITHUB_TOKEN` env var) |

### Example

```bash
# Using the --token flag
python delete_repo.py myusername my-old-repo --token ghp_xxxxxxxxxxxx

# Or using the GITHUB_TOKEN environment variable
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
python delete_repo.py myusername my-old-repo
```

On success the script prints:

```
Repository 'myusername/my-old-repo' deleted successfully.
```

On failure it prints an error message and exits with a non-zero status code.

## ⚠️ Warning

**Deleting a repository is irreversible.** All code, issues, pull requests, and other data associated with the repository will be permanently removed.
