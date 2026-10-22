# Manage app and program access

Keep administrative access, program membership, and Jira source permissions aligned. Each serves a different purpose.

## App administrators and program creators

Authorized administrators use **App settings → Access** to manage app access and program-creator grants. Grant program creation to people responsible for setting up and managing a review practice.

App administration enables administrative functions such as diagnostics and supported data-erasure controls. It does not grant access to private reviews. An administrator who also needs to review or manage a program must have the appropriate program role and Jira access.

## Program participation

Program managers maintain reviewers, reviewed agents, and manager responsibilities using the program's people and manager controls. Check current Jira/JSM access before assigning reviews.

When someone changes role or leaves the team:

1. Review their app grants and program participation.
2. Check pending review and calibration assignments.
3. Use supported assignment or exercise recovery actions where needed.
4. Update Jira permissions through your organization's normal process.

Removing access does not change a past judgment into a different outcome. It changes which retained content can currently be disclosed.

## Diagnose an access problem

Check the actual signed-in Atlassian account, then confirm the program role, assignment, review state, and source visibility. Jira issue access and comment/JSM visibility can differ.

If the source check is unavailable or ambiguous, the app withholds affected content. Restore the required access and retry the displayed action. Do not grant broader permissions simply to make a particular score visible.

For report numbers and CSV, current issue visibility applies without disclosing cited comment text. See [Results and exports](../guides/results.md).

## Collect safe diagnostics

An administrator opens **App settings → Diagnostics** and copies **Support information** when contacting support. The summary contains app version, licence state, counts, and recent failure categories without names, account identifiers, or ticket text.

Send it through [support's private channels](../help/support.md), alongside the action, time, and time zone. Never include passwords, API tokens, ticket bodies, or private review content in a public GitHub issue.
