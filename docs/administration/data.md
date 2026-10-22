# Data, retention, and deletion

Service Quality Review stores the program configuration, review criteria, selection and assignment history, human assessments, cited evidence, optional AI suggestions, calibration, findings, and released coaching needed for the review workflow.

The app runs on Atlassian Forge with hosted storage. Optional AI uses Forge LLMs. The runtime has no separate Magnascale-hosted application backend or external analytics service. Support correspondence is handled separately through Magnascale's support channels.

## Current permissions apply to retained content

Stored evidence and derived content do not bypass current Jira/JSM access. The app withholds affected content when source access cannot be verified, or when a stored excerpt no longer matches an edited or deleted source.

Numeric report rows and completed-results CSV follow current issue visibility and exclude private notes, quotations, and AI text. See [Results and exports](../guides/results.md).

## Fixed retention

Retention is fixed; there is no customer retention editor or legal-hold guarantee. Earlier parent-record expiry can shorten these periods. The table describes policy bounds, not an exact physical-deletion deadline. Background cleanup is bounded and can wait while related work remains active.

| Information | Retention |
| --- | --- |
| Unsubmitted drafts | Up to 90 days after last save. |
| Unused AI evidence and suggestions | Up to 30 days after the request. |
| Submitted reviews, revisions, cited evidence, and period history | Up to 365 days after the period first closes or is cancelled. Reopening or corrections do not restart that clock. |
| Calibration history | Up to 365 days after reveal or cancellation, within a maximum 730-day exercise lifetime and earlier linked-record expiry. |
| A period that is never closed | Hidden 730 days after opening, with advance notices. Cleanup can wait for related active work. |
| Findings spanning periods | Subject to linked-period expiry, up to 365 days after the latest linked period first ends, and no more than 730 days after finding creation. |
| Configuration audit history | 365 days. |
| Published review criteria | While referenced, then 365 days after the last reference expires. |
| In-app Updates and read state | Up to 365 days, never beyond the parent record. |
| Program settings | Until program or site data is deleted. |
| Content-free deletion receipts | 30 days. |
| Program-closure safety marker | An opaque program identifier and completion time remain indefinitely after program deletion to block late writes; no account association or review content is retained in that marker. |

Expired information is withheld when checked for access. Previously downloaded or delivered content cannot be recalled.

## Delete a program or site app data

Program managers can delete their program from its settings. Jira or app administrators can delete a program or erase all app data for the site from **App settings → Access**. Managers can also delete review periods that have not started reviews.

1. Export authorized completed results you need before deleting.
2. Select the intended program or site scope.
3. Preview the deletion and inspect its record counts.
4. Read and confirm the permanent-deletion statement.
5. Use **Check deletion status** to follow cleanup. If it reports a failure, use **Retry cleanup**.

Accepted deletion hides the affected data immediately; physical cleanup continues in the background. The app cannot restore it. Deleting app data does not delete the original Jira requests, created corrective Jira work, or copies of exports held elsewhere. Atlassian platform backups follow Atlassian's own lifecycle.

## Closed Atlassian accounts

When Atlassian reports a stored account as closed, the app redacts the account's identity in place within 30 days of learning of the closure. Affected program review content is temporarily hidden during processing; unrelated programs remain available.

History retains scores and counts under a **Former user** replacement identifier. Notes, quotations, and other free text about that person on reviews of their work are removed, and calibration results they participated in are removed. Names mentioned in free text about other people are not automatically searched. A replacement label does not guarantee anonymity in the wider context.

For a privacy request, contact [privacy@magnascale.com](mailto:privacy@magnascale.com).

## Licence expiry and uninstalling

Licence expiry does not erase records: authorized reading and completed-results export continue under the normal retention and access rules. New work pauses. Renewal does not automatically replay work that failed while unlicensed.

Export needed outcomes **before uninstalling**. A reinstall starts a new installation and does not automatically restore old data. Contact support within **21 days of uninstalling** if you need help requesting recovery through Atlassian. Recovery depends on Atlassian and is not guaranteed. See [Atlassian's hosted-storage lifecycle](https://developer.atlassian.com/platform/forge/storage-reference/hosted-storage-data-lifecycle/).

## Residency and policy information

Supported Forge storage residency follows the host product's pinning and migration. This does not fix the location of every AI inference, invocation, log, or support interaction. See [Availability and policies](../help/availability.md) for policy context and contact details.
