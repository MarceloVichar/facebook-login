# Stress Test of Four Global/USD Finalists: Saturation, Demand and Feasibility (verified October 2026)

Unless stated otherwise, every data point was collected on **2026-10-12**. Labels:
- **[V]** verified on a primary page, API or statute.
- **[S]** a vendor's own claim.
- **[3P]** a third-party or secondary source.
- **[SS]** taken from a search-engine summary because the page itself could not be fetched; confirm before relying on it.

Method notes:
- **Search.** WebSearch worked. Bing via curl returned unrelated dictionary results for "send…", DuckDuckGo answered 202, and Brave answered 429, so a literal Google results page could not be captured. Results-page crowding is therefore estimated from which competitors WebSearch returned, competitor content footprints and Google Autocomplete.
- **Traffic proxy.** The Tranco top-1M list (list 4672X, created 2026-10-11, 30-day window combining CrUX, Farsight, Majestic, Radar and Umbrella) — [Tranco](https://tranco-list.eu/).
- **Blocked sources.**
  - EUR-Lex returned a WAF 202 to curl and failed DNS in WebFetch. The German transposition, §356a BGB, was verified on the official federal portal instead.
  - The Wayback Machine CDX API timed out, so founding dates come from the sites themselves, TrustMRR or store launch dates.

---

## Q1. Finalist 1: Online letters and certified mail (US and UK) on print-and-mail APIs. Is it saturated, can a Brazil-based founder use the APIs, what does certified mail cost, and what are the risks?

### Takeaway
Demand and willingness to pay are real and verified. Two tiny newcomers make $4–6k per 30 days, one of them a non-UK (UAE) operator founded in May 2026. But the results page is crowded with 10+ US and 6+ UK retail competitors, and margins are thin: about $2.5–3.5 gross per certified letter.

There are also hard feasibility blockers:
- Lob's and PostGrid's terms prohibit resale or "providing access" to third parties, and PostGrid also bars "competing products". Written permission is needed.
- ClickSend Post is closed to new customers.
- Paddle (the merchant of record available to a Brazilian seller) prohibits "products that require physical delivery".

**Verdict: CONDITIONAL.** Build only after written confirmation from Lob (or another provider) that a consumer storefront is allowed, and with Stripe Brasil as the payment path.

### Cited Findings
**Willingness to pay and demand (revenue numbers verified by TrustMRR via Stripe)**
- PostalForm (US, founded 2024-10-01): $20,404 total and $6,380 in the last 30 days. The founder has 116 X followers — [TrustMRR](https://trustmrr.com/startup/postal-form) (per the prior verified notes in `verified_revenue_niches.md`; not re-fetched today because TrustMRR relays were failing).
- PostalForm's pricing today [V]:
  - "Starting at $3.40", with $3.80 standard and $11.80 Certified Mail for the example order.
  - It runs SEO pages for "Send Certified Mail online", "Compare Certified Mail online options", "Compare online print-and-mail services", dispute letters, landlord notices by state and "Respond to a debt collector".
  - Operated by PostalForm LLC. Orders are non-refundable once printing starts.
  - Sources: [postalform.com](https://postalform.com/); [PostalForm terms](https://postalform.com/terms).
- Send Letters Online (UK, founded 2026-05-14): $21,192 total and $4,315 in the last 30 days, with a domain rating of 5 — [TrustMRR](https://trustmrr.com/startup/send-letters-online-uk) (per prior notes).
- Send Letters Online's site today [V]:
  - "Send Letters Online is operated by Spark Labs FZ-LLC, based in the United Arab Emirates… Founded in May 2026."
  - Prices start "From £2.99 per letter" all-in, plus "A £0.99 processing fee applies to card checkout." Other listed price points are £4.99, £7.45, £7.95 and £15.95; the page does not map them to services.
  - Mail enters Royal Mail "via an authorised Wholesale distributor".
  - It offers Signed For, Tracked 24/48, Special Delivery and international post, an API, "AI Assistants (MCP)" and about 80 long-tail SEO pages (HMRC, DVLA, Section 8 notice and others).
  - It self-reports "4.9 / 5 · Verified reviews" [S].
  - Source: [sendlettersonline.co.uk](https://sendlettersonline.co.uk/).
- Contradicting signal: its Trustpilot page shows 3.2 from a single review, which complains of an 8–10-day delivery [SS] — [Trustpilot](https://fr-be.trustpilot.com/review/sendlettersonline.co.uk).
- Postage.to (letters worldwide, founded 2025-01-14): $2,888 total, $5.99 per letter, listed for sale at $9,500. This shows not every entrant wins — [TrustMRR](https://trustmrr.com/startup/postage-to) (prior notes).

**US competitor census (all accessed 2026-10-12)**

| Competitor | Price evidence | Traffic proxy / notes |
|---|---|---|
| Mailform.io | $2.99 first page; +$8.99 Certified; +$3.02 electronic return receipt; +$5.30 green card; +$17.99 Priority; +$39.99 Priority Express; plans at $50/$200/$1,000 per month [V] — [pricing](https://www.mailform.io/pricing) | Not in Tranco top 1M. Claims "Thousands of happy customers" [S]. No-account checkout — [LP](https://www.mailform.io/lp/Send-Certified-Mail-Online) |
| LetterStream (+ OnlineCertifiedMail.com) | Electronic return receipt +$2.91 [V]; certified letter "as low as $8.34", first-class "$1.23" [SS] — [pricing](https://www.letterstream.com/mailing/pricing) | Tranco #951,756. Its help center sends users with ≤10 letters to OnlineCertifiedMail.com [SS] — [help](https://help.letterstream.com/article/71-how-to-send-certified-mail-online) |
| Certified Mail Labels | Claims savings of "$3.45 on each certified letter" [SS] | **Tranco #433,484**, the largest retail certified-mail site found. Site returned 403 to curl — [site](https://certifiedmaillabels.com/) |
| The Letter Pilot | First-Class from $4.99, Certified from $11.00 [V]; claims "10,000+ letters mailed" [S] | Not in top 1M — [certified page](https://www.theletterpilot.com/services/certified-mail-online); [home](https://theletterpilot.com/) |
| PostalForm | $3.40 / $3.80 / $11.80 [V] | Not in top 1M; TrustMRR-verified revenue (above) |
| Click2Mail (retail and API) | Pricing page returned 403. Third-party listings give "from $0.40" [3P] | Tranco #910,144. Runs a "how to send certified mail online" blog — [blog](https://blog.click2mail.com/2025/10/22/how-to-send-certified-mail-online/) |
| Quadient e-Certify | Claims to save $1.25 per return receipt and "up to 37%" [SS] | — [e-certify](https://www.quadientdirect.com/e-certify) |
| USPS Click-N-Ship (DIY) | You print the Certified Mail label yourself, no post-office visit [3P/SS] | usps.com is Tranco #845 — [USPS FAQ](https://faq.usps.com/articles/Knowledge/Click-N-Ship-The-Basics) |
| Also seen | PostalMethods, Docsmit, SimpleCertifiedMail, US Global Mail, Stamps.com (none in Tranco top 1M) | — [Gitnux roundup](https://gitnux.org/best/certified-mail-software/) [3P, AI-assisted] |

- WebSearch for "send certified mail online" returned only incumbents: LetterStream (several URLs), Click2Mail, Mailform, Certified Mail Labels and The Letter Pilot — [WebSearch results](https://mailform.io/lp/Send-Certified-Mail-Online).
- Tranco ranks for providers and portals: usps.com #845, royalmail.com #5,494, clicksend.com #118,224, lob.com #131,101, postgrid.com #297,889. postalform.com, sendlettersonline.co.uk, mailform.io and theletterpilot.com are all outside the top 1M [V] — [Tranco list 4672X](https://tranco-list.eu/).

**UK competitor census**
- UK Postbox: upload a letter and choose any Royal Mail class, including Signed For and Special Delivery [S] — [UK Postbox](https://www.ukpostbox.com/services/send-letters-online).
- Others found:
  - Modernmail (Trustpilot positive) [SS] — [Trustpilot](https://de.trustpilot.com/review/modernmail.co.uk)
  - PrintPigeon [3P] — [webcatalog](https://webcatalog.io/en/apps/printpigeon-co-uk)
  - Postworks [3P] — [CB Insights](https://www.cbinsights.com/compare/ipostal1-vs-postworks)
  - CFH Docmail (business hybrid mail; "no minimum or maximum spend") [SS] — [Docmail help](https://cfh-docmail-ltd.helpjuice.com/en_US/additional-information/1854876-untitled-article)
  - Stannp (API/B2B, UK letters "From £0.38", PAYG, ex-VAT) [V] — [Stannp letters](https://www.stannp.com/uk/letters)

**Can a Brazil-based individual or company use the APIs? (terms and signup)**
- **Lob: no country ban in its terms beyond US export rules.**
  - The customer warrants it is not on a US prohibited-party list or located in an embargoed country.
  - ACH requires a US-based bank.
  - Under "General Restrictions" the customer must not "rent, lease, copy, transfer, resell, sublicense, lease, time-share, or otherwise provide access to the Lob Service to a third party (except Authorized Users or as permitted under the Service Specific Terms)".
  - The terms do refer to "Customer Applications".
  - Suspension carries a "Suspension Reinstatement Fee" of 10% of annual spend.
  - The customer indemnifies Lob for claims arising from its use.
  - Source [V]: [Lob Terms](https://www.lob.com/legal).
- **Lob payment methods** [V]:
  - credit card "with a 3% service fee";
  - international wire to SVB (SWIFT SVBKUS6S);
  - checks;
  - ACH pull only from a verified US account.
  - Source: [Lob payment methods](https://help.lob.com/account-management/billing/lob-payment-methods.md).
- No public Lob page describes KYC or a business-verification gate for live API keys. The help docs only describe separate test and live keys [SS] — [Lob API keys](https://help.lob.com/account-management/api-keys).
- **PostGrid.** Eligibility is only 18+, legal capacity, and not being barred by law. But:
  - the license is "for your internal business purposes";
  - the customer must not "use the Services to build a competing product" or "share, resell, sublicense, or otherwise provide access to the Services to any third party";
  - PostGrid may suspend accounts that "appear fraudulent, compromised, or high-risk".
  - Source [V]: [PostGrid Terms](https://www.postgrid.com/terms-of-service/).
- **Click2Mail.** International cards are accepted with a valid US billing address. Cards must be from a US bank or an international bank that participates in AVS, and PayPal is available [SS] — [Click2Mail payment options](https://support.click2mail.com/article/334-available-payment-options).
- **ClickSend Post.** "Post has left the building — it's no longer available to new customers." [V] — [ClickSend pricing](https://www.clicksend.com/us/pricing/us/).
- **Stannp.** UK, US and Canada production. No terms page was retrievable (404), and no Signed For / recorded option was found [SS] — [Stannp KB](https://knowledge.stannp.com/eu/how-to-send-a-letter-through-api).
- **Payment collection.**
  - Paddle forbids "Physical products or products that require physical delivery" [V] — [Paddle prohibited list](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle).
  - Stripe Brasil prices in BRL, adds 2% for international cards and charges conversion from 2% [V, prior notes] — [Stripe BR pricing](https://stripe.com/br/pricing).

**What certified mail costs through each API and at USPS**
- **USPS Notice 123** ("Effective October 04, 2026") [V] — [USPS Notice 123](https://pe.usps.com/text/dmm300/Notice123.htm):
  - Certified Mail fee $5.55; Restricted Delivery or Adult Signature $14.35.
  - Return Receipt: hard copy $4.65, electronic $2.91.
  - First-Class 1 oz letter: $0.82 stamped, $0.78 metered.
- **Lob** (public pricing; Developer, Startup and Growth tiers all the same) [V] — [Lob pricing details](https://help.lob.com/print-and-mail/ready-to-get-started/pricing-details.md):
  - Certified Mail (First Class only) $6.950; Electronic Return Receipt $2.910; Certified with ERR $9.860; Registered $24.500.
  - B&W First-Class letter $1.066 on Developer (another table on the same page shows $1.060); additional page $0.10.
  - Subscriptions: Developer $0, Startup $260/mo, Growth $550/mo.
  - Certified is "only available for First Class mail sent domestically within the US" — [Lob certified help](https://help.lob.com/print-and-mail/building-a-mail-strategy/mailing-classes-and-postage/certified-mail-or-registered-mail).
- **PostGrid.** Letters cost $0.75 on Essential ($0/mo), $0.63 on Business ($449 or $499/mo; both figures appear on the page) and $0.59 on Growth ($900 or $999/mo). No public certified surcharge [V] — [PostGrid pricing](https://www.postgrid.com/plans-and-pricing/).
- **Click2Mail.** Certified price not public; the pricing page returned 403.
- **Retail price points for comparison:**
  - Mailform $2.99 + $8.99 = $11.98 certified, plus $3.02 ERR [V];
  - PostalForm $11.80 [V];
  - The Letter Pilot $11.00 [V];
  - LetterStream from about $8.34 [SS].

**USPS rules, fraud, chargebacks and legal-notice liability**
- **Mailform's terms:**
  - prohibit content that is "unlawful, threatening, abusive, harassing, defamatory… deceptive, fraudulent";
  - disclaim liability for content and for third-party carriers.
  - Source [V]: [Mailform Terms](https://www.mailform.io/terms).
- **PostalForm's terms** [V] — [PostalForm Terms](https://postalform.com/terms):
  - "We are not responsible for delays, loss, misdelivery… caused by mail carriers";
  - Express orders "cannot be changed, canceled, or refunded after payment".
- The online route cannot produce the physical green card, only an electronic return receipt [3P] — [Techlasi guide](https://techlasi.com/savvy/how-to-send-certified-mail-step-by-step-guide/).
- Providers advise confirming that proof of mailing meets local legal-notice requirements (WebSearch synthesis of vendor pages) [SS].

### Inferences
- **Unit economics** (my arithmetic from verified prices):
  - **Certified via Lob:** $1.066 + $6.95 = **$8.02**, or $8.26 with Lob's 3% card fee.
  - **Gross margin at PostalForm's $11.80:** about $3.54. After Stripe Brasil (about 4% + 2% international + 2% FX, roughly $0.95), that leaves **about $2.6 per certified letter**.
  - **Standard letter:** $3.40 − about $1.10 − about $0.35 ≈ **$1.9**.
  - **Volume needed:** reaching PostalForm's $6.4k per 30 days means roughly 600–1,800 orders a month at these margins, for roughly $1.5–3k of gross profit. The postage float must be prepaid in USD.
- **Saturation is high but not fatal.** Small SEO-led entrants (PostalForm, Send Letters Online) reached $4–6k/month with no audience. Send Letters Online did it within five months as a UAE entity. That is the strongest "solo newcomer, no contacts" proof among the four finalists.
  - The catch: winners compete on dozens of intent-specific landing pages. PostalForm covers dispute letters, landlord notices and debt-collector responses. Send Letters Online covers HMRC, DVLA, Section 8 and more.
  - A newcomer needs a vertical wedge rather than generic "mail a letter online".
- **The real blocker is contractual, not technical.**
  - Lob's clause bars giving third parties access to the Lob Service. A storefront that submits jobs itself arguably does not give access, but this is ambiguous.
  - PostGrid's "competing product" and "internal business purposes" clauses are stronger red flags.
  - Get written approval from Lob before building.
- **Payments.** A Brazil-based founder cannot use Paddle for this product. Stripe Brasil works but adds about 4% of FX and international fees and makes the founder seller of record. A US LLC (Stripe Atlas or similar) exceeds the $130 budget.
- **Chargebacks and abuse** come from the irreversibility of physical mail plus misuse (harassment, fake legal threats). PostalForm and Mailform both run explicit no-refund-after-print and prohibited-content policies. Expect to need these, plus manual review of flagged content.
- **UK vs US.** The UK version needs a Royal Mail–integrated print partner offering Signed For and Special Delivery; Stannp's support for these was not confirmed. The UAE-operated Send Letters Online shows the UK route is reachable from abroad.

### Gaps
- Lob's actual KYC at signup for a Brazil-addressed account, and whether Lob considers a consumer storefront to violate its resale clause. Needs a support ticket; no public page answers it.
- PostGrid's and Click2Mail's certified per-piece prices; Click2Mail's terms (403 to curl).
- Stannp's Signed For availability and pricing, and its account eligibility for non-UK entities.
- Which provider PostalForm and Send Letters Online actually use.
- Google Ads CPCs for "send certified mail online": no free tool reachable. Real search volumes: Autocomplete gives no counts.
- Chargeback and dispute rates for online mail services: no data found.

---

## Q2. Finalist 2: The EU electronic withdrawal function (Directive (EU) 2023/2673) for sites not on Shopify. Is the requirement real, is the platform gap real, and is there demand?

### Takeaway
The legal requirement is real and in force since 19 June 2026, verified on the German statute (§356a BGB). But the "non-Shopify gap" has closed:
- WooCommerce has **68 withdrawal plugins added in 2026**, mostly free, plus Germanized (70k installs) with the feature built in.
- Shopware ships the function **in core since 6.7.9.0** (April 2026).
- Wix has about 7 apps, all free or freemium, each with 4 reviews or fewer.
- PrestaShop has at least 4 paid modules at €29–60.
- Jimdo has a native button; eRecht24, Händlerbund and widerrufonline.de cover website builders.

Outside Shopify, paid demand looks weak: tiny review counts and free alternatives everywhere. **Verdict: KILL.**

### Cited Findings
**Legal requirement and date**
- **§356a BGB, "Elektronische Widerrufsfunktion bei Fernabsatzverträgen"** [V] — [gesetze-im-internet.de §356a BGB](https://www.gesetze-im-internet.de/bgb/__356a.html). For distance contracts concluded via an online interface, the trader must provide a withdrawal function that is:
  - labelled "Vertrag widerrufen" (or an equivalent unambiguous phrase);
  - "ständig verfügbar, hervorgehoben platziert und… leicht zugänglich" throughout the withdrawal period;
  - able to collect name, contract identification and the electronic channel for the confirmation;
  - followed by a confirmation function labelled "Widerruf bestätigen";
  - followed by an acknowledgement of receipt on a durable medium, sent without delay, with date and time.
- **Date and penalties** [3P] — [Xictron (Sept 2026)](https://www.xictron.com/de/blog/widerrufsbutton-umsetzung-shopware-juni-2026/):
  - Directive (EU) 2023/2673 of 22 Nov 2023 applies "seit 19. Juni 2026" and inserts Art. 11a into Directive 2011/83/EU.
  - Art. 246e EGBGB (BGBl. 2026 I Nr. 28) sets fines up to €50,000, or up to 4% of turnover above €1.25M, "nur im Rahmen einer koordinierten Durchsetzungsmaßnahme".
- Primary EUR-Lex text could not be fetched (WAF/DNS). The date also matches prior notes — [Winston Taylor](https://www.winstontaylor.com/insights/eu-withdrawal-buttons-required-for-consumer-online-contracts-from-june-19-2026-are-you-ready).

**Platform census**
- **WordPress.org / WooCommerce** [V] — [WP API search "withdrawal button"](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=withdrawal%20button&request[per_page]=50):
  - 11 searches (EN/DE/NL/DA/CS/IT/FR/ES terms) returned **68 unique withdrawal-related plugins added in 2026**, with 11,590 active installs combined.
  - "withdrawal button" alone returns 224 results.
  - Top plugins:

    | Plugin | Installs | Ratings | Added |
    |---|---|---|---|
    | EU Order Withdrawal Button for WooCommerce | 6,000 | 7 | 2026-03-26 |
    | WebToffee EU Order Withdrawal Button | 1,000 | 10 | 2026-06-11 |
    | EU Withdrawal and Legal Guarantee Compliance | 1,000 | 17 | 2026-05-15 |
    | EU Withdrawal Button for WooCommerce | 500 | — | — |
    | Withdrawal Button – Easy Return | 400 | — | — |
    | Bitron Right of Withdrawal | 400 | — | — |
    | Widerrufsbutton | 300 | — | 2026-03-31 |

  - Language-specific entrants exist for NL, DK, SK, IT, FR, SE and others.
- **Germanized for WooCommerce** (70,000 installs, 4.8★ from 495 ratings) now ships "Withdrawal Button – Add a withdrawal button (EU directive 2023/2673) to your store" [V] — [WP plugin info](https://wordpress.org/plugins/woocommerce-germanized/).
- **Shopware.** "Seit Version 6.7.9.0 vom April 2026 bringt Shopware ein Widerrufsformular im Kernsystem mit; die Funktion wurde auf Shopware 6.6 zurückgeführt und steht auch in der Community Edition zur Verfügung" [3P] — [Xictron](https://www.xictron.com/de/blog/widerrufsbutton-umsetzung-shopware-juni-2026/).
  - The Shopware Store also lists plugins (fript, codixio) [SS] — [Shopware Store](https://store.shopware.com/en/fript64540696853m/withdrawal-button-legally-compliant-withdrawal-with-flexible-flows.html).
- **Wix App Market** returns "9 Apps" for "withdrawal" [V] — [Wix search](https://www.wix.com/app-market/search-result?query=withdrawal):

  | App | Rating (reviews) | Price |
  |---|---|---|
  | Cooloff EU Withdrawal Button | 5.0 (3) | free |
  | EU Withdrawal Button | 5.0 (4) | free |
  | EU Withdrawal Button "Easy Comply" | 5.0 (2) | free |
  | EU Shop Kit | 0 reviews | free plan |
  | "EU withdrawal button for your online store" | — | "-90%" sale |
  | EU Compliance Kit | 1.0 (1) | — |
  | StoreCompliant: EU Shop Rules | — | — |

  - One listing has a Pro tier at $39/month [SS] — [Wix listing](https://www.wix.com/app-market/armaisdiaz-eu-withdrawal-button-1).
  - No native Wix feature was found [SS].
- **PrestaShop modules** (vendor sites; Addons returned 403) [SS]:
  - Silbersaiten €29 — [Silbersaiten](https://www.silbersaiten.de/en/prestashop-modules/425-eu-withdrawal-button-prestashop-module.html)
  - Linea Gráfica €59.99 — [Linea Gráfica](https://www.lineagrafica.es/en/products/modulo-desistimiento-directiva-ue-2023-2673)
  - IDNovate €55.99/year — [IDNovate](https://www.idnovate.com/en/1464-european-withdrawal-online-cancellation-returns-compliance.html)
  - Alabazweb MEGADESIST — [Alabazweb](https://www.alabazweb.com/en/addons-from-prestashop/600-megadesist-boton-desistimiento-prestashop-directiva-ue-para-prestashop.html)
- **Squarespace and Webflow.** No dedicated app found; their store search URLs returned 404. eRecht24's table lists Squarespace as supported with documentation [SS] — [eRecht24 overview](https://www.e-recht24.de/ecommerce/13472-widerrufsbutton.html).
- **System-independent solutions:**
  - eRecht24's members-only HTML embed — [eRecht24](https://www.e-recht24.de/mitglieder/widerrufsbutton-lp/)
  - Händlerbund's code snippet (Shopify, WooCommerce, Shopware, JTL, WordPress)
  - widerrufonline.de, an externally hosted form for Jimdo, Wix and Squarespace [SS] — [openPR](https://www.openpr.de/news/1309544/Widerrufsbutton-2026-Systemunabhaengige-Loesung-widerrufonline-de.html)
- **Stripe/SaaS.** The Stripe customer portal lets customers cancel subscriptions ("enabled by default") and supports cancellation deep links [SS] — [Stripe docs](https://docs.stripe.com/customer-management/cancellation-page).

**Shopify as proof of payment (saturated)** [V]
- EW: EU Withdrawal Button & Form: **4.9★ from 2,317 ratings**, launched January 9, 2026, with a Free plan, $99.99/year and $299.99/year — [Shopify](https://apps.shopify.com/eu-widerrufsbutton).
- Address Check & Withdrawal Pro: 5.0★ (326), launched May 7, 2026 — [Shopify](https://apps.shopify.com/eu-widerruf-pro).
- EU Widerrufsbutton Pro: 5.0★ (50), launched May 12, 2026, $60/year or $250/year — [Shopify](https://apps.shopify.com/eu-widerrufsbutton-1).
- inventivo: $4.99/month or $49.90/year, launched April 2, 2026 — [Shopify](https://apps.shopify.com/eu-withdrawal-button).
- WiderrufButton: launched July 15, 2026 — [Shopify](https://apps.shopify.com/widerrufbutton).

**Warning letters (Abmahnungen)**
- Händlerbund, 26.08.2026 [V] — [Händlerbund](https://ohn.haendlerbund.de/recht/abmahnungen/erste-abmahnungen-wegen-widerrufsbutton-das-muessen-online-haendler-jetzt-beachten):
  - the Verband Sozialer Wettbewerb warned a sweets shop that had no withdrawal button;
  - the letter also cited health claims and missing base prices;
  - Abmahnkosten were €416.50.
- IT-Recht Kanzlei, 21.08.2026: "Abmahnung ist da: 'Widerrufsbutton' wird beanstandet" (an insufficient button) [V] — [IT-Recht Kanzlei](https://www.it-recht-kanzlei.de/abmahnung-widerrufsbutton-unzureichend.html).
- No count of warning letters or court rulings was found [SS].

### Inferences
- **Where demand was:** about 2,300 reviews on one Shopify app versus at most 17 ratings on any WooCommerce plugin and at most 4 reviews on any Wix app. Willingness to pay concentrated on Shopify, and adoption happened mostly before or around the deadline.
- **What is left outside Shopify:**
  - the deadline has passed;
  - WooCommerce and Shopware merchants have free or core options;
  - website-builder users have legal-text memberships (eRecht24, Händlerbund) that bundle the button.
- **Enforcement is real but mild** (one association letter at €416.50, bundled with other violations). It is enough to keep merchants installing free tools, not enough to make them pay a new vendor.
- The only untested micro-niches are Webflow (small EU B2C share) and services or SaaS sellers outside Stripe's portal. Autocomplete surfaced "widerrufsbutton dienstleistungen", "digitale produkte" and "digistore24". These are too small or too legally risky for a solo non-German-speaking founder: defective implementations draw warning letters, and the vendor carries the reputational risk.

### Gaps
- The verbatim EUR-Lex Art. 11a text and application article (EUR-Lex unreachable); confirmed indirectly via §356a BGB and secondary sources.
- Install counts on the Wix App Market (not shown); Squarespace and Webflow marketplace listings (search 404).
- Any count of warning letters since June 2026; search volumes for "Widerrufsbutton Wix/Webflow/Squarespace" (Autocomplete shows "widerrufsbutton wix" exists, but gives no volume).

---

## Q3. Finalist 3: A Forge-native Gantt/timeline app for Jira (Connect end of support Q4 2026). How saturated is it, does native Jira make it unnecessary, do payouts work for a Brazilian, and is it buildable fast?

### Takeaway
Willingness to pay and buyer purchasing power are excellent: paid Gantt apps charge $450–2,090/year at 100 users. But the space is crowded:
- 69 "gantt" cloud results.
- The biggest vendors (Appfire BigGantt, HeroCoders, DevSamurai GanttTable, Simple Gantt, Swanly) are **already on Forge and updated in 2026**.
- Most apps are **free up to 10 users**.
- Jira's native Timeline (all plans) and Plans (Premium/Enterprise) cover basic needs.

The "Connect apps will die" thesis is weak. Connect apps update server-side, so old Marketplace version dates don't prove abandonment, and Atlassian's Phase 2 lets Connect apps keep updating once they adopt a Forge manifest.

Payouts: a Brazilian individual already lists paid apps, but Atlassian publishes no country list. A competitive Gantt is not a weeks-long build.

**Verdict: CONDITIONAL** (only as a narrow wedge, not a general Gantt clone).

### Cited Findings
**Marketplace census**
- Live API counts for Jira Cloud [V] — [API](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=gantt&limit=50&withVersion=true):
  - "gantt": 69 results
  - "timeline": 237 results
  - "roadmap": 122 results
- Key apps (installs | rating (reviews) | Connect flag | latest Marketplace version date) [V]:

  | App | Vendor | Installs | Rating (reviews) | Connect | Version date |
  |---|---|---|---|---|---|
  | Structure (PPM) | Tempo | 12,712 | 4.55 (408) | Connect | 2023-04 |
  | BigPicture | Appfire | 10,503 | 3.91 (504) | Connect | 2025-07 |
  | Gantt Charts for Structure | Tempo | 6,306 | 4.20 (61) | Connect | 2021-04 |
  | **BigGantt** | Appfire | 5,548 | 3.46 (273) | **Forge** | **2026-08-17** |
  | WBS Gantt-Chart | Ricksoft | 5,293 | 3.48 (160) | Connect | 2019-12 |
  | **Portfolio by HeroCoders** | HeroCoders | 4,993 | 4.45 (77) | **Forge** | **2026-10-03** |
  | Project Mgmt/Resource/Gantt | DevSamurai | 3,062 | 4.34 (175) | Connect | — |
  | **Swanly** | Appfire | 1,418 | 4.06 (61) | **Forge** | **2026-05-04** |
  | **GanttTable** | DevSamurai | 1,300 | 4.69 (16) | **Forge** | **2026-07-28** |
  | Gantt Suite | BrizoIT | 1,075 | 4.42 (15) | Connect | — |
  | Gantt Cloud | WISOFT | 916 | 2.96 (85) | Connect | 2021-11 |
  | Gantt-Chart for Jira | Werkstack | 477 | 3.45 (129) | Connect | 2022-03 |
  | **Simple Gantt & Roadmap Timeline Gadget** | Agilis | 267 | 5.0 (1) | **Forge** | **2026-10-11** |
  | GanttChart Project – Enterprise | Soyatec | 238 | 2.48 (150) | — | — |

- Live annual cloud prices, 10 / 50 / 100 users [V] (from `https://marketplace.atlassian.com/rest/2/addons/{key}/pricing/cloud/live`):

  | App | 10 users | 50 users | 100 users |
  |---|---|---|---|
  | BigGantt | $0 | $1,045 | $2,090 |
  | WBS Gantt | $0 | $660 | $1,320 |
  | Structure Gantt | $100 | $730 | $1,460 |
  | Gantt-Chart for Jira | $60 | $600 | $1,200 |
  | Gantt Cloud | $25 | $225 | $450 |
  | GanttTable | $0 | $750 | $1,500 |
  | Simple Gantt | $0 | $250 | $500 |
  | Gantt Suite | $0 | $800 | $1,600 |
  | HeroCoders Portfolio | $0 | $450 | $900 |
  | Soyatec | $110 | $3,300 | $6,600 |

**Connect end of support** [V] — [Atlassian blog, 17 Mar 2025](https://www.atlassian.com/blog/developer/announcing-connect-end-of-support-timeline-and-next-steps)
- Phase One (no new Connect apps): enforcement 17 Sep 2025.
- Phase Two: Connect descriptor apps can no longer be updated from March 2026, but "apps using Connect modules will still be able to receive updates, as long as they have adopted the Forge manifest".
- Phase Three: "Connect enters end of support", enforcement Q4 CY2026.

**Jira native features**
- Jira Plans (formerly Advanced Roadmaps) is "available in Jira Premium and Jira Enterprise" [SS] — [Atlassian guide](https://www.atlassian.com/software/jira/guides/advanced-roadmaps/overview).
- Cross-project planning is only possible in a plan [SS] — [Atlassian docs](https://confluence.atlassian.com/jirasoftwarecloud/manage-epics-on-the-roadmap-976172306.html).
- ClickUp, a competitor, claims the Standard timeline shows epics with finish-to-start dependencies only, and that no Jira plan offers critical path or baselines [SS, vendor claim] — [ClickUp](https://clickup.com/learn/topic/project-management/tools/jira/gantt-charts/).

**Economics and payouts** [V] — [Atlassian pricing, payment and billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)
- From 1 Jan 2026, partners get "100% of gross revenue earned on Forge, up to $1 million in lifetime Forge revenue".
- After that, Forge revenue share is 84%, falling to 83% from 1 Oct 2026; Connect is 80%, falling to 75%.
- "We owe you remittance for your sales after you reach $500 USD in profit. We pay you within 30 days [to] 60 days after."
- You cannot change an app from **Free → Paid via Atlassian**, so an app must launch as paid from day one.
- **Individuals can apparently be partners** [3P, forum] — [Atlassian developer community](https://community.developer.atlassian.com/t/can-an-individual-sole-proprietor-based-in-turkey-publish-and-sell-paid-marketplace-apps/102081):
  - partner due diligence asks for a "registration and/or tax ID number";
  - a UK sole trader reportedly got private confirmation (ticket ECOHELP-151223) that the individual path works;
  - a Turkey-specific question was still open in Aug 2026.
- **Brazilian precedent** [V]:
  - Individual developer Victor Torres (Belo Horizonte, MG) lists 3 "Paid via Atlassian" apps (Special Messages, Tree View, Attachment Text Editor) with 0–1 installs each, released May–Aug 2026 — [vendor page](https://marketplace.atlassian.com/vendors/683198338/victor-torres); [API](https://marketplace.atlassian.com/rest/2/addons/vendor/683198338).
  - Fator Tec LTDA (São Paulo) lists one paid app with 2 installs — [vendor](https://marketplace.atlassian.com/vendors/895814828/fator-tec-ltda).

**Security obligations** [SS] — [Atlassian Marketplace bug bounty](https://developer.atlassian.com/platform/marketplace/marketplace-security-bug-bounty-program/)
- Bug bounty participation is required at Marketplace Partner Program tiers:
  - Silver: the most-installed paid cloud app;
  - Gold: paid cloud apps with 100+ installs;
  - Platinum: all paid cloud apps.
- It is also a prerequisite for Cloud Fortified.
- Programs were expected to be public by 30 June 2026.
- Partners fund the rewards (implied).

### Inferences
- **The forced-switch window is overstated.** The largest Gantt apps (BigGantt, HeroCoders Portfolio, GanttTable, Swanly) are already on Forge. Connect-flagged incumbents (Structure Gantt, WBS) can keep shipping by adding a Forge manifest. Customers of Connect apps are not forced to change vendor.
- **Cold start is the binding constraint.** Marketplace search ranks by installs and reviews. New Forge apps, including the Brazilian developer's, sit at 0–7 installs months after launch. The norm of free for 10 users or fewer also delays revenue until a customer has more than 10 users.
- **Buildability.** An MVP (read-only Gantt from issue dates plus issue-link dependencies) is feasible in weeks. Parity with BigGantt or WBS is not: drag-reschedule, baselines, critical path, large-instance performance within Forge limits, and enterprise permissions take months.
- **Payout path looks feasible** (a BR individual lists paid apps), but it is unconfirmed until the partner team approves BR tax data. Remittance only starts after $500 profit, plus 30–60 days.
- A viable wedge would be something the big Gantt suites and native Timeline don't do well and that sells under $1/user/month: for example, a lightweight Gantt dashboard gadget, Gantt export to PDF or PowerPoint, or a baseline/variance tracker on top of native Timeline. This is an inference; demand for these wedges was not validated.

### Gaps
- Atlassian's official supported payout countries and method (wire or ACH) for Brazil; whether a CPF is accepted as the tax ID.
- Exact Phase 3 date in Q4 2026, and what happens to un-migrated Connect apps.
- Marketplace revenue for any Gantt app (not public); the Forge Custom UI and storage limits that would affect large-instance Gantt performance (not checked).

---

## Q4. Finalist 4: A Google Sheets ⇄ Google Calendar sync add-on. How saturated is it, do the scopes trigger CASA, and do users pay?

### Takeaway
It is saturated. At least 15 Sheets→Calendar add-ons exist, and the premise that incumbents are poorly rated is only half true:
- Sheets2GCal is 3.2★ (8M+, 133 reviews) and Calendar Events Creator is 2.5★ (3M+, 457 reviews).
- But **4.1–4.8★ alternatives** (Sheet to Calendar Evento 176K+, Sheet2Cal 25K+, Sheet.Cal 25K+) exist, and a wave of 2026 entrants sits at 1–174 installs.
- Free Apps Script recipes appear in Autocomplete ("google sheets to google calendar script").

Scopes: Calendar scopes are not on Google's restricted list (only Gmail and Drive are), so no CASA assessment is needed, only sensitive-scope verification (demo video, roughly 2–8 weeks). Willingness to pay is thin: Sheets2GCal charges €5/month or €48–299/year, and no verified revenue was found.

**Verdict: KILL.**

### Cited Findings
**Workspace Marketplace census** (installs and ratings from search results; review counts and update dates from listings) [V]

| Add-on | Rating | Installs | Reviews | Updated | Pricing / link |
|---|---|---|---|---|---|
| Sheets2GCal (GCalTools) | 3.2 | 8M+ | 133 | Aug 10, 2026 | "Free of charge with paid features" — [listing](https://workspace.google.com/marketplace/app/sheets2gcal/137564231775) |
| Calendar Event Automator (formapprovals.com, form-based) | 3.6 | 4M+ | 59 | Aug 17, 2026 | — [listing](https://workspace.google.com/marketplace/app/calendar_event_automator/688032838695) |
| Calendar Events Creator (New Addons) | 2.5 | 3M+ | 457 | May 28, 2026 | — [listing](https://workspace.google.com/marketplace/app/calendar_events_creator/101859618418) |
| Event-o-Matic (Amplified Labs) | 3.5 | 672K+ | 103 | Feb 1, 2026 | — [listing](https://workspace.google.com/marketplace/app/eventomatic/713368976382) |
| Add events with Meet link (Fast123.ca) | 3.1 | 522K+ | — | — | — |
| Sheet to Calendar Evento (Shihan Khan) | 4.1 | 176K+ | 126 | Jun 16, 2026 | Free trial — [listing](https://workspace.google.com/marketplace/app/sheet_to_calendar_evento/181338836227) |
| Sync Sheets to Calendar (EventTrakr) | 1.9 | 56K+ | — | — | — |
| Sheet.Cal 2-Way | 4.5 | 25K+ | 34 | Dec 27, 2025 | — [listing](https://workspace.google.com/marketplace/app/sheetcal_2way_sheets_to_calendar_sync/651641326432) |
| Sheet2Cal (mhova.dev) | 4.8 | 25K+ | 16 | Aug 31, 2026 | Freemium — [listing](https://workspace.google.com/marketplace/app/sheet2cal/104675878787) |
| Calendar Booker | 3.0 | 819 | 2 | Apr 23, 2026 | — |
| Sheets2GCal Sync | — | 419 | — | — | — |
| Calendar Sync for Sheets (Marinette) | 5.0 | 174 | — | — | — |
| Calrows | 5.0 | 25 | — | — | — |
| Heculeads 2-Way Sync | — | 7 | — | — | — |
| CalWeave | — | 2 | — | — | — |
| CalBatch | — | 1 | — | — | — |

- Search source: [Marketplace search "sheets to calendar"](https://workspace.google.com/marketplace/search/sheets%20to%20calendar).
- Reverse direction (Calendar→Sheets) [V]:
  - Calendar to Sheet (Jose Luis Guillén): 3.9★, 811K+
  - Export Calendar Events to Spreadsheet: 2.9★, 143K+
  - Calendar Importer: 3.9★, 92K+
  - Calendar to Sheets: 3.9★, 41K+

**Pricing and willingness to pay**
- Sheets2GCal [V] — [sheets2gcal.com](https://www.sheets2gcal.com/):
  - "S2GCal Monthly Personal €5.00 per Month";
  - €48.00 per year;
  - €59.00 per year;
  - €299.00 per year for "your entire GSuite domain".
- Its listing says users without a free licence are limited to 2,000 imports and 50 updates or deletes per day; a paid licence removes all limits [V] — [listing](https://workspace.google.com/marketplace/app/sheets2gcal/137564231775).
- No Marketplace billing was observed; Sheets2GCal sells licences on its own site (also stated in the prior `marketplace_gaps.md` notes) — [sheets2gcal.com](https://www.sheets2gcal.com/).

**OAuth scopes and CASA**
- Google's restricted-scope list covers only Gmail API scopes (readonly, metadata, modify, insert, compose, settings.*) and Drive scopes (drive, drive.readonly, drive.activity*, drive.metadata*, drive.scripts, drive.meet.readonly). **No Calendar or Sheets scope is listed** [V] — [Google Cloud Help: Restricted scopes](https://support.google.com/cloud/answer/13464325?hl=en).
- The security assessment is for "applications requesting access to restricted scopes" [V] — [Google Cloud Help: Security Assessment](https://support.google.com/cloud/answer/13465431?hl=en):
  - it is annual;
  - it uses the App Defense Alliance CASA framework, AL1 or AL2;
  - it ends with a "Letter of Validation".
- Sheets scopes [V] — [Sheets API scopes](https://developers.google.com/workspace/sheets/api/scopes):
  - `spreadsheets` and `spreadsheets.readonly` are Sensitive;
  - `drive.file` is "Recommended Non-sensitive";
  - `drive` and `drive.readonly` are Restricted.
- The Calendar auth page lists 20 scopes, including `calendar.events`, `calendar.events.owned` and `calendar.app.created`, but the fetched text has no classification column [V] — [Calendar API auth](https://developers.google.com/workspace/calendar/api/auth).
- A Nylas guide classifies `calendar.events` as sensitive: verification required, no security assessment [SS] — [Nylas](https://developer.nylas.com/docs/provider-guides/google/google-verification-security-assessment-guide.md).
- Sensitive-scope verification requires an unlisted YouTube demo video of the consent flow and each scope's use [SS] — [Google sensitive scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification?hl=pt).
- Timing: vendor guides estimate 2–8 weeks [SS] — [Unipile](https://developer.unipile.com/docs/google-oauth).
- One developer's verification had been pending since 22 Apr 2026 with no Trust & Safety email [3P] — [Google Developer forum](https://discuss.google.dev/t/oauth-verification-pending-since-22-apr-2026-first-trust-safety-email-never-received/392005).
- Apps Script editor add-ons can use the `currentonly` scope ("only available within Apps Script") [V] — [Workspace add-on scopes](https://developers.google.com/workspace/add-ons/concepts/workspace-scopes).

### Inferences
- **Better ratings don't win share.** Sheet2Cal (4.8★) and Sheet.Cal (4.5★) are stuck at 25K+ installs while 2.5–3.2★ incumbents hold 3–8M. Marketplace ranking and inertia favour installs, so "a better-rated clone" is not a winning plan.
  - The 2026 entrants (Calrows, CalWeave, CalBatch, Heculeads, Marinette) at 1–174 installs show the crowd is still growing.
- **Payment.** A €5/month price point, a teacher- and school-heavy audience, and free DIY Apps Script mean low purchasing power. No verified revenue exists for any Sheets⇄Calendar add-on.
- **Scopes.** A Sheets plus Calendar add-on avoids CASA. With `spreadsheets.currentonly` plus a Calendar events scope, expect sensitive-scope verification only. That removes a cost risk but not the saturation problem.

### Gaps
- Google's own sensitivity label for each Calendar scope (not in the fetched page text); whether `calendar.app.created` is non-sensitive.
- CASA cost in USD (not on Google's pages; irrelevant if restricted scopes are avoided).
- Revenue figures for Sheets2GCal, Sheet2Cal and Sheet.Cal (Sheet.Cal's and Sheet2Cal's pricing pages did not return content).

---

## Q5. Demand signals across all four (Google Autocomplete and free proxies)

### Takeaway
Autocomplete confirms live search demand for all four, but much of it is for the **free or cheapest** option. Mail and Sheets→Calendar queries carry "free", "cheap", "reddit" and "script" modifiers. Withdrawal-button queries are dominated by Shopify, WooCommerce, PrestaShop and marketplace (Etsy/eBay) variants. Jira Gantt queries include "free" and native "timeline vs plan".

### Cited Findings
All from the Google Suggest API, accessed 2026-10-12 [V] — [Google Suggest](https://suggestqueries.google.com/complete/search?client=firefox&hl=en&q=send+certified+mail+online).
- **"send certified mail online"** → free, usps, cheap, reddit, free usps, cost, cheapest, with return receipt, same day.
- **"mail a letter online"** → free, reddit, usps, free usps; "send a letter online" → free, to an address, royal mail, uk, australia, usa, anonymously.
- **UK:** "send letter online uk" → print and send letter online uk, write and send a letter online uk. "send recorded delivery letter online" → can i send a letter recorded delivery online.
- **"online letter mailing service"** → online letter sending service uk, best online letter mailing service reddit.
- **German, "widerrufsbutton"** → 2026, pflicht, shopify, etsy, beispiel, ebay, österreich, bgb, gesetz, onlineshop.
  - "widerrufsbutton w…" → woocommerce, wix, wordpress, wko, website, woocommerce germanized.
  - "widerrufsbutton s…" → shopify, shopware, shopware 6, schweiz, shopware 5, strafe, strato.
  - "widerrufsbutton p…" → pflicht für wen, b2b, prestashop, pflicht makler.
  - "widerrufsbutton d…" → digitale produkte, digistore24, dienstleistungen, discogs.
- **Dutch, "herroepingsknop"** → webshop, shopify, woocommerce, website, verplicht, bol.com, acm. **French, "bouton de rétractation"** → shopify, obligatoire, prestashop, woocommerce. **Spanish, "botón de desistimiento"** → shopify, ecommerce.
- **"jira gantt chart"** → plugin, view, free, tutorial, template, with dependencies. "gantt chart for jira" → free, gantt table, wbs gantt chart ricksoft, biggantt, best. "jira timeline" → vs roadmap, vs plan, show subtasks, show dependencies.
- **"google sheets to google calendar"** → script, integration, template, apps script, automation, sync. "sheets to calendar" → add on, sync, events, template, script.
- **Tranco traffic proxy:** only usps.com, royalmail.com, clicksend.com, lob.com, postgrid.com, certifiedmaillabels.com (#433,484), click2mail.com and letterstream.com are in the top 1M; every small retail mail site sits below it [V] — [Tranco](https://tranco-list.eu/).

### Inferences
- **Mail:** demand is broad but price-sensitive. "Reddit" and "cheapest" modifiers favour whoever is cheapest or most trusted. Vertical intent pages (disputes, landlords, HMRC/DVLA) are how small players rank.
- **Withdrawal button:** German demand clusters on platforms that are already served (Shopify, WooCommerce, Shopware, PrestaShop) or where a third party can't help (Etsy, eBay, Discogs).
- **Jira and Sheets:** "free" and "script" modifiers point to strong free substitutes.

### Gaps
- No absolute search volumes. Keyword Planner, Ahrefs and Similarweb were unavailable, and the Ahrefs/Similarweb MCP servers failed to connect. No literal Google results page, and no ad-density count.

---

## Q6. Scores (1–5) and ranked verdicts

### Takeaway
Ranking:
1. **Online letters / certified mail: CONDITIONAL.** Best newcomer evidence, but there are contractual and payment blockers to clear first.
2. **Forge Gantt for Jira: CONDITIONAL.** Only as a narrow wedge; general Gantt is crowded by Forge-native incumbents.
3. **Sheets ⇄ Calendar: KILL.** Saturated, low willingness to pay.
4. **EU withdrawal function outside Shopify: KILL.** The gap is closed and the deadline has passed.

### Cited Findings
- The scores rest on the evidence cited in Q1–Q5:
  - TrustMRR revenues — [PostalForm](https://trustmrr.com/startup/postal-form); [Send Letters Online](https://trustmrr.com/startup/send-letters-online-uk)
  - Lob terms and prices — [Lob Terms](https://www.lob.com/legal); [Lob pricing details](https://help.lob.com/print-and-mail/ready-to-get-started/pricing-details.md)
  - Paddle exclusion — [Paddle](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle)
  - WordPress and Wix census — [WP API](https://api.wordpress.org/plugins/info/1.2/?action=query_plugins&request[search]=withdrawal%20button&request[per_page]=50); [Wix](https://www.wix.com/app-market/search-result?query=withdrawal)
  - Shopware core — [Xictron](https://www.xictron.com/de/blog/widerrufsbutton-umsetzung-shopware-juni-2026/)
  - Atlassian API, pricing and billing — [API](https://marketplace.atlassian.com/rest/2/addons?hosting=cloud&application=jira&text=gantt&limit=50&withVersion=true); [billing](https://developer.atlassian.com/platform/marketplace/pricing-payment-and-billing/)
  - Workspace listings and restricted scopes — [Workspace search](https://workspace.google.com/marketplace/search/sheets%20to%20calendar); [Restricted scopes](https://support.google.com/cloud/answer/13464325?hl=en)

### Inferences
**Scorecard** (5 = best; "Low saturation" and "Low risk" are scored so that higher is better):

| Finalist | WTP evidence | Low saturation | Buyer power | Distribution w/o contacts | Buildability | Speed to 1st revenue | Low risk | **Total /35** | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| 1. Online letters & certified mail (US/UK) | 4 (verified $4–6k/30d for 2 tiny newcomers) | 2 (10+ US, 6+ UK retail players, SEO-heavy) | 3 (consumers and landlords, $3–12/order) | 3 (SEO/ads; price-sensitive queries) | 4 (Lob API documented; certified via `extra_services`) | 3 (pay-per-order; but SEO ramp) | 2 (resale clauses, no Paddle, prepaid postage, legal-notice and abuse liability, thin margin) | **21** | **CONDITIONAL** |
| 3. Forge Gantt for Jira | 5 ($450–2,090/yr per 100 users) | 2 (69 results; top vendors already Forge; native Timeline/Plans) | 5 (USD B2B, per-seat) | 3 (marketplace search, but install-weighted cold start) | 2 (MVP in weeks; parity in months) | 2 (free ≤10 users; $500 remittance threshold + 30–60 days) | 3 (platform risk; Free→Paid lock; BR payout unconfirmed) | **22** | **CONDITIONAL** (narrow wedge only) |
| 4. Sheets ⇄ Calendar | 2 (€5/mo; no verified revenue) | 1 (15+ add-ons incl. 4.5–4.8★; 2026 entrants stuck) | 2 (teachers, SMB) | 3 (marketplace search) | 4 (Apps Script; no CASA) | 2 (verification 2–8 weeks; low freemium conversion) | 3 (Google policy/verification stalls) | **17** | **KILL** |
| 2. EU withdrawal fn outside Shopify | 2 (Wix ≤4 reviews, WooCommerce mostly free) | 1 (68 WP plugins, Germanized, Shopware core, 7 Wix apps, PrestaShop modules, eRecht24/Händlerbund/widerrufonline) | 3 (EU SMB) | 2 (deadline passed; legal-text memberships bundle it) | 5 (two-step form, days) | 2 (rush over) | 2 (warning-letter exposure for defects; German-language legal nuance) | **17** | **KILL** |

1, 3 and 2 are the finalist numbers from the brief.

The ranking deliberately overrides the raw totals in two places:
- **Mail (21) ranks above Gantt (22).** Mail is the only finalist with verified evidence that a no-audience newcomer reached $4–6k/30d: Send Letters Online did it within five months of launch as a non-UK entity, and PostalForm's founder has 116 followers. The Gantt score is driven by price per seat, while the only observed newcomers (including a Brazilian developer) have 0–7 installs. Both of mail's blockers can also be resolved with one support ticket each.
- **Sheets ⇄ Calendar ranks above the withdrawal function (17 each).** Sheets demand at least persists, while withdrawal demand peaked at a deadline that has passed.

**Ranked verdicts with conditions**
1. **Online letters / certified mail: CONDITIONAL GO.** Go only if all three hold:
   - Lob (or another API) confirms in writing that a consumer-facing storefront is allowed under its "resell / provide access" clause;
   - a Stripe Brasil account accepts USD/international card checkout for physical mail fulfilment;
   - the product launches with a vertical wedge (e.g., a specific notice type or state-specific landlord or HOA notices) rather than generic "mail a letter".
   - Kill if any of these fail. On ~$2.6 per certified letter, $5k/month gross profit needs about 1,900 certified orders a month.
2. **Forge Gantt for Jira: CONDITIONAL.** Do not build a general Gantt. Proceed only with a narrow, sub-$1/user wedge that native Timeline and the big suites don't cover, after Atlassian's partner team confirms BR individual onboarding and payouts. Launch as Paid via Atlassian from day one, because Free→Paid is impossible.
3. **Sheets ⇄ Calendar: KILL.** Saturated with well-rated alternatives and free scripts; low willingness to pay.
4. **EU withdrawal function outside Shopify: KILL.** The platform gap is closed (WooCommerce, Shopware core, Wix, PrestaShop, Jimdo, membership embeds), the deadline has passed, and non-Shopify willingness to pay is near zero.

### Gaps
- None of the conditions for finalists 1 and 3 can be verified from public pages. Each needs a direct support or partner ticket (Lob resale permission and KYC; Atlassian BR payouts).
- Ad costs (CPC) and absolute search volumes remain unmeasured for all four.
