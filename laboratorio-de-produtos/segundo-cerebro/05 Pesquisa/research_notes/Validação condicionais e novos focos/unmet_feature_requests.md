# Unmet Feature Requests on Public Trackers as Add-on Demand, plus the Final Jira Verdict (data collected 2026-10-12)

*Method note. All Atlassian numbers come from my own calls on 2026-10-12:*
- *the public tracker's REST API (`jira.atlassian.com/rest/api/2/search`, JQL `type = Suggestion AND status not in (Closed, Resolved) ORDER BY votes DESC`);*
- *the Marketplace REST API (`marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=…&text=…&withVersion=true`, plus the `/pricing/cloud/live` and `/versions` endpoints).*

*"inst" means active cloud installs (`totalInstalls`). Ratings are shown as stars(count). The Connect/Forge flag in the API varies between queries for the same app, so treat it as approximate (round 1 saw the same thing). The `/versions` endpoint returns at most 50 versions, so "oldest" is a true first release only when the app has 50 or fewer versions.*

*Other trackers I fetched directly:*
- *Asana (Discourse JSON);*
- *ClickUp (Canny HTML state);*
- *Zendesk (Help Center community API).*

*Blocked or not reached:*
- *HubSpot Ideas (Cloudflare 403);*
- *Google Issue Tracker (HTTP 401 without a session);*
- *monday.com (Bettermode, JS/GraphQL only);*
- *Figma, Airtable, Zoom and Calendly forums (inSided, JS-only);*
- *Canva, Notion and Trello community hosts (proxy 502);*
- *Microsoft Feedback Portal (JS-only).*

*Playwright could not launch (Chromium sandbox error as root). I used 6 of the 15 allowed WebSearch calls.*

---

## Q1. Atlassian public tracker: most-voted open suggestions, and whether Marketplace apps already solve them

### Takeaway
There is enormous, decade-old demand, with about 14,700 open suggestions across the three projects and many over 1,000 votes. But most top requests are either:
- **not buildable by an app**: native UI, native emails, card layout, permissions; or
- **already served by entrenched paid or free apps**.

The decisive new fact for 2026 is that **tracker mining is itself a crowded strategy**. Solo and AI-assisted vendors now post "I built this" comments on the biggest tickets, and their apps sit at **0–18 installs** months later.

### Cited Findings
**Size of the open backlog (2026-10-12)**
- Open suggestions: **JRACLOUD 5,716, CONFCLOUD 4,359, JSDCLOUD 4,641** (JQL `total`) — [JRACLOUD query](https://jira.atlassian.com/rest/api/2/search?jql=project%20%3D%20JRACLOUD%20AND%20type%20%3D%20Suggestion%20AND%20status%20not%20in%20(Closed%2C%20Resolved)%20ORDER%20BY%20votes%20DESC)
- JSWCLOUD (the old Jira Software project) holds only 161 open suggestions, the largest with 114 votes. Timeline and Plans items now live in JRACLOUD — [JSWCLOUD query](https://jira.atlassian.com/rest/api/2/search?jql=project%20%3D%20JSWCLOUD%20AND%20type%20%3D%20Suggestion%20AND%20status%20not%20in%20(Closed%2C%20Resolved)%20ORDER%20BY%20votes%20DESC)

**Top open Jira (JRACLOUD) suggestions, with an app check**

Columns: votes, created date, tracker status, then the Marketplace situation (installs, rating, annual price at 25 users unless noted).

| Key | Request | Votes | Created | Tracker status | Marketplace situation |
|---|---|---|---|---|---|
| [JRACLOUD-4812](https://jira.atlassian.com/browse/JRACLOUD-4812) | Default values of system fields | 2,798 | 2004-10-06 | Future Consideration | Big Fig Tree "Default Values for 'Create Issue' screen" is **free**: 2,445 inst, 4.09(26). Newcomers Kalaux (2 inst, 2026-02) and Ordixio "Field Defaults" (1 inst, 2026-07) |
| [JRACLOUD-85694](https://jira.atlassian.com/browse/JRACLOUD-85694) | Customize card fields in team-managed projects | 2,462 | 2018-11-21 | Future Consideration | Native board UI; no app surface (inference) |
| [JRACLOUD-91595](https://jira.atlassian.com/browse/JRACLOUD-91595) | Milestones for (basic) Timeline | 2,425 | 2019-03-05 | Under Consideration | Every Gantt suite has milestones. "Project Milestones" (ij-solutions) has 59 inst at $62.5/yr. Millarum Roadmap, promoted in the ticket's comments on 2026-07-06, has **6 inst** |
| [JRACLOUD-85680](https://jira.atlassian.com/browse/JRACLOUD-85680) | Issues from other projects on a team-managed board | 1,897 | 2018-11-01 | Future Consideration | Native board; no app surface (inference) |
| [JRACLOUD-91572](https://jira.atlassian.com/browse/JRACLOUD-91572) | Subtasks in Timeline | 1,848 | 2020-01-16 | **In Progress** | Platform is absorbing it |
| [JRACLOUD-72631](https://jira.atlassian.com/browse/JRACLOUD-72631) | Plain-text Markdown editor | 1,772 | 2019-07-30 | Future Consideration | Markdown apps are small: Fulstech 301 inst at 2.68(14). The native editor can't be replaced (inference) |
| [JRACLOUD-37520](https://jira.atlassian.com/browse/JRACLOUD-37520) | Bulk clone | 1,755 | 2014-03-17 | Under Consideration | **Saturated:** Deep Clone 11,670 inst 4.47(134); Elements Copy & Sync 2,352; Clone Plus 1,612; Easy Clone 1,029 4.86(36) |
| [JRACLOUD-7266](https://jira.atlassian.com/browse/JRACLOUD-7266) | Customize notification email templates | 1,597 | 2005-07-08 | Gathering Interest | Email This Issue 5,548 inst 4.41(182), $500/yr. Notification Assistant 1,145 inst, $500/yr ($2,000 at 100 users). Apps send their own emails; native emails can't be changed (inference) |
| [JRACLOUD-75868](https://jira.atlassian.com/browse/JRACLOUD-75868) / [72007](https://jira.atlassian.com/browse/JRACLOUD-72007) | JQL for sprint added/removed; sprint dates in JQL | 1,491 / 1,319 | 2018 / 2019 | Gathering Interest | JQL Search Extensions 3,864 inst; JQL Tricks 1,104; GO! JQL 186; Advanced JQL Functions 163; SnapJQL 15 |
| [JRACLOUD-10507](https://jira.atlassian.com/browse/JRACLOUD-10507) | Archive components | 1,234 | 2006-06-29 | Gathering Interest | Component Archiver (KeulTech), 1 inst, first release 2026-10-01; Subcomponents 1,169 inst 3.39 |
| [JRACLOUD-34307](https://jira.atlassian.com/browse/JRACLOUD-34307) | Single-project export/backup | 1,031 | 2013-08-14 | Gathering Interest | Rewind 1,287; Revyz 967; GitProtect 462; plus a 2026 newcomer at 1 inst |
| [JRACLOUD-40049](https://jira.atlassian.com/browse/JRACLOUD-40049) | Translate custom-field options | 993 | 2014-09-19 | Under Consideration | No dedicated app found. Native option rendering can't be changed by an app (inference) |
| [JRACLOUD-91568](https://jira.atlassian.com/browse/JRACLOUD-91568) / [91560](https://jira.atlassian.com/browse/JRACLOUD-91560) | Epics or issues from several projects on the Timeline | 969 / 812 | 2018 / 2020 | Gathering / Future Consideration | Covered by Gantt, roadmap and portfolio apps (see Q2) |
| [JRACLOUD-62109](https://jira.atlassian.com/browse/JRACLOUD-62109) | Two-Dimensional gadget summing story points | 853 | 2011-03-07 | Gathering Interest | **Saturated:** Rich Filters 9,595; eazyBI 10,750; Custom Charts 7,893; Great Gadgets 3,603 |
| [JRACLOUD-2734](https://jira.atlassian.com/browse/JRACLOUD-2734) | Last comment as a navigator column | 796 | 2003-11-21 | Gathering Interest | codefortynine "Comment Custom Fields" already does this: 266 inst |
| [JRACLOUD-36415](https://jira.atlassian.com/browse/JRACLOUD-36415) | Trash/recycle bin | 707 | 2014-01-08 | Under Consideration | Not checked |
| [JRACLOUD-90480](https://jira.atlassian.com/browse/JRACLOUD-90480) | Velocity gadget | 573 | 2014-05-30 | Gathering Interest | Broken Build velocity gadget 2,263 inst at $212.5/yr; others |
| [JRACLOUD-68499](https://jira.atlassian.com/browse/JRACLOUD-68499) / [87846](https://jira.atlassian.com/browse/JRACLOUD-87846) | Public wallboard link; share roadmaps without a license | 548 / 440 | 2018 / 2019 | Gathering Interest | External Share for Jira 1,057 inst 4.71(39), **$687.5/yr at 25 users, $2,750 at 100**. Laya Board (free) 317; miniOrange 135; Apportunity 69 at 2.75★ |

Sources:
- [JRACLOUD top-voted query](https://jira.atlassian.com/rest/api/2/search?jql=project%20%3D%20JRACLOUD%20AND%20type%20%3D%20Suggestion%20AND%20status%20not%20in%20(Closed%2C%20Resolved)%20ORDER%20BY%20votes%20DESC&maxResults=60)
- Marketplace searches, e.g. ["default values"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=default%20values&limit=10&withVersion=true), ["bulk clone"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=bulk%20clone&limit=10&withVersion=true) and ["external share dashboard"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=external%20share%20dashboard&limit=10&withVersion=true)
- Pricing, e.g. [External Share pricing](https://marketplace.atlassian.com/rest/2/addons/ovh.atlasinc.jira.jira-share/pricing/cloud/live)

**Top open Confluence (CONFCLOUD) suggestions, with an app check**

| Key | Request | Votes | Created | Marketplace situation |
|---|---|---|---|---|
| [CONFCLOUD-46077](https://jira.atlassian.com/browse/CONFCLOUD-46077) | Adjust font size | 1,276 | 2017-02-01 | Fonts for Confluence (free) 200 inst at **1.88★**; three paid apps at 5–16 inst. The editor itself can't be restyled by an app (inference) |
| [CONFCLOUD-78513](https://jira.atlassian.com/browse/CONFCLOUD-78513) | Nest bodied macros | 1,209 | 2019-10-28 | Native editor; no app surface |
| [CONFCLOUD-5095](https://jira.atlassian.com/browse/CONFCLOUD-5095) | Inherited edit permissions | 973 | 2006-01-09 | Native permissions; no app surface |
| [CONFCLOUD-3191](https://jira.atlassian.com/browse/CONFCLOUD-3191) | Copy an entire space | 882 | 2005-05-10 | Copy Space (Appfire) 1,264 inst at 3.83(31); Copy Page Tree 2,092; Space Sync 767 |
| [CONFCLOUD-36137](https://jira.atlassian.com/browse/CONFCLOUD-36137) | Custom CSS | 877 | 2012-11-08 | Very weak incumbents: weweave Custom CSS 142 inst at 1.88(4), Connect 2021; Atlas Cloudlet at 1.25★. Forge cannot inject site-wide CSS (inference, not verified) |
| [CONFCLOUD-1732](https://jira.atlassian.com/browse/CONFCLOUD-1732) | Numbered headings | 674 | 2004-08-27 | **Saturated:** Appfire Numbered Headings 5,132 inst 4.54(114); Warsaw Dynamics bundle 3,163; 2026 newcomers at 2–7 inst |
| [CONFCLOUD-35218](https://jira.atlassian.com/browse/CONFCLOUD-35218) | Incoming-links macro | 629 | 2014-10-08 | Linking for Confluence (Appfire) 1,218 inst at 3.54(42), $162.5/yr. Apps+ Incoming & Outbound Links+ 232 inst, $145/yr. The newcomer "Incoming Links for Confluence" (released 2026-09-20, promoted in the ticket on 2026-10-07) has 1 inst |
| [CONFCLOUD-71390](https://jira.atlassian.com/browse/CONFCLOUD-71390) | Task report across all spaces | 287 | 2021-01-04 | Meetical's free helper has 364 inst; Reporting for Confluence 1,042 |

Sources: [CONFCLOUD query](https://jira.atlassian.com/rest/api/2/search?jql=project%20%3D%20CONFCLOUD%20AND%20type%20%3D%20Suggestion%20AND%20status%20not%20in%20(Closed%2C%20Resolved)%20ORDER%20BY%20votes%20DESC), [API "incoming links"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=confluence&text=incoming%20links&limit=10&withVersion=true), [API "custom css theme"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=confluence&text=custom%20css%20theme&limit=10&withVersion=true)

**Top open Jira Service Management (JSDCLOUD) suggestions, with an app check**

| Key | Request | Votes | Created | Status | Marketplace situation |
|---|---|---|---|---|---|
| [JSDCLOUD-4328](https://jira.atlassian.com/browse/JSDCLOUD-4328) | Read-only fields in the customer portal | 1,724 | 2016-09-27 | Under Consideration (PM, 2021: "will not be able to prioritise") | Deviniti Extension for JSM 5,301 inst 4.58(150), **$610/yr at 25 users**. My Requests Extension 1,500. Extra Fields for JSM (Narva) 193 inst at 3.75, $125/yr. Newcomers: PortalView (AppRL, key `br.com.apprl`, apparently Brazilian; first release 2026-01-16) **18 inst** at $247.5/yr; Pitronote "Issue Details" (promoted in the ticket 2026-05-18) **5 inst**; Katabarwa "Portal Extension" (promoted 2026-10-05) **1 inst** |
| [JSDCLOUD-4698](https://jira.atlassian.com/browse/JSDCLOUD-4698) | Outgoing email logs | 1,511 | 2017-01-25 | Gathering Interest | An app can't see Atlassian's own sent mail (inference). Katabarwa "Notification Log for JSM" has 2 inst |
| [JSDCLOUD-4642](https://jira.atlassian.com/browse/JSDCLOUD-4642) | Custom field values in customer notifications | 1,286 | 2017-01-11 | Under Consideration | Email This Issue and Notification Assistant (both $500/yr at 25 users) |
| [JSDCLOUD-4685](https://jira.atlassian.com/browse/JSDCLOUD-4685) | **Merge issues** | 1,238 | 2017-01-23 | Future Consideration. Atlassian, 19 Sep 2022: "We aren't considering this at this point in time" and recommends linking | Merge Agent (codefortynine) 759 inst at 4.29(7), **$260/yr at 25, $1,040 at 100**, actively updated (latest version 2026-10-12). Ticket Merger (free) 390 at 3.75(10). Duplicate AI 100. Merge Assistant (La Forge, 2025-10) 35. IssueMerge (Protty, 2026-07) 0. Merge Better 3 |
| [JSDCLOUD-12765](https://jira.atlassian.com/browse/JSDCLOUD-12765) | Canned responses on resolution/transition screen | 1,155 | 2023-06-19 | Under Consideration | Canned Responses Pro (Appfire) 1,967 inst 4.70(108), $432.5/yr |
| [JSDCLOUD-328](https://jira.atlassian.com/browse/JSDCLOUD-328) / [325](https://jira.atlassian.com/browse/JSDCLOUD-325) / [4636](https://jira.atlassian.com/browse/JSDCLOUD-4636) | Assignee, SLA and linked issues on the portal | 888 / 654 / 857 | 2014–2017 | Reviewing / Under Consideration | Same crowd as JSDCLOUD-4328, plus ChiliShelf "Customer Portal SLAs" 48 inst at $250/yr |

Sources: [JSDCLOUD query](https://jira.atlassian.com/rest/api/2/search?jql=project%20%3D%20JSDCLOUD%20AND%20type%20%3D%20Suggestion%20AND%20status%20not%20in%20(Closed%2C%20Resolved)%20ORDER%20BY%20votes%20DESC), [JSDCLOUD-4685 issue JSON](https://jira.atlassian.com/rest/api/2/issue/JSDCLOUD-4685?fields=status,description,comment), [API "merge"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=merge&limit=10&withVersion=true), [API "portal request details read only fields"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=portal%20request%20details%20read%20only%20fields&limit=10&withVersion=true), [Merge Agent pricing](https://marketplace.atlassian.com/rest/2/addons/com.codefortynine.merge-for-jira/pricing/cloud/live)

**Tracker-mining newcomers (adversarial evidence)**
- Katabarwa Labs published **10+ Forge apps between 2026-09-01 and 2026-10-06**, each a top-voted ticket turned into an app (portal fields, notification log, templates/defaults, project backup, assets export…). All have **0–2 installs** — [API "Katabarwa"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=Katabarwa&limit=10&withVersion=true)
- Millarum: three apps from 2026-07/08 with 5–6 installs each, promoted in JRACLOUD-91595 — [API "Millarum Roadmap"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=Millarum%20Roadmap&limit=10&withVersion=true)
- Vendors replying on the top tickets with their own apps: JSDCLOUD-4328 (Pitronote 2026-05-18; Katabarwa 2026-10-05), CONFCLOUD-35218 (2026-10-07) and JRACLOUD-91595 (Millarum 2026-07-06) — issue JSON for [JSDCLOUD-4328](https://jira.atlassian.com/rest/api/2/issue/JSDCLOUD-4328?fields=comment), [CONFCLOUD-35218](https://jira.atlassian.com/rest/api/2/issue/CONFCLOUD-35218?fields=comment) and [JRACLOUD-91595](https://jira.atlassian.com/rest/api/2/issue/JRACLOUD-91595?fields=comment)
- JSDCLOUD-4685 has had vendor links in its comments since 2018 (codefortynine 2018-12-03, Issue Merger 2020/2022, Neil Simbulan 2025-06-07, La Forge 2025-10-27) — [issue JSON](https://jira.atlassian.com/rest/api/2/issue/JSDCLOUD-4685?fields=comment)

**Newcomers that did gain traction, all from vendors with existing portfolios**
- "Simple Gantt & Roadmap Timeline Dashboard Gadget" (Agilis/Simple Reports):
  - first version 2026-01-31;
  - **267 installs**, $125/yr at 25 users, $500 at 100;
  - the vendor has 10 apps and about 7,005 installs in total.
  - Sources: [versions](https://marketplace.atlassian.com/rest/2/addons/com.simple-reports.gantt/versions?limit=50&hosting=cloud), [pricing](https://marketplace.atlassian.com/rest/2/addons/com.simple-reports.gantt/pricing/cloud/live), [vendor](https://marketplace.atlassian.com/rest/2/addons/vendor/1215481)
- "Laya Export Studio" (Agile Pulse):
  - first version 2026-06-09;
  - **530 installs**, 5.0(4), paid;
  - the vendor has 8 apps and about 7,590 installs.
  - Laya Board (2026-07-21, free) has 317.
  - Sources: [versions](https://marketplace.atlassian.com/rest/2/addons/LayaExportStudio/versions?limit=50&hosting=cloud), [vendor](https://marketplace.atlassian.com/rest/2/addons/vendor/1225397)
- Blue Leap Apps "Simple Gantt" (first version 2026-05-01, free) has 133 installs — [versions](https://marketplace.atlassian.com/rest/2/addons/blueleapapps.simple-gantt/versions?limit=50&hosting=cloud)

### Inferences
- In 2026 the votes on a ticket do not translate into installs for a cold-start vendor. On the 1,724-vote portal-fields ticket, three new apps got 1–18 installs; on the 1,238-vote merge ticket, two recent newcomers got 0 and 35. **Marketplace ranking, existing reviews and vendor cross-promotion dominate.** The only fast-growing newcomers I found belong to vendors with 8–10 existing apps.
- Of the roughly 40 top requests reviewed, about a third cannot be built by an app because they live in native UI, editor, permissions or email. About half are already served by apps with 1,000+ installs. Only a handful (merge, incoming links, external sharing, archive components) have thin or stale coverage, and each has a small buyer pool (see Q5).
- An AI-assisted shotgun approach (Katabarwa) is already running, so a "build what the tracker asks for" playbook has no edge by itself.

### Gaps
- Atlassian publishes no per-app revenue, so the paid-install share (sites with more than 10 users) is unknown.
- I did not open the comment threads of the remaining top tickets to check for still more vendor plugs.

---

## Q2. Timeline and Plans gaps: baselines, PDF/PowerPoint export, cross-project dependencies on Standard

### Takeaway
The timeline gaps with real vote mass are milestones (2,425), cross-project timelines (812 + 969) and external sharing (440). Baselines (323) and timeline PDF export (25) are small. Every large one is already served by about 70 Gantt and roadmap apps, and the newcomers who aimed at these exact gaps in 2026 have 6–29 installs. The "narrow wedge" recommended in round 1 has been tried by others and is not working for them.

### Cited Findings
Most-voted open Timeline and Plans suggestions (components "Timeline (legacy)…" and "Plans…"):
- Milestones for basic Timeline: 2,425 votes (2019).
- Subtasks in Timeline: 1,848 (In Progress).
- Epics from different projects: 969 (2018).
- Milestones for Plans: 850 (2014).
- Cross-project Timeline: 812 (2020, Future Consideration).
- More custom fields in Plans: 534.
- Share roadmaps without a license: 440.
- Exclude weekends: 380.
- Epic adjusts children's dates: 343.
- Working days in Plans: 339.
- **Baseline a plan: 323 (2020).**
- Dashboard gadgets for Plans: 222.
- Critical path: 98.

Source: [Timeline/Plans component query](https://jira.atlassian.com/rest/api/2/search?jql=project%20%3D%20JRACLOUD%20AND%20type%20%3D%20Suggestion%20AND%20status%20not%20in%20(Closed%2C%20Resolved)%20AND%20component%20in%20(%22Plans%20-%20Timeline%22%2C%22Timeline%20(legacy)%20-%20Timeline%20View%22%2C%22Plans%20-%20Share%20%2F%20Export%22)%20ORDER%20BY%20votes%20DESC)

Export requests are tiny:
- "Export plan as PDF": **25 votes** (2023).
- Dependencies report to Excel: 39.
- Monthly view in timeline export: 21.
- An API or automation action to export the Plans timeline as PDF: 3.
- One bug report mentions "Date not visible when exporting timeline view as image", which implies an image export already exists natively.

Source: [export query](https://jira.atlassian.com/rest/api/2/search?jql=project%20in%20(JRACLOUD%2C%20JSWCLOUD)%20AND%20type%20%3D%20Suggestion%20AND%20status%20not%20in%20(Closed%2C%20Resolved)%20AND%20(summary%20~%20%22export%20plan%22%20OR%20summary%20~%20%22timeline%20PDF%22)%20ORDER%20BY%20votes%20DESC)

Baseline apps:
- "Baseline X" (Optimizory): first version 2024-10-23, **29 installs after about 2 years**, $205/yr at 25 users and $820 at 100.
- "Baseline Guard": 1 install (2026-08).
- "Baseliner.ai": 3 installs.
- Google Autocomplete for "jira timeline baseline" returns **no suggestions**.
- Sources: [API "baseline"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=baseline&limit=10&withVersion=true), [Baseline X versions](https://marketplace.atlassian.com/rest/2/addons/com.otpl.jira.plugins.baselinex/versions?limit=50&hosting=cloud), [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=jira%20timeline%20baseline)

Cross-project timeline apps:
- The "cross project timeline" search returns 2,142 results.
- Activity Timeline: 3,594 inst, 4.69(122).
- Hierarchy for Jira: 1,130.
- Portfolio Roadmaps (free): 1,467.
- Swanly: 1,418.
- Plus the Gantt suites from round 1: BigGantt 5,548, Structure Gantt 6,306, Portfolio by HeroCoders 4,993 and GanttTable 1,300.
- Source: [API "cross project timeline"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=cross%20project%20timeline&limit=10&withVersion=true)

PowerPoint export:
- "roadmap powerpoint" returns only generic roadmap apps.
- PDF exporters are entrenched: Better PDF Exporter 4,234 inst 4.82(469); Xporter 3,745 4.63(293); BigTemplate 3,611.
- Sources: [API "roadmap powerpoint"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=roadmap%20powerpoint&limit=10&withVersion=true), [API "timeline export pdf"](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=timeline%20export%20pdf&limit=10&withVersion=true)

Other wedges:
- The dashboard Gantt-gadget wedge suggested in round 1 was filled by Agilis on 2026-01-31: 267 installs, $125/yr at 25 users (see Q1).
- Google Autocomplete for "jira timeline milestones" returns only "jira timeline show milestones" — [Autocomplete](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&gl=us&q=jira%20timeline%20milestones)

### Inferences
- **Baselines:** low votes, Premium-only context (Plans), a 2-year-old app with 29 installs, and no search demand. This fails G1 and G4.
- **PDF/PPT export of the timeline:** 25 votes, a native image export, and entrenched PDF exporters. This fails G2 and G4.
- **Cross-project dependencies and milestones on Standard:** large votes, but apps cannot extend the native Timeline. A newcomer must ship yet another timeline view and compete with roughly 10 suites at 1k–6k installs. That fails G2, and parity also fails G5.

### Gaps
- I did not check whether Forge exposes any extension point inside the native Timeline view. I found none in the marketplace evidence, and none of the dozens of timeline apps add to the native view.

---

## Q3. Final verdict on the round-1 CONDITIONAL "narrow Forge app for Jira" (Gantt/timeline wedge)

### Takeaway
**KILL** the timeline, Gantt and roadmap wedge. All three candidate wedges failed:
- baselines and export have tiny demand;
- the dashboard gadget wedge was taken in January 2026;
- milestones and cross-project already have Millarum and others at about 6 installs.

Recent tracker-mining newcomers without an existing portfolio sit at 0–29 installs. Atlassian as a marketplace stays usable (billing, Brazil payouts look feasible; see Q4), but no Jira timeline wedge passes G2, G4 or G8.

### Cited Findings
- Evidence for each wedge: see Q2 (Baseline X 29 inst; export PDF 25 votes; Agilis gadget; Millarum 6 inst).
- Round 1 already found that the largest Gantt vendors are on Forge with 2026 releases, and that most apps are free up to 10 users — [finalists_global_verification](../Oportunidade%20de%20produto%20validada%202026/finalists_global_verification.md)
- Remittance only starts after **US$500 in profit**, paid "within a minimum of 30 days from the time of sale, and no more than 60 days" — [Atlassian pricing, payment and billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)
- App approval "take[s] 10-15 business days, but approval times vary", and partners with Platinum, Gold or Silver status get expedited SLAs — [App approval guidelines](https://developer.atlassian.com/platform/marketplace/app-approval-guidelines/)

### Inferences
- **G8 arithmetic:**
  - Typical niche pricing is $125–260/yr at 25 users.
  - US$5k/month means about $60k/yr, which needs **about 230–480 paying 25-user sites**.
  - Only sites above 10 users pay.
  - The best 2026 newcomer in the category (Agilis, with a 10-app portfolio) has 267 total installs after 8 months.
  - Time to first payout is at least: build (4 wks) + approval (2–3 wks) + trial (30 days) + $500 threshold + 30–60 days. That is roughly **3–5 months** before any cash arrives.
- **Scores:**

  | Option | WTP | Saturation | Buyer power | Distribution | Build | Speed | Risk | Total |
  |---|---|---|---|---|---|---|---|---|
  | Jira timeline wedge (round 1 was 22) | 4 | 1 | 5 | 2 | 3 | 1 | 3 | **19/35** |

### Gaps
- None material for the decision. Per-app revenue is not public.

---

## Q4. Atlassian Marketplace payouts to a Brazilian individual or company (payment method, countries, tax forms, thresholds)

### Takeaway
Payouts look **feasible for a Brazilian individual using a CPF**:
- the Partner Agreement contracts with "the individual or entity";
- payment is by EFT or international wire to a bank account in the partner's own name;
- the threshold is US$500;
- Atlassian staff in October 2026 confirmed payouts for other non-listed countries (Canada, Guatemala) on the same KYC + W-8BEN/W-8BEN-E path;
- Brazilian vendors already list paid apps.

The open risk is **US withholding**. Atlassian acts as a US withholding agent (30% default without a W-8). The US has **no income-tax treaty with Brazil**, so a Brazilian cannot claim a reduced treaty rate. Whether anything is withheld depends on how Atlassian classifies the income: business profits/sales (one partner was told this) or royalties (30%). This must be confirmed in writing before building.

### Cited Findings
**Contract and payment mechanics (Marketplace Partner Agreement)**
- The Agreement is between Atlassian Pty Ltd and "the individual or entity registering as a vendor or partner". It was last revised on 1 December 2025 — [Marketplace Partner Agreement](https://www.atlassian.com/licensing/marketplace/publisheragreement)
- "You agree to provide Atlassian with information on a valid bank account in your name, and Atlassian will make payments to that account via Electronic Funds Transfer". Payments may be withheld "until the total amount due to you (net of any tax withholding…) is at least U.S. $500.00", and "fees charged by your bank in connection with wire transfers… are solely your responsibility" — [Marketplace Partner Agreement](https://www.atlassian.com/licensing/marketplace/publisheragreement)
- "Atlassian maintains the right to deduct or withhold any applicable taxes payable by you from amounts due" — [Marketplace Partner Agreement](https://www.atlassian.com/licensing/marketplace/publisheragreement)

**Atlassian developer documentation**
- An individual can create a partner profile under their own name — [Become a partner](https://developer.atlassian.com/platform/marketplace/become-a-partner/)
- Partner due diligence requires:
  - "Business name, physical address, registration number and/or tax identification number";
  - an ID document;
  - a Stripe selfie verification;
  - the Partner Security Questionnaire, completed within 14 days.
  - Source: [Partner due diligence](https://developer.atlassian.com/platform/marketplace/partner-due-diligence/)
- The onboarding hub (updated 19 May 2026) requires "Tax, legal, and payout setup completed so you can receive disbursements", plus End User Terms and, where applicable, a DPA — [Decide pricing and licensing model](https://developer.atlassian.com/platform/marketplace/onboarding-hub/launch/decide-pricing-and-licensing-model/)
- Revenue share: 100% of Forge revenue up to US$1M lifetime, then 83% from 1 Oct 2026 — [Atlassian pricing, payment and billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/) (also in round 1)

**Country support, from Atlassian staff on the developer community (October 2026)**
- Canada: "fully supported… payouts directly to your Canadian bank account in USD (via wire/EFT). You'll just need to complete standard KYC and a Form W-8BEN… A registered/incorporated company is not required." A custom domain email is required; free webmail is not allowed. Posted 2026-10-07 by Atlassian staff (Kay Lawal) — [thread 103113](https://community.developer.atlassian.com/t/is-canada-a-supported-payout-country-for-marketplace-partners/103113)
- Guatemala company: "Atlassian pays revenue share in USD via international wire (SWIFT)… You will also complete a standard W-8BEN-E tax form". Posted 2026-10-02 by Atlassian staff — [thread 103074](https://community.developer.atlassian.com/t/can-a-company-registered-in-guatemala-become-a-marketplace-partner-and-receive-usd-payouts/103074)
- No published country list. A partner asked on 2026-08-09 and noted the support form requires a Vendor ID — [thread 102084](https://community.developer.atlassian.com/t/supported-countries-for-marketplace-partner-registration-and-payouts-where-is-this-documented/102084)
- A Ukrainian sole proprietor receives payouts directly to a local bank account (monobank) without Payoneer — [thread 102880](https://community.developer.atlassian.com/t/payouts-to-ukraine-bank-account-for-individual-developer-sole-proprietor-supported/102880)

**Tax form detail, from a Portuguese sole trader (partner-reported, September 2026)**
- Verification was approved using a personal tax number as both registration and tax ID.
- "Paid via Atlassian means Atlassian pay you, and they act as a US withholding agent. With no W-8 on file the statutory default is 30%". The W-8BEN is attached to the ECOHELP ticket.
- Atlassian told him "a U.S. TIN is required for exemption", but he used a foreign TIN on line 6a.
- Atlassian told him Marketplace sales are "business profits under Article 7, not royalties".
- Source: [thread 102404](https://community.developer.atlassian.com/t/individual-developer-no-registered-company-whats-the-minimum-verification-needed-to-publish-a-paid-via-atlassian-app/102404)
- **Contradiction to note:** the Agreement names Atlassian Pty Ltd (Australia) as the counterparty, while the partner reports US withholding-agent treatment. Both may be true (a US paying entity), but it is unverified.

**Brazil specifics**
- The IRS treaty list goes from "Bangladesh, Barbados, Belgium, Bulgaria" to "Canada, Chile, China". **Brazil is not a US treaty country** — [IRS tax treaties A–Z](https://www.irs.gov/businesses/international-businesses/united-states-income-tax-treaties-a-to-z)
- Brazilian vendors with paid listings:
  - individual Victor Torres (Belo Horizonte), 3 paid apps — [vendor](https://marketplace.atlassian.com/vendors/683198338/victor-torres);
  - Fator Tec LTDA — [vendor](https://marketplace.atlassian.com/vendors/895814828/fator-tec-ltda) (both from round 1);
  - AppRL (app key `br.com.apprl.portalview`), with a paid JSM app since 2026-01 — [API](https://marketplace.atlassian.com/rest/2/addons/br.com.apprl.portalview).

### Inferences
- **Registration and payout for a Brazilian individual: likely yes.** It would use the CPF as tax ID, KYC, a W-8BEN, a USD-capable account in his own name (a SWIFT-receiving Brazilian account), and a custom-domain email (about US$10–15/yr, which fits the budget).
- **The withholding risk is specific to Brazil:**
  - Without a treaty, a "royalty" classification would mean 30% US withholding, with no reduced rate available.
  - A "sale/business profits" classification (what Atlassian told the Portuguese partner) would normally mean no US withholding for a foreign person without a US trade or business.
  - This is my reading, not tax advice. It is the single fact to get in writing from Atlassian (ECOHELP ticket) before building.
- **Brazilian side:** the foreign income must be declared, monthly via carnê-leão as an individual, or through a company. Exchange contracts on inbound wires apply. I did not verify rates in this round; see the gtm_economics_payments notes from round 1.

### Gaps
- No official Atlassian statement on Brazil specifically. The cheapest resolution is to email the Marketplace partnerships contact who answered the Canada and Guatemala threads (address published in [thread 103113](https://community.developer.atlassian.com/t/is-canada-a-supported-payout-country-for-marketplace-partners/103113)), or to post a "Brazil individual" thread. Ask four things: (1) Brazil supported? (2) CPF accepted? (3) W-8BEN line 6a with a CPF and no treaty claim? (4) Income classified as royalty or sale?
- The exact Atlassian paying entity and whether it withholds on non-treaty residents.

---

## Q5. Other public trackers with vote counts: top unmet requests and marketplace or API fit

### Takeaway
Outside Atlassian, the public vote data I could reach (Asana, ClickUp, Zendesk) shows demand mostly for core-product features that no app can deliver (multiple assignees, subtask statuses), or vote counts in the hundreds (Zendesk). Most of these platforms also lack marketplace billing:
- Asana, ClickUp and HubSpot have no marketplace billing;
- Google Workspace has none (round 1);
- Microsoft requires a SaaS offer through Partner Center.

monday.com does have mandatory platform billing, but its board was unreadable here. **No non-Atlassian candidate passed the screening.**

### Cited Findings
**Asana** (forum.asana.com, Product Feedback, sorted by votes; "launched" items excluded)
- Multiple assignees: **2,412 votes** (2017).
- Visibility of all recurring tasks: 1,437 (2017).
- Tasks across workspaces: 1,110.
- Hide completed subtasks: 843 (in development).
- **Real-time two-way calendar integration: 810** (2017).
- Global rules library: 650.
- Hide weekends in timeline: 642.
- Rules that respect business days: 562 ("considered").
- Source: [Asana feedback JSON](https://forum.asana.com/c/forum-en/product-feedback/20/l/latest.json?order=votes&ascending=false)

**ClickUp** (clickup.canny.io, top)
- Subtasks inherit parent fields: **5,255** (2019, planned).
- Different statuses for subtasks: 4,685 (future).
- Email V2: 4,383.
- **Two-way Google Calendar sync: 4,064, "building now"**.
- Move items across workspaces: 2,840.
- Formula fields in dashboards: 2,787 (planned).
- Time blocking: 2,667 (planned).
- Source: [ClickUp Canny](https://clickup.canny.io/feature-requests?sort=top)

**Zendesk** (support.zendesk.com community API, sorted by votes; 18,024 posts)
- Top open or not-planned items:
  - add end-user as CC via trigger: 491 votes (2009, not_planned);
  - dashboard customization: 267 (not_planned);
  - follow article updates: 186;
  - automatic refresh in views: 176 (not_planned);
  - custom ticket fields in the Help Center request table: 175 (planned);
  - remove-CC trigger action: 154;
  - rich text in dynamic content: 150 (not_planned);
  - macro-usage report: 125 (not_planned);
  - Guide articles to PDF: 88.
- Source: [Zendesk posts by votes](https://support.zendesk.com/api/v2/community/posts.json?sort_by=votes&per_page=60)
- Zendesk paid apps are billed through a Stripe account linked to Zendesk's, with 1–90-day trials. I did not find the revenue share — [Zendesk submit your app](https://developer.zendesk.com/documentation/apps/publish-your-app-theme-or-bot/submit_your_app/)

**monday.com**
- The feature-request board exists, with 25 votes per member per month and quarterly review of top items. I could not extract the counts — [monday community process](https://community.monday.com/t/all-you-need-to-know-about-our-new-feature-request-process/58166)
- Revenue share is unclear:
  - a 2024 changelog says developers keep 85% after US$200k lifetime revenue — [monday revshare changelog](https://developer.monday.com/apps/changelog/announcing-the-revshare-program);
  - an undated monetization page says 0/100 — [monday monetization](https://monday.com/appdeveloper/monetization).

**Microsoft (Office add-ins)**
- Paid add-ins must be sold as SaaS offers through the Commercial Marketplace. Transactable SaaS can only be bought with work or school accounts — [Microsoft Learn](https://learn.microsoft.com/en-us/office/dev/store/monetize-addins-through-microsoft-commercial-marketplace)
- The Feedback Portal itself was not readable.

**Not reached**
- HubSpot Ideas (Cloudflare 403), Google Issue Tracker (401), Figma, Airtable, Zoom, Calendly (JS-only inSided), and Canva, Notion, Trello (proxy 502).
- Google's own docs say feature requests are prioritized by stars, and point to Apps Script component 191640 — [Google Cloud issue trackers](https://docs.cloud.google.com/support/docs/issue-trackers)

### Inferences
- The Asana and ClickUp top requests are core-product features. No app can add multiple assignees or subtask statuses.
- ClickUp's two-way calendar sync is "building now". The Asana calendar-sync request is better served by existing sync tools, and Asana has no marketplace billing. Sync tools were also killed in round 1 (Sheets ⇄ Calendar).
- Zendesk's vote counts are about 5× lower than Atlassian's and many items are "completed". I found no evidence that justifies a Zendesk build without a further census of the Zendesk Marketplace, which I did not run.

### Gaps
- Vote data for HubSpot, Google Workspace, Microsoft Excel/Outlook/Teams, monday.com, Figma, Notion, Canva, Trello, Airtable, Calendly, Zoom, Freshdesk and Shopify. Shopify's Discourse community has **no feature-request category** in its category list ([categories.json](https://community.shopify.com/categories.json)).
- These need a working headless browser or more search budget. I would expect them to repeat the pattern seen here (core features first), but that is unverified.

---

## Q6. Best 10 candidates, with deep validation of the top 3 through all gates

### Takeaway
**None is APPROVED.**
- Best three:
  1. **Merge tickets for JSM**: CONDITIONAL, weak.
  2. **External share of Jira dashboards and roadmaps**: CONDITIONAL, weak.
  3. **Confluence incoming links/backlinks**: KILL.
- The others are KILL.
- The binding failures are **G2** (no evidence that a portfolio-less newcomer wins in 2026) and **G8** (small buyer pools at US$125–700/yr per site).

### Cited Findings (candidate table; evidence in Q1–Q5)

Score columns: WTP = willingness to pay, Sat = low saturation, Power = buyer power, Dist = distribution without contacts, Build = buildability, Speed = speed to first revenue, Risk = low risk (1–5 each).

| # | Candidate | Demand evidence | Closest competitors (inst, rating, price/yr at 25 users) | WTP | Sat | Power | Dist | Build | Speed | Risk | Total | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Merge tickets for JSM (Forge) | JSDCLOUD-4685, 1,238 votes, 2017; Atlassian said in 2022 it was "not considering"; Autocomplete has "jira merge tickets" and "jira service management merge tickets" | Merge Agent 759, 4.29(7), $260; Ticket Merger (free) 390, 3.75; Duplicate AI 100; Merge Assistant 35; IssueMerge 0 | 4 | 3 | 5 | 2 | 4 | 2 | 3 | **23** | CONDITIONAL (weak) |
| 2 | External/public share of dashboards and timelines | JRACLOUD-68499 (548) + JRACLOUD-87846 (440); Autocomplete has "share jira dashboard externally" and "with customer" | External Share 1,057, 4.71(39), **$687.5**; Laya Board (free) 317; miniOrange 135; Apportunity 69, 2.75 | 5 | 3 | 5 | 2 | 2 | 2 | 2 | **21** | CONDITIONAL (weak) |
| 3 | Confluence incoming links/backlinks macro | CONFCLOUD-35218, 629 votes, 2014; Autocomplete has 7 variants, e.g. "confluence cloud incoming links" | Linking for Confluence 1,218, 3.54(42), $162.5; Apps+ 232, $145; newcomer (2026-09) at 1 inst | 3 | 3 | 5 | 2 | 3 | 2 | 3 | **21** | KILL (pool and ceiling too small; a newcomer is already in) |
| 4 | Read-only fields, SLA and assignee on the JSM portal | JSDCLOUD-4328 (1,724), -328, -325, -4636 | Deviniti 5,301, $610; Extra Fields 193, $125; PortalView (BR) 18; Pitronote 5; Katabarwa 1 | 5 | 1 | 5 | 1 | 4 | 1 | 3 | 20 | KILL (newcomers failing in the same niche) |
| 5 | Jira timeline wedge (milestones, baselines, export, gadget) | 2,425 / 323 / 25 votes | ~70 Gantt apps; Agilis gadget 267; Baseline X 29; Millarum 6 | 4 | 1 | 5 | 2 | 3 | 1 | 3 | 19 | **KILL** (see Q3) |
| 6 | Archive components (Jira) | JRACLOUD-10507, 1,234 | Component Archiver 1 inst (2026-10); Subcomponents 1,169, 3.39 | 2 | 3 | 5 | 2 | 4 | 2 | 3 | 21 | KILL (no proof anyone pays for this alone) |
| 7 | Default values for system fields (Forge UI modifications) | JRACLOUD-4812, 2,798, 2004 | Free Big Fig Tree 2,445; Kalaux 2; Ordixio 1; Katabarwa 1 | 1 | 2 | 5 | 2 | 4 | 2 | 3 | 19 | KILL (free incumbent) |
| 8 | Sprint JQL functions (added/removed, dates) | JRACLOUD-75868 (1,491), -72007 (1,319) | JQL Search Extensions 3,864; JQL Tricks 1,104; GO! JQL 186; Advanced JQL 163; SnapJQL 15 | 4 | 2 | 5 | 2 | 4 | 2 | 3 | 22 | KILL (crowded; newcomers at 15–186) |
| 9 | Customizable or extra notifications (Jira/JSM) | JRACLOUD-7266 (1,597), JSDCLOUD-4642 (1,286) | Email This Issue 5,548, $500; Notification Assistant 1,145, $500 | 5 | 2 | 5 | 2 | 2 | 1 | 2 | 19 | KILL (needs an email service outside Forge; entrenched) |
| 10 | Asana or ClickUp calendar sync / Zendesk view auto-refresh | Asana 810; ClickUp 4,064 (building now); Zendesk 176 | Sync tools (round 1); ClickUp shipping natively | 2 | 2 | 3 | 2 | 4 | 2 | 2 | 17 | KILL (platform absorbing, or no marketplace billing) |

**Deep validation, Top 1: Merge tickets for JSM (CONDITIONAL, weak)**
- **Product:** a Forge app for JSM and Jira. It merges duplicate requests into a primary one: copies comments (internal or public), attachments, request participants and watchers; links and closes the duplicate with a resolution; notifies the customer; and keeps an audit comment. It runs in bulk from the queue and through an Automation action.
- **Buyer and pool:** JSM admins. Leader Merge Agent has 759 installs after about 8 years in the store. The whole niche (installs of the top five) is about 1,300 sites, some on the free tier for 10 users or fewer.
- **Pain evidence:**
  - 1,238 votes and 201 comments, the latest on 2026-06-26 ("the majority of other ticket systems provide this feature as a core functionality").
  - Atlassian declined to build it in 2022, which lowers the risk of the platform absorbing it.
  - Source: [JSDCLOUD-4685](https://jira.atlassian.com/rest/api/2/issue/JSDCLOUD-4685?fields=status,description,comment)
- **Competitors:** Merge Agent at $260/yr for 25 users and $1,040 for 100, actively maintained; free Ticket Merger at 3.75★; small AI-duplicate detectors.
- **Revenue evidence:** none verified. Only paid listings and install counts exist.
- **Weaknesses:**
  - Merge Agent has only 7 reviews.
  - Ticket Merger is rated 3.75★ and was last updated 2025-06.
- **Gates:**
  - G1: PASS, weak. Two or more paid listings (Merge Agent, Duplicate AI, historically Issue Merger Pro), but no verified revenue.
  - G2: **FAIL so far.** Two newcomers in 12 months got 0 and 35 installs.
  - G3: PASS (USD B2B; JSM agents are paid seats).
  - G4: **WEAK.** Autocomplete shows the queries, but marketplace search is install-weighted.
  - G5: PASS (Forge REST APIs; about 2–3 weeks).
  - G6: PASS.
  - G7: PASS pending the Brazil and withholding confirmation (Q4).
  - G8: **FAIL on current evidence.** Even matching Merge Agent's 759 installs at about 50% paid × about $300/yr gives about $9.5k/month. That is the ceiling for the niche leader after years, not a path for a newcomer.
- **Cheapest test (about US$15 plus 4 weeks):**
  1. Register the partner profile and complete KYC first. That also resolves Q4.
  2. Post a "coming soon" landing page and offer founding-customer pricing through the vote thread and the Atlassian Community.
  3. **Pass:** 15 or more opt-ins or demo requests from distinct JSM sites within 30 days, and Atlassian confirms Brazil payout and the income classification in writing.
  4. **Fail:** 5 or fewer opt-ins, which kills it.

**Deep validation, Top 2: External share of Jira dashboards and timelines (CONDITIONAL, weak)**
- **Product:** read-only public or password links to a Jira dashboard view, a filter, or a timeline snapshot, for customers and executives without a license. Expiry, IP and email gating, and a static HTML/PNG snapshot instead of live data.
- **Pool:** External Share has 1,057 installs at **$687.5/yr for 25 users** and $2,750 for 100, the highest price per seat seen in this round (G1 strong). Few rivals, and the free Laya Board grows fast (317 in 3 months).
- **Pain:** 548 + 440 votes since 2018–2019, plus commercial-intent autocomplete ("share jira dashboard externally", "with customer").
- **Gates:**
  - G1: PASS.
  - G2: weak. Rivals are few, but a free newcomer from a portfolio vendor is growing.
  - G3: PASS.
  - G4: weak.
  - G5: **RISK.** Serving pages to anonymous users needs Forge web triggers or an external host, and exposure of customer data invites security scrutiny (bug bounty at partner tiers; round 1).
  - G6: PASS.
  - G7: pending Q4.
  - G8: about 90–100 paying sites at about $600/yr reach $5k/month. That is plausible against 1,057 incumbent installs, but G2 is not proven.
- **Cheapest test:** the same landing-page test as Top 1. Separately, confirm on developer.atlassian.com that Forge web triggers can serve unauthenticated HTML and stay eligible for "Runs on Atlassian"; I did not verify this. **Pass:** 10 or more opt-ins and a feasible Forge path; otherwise KILL.

**Deep validation, Top 3: Confluence incoming links (KILL)**
- 629 votes over 12 years, incumbents at $145–162.5/yr for 25 users, and a newcomer that got 1 install after plugging the ticket in October 2026.
- **G8:** at about $150–300/yr per site, US$5k/month needs about 200–400 paying sites. The two incumbents total about 1,450 installs after 5+ years.
- Buildability is also doubtful: I found no evidence that the Confluence Cloud REST API or CQL exposes incoming links, so the app may have to crawl and index content (unverified).

### Inferences
- **The core lesson of this round:** "thousands of votes for years" is visible to everyone, and in 2026 AI-assisted vendors are mass-producing apps for exactly those tickets with almost no uptake. Votes signal pain, not a reachable buyer for a cold-start vendor. The Atlassian marketplace rewards established portfolios (Agilis, Agile Pulse) and review history.
- If the client still wants an Atlassian play, the only defensible route is:
  1. register and confirm payouts (zero cost, resolves G7);
  2. pre-sell **one** high-price-per-seat utility (external share or merge) before building;
  3. accept 3–5 months to first cash.

  That conflicts with "first revenue within weeks". This front should therefore rank **below** the round-1 alternatives that reach cash sooner.

### Gaps
- Per-app revenue on Atlassian is not public, so G1 is "paid listings exist", never verified revenue.
- Vote data for HubSpot, Google, Microsoft, monday, Figma, Notion, Canva, Trello, Airtable, Calendly, Zoom and Freshdesk was not obtainable with the tools available (see Q5).
- Forge capabilities I did not verify: anonymous web pages through web triggers, and incoming-link APIs.
