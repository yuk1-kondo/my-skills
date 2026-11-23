---
name: verify-checkable-claims
description: "Check quotas, prices, catalog contents and other checkable facts against a primary source before stating them, and present anything unconfirmed as unconfirmed."
---

# Verify Checkable Claims Before Asserting Them

## Classify the claim

- Sort each factual claim you are about to make into numbers such as quotas, prices and limits, existence claims about products, apps or features, and current state claims such as schedules or catalog contents.

- Treat all three kinds as checkable, and hold them to the same standard before stating any of them as fact.

- Downgrade a claim to a clearly marked estimate or unknown when you cannot check it in this session, instead of presenting it with the same confidence as a verified one.

## Check the primary source

- Go to the primary source for the claim, such as the vendor's own documentation, pricing page, official catalog or the live service itself, before repeating a figure from a post, article or third party summary.

- Use `browser.search` to find the primary source and `browser.open` or `browser.browse` to read it, and record which source settled the claim.

- Say explicitly when the primary source does not publish the figure, rather than filling the gap with a third party number.

- Recheck time sensitive claims such as event tracks, deadlines and plan terms at the moment you rely on them, because an earlier reading may already be stale.

## Handle absence claims with extra care

- Search the actual catalog, hub or listing itself before saying a product, app or integration does not exist.

- Phrase a negative result as what you searched and did not find, naming the catalog and the terms used, instead of a flat statement that the thing does not exist.

- Revisit an absence claim whenever new research touches the same catalog, and correct the earlier statement plainly when the thing turns up.

## Present with the source state attached

- Attach the source to each load bearing number or existence claim in your reply, so the user can see what it rests on without asking.

- Separate verified facts, secondary reports and your own inference into visibly different statements.

- Correct a claim immediately and in the same thread when a check overturns it, and restate the corrected version rather than only noting the error.

## Available connectors

- Use `muse.connector_search` to find other connectors and `muse.skill_search` to find related skills.

- If nothing here fits, look on the web for a maintained API or MCP server and set it up with [Custom Connectors and MCPs](/opt/muse/skills/custom-connector-setup/SKILL.md), or build a custom connector.

## Alternatives for better results

- Prefer one primary source read over several secondary summaries when a single figure or existence claim decides the recommendation.

- Ask the user to confirm from their own account screen when a quota or plan detail is only visible after login and no public source publishes it.
