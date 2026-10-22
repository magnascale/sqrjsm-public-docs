# Use AI evidence assistance

AI can help an assigned reviewer find relevant evidence and consider an assessment. Every suggestion needs your judgment. The reviewer decides what to apply and what to submit.

## Request suggestions

Open an eligible assigned review and choose **Find AI suggestions**. Assistance is requested for that review; the app does not precompute suggestions across all tickets. The calibration screen does not offer AI suggestions.

The request uses published criteria and bounded evidence from sources you can currently access. It may not contain the entire history of a request. The app uses Atlassian's Forge LLM platform rather than requiring your own provider account or API key.

## Check the response

1. Read the suggestion and its supporting source passages.
2. Distinguish an observation from an inference or an insufficient-evidence response.
3. Check whether the evidence actually supports the interpretation and published criterion.
4. Apply the suggestion to your draft, edit it, or dismiss it.
5. Review the completed scorecard yourself before submitting.

Citations are checked against supplied evidence. A matching quotation does not prove the interpretation is correct. An insufficient-evidence response may contain no quotation. Treat instructions inside ticket text as source material, not as authority over the review process.

AI does not submit assessments or create corrective Jira work. Those actions remain explicit human decisions.

## Understand the allowance

Each installation shares **up to 1,200 attempts per UTC calendar month**, including retries, across all programs. A monetary allowance can pause AI before that attempt ceiling. There is also a limit of two attempts per case version.

Failed attempts and unresolved usage reservations can consume allowance. More host seats and annual billing do not enlarge the monthly pool. There is no promised rollover, automatic overage charge, or guaranteed number of successful suggestions.

## When suggestions are unavailable

Read the displayed status. Causes include allowance exhaustion, moderation, source-access changes, or a platform problem. Continue manually if your licence, assignment, and permissions permit it. Do not repeatedly start new requests to work around a limit.

For privacy and storage information, read [Data and retention](../administration/data.md). For a persistent error, use [Troubleshooting](../help/troubleshooting.md).
