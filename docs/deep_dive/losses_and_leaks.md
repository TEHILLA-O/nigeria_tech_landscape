# The biggest holes in the wallet: losses and leaks

Last verified: **2026-10-19**. Every loss below has a source. Where we turn naira into dollars or add numbers together, the row says **our calc** or **estimate** and shows the arithmetic. Some sizes are not comparable (a fine imposed is not the same as cash lost), and we say so.

Conversion rates: ₦1,535/$ for 2024 figures (year-end rate quoted in [S001]); about ₦1,520/$ for 2025 and ₦1,385/$ for 2026 (World Bank series averages in [S163]).

## The ranking first

| Rank | Hole | Size (dated) | USD (our calc unless stated) | Type | Confidence |
|---|---|---|---|---|---|
| 1 | FX devaluation on dollar costs and dollar debt | MTN Nigeria net FX loss ₦925.4bn in 2024 ([S074]); ten listed companies ₦2.17tn of FX losses in 2024 ([S075]) | About $603m (MTN); about $1.41bn (ten firms) | Accounting loss, real cash impact | High (audited) |
| 2 | Credit losses in lending | Banks: NPL ratio 5.76% in June 2025, above the 5% benchmark ([S156]); Vanguard's tally of 11 banks: ₦21.2tn NPLs at Q3 2025 ([S156]). Fintechs: OPay credit loss expense $118.4m and write-offs $113.2m in H1 2026 ([S037]); FairMoney impairments ₦59.4bn in 2024 ([S055]) | OPay $118.4m in six months (stated); FairMoney about $39m | Realised and expected credit losses | High for OPay and banks; medium for FairMoney (unaudited) |
| 3 | Power and diesel | Manufacturers spent ₦1.11tn on alternative energy in 2024, up 42.3% ([S158]) | About $723m | Operating cost | High for manufacturers; **tech sector figure not available**, used as a proxy for the cost of running anything in Nigeria |
| 4 | Capital burned in failed startups | Sourced amounts raised by eight failures: Dash (more than $80m) ([S143]), 54gene ($45m) ([S144]), Okra ($16.5m) ([S145]), Lidya ($16.45m) ([S147]), Medsaf (over $7m) ([S155]), Edukoya ($3.5m) ([S148]), Pivo ($2.6m) ([S150]), Thepeer ($2.3m) ([S149]) | At least $173m raised (our calc, lower bound); some was returned, e.g. Okra about $5.5m ([S145]) | Investor capital lost or returned | Medium (amounts raised, not audited losses) |
| 5 | Regulatory fines | Meta $220m (upheld April 2025; payment not confirmed by September 2025) ([S105], [S106]); CBN ₦15bn on 29 banks for AML breaches ([S129]); ₦1.35bn on 9 banks for ATM cash failures ([S130]); reported ₦1bn each on Moniepoint and OPay, denied by OPay ([S128]); NDPC ₦555.8m on Fidelity ([S107]) and ₦766.2m on Multichoice ([S108]) | Meta $220m (stated); the naira fines listed sum to about ₦19.7bn, roughly $13m (our calc, including the disputed fintech fines) | Fines imposed (not all paid) | High for imposition; low for payment |
| 6 | Telco USSD debt | Banks owed telcos about ₦250bn by the telcos' count ([S029]); revised to about ₦180bn, of which 95% (about ₦171bn) was paid by June 2025 ([S030]) | About $118m on the revised figure at the 2025 rate | Disputed receivable, mostly settled | Medium |
| 7 | Payment fraud | ₦52.26bn lost in 2024, of which one incident at one entity was ₦31.1bn ([S132], [S133]); ₦25.85bn in 2025 ([S133]) | About $34m (2024) and $17m (2025) | Cash lost | High (NIBSS) |
| 8 | Operational and chargeback losses at processors | Interswitch: ₦11.45bn chargeback fraud operating loss in its loss-making year ([S041]), from about ₦30bn of suspected fraudulent chargebacks first reported in 2023 ([S042]); Flutterwave: ₦21.2bn exposure from the October 2023 POS glitch, with ₦7.2bn preserved ([S138], [S139]), plus ₦2.95bn moved in a February 2023 incident ([S137]) | Not converted: the naira amounts span FX regimes and recoveries are incomplete | Operating loss and exposure | Medium |
| 9 | Mobility collapse | Moove handed about ₦35bn of vehicles to drivers on exit, after Uber left in September 2026 ([S064], [S065]) | About $25m at the 2026 rate | Asset write-down (estimate: the transfer value is what Moove says, not an audited loss) | Medium |
| 10 | POS hardware treadmill | 5.90m deployed terminals (March 2025) ([S005]); device prices ₦21,500 to ₦85,000 ([S006]) | **Estimate**: replacing the deployed fleet would cost ₦127bn to ₦502bn (our calc: 5.90m × ₦21,500 and × ₦85,000), about $83m to $330m | Capital expenditure, not a loss | Low (estimate) |

Below the top ten, we cover cybersecurity breaches, CAC and churn, cash-out fees, taxes and levies, downtime, talent flight and the funding drought. The CSV is in [`data/losses.csv`](../../data/losses.csv).

**How to read the ranking.** It is by naira or dollar size where sources allow. It is not a measure of how much each hole hurts the average fintech. For a small startup, a ₦10 million NDPA fine or a weeks-long onboarding freeze can be fatal while barely registering in the totals.

## 1. FX devaluation: the hole under everything

The naira went from around ₦500/$ in early 2023 to around ₦1,500/$ in 2025 ([S006]) after the June 2023 unification ([S162]). Three groups got hit:

* **Firms with dollar debt or dollar payables.** MTN Nigeria posted a ₦400.4bn loss after tax in 2024 on ₦3.36tn of revenue, driven by a ₦925.4bn net FX loss ([S074]). Adjusted for FX, it would have earned ₦247.3bn ([S074]).
* **Firms that report in dollars but earn naira.** Jumia's 2024 revenue fell 10% to $167.5m in dollars even though it grew 17% in constant currency ([S063]).
* **Firms whose inputs are imported.** POS terminals rose 30% to 100% in price ([S006]). PAYG solar sales roughly halved in H1 2024 ([S069]).

Interswitch's loss-making year was driven by naira devaluation on FX liabilities and by chargeback fraud ([S041]); it returned to profit the following year ([S040]).

**Plugs.** Naira-denominated debt matched to naira revenue (Sun King's $80m naira facility ([S068]) and d.light's ₦10bn securitisation ([S070])); dollar revenue lines (Flutterwave's enterprise and cross-border business ([S044])); and FX-aware pricing and treasury tooling for SMEs.

## 2. Credit losses: the price of the lending pivot

Lending is now the biggest profit line for the wallets ([S037]), which means defaults are now the biggest risk.

* **OPay.** Credit loss expense rose 210.3% to $118.4m in H1 2026, 25.3% of revenue. Write-offs were $113.2m in six months versus $70.0m in all of 2025. $113.8m, or 27.4% of loans and interest owed, was overdue at 30 June 2026 ([S037]). OPay says it tightened consumer lending and shifted toward merchant loans ([S037]).
* **FairMoney.** ₦59.4bn of loan impairments against ₦121.9bn revenue in 2024 ([S055]).
* **Microfinance banks.** Portfolio at risk was 12.25% in June 2024, far above the 5% threshold ([S157]).
* **Banks.** NPL ratio 5.76% in June 2025, up from 4.87% in December 2024, with net NPLs to capital rising to 13.90% from 4.91% ([S156]).
* **Standalone lenders fail first.** Lidya shut in October 2025 ([S146]).

**Plugs.** Cash-flow underwriting using merchant transaction data, collections tooling that complies with the FCCPC's 2025 conduct rules ([S111]), better use of GSI recovery ([S023]) and bureau reporting to at least two bureaus ([S022]).

## 3. Power and diesel

Manufacturers spent ₦1.11tn on alternative energy in 2024, up 42.3% from ₦781.68bn in 2023 ([S158]). We found no comparable figure for tech companies, data centres or agents. We include it because every agent, office and server room in Nigeria pays some version of this cost, and blank is better than a made-up tech-sector number.

**Plugs.** PAYG solar for agents and SMEs, financed in naira ([S068]); power-aware POS and kiosk hardware.

## 4. Startups that failed, and why

| Company | Sector | Raised (sourced) | Closed | Why it failed | Source |
|---|---|---|---|---|---|
| Dash | Payments | More than $80m | Oct 2023 | Audits found inflated user and transaction numbers and unaccounted funds | [S143] |
| 54gene | Genomics | $45m | 2023 | Could no longer operate financially; costly operations, leadership churn | [S144] |
| Bundle Africa | Crypto exchange | Not cited | Jul 2023 | Shut exchange, pivoted to P2P payments | [S154] |
| Thepeer | Payments infrastructure | $2.3m | Apr 2024 | Compliance struggles, could not scale | [S149], [S176] |
| Pivo | SME fintech | $2.6m | 2024 | Co-founder disagreements | [S150] |
| Medsaf | Health supply chain | Over $7m | 2024 | Funding, FX and debt collection problems | [S155] |
| Gokada | Mobility | Not totalled here | Oct 2024 | Chapter 11 filing in Delaware | [S153] |
| Kobo360 | Logistics | Not totalled here | Nov 2024 (restructured) | Cut at least 30 of 50 Nigerian staff, paused most operations | [S067] |
| Bento Africa | Payroll and HR | Not cited | Feb 2025 (temporary) | Allegations of unremitted PAYE and pension deductions, unpaid salaries; CEO resigned | [S151], [S152] |
| Edukoya | Edtech | $3.5m | Feb 2025 | Connectivity, device access, low disposable income | [S148] |
| Okra | Open banking API | $16.5m | May 2025 | Dollar-priced infrastructure, failed cloud pivot, returned about $5.5m | [S145], [S174] |
| Lidya | SME lending | $16.45m | Oct 2025 | Severe financial distress after failed restructuring | [S146], [S147] |
| Moove (Nigeria) | Mobility finance | Group-level funding; see ranked sheet | Oct 2026 | Uber's exit removed its main platform | [S064], [S065] |

The pattern is consistent: **governance failures** (Dash, Bento, Pivo), **dollar costs against naira revenue** (Okra, Medsaf), **dependency on one partner or rule** (Moove on Uber, Thepeer on compliance) and **market readiness** (Edukoya). Very few of these died because a competitor built a better product.

## 5. Fines and enforcement

| Date | Who | Fine | Regulator | Status | Source |
|---|---|---|---|---|---|
| 2024 | 29 banks | ₦15bn total | CBN | AML/CFT breaches | [S129] |
| 2024 | Moniepoint, OPay | ₦1bn each (reported) | CBN | OPay denied | [S128] |
| Aug 2024 | Fidelity Bank | ₦555.8m | NDPC | Disputed by the bank | [S107] |
| Jan 2025 | 9 banks | ₦1.35bn total | CBN | ATM cash availability | [S130] |
| Apr 2025 | Meta/WhatsApp | $220m plus $35,000 costs | FCCPC (upheld by tribunal) | Payment not confirmed by Sep 2025 | [S104], [S105], [S106] |
| Jul 2025 | Multichoice Nigeria | ₦766.2m | NDPC | Imposed | [S108] |
| Feb 2025 onward | Binance | $81.5bn claim (not a fine) | FIRS, in court | No final judgment reported by Oct 2025 | [S102], [S103] |

**Plugs.** Consent management and data mapping for NDPA ([S109], [S110]); AML case management; ATM and agent cash forecasting.

## 6. Payment fraud

NIBSS's numbers tell a story that the headline hides:

| Year | Losses | Cases | Note | Source |
|---|---|---|---|---|
| 2020 | ₦11.61bn | 101,624 | | [S132] |
| 2023 | ₦17.67bn | | | [S132] |
| 2024 | ₦52.26bn | 70,111 | ₦31.1bn from a single incident at one entity; fraud to transaction value ratio 0.0040% | [S132], [S133] |
| 2025 | ₦25.85bn | 67,518 | Lagos 63.43% of fraud activity; joint industry action prevented about ₦20bn | [S133] |

Strip out the ₦31.1bn single incident and 2024 losses were about ₦21.2bn (our calc), so the "tripling" in 2024 was mostly one event. That matters: **concentration risk inside one institution** is as big a threat as widespread retail scams.

Where fraud happens: in 2023, mobile led with ₦5.69bn lost, then POS ₦4.42bn, internet banking ₦4.09bn and web ₦2.22bn ([S134]). In 2025, NIBSS said e-commerce and internet banking were the most affected channels, and named insider abuse as the most prevalent technique ([S133]). FITC's bank fraud data shows how spiky it is: branch fraud losses were ₦9.2bn in Q3 2024 and ₦786.7m in Q4 ([S135]).

Identity is the root. NIBSS described about ₦400m moved through accounts opened with stolen senior citizens' identities, and over ₦1bn through accounts opened with BVNs registered for minors by compromised staff ([S136]).

**Plugs.** Insider risk monitoring at onboarding (staff and agent behaviour analytics); liveness and document checks that flag reused selfies across institutions ([S136]); faster cross-institution fraud reporting, since NIBSS says fraudsters move to institutions that do not report ([S133]); ISO 20022 richer data for screening ([S008]).

## 7. Processor losses and cybersecurity breaches

| Incident | Date | Amount | Outcome | Source |
|---|---|---|---|---|
| Patricia hack | Jan 2022 (disclosed 2023) | About $2m | Withdrawals suspended; police later linked ₦607m of diverted funds | [S141], [S142] |
| Flutterwave | Feb 2023 | ₦2.95bn moved to 28 accounts | Accounts frozen by court order | [S137] |
| Flutterwave POS glitch | Oct 2023 | ₦21.2bn exposure, ₦7.2bn preserved | A court refused a police request to reverse some withdrawals | [S138], [S139] |
| Interswitch chargebacks | 2023 to 2024 | About ₦30bn suspected; ₦11.45bn operating loss booked | Recovery process ongoing | [S042], [S041] |
| Flutterwave | Apr to May 2024 | Reported attempted breach | Company said it was blocked and customer funds were safe | [S140] |

Techpoint reported that an error at NIBSS worsened the Flutterwave October 2023 glitch ([S139]). Shared rails mean one participant's bug can become everyone's loss.

**Plugs.** Real-time reconciliation between processor, switch and bank ledgers; automated hold-and-reverse within the CBN dispute windows; chargeback evidence management for acquirers.

## 8. POS capex and agent churn

* Terminals are imported and priced in dollars: entry devices about ₦21,500, smart devices ₦62,000 to ₦85,000 ([S006]).
* OPay and Moniepoint moved from free terminals to outright sales or caution deposits with volume targets ([S170]).
* The October 2025 rules capped daily agent cash-out at ₦1.2m and tied terminals to one location ([S115]). That lowers the revenue ceiling per terminal.
* We found no recent public agent churn rate. Left blank.

**Plugs.** Device leasing tied to volume, refurbishment and reuse programmes, agent performance analytics that move idle terminals to busy areas within the new geofencing rules.

## 9. Customer acquisition cost and churn

Technext reported CAC estimates of ₦2,000 to ₦5,000 per user, with users who claim referral bonuses and then leave ([S171]). This is a press estimate, not a company disclosure. Cowrywise wrote that it stopped cash referral bonuses because referred users churned after their plans matured ([S172]). The wallets that won (OPay, PalmPay) paid for growth with free transfers for years, backed by large foreign shareholders ([S073], [S169]).

**Plugs.** Incentives tied to second and third transactions, not signups; cohort retention analytics.

## 10. Cash-out fees and the cost of cash

During the 2023 cash crunch, agents charged 10% to more than 20% for withdrawals ([S167]). In 2025, a ₦10,000 withdrawal typically cost ₦200 to ₦300 ([S168]). From January 2026, bank withdrawals above ₦500,000 a week cost 3% for individuals ([S117]). Cash is the most expensive service in the system for the poorest users.

## 11. Taxes and levies

* ₦50 EMTL on inflows from December 2024 ([S093]), replaced by ₦50 stamp duty paid by the sender from January 2026 ([S092]).
* A 0.5% cybersecurity levy was ordered in May 2024 and suspended within days ([S090], [S091]).
* Banks paid a 70% windfall levy on realised FX gains for 2023 to 2025 ([S125]).
* The 2025 tax reform added a 4% development levy for companies above the small company threshold ([S123]).

## 12. Downtime and failed transactions

In February 2023, e-payment value fell to ₦37tn as failed transactions mounted during the cash crunch ([S166]). Ecofin reports later core banking migrations that left customers without access for days and delayed salaries by up to 72 hours ([S073]); it does not name the bank, so we do not either. We found no NIBSS-published annual downtime statistic. Left blank.

## 13. Talent flight

Afrobarometer found 56% of Nigerians had considered emigrating in 2024, including 60% of 18 to 35 year olds ([S159]). We found no reliable count of tech workers who left or a cost to employers. Left blank.

## 14. The funding drought

Nigerian startups raised $343m in 2025, down 16.3% from $410m in 2024, and Nigeria's share of African funding fell from 18.6% to 10.7% (Africa: The Big Deal data) ([S160], [S173]). Briter put Nigeria's 2025 share at 8%, its lowest since 2019 ([S161]). Less new money makes every other hole on this page harder to survive.

## What would plug the holes

| Hole | Product or fix | Who would buy it | Difficulty |
|---|---|---|---|
| FX mismatch | Naira-denominated asset finance; FX exposure dashboards for SMEs | Solar, mobility, importers | High (needs capital) |
| Credit losses | Cash-flow underwriting on transaction data; compliant collections workflows | MFBs, wallets, FCCPC-registered lenders | Medium |
| Insider and identity fraud | Staff and agent behaviour monitoring; cross-institution selfie and device reuse checks | Banks, MFBs, KYC vendors | Medium |
| Reconciliation failures | Ledger-to-ledger matching between bank, switch and processor with automated reversals | Gateways, MFBs, merchants | Medium (software heavy, low licence need) |
| Chargebacks | Evidence collection and dispute automation | Acquirers, schemes | Medium |
| NDPA exposure | Consent records, data maps, DPIA templates | Any firm handling customer data | Low to medium |
| Agent economics | Terminal leasing, idle terminal redeployment, float forecasting | Moniepoint-class acquirers, super agents | Medium |
| Power | PAYG solar bundles for agents | Agents, SMEs | High (hardware and finance) |

Several of these (reconciliation, dispute and fraud operations, bookkeeping automation, compliance documentation) are software-only problems that sit on top of licensed firms rather than requiring a licence. That is the kind of work a small automation and ML team such as Omnific Hand could take on, but none of it is easy and each needs a licensed partner willing to share data.

Related files: [`money_flows.md`](money_flows.md), [`regulation.md`](regulation.md), [`../../FAILURES.md`](../../FAILURES.md), [`SOURCES.md`](SOURCES.md).

<!-- reference links: generated by scripts/build_deep_dive_refs.py -->
[S001]: https://nairametrics.com/2025/01/29/e-payment-transactions-in-nigeria-hit-all-time-high-of-n1-07-quadrillion-in-2024/
[S005]: https://newtelegraphng.com/nibss-more-nigerians-embrace-pos-as-deployed-terminals-up-119-4-to-5-90m/
[S006]: https://nairametrics.com/2025/09/30/pos-terminals-cost-jumps-30-100-in-nigeria-over-two-years/
[S008]: https://nairametrics.com/2025/08/26/cbn-sets-october-31-deadline-for-payment-companies-to-comply-with-iso-20022/
[S022]: https://cban.ng/faq/
[S023]: https://www.cbn.gov.ng/Out/2020/CCD/CBN%20-%20Operational%20Guidelines%20on%20Global%20Standing%20Instructions%20GSI%20-%20Individuals.pdf
[S029]: https://punchng.com/cbn-ncc-order-banks-telcos-to-settle-n250bn-ussd-debt-dispute/
[S030]: https://nairametrics.com/2025/06/19/banks-clear-95-of-n180-billion-ussd-debt-3-lenders-still-owing-alton/
[S037]: https://nairametrics.com/2026/10/13/opay-earns-more-from-lending-than-payments-as-profit-hits-90-9-million/
[S040]: https://moneycentral.com.ng/exclusive/article/interswitch-navigates-fx-headwinds-moves-to-n14-7-billion-profit-after-prior-year-loss/
[S041]: https://moneycentral.com.ng/companies/article/interswitch-reports-n1-67bn-loss-in-2024-on-exchange-rate-movement-charge-back-fraud/
[S042]: https://techcabal.com/2023/11/02/interswitch-loses-n30bn-fraud/
[S044]: https://flutterwave.com/us/blog/building-for-the-long-term-2024-in-review
[S055]: https://www.tekedia.com/fairmoney-revenue-surges-to-n121-9-billion-in-2024-amid-shift-to-customer-deposit-funded-lending/
[S063]: https://www.sec.gov/Archives/edgar/data/1756708/000175670825000005/jumia-ex991q42024.htm
[S064]: https://punchng.com/moove-exits-nigeria-transfers-n35bn-vehicles-to-customers/
[S065]: https://www.bbc.com/news/articles/c86xpv8l9y9o
[S067]: https://techcabal.com/2025/01/20/kobo360-layoff/
[S068]: https://www.ifc.org/en/pressroom/2025/sun-king-ifc-and-stanbic-ibtc-bank-close-80-million-debt-facility-to-expand-solar-
[S069]: https://gogla.org/reports/semi-annual-solar-market-report/insights-from-the-january-june-2024-sales-and-impact-data/
[S070]: https://chapelhilldenham.com/d-light-and-chapel-hill-denham-close-n10-billion-in-securitised-financing-to-fund-off-grid-solar-expansion-in-nigeria/
[S073]: https://www.ecofinagency.com/insights/0809-48489-in-nigerian-bank-technology-failures-pushed-opay-and-palmpay-to-leadership-in-daily-payments
[S074]: https://doclib.ngxgroup.com/Financial_NewsDocs/43207_MTN_NIGERIA_COMMUNICATIONS_PLC-MTN_NIGERIA_FY_2024_EARNINGS_RELEASE_CORPORATE_ACTIONS_FEBRUARY_2025.pdf
[S075]: https://nairametrics.com/2025/04/07/ten-nigerian-companies-incur-n2-17-trillion-in-forex-losses/
[S090]: https://www.reuters.com/world/africa/nigeria-suspends-cybersecurity-levy-amid-cost-of-living-crisis-2024-05-14/
[S091]: https://punchng.com/cbn-withdraws-circular-on-cybersecurity-levy/
[S092]: https://www.thecable.ng/banks-to-start-charging-senders-n50-stamp-duty-on-transfers-above-n10k-from-january/
[S093]: https://www.legit.ng/business-economy/industry/1628352-fg-begins-n50-electronic-transfer-levy-charges-opay-palmpay-companies-send-messages/
[S102]: https://www.reuters.com/world/africa/nigeria-seeks-815-bln-economic-losses-back-tax-against-binance-court-document-2025-02-19/
[S103]: https://nairametrics.com/2025/10/15/firs-vs-binance-court-to-decide-81-billion-substituted-service-nov-12/
[S104]: https://fccpc.gov.ng/violations-tribunal-upholds-fccpcs-220-million-fine-against-meta-whatsapp/
[S105]: https://www.reuters.com/sustainability/boards-policy-regulation/nigerian-tribunal-upholds-220-million-fine-against-meta-violating-consumer-data-2025-04-25/
[S106]: https://techpoint.africa/insight/meta-and-fccpc-continue-tussle/
[S107]: https://www.reuters.com/business/finance/nigerian-data-agency-fines-fidelity-bank-breaches-2024-08-22/
[S108]: https://www.reuters.com/sustainability/boards-policy-regulation/nigerian-agency-fines-multichoice-766-million-naira-data-privacy-breaches-2025-07-07/
[S109]: https://assets.kpmg.com/content/dam/kpmgsites/ng/pdf/nigeria-data-protection-act2023.pdf.coredownload.pdf
[S110]: https://ndpc.gov.ng/wp-content/uploads/2025/03/NDP-ACT-GAID-2025-MARCH-20TH.pdf
[S111]: https://fccpc.gov.ng/wp-content/uploads/2025/11/Digital-Electronic-Online-or-Non-Traditional-Consumer-Lending-Regulations-2025.pdf
[S115]: https://punchng.com/cbn-caps-pos-agent-daily-transactions-at-n1-2m-in-new-guidelines/
[S117]: https://nairametrics.com/2025/12/03/cbn-revises-cash-withdrawal-rules-effective-january-2026-ends-special-authorisation/
[S123]: https://www.pwc.com/ng/en/publications/the-nigerian-tax-reform-acts.html
[S125]: https://www.olaniwunajayi.net/wp-content/uploads/2025/02/OALP-TAX-Wrap-Up-Report-and-Outlook-2025.pdf
[S128]: https://techcabal.com/2024/12/10/cbn-fines-moniepoint-and-opay/
[S129]: https://independent.ng/cbn-fines-29-banks-n15bn-for-money-laundering-breaches-cardoso/
[S130]: https://www.thisdaylive.com/2025/01/15/cbn-fines-9-banks-n1-35bn-over-failure-to-dispense-cash-via-atms/
[S132]: https://nairametrics.com/2025/02/26/nigerias-financial-sector-suffers-n52-26-billion-loss-to-fraud-in-2024-nibss-report/
[S133]: https://nibss-plc.com.ng/digital-payment-fraud-drops-51-to-n25-85b-lagos-accounts-for-63/
[S134]: https://nibss-plc.com.ng/wp-content/uploads/2024/04/2023-Annual-Fraud-Landscape.pdf
[S135]: https://fitc-ng.com/wp-content/uploads/2025/08/Fraud-and-Forgery-2024-4th-Quarter.pdf
[S136]: https://nairametrics.com/2025/02/26/fraudsters-steal-n400-million-through-accounts-opened-with-stolen-identity-in-2024-nibss/
[S137]: https://techpoint.africa/news/hackers-have-stolen-2-9-billion-from-flutterwave/
[S138]: https://nairametrics.com/2024/08/15/exclusive-nigerian-court-refuses-igps-request-to-reverse-billions-allegedly-withdrawn-from-flutterwave-in-2023-glitch/
[S139]: https://techpoint.africa/insight/a-fatal-error-by-nibss-worsened-flutterwaves-%e2%82%a621-billion-glitch/
[S140]: https://nairametrics.com/2024/05/16/flutterwave-blocks-security-breach-on-platform-says-customers-funds-safe/
[S141]: https://techcabal.com/2023/05/27/patricia-loses-2m-to-hack/
[S142]: https://techpoint.africa/news/arrested-wilfred-bonse-in-patricia-hack/
[S143]: https://weetracker.com/2023/10/06/dash-african-fintech-scandal/
[S144]: https://techcabal.com/2023/09/27/54gene-shutting-down-operations/
[S145]: https://technext24.com/news/okra-blames-shutdown-on-market-challenge/
[S146]: https://nairametrics.com/2025/10/24/fintech-startup-lidya-shuts-down-after-nine-years/
[S147]: https://techpoint.africa/insight/lydia-shuts-down/
[S148]: https://nairametrics.com/2025/02/26/nigerian-edtech-startup-edukoya-shuts-down-4-years-after-raising-3-5-million/
[S149]: https://techcabal.com/2024/04/01/thepeer-shuts-down/
[S150]: https://techpoint.africa/news/pivo-has-shut-down/
[S151]: https://technext24.com/news/bento-africa-temporarily-shuts-down/
[S152]: https://techcabal.com/2025/01/27/bento-africa-investigation/
[S153]: https://cdn.pacermonitor.com/pdfserver/D3XGTLY/199916559/Gokada_Inc__debke-24-12377__0001.0.pdf
[S154]: https://techcabal.com/2023/07/21/bundle-africa-shuts-down/
[S155]: https://thecondia.com/medsaf-shutdown-drug-supply/
[S156]: https://www.vanguardngr.com/2026/02/businesses-buckle-under-debt-as-defaults-push-bad-loans-to-n21-2trn/
[S157]: https://nairametrics.com/2025/04/10/nigerias-microfinance-banks-in-a-cashless-economy-evolving-for-a-digital-first-future/
[S158]: https://www.thisdaylive.com/2025/04/23/report-manufacturers-expenditure-on-alternative-energy-surged-to-n1-11trn-in-2024/
[S159]: https://www.afrobarometer.org/wp-content/uploads/2024/12/R10-News-release-Nigerians-consider-emigration-for-better-opportunities-Afrobarometer-bh-17dec24.pdf
[S160]: https://technext24.com/funding/nigerian-startups-raise-343-million-2025/
[S161]: https://techpoint.africa/news/nigeria-lowest-funding-share/
[S162]: https://www.imf.org/-/media/files/publications/selected-issues-papers/2026/english/sipea2026045.pdf
[S163]: https://www.ceicdata.com/en/nigeria/foreign-exchange-rates-annual/official-exchange-rate-period-average-local-currency-to-usd
[S166]: https://punchng.com/e-payment-falls-to-n37tn-as-failed-transactions-mount/
[S167]: https://archive.dataphyte.com/latest-reports/cash-strapped-nigerians-besiege-pos-locations-despite-over-20-charges/
[S168]: https://techpoint.africa/insight/pos-withdrawal-charges-rise-as-agents-lament-cash-scarcity-and-rising-costs/
[S169]: https://punchng.com/palmpay-sustains-zero-fee-transfer-to-drive-financial-inclusion/
[S170]: https://thewhistler.ng/hike-in-terminal-charge-by-opay-moniepoint-is-turning-pos-business-into-unattractive-venture-operators/
[S171]: https://technext24.com/fintech/nigerian-fintech-millions-get-customers/
[S172]: https://cowrywise.com/blog/referral-bonus-experiment/
[S173]: https://africathebigdeal.com/wp-content/uploads/2025/01/ATBD-2024-Round-Up.pdf
[S174]: https://techpoint.africa/insight/okra-return-funds-investors/
[S176]: https://techpoint.africa/news/nigerian-startup-thepeer-to-shut-down/
