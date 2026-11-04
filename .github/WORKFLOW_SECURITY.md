# Codex automation is paused

All five Codex workflows are intentionally paused. Issue creation, issue edits,
comments, pull requests, branch pushes and tag pushes no longer start them.
Manual dispatch on `main` reports the pause and fails; other refs skip the job.
No review, issue response, documentation edit, translation or release is produced.

The paused workflows have `permissions: {}` and contain no checkout, package
installation, secret references, agent invocation or publishing steps. They do
not consume issue text, PR titles, branch names or repository code in shell
scripts. This also removes the incorrect `codex` npm package installation from
the review workflow. No replacement CLI or authentication setup is claimed to
work yet.

## Before restoring a task

- Keep the entry point manual and limited to a reviewed, trusted ref. Review the
  workflow definition as well as the code and content it will consume.
- Treat issue/comment text, PR metadata, diffs, commit messages and repository
  files as untrusted data. Pass data through files or environment variables with
  quoted arguments; never substitute GitHub event expressions into shell code.
- Use a reviewed, pinned official Codex version and supported authentication.
  Keep the sandbox enabled and fail if the required sandbox is unavailable.
  A prompt instruction alone is not a security boundary.
- Do not execute contributor code or model-selected commands in a context with
  secrets or repository write credentials. Disable persisted checkout credentials.
  Isolate untrusted analysis from any authenticated or publishing step.
- Start with no token permissions, adding only the permissions a reviewed step
  needs. Require human review before publishing model-generated output or edits.
- Validate CLI compatibility and isolation without production secrets before a
  maintainer separately authorizes any authenticated test or restored automation.

## Diagnose the observed error

Read the actual failing step, exit status and sanitized error. The old diagnostic
comment always named a sandbox error, regardless of the real failure, so its
heading is not evidence of a sandbox failure or of successful agent execution.
For an authentication error, privately verify the selected authentication method,
secret availability for that event and API access. Never print credentials,
environment dumps or authentication files. If a sandbox really fails, stop and
repair a supported sandbox environment before retrying; keep protections enabled.
No credentials or account security settings were changed by this patch.

## Scope and limitations

These are repository-file changes. They take effect only after a maintainer
reviews and applies them. Older refs can retain the previous workflows, and
already queued or running jobs are not cancelled by this patch. No live workflow
or secret-bearing test was run, and previous executions were not re-audited here.
This patch does not establish whether any prior execution exposed information.

References: [GitHub workflow syntax and permissions](https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions),
[Codex authentication](https://developers.openai.com/codex/auth),
[Codex sandboxing](https://developers.openai.com/codex/sandboxing).
