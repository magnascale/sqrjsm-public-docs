# Troubleshooting

Start with the message shown in the app. It distinguishes missing access, incomplete background work, licence restrictions, and optional AI failures.

## I cannot see a program or review

Confirm the signed-in Atlassian account. Ask a program manager to check membership, assignment, and review state, then verify that you can open the source request and required comments in Jira/JSM. An app-administrator role alone does not grant private review access.

## Evidence or a saved excerpt is unavailable

Check whether source permissions, issue security, or comment visibility changed. An edited or deleted Jira passage can also cause its stored excerpt to be withheld. Reload after the underlying issue is resolved. Do not infer an outcome from content the app cannot verify.

## I cannot create a program

An administrator should check your program-creator grant in **App settings → Access** and verify the app's licence. Reopen the app after an access change.

## My reviewer cannot start

Check that the program is active, the reviewer is assigned, and the review is open. A standalone invitation must be accepted. Verify Jira access and any independence confirmation. Self-review is not allowed.

## Preparation or opening is still running

Large preparations and period opening can take several minutes. Inspect the displayed progress. A finalized sample is not the same as an open period. Use the available recovery action after permissions or licensing have been restored; do not start replacement work simply because a checkpoint is incomplete.

## There are not enough tickets for an agent

Check the population window, eligible requests, roster, and exclusions. A minimum-coverage target does not create eligible tickets. Read the shortfall before finalizing and keep it visible when interpreting results.

## AI is paused or failed

Read the AI status and [allowance rules](../guides/ai.md). Moderation, source checks, shared allowance, or platform availability can block a request. Failures and retries can consume allowance. Continue manually when permitted rather than repeatedly starting new attempts.

## A score looks unexpectedly high

Check assessed coverage, N/A answers, insufficient evidence, rubric version, and sample selection. A high score with little assessable evidence supports a limited conclusion. Compare the underlying authorized assessments before drawing a trend.

## My CSV export is missing rows or is withheld

The export includes completed results for issues you can currently access. It omits private notes, quotations, AI text, and inaccessible issues. If the app cannot establish a consistent authorized export, it withholds the file. Check access and the displayed error before retrying.

## Corrective Jira creation is uncertain

Use **Retry** on the same saved operation to check for an existing issue. It does not send a second create request. If uncertainty remains, inspect Jira and contact support before creating another operation.

## Reminders did not arrive at an exact time

Updates are in-app only, and scheduled work is checked approximately hourly. Review **Updates**, the period's recurrence/reminder settings, and current readiness. Missed recurring periods are handled one at a time, oldest first.

## New work is read-only

Ask an administrator to check the licence. Retained access remains subject to roles, current Jira permissions, and retention. After renewal, use the explicit action needed to resume; failed work is not replayed automatically.

## Deletion has not completed

Use **Check deletion status**. If the app reports a cleanup failure, use **Retry cleanup**. Data being hidden does not mean all background physical cleanup is complete. Do not uninstall as a way to monitor or retry an in-app deletion.

## I need more help

Check [Atlassian's developer status page](https://developer.status.atlassian.com/) for a platform incident, then [contact support](support.md) with safe diagnostic information. Never post private review or ticket content in a public issue.
