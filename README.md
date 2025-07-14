# GitHub Issue Summarizer CLI by Mourad

This is a Python command-line tool that fetches and summarizes issues from a GitHub repository. It prints the issue title and a short version of its description.

## How It Works

This tool connects to the GitHub API and gets the list of issues from the repository you enter. It then shows the first 10 issues with short summaries.

## File Structure

- `main.py`  
  This is the main entry point. It gets the repo name from the command line, fetches the issues, summarizes them, and prints the results.

- `fetch.py`  
  This file sends a request to GitHub and returns a list of issues (not pull requests).

- `Sum.py`  
  This file shortens the issue description to the first 400 characters only.


## How To Use It


```bash
git clone https://github.com/mouradgad1/github-issue-summarizer.git
cd github-issue-summarizer
