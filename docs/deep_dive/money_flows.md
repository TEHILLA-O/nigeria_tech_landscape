# Where the money is actually made

Last verified: **2026-10-19**. All "our calc" figures are simple arithmetic on cited numbers and are labelled. Where a pool has no public size, the cell says "not disclosed" rather than an estimate dressed up as fact. Conversions use the ₦1,535/$ year-end 2024 rate quoted in [S001] for 2024 figures, and the World Bank series averages in [S163] (about ₦1,520/$ for 2025 and ₦1,385/$ for 2026) for later figures.

## The one-paragraph answer

Most of the money in Nigerian finance is still made on the balance sheet, not on the transaction. Banks earn trillions of naira from the gap between what they pay depositors and what they earn on loans and government securities ([S076]). The fintechs that became profitable did it the same way: OPay now earns more from lending than from payments ([S037]), Moniepoint lends over ₦1 trillion a year to the merchants it processes for ([S033]), and Paystack bought a bank licence ([S049]). Payment fees are real money but thin, capped and under political pressure. Payments are how you find the customer. Credit, float and fees on government plumbing are how you get paid.

## Revenue pools, ranked

Size is the latest disclosed figure for the named firms, not the whole market. Margin and certainty are our judgements, with the reasoning shown.

| Rank | Pool | Disclosed size (dated) | Margin | Certainty | Why |
|---|---|---|---|---|---|
| 1 | Bank net interest income | Five tier one banks: ₦6.98 trillion in 2024 (our calc: sum of ₦1.73tn, ₦1.53tn, ₦1.40tn, ₦1.26tn, ₦1.06tn), about $4.5bn at ₦1,535/$ ([S076]) | High: Zenith and GTCO each turned this into over ₦1tn profit after tax ([S077], [S078]) | High (audited bank accounts) | High rates after 2023 and cheap deposits |
| 2 | Fintech consumer and SME lending | OPay loan income $236.1m in H1 2026 ([S037]); Moniepoint ₦1tn+ disbursed in 2025 ([S033]); FairMoney revenue ₦121.9bn in 2024 ([S055]) | Medium: OPay's credit loss charge was 25.3% of total revenue in H1 2026 ([S037]); FairMoney impairments were ₦59.4bn ([S055]) | High for OPay (F-1), medium for others | Wallet data makes underwriting cheap; defaults are the swing factor |
| 3 | Payment and transaction fees | OPay $130.6m in H1 2026 ([S037]); Interswitch core processing about 39% of ₦137.5bn, so about ₦53.6bn (our calc, year to March 2025) ([S040]); eTranzact revenue ₦29.9bn in 2024 ([S061]) | Low to medium: caps on card and transfer pricing ([S127], [S048]) | High for listed and filing firms; low for Paystack, Flutterwave, Moniepoint (not disclosed) | Huge volume, small per transaction take |
| 4 | Card scheme fees | Verve about 32% of Interswitch revenue, so about ₦44.0bn (our calc, year to March 2025) ([S040]) | Medium to high (scheme economics) | Medium | 70m+ Nigerian Verve cards ([S016]) |
| 5 | Float and treasury income | OPay short-term investment interest $50.6m in H1 2026 ([S036], [S037]) | High: earning on balances customers leave idle | Medium (only OPay discloses) | Wallet balances invested while yields are high |
| 6 | Government and enterprise infrastructure | Interswitch non-transaction revenue ₦34.3bn, up 81% (year to March 2025), including FIRS e-invoicing and pensions ([S040], [S017]) | Medium to high (contracted, sticky) | Medium | Mandatory e-invoicing creates captive demand |
| 7 | Insurance premiums | Gross written premiums ₦1.5587 trillion in 2024 ([S071]) | Varies by line | High (NAICOM) | Penetration is low; insurtech share not disclosed |
| 8 | Cross-border FX spread and fees | Flows: about $21.8bn formal remittances in 2025 ([S164]); LemFi $1bn+ a month ([S057]). Revenue: not disclosed | Medium, but squeezed by naira-only payout rules ([S087]) | Low | Spreads are not published |
| 9 | Agent cash-out fees | ₦200 to ₦300 per ₦10,000 withdrawal in 2025 ([S168]), so 2% to 3% (our calc). Total pool: not disclosed | High per transaction, shared between agent and platform | Low | Customers pay for access to cash; caps on daily cash-out limit growth ([S114]) |
| 10 | Telco USSD session fees | ₦6.98 per banking USSD transaction ([S027]). Pool: not disclosed; banks had ₦180bn of accumulated arrears by 2025 ([S030]) | Medium | Medium | Now billed to airtime |
| 11 | Crypto trading and on-ramps | $92.1bn crypto value received (July 2024 to June 2025) ([S072]). Revenue: not disclosed | Unknown | Low | Volume is large, licensed share is small |
| 12 | Merchant software (SaaS, bookkeeping) | Not disclosed. Moniepoint launched Moniebook (payments plus bookkeeping) in 2025 ([S033]) | Potentially high | Low | Usually bundled free with payments |

The CSV version is in [`data/revenue_pools.csv`](../../data/revenue_pools.csv).

### The top five, in plain words

1. **Banks lending and holding government paper.** ₦6.98 trillion of net interest income at the top five banks in 2024 dwarfs every fintech revenue line in this file.
2. **Fintech credit.** Over half of OPay's revenue is now loans ([S037]). This is where the next decade's fintech profits will be made or lost.
3. **Transaction fees.** Real, recurring and capped. The volume leaders make money here only because the volume is enormous.
4. **Card scheme fees.** Verve is a domestic toll road with over 70 million Nigerian cards ([S016]).
5. **Float.** Idle wallet balances earning treasury yields are close to pure profit while rates are high.

## Take rates and unit economics

### Prices the customer sees

| Charge | Price | Effective rate (our calc) | Source |
|---|---|---|---|
| NIP transfer, up to ₦5,000 | Up to ₦10 | Up to 0.2% on ₦5,000 | [S127] |
| NIP transfer, ₦5,001 to ₦50,000 | ₦25 | 0.05% to 0.5% | [S127] |
| NIP transfer, above ₦50,000 | ₦50 | 0.1% at ₦50,000, lower above | [S127] |
| Merchant service charge on cards (general) | 0.5%, capped at ₦1,000 | 0.5% up to ₦200,000; 0.2% at ₦500,000 | [S127] |
| Paystack local card or transfer | 1.5% plus ₦100, ₦100 waived under ₦2,500, capped at ₦2,000 | 1.5% at ₦2,000; 2.5% at ₦10,000; 1.0% at ₦200,000 | [S048] |
| Paystack international card | 3.9% plus ₦100 | 4.9% at ₦10,000 | [S048] |
| Paystack dedicated virtual account | 1%, capped at ₦300 | 1% up to ₦30,000; 0.3% at ₦100,000 | [S048] |
| Paystack terminal card | 0.5%, capped at ₦1,000 | Same as CBN MSC | [S048] |
| Agent cash-out, ₦10,000 | About ₦200, some ₦300 | 2% to 3% | [S168] |
| Stamp duty on transfers of ₦10,000 or more (from Jan 2026) | ₦50, paid by sender | 0.5% at ₦10,000 | [S092] |
| USSD banking session | ₦6.98 | Flat | [S027] |
| Cash withdrawals above weekly limits (from Jan 2026) | 3% individuals, 5% companies | 3% to 5% | [S117] |

Two things jump out. First, **caps make large payments cheap and small payments relatively expensive.** A ₦10,000 online sale through a list-price gateway costs the merchant 2.5%, while a ₦200,000 sale costs 1.0% (our calc from [S048]). Second, **cash access is the most expensive thing in the system** for the user: 2% to 3% at an agent, against fractions of a percent for a transfer.

### Who keeps what

The split of an NIP fee between the sending institution, NIBSS and the receiving side is not published in a source we could cite. Neither is the split of the merchant service charge between acquirer, issuer, switch and scheme. We have left these blank rather than repeat industry folklore.

### Company unit economics we can actually calculate

| Metric | Value | How | Source |
|---|---|---|---|
| OPay average transaction | About $6.19 | $558bn / 90.1bn transactions, 12 months to June 2026 | [S038] |
| OPay revenue per $ of volume, 2025 | About 0.15% (15 basis points) | $536.3m revenue / $358bn GTV (our calc) | [S175] |
| OPay credit loss as share of loan income, H1 2026 | About 50% | $118.4m credit loss expense / $236.1m loan income (our calc) | [S037] |
| OPay lending income per $ disbursed, H1 2026 | About 25% | $236.1m / $927.6m new Nigerian loans (our calc; this is not an APR, it mixes tenors and timing) | [S037] |
| OPay overdue share of loan receivables | 27.4% at 30 June 2026, from 34.2% at December 2025 | Reported | [S037] |
| Moniepoint average transaction, 2025 | About ₦29,400 | ₦412tn / 14bn transactions (our calc) | [S033] |
| Interswitch net margin, year to March 2025 | About 10.7% | ₦14.7bn / ₦137.5bn (our calc) | [S040] |
| eTranzact net margin, 2024 | About 11.3% | ₦3.39bn / ₦29.9bn (our calc) | [S061] |
| FairMoney impairments as share of revenue, 2024 | About 49% | ₦59.4bn / ₦121.9bn (our calc) | [S055] |
| FairMoney net margin, 2024 | About 4.8% | ₦5.85bn / ₦121.9bn (our calc) | [S055] |

Read together: **payments businesses run on net margins around 10% at the infrastructure layer, while consumer credit can roughly double revenue but hands about half of it back as losses.** The profit is in getting underwriting right.

The OPay average ($6.19) against Moniepoint's (about ₦29,400, roughly $19 at the 2025 average rate, our calc) also shows two different businesses: OPay is consumer micro payments; Moniepoint is merchant and business flows.

## Who is profitable, with sources

| Company | Status | Evidence | Source |
|---|---|---|---|
| OPay | Profitable since 2025 | $72.5m net income in 2025 after a $50.8m loss in 2024; $90.9m in H1 2026 | [S036], [S175], [S177] |
| Moniepoint | Says it is profitable | "Operating profitably" with "industry-leading gross profit and EBITDA margins"; no figures published | [S031] |
| Paystack | Profitable at group level since February 2025 | Seven profitable months in 2025 | [S047] |
| Interswitch | Profitable in year to March 2025 | ₦14.7bn profit after tax after a loss the year before | [S040], [S041] |
| eTranzact | Profitable | ₦3.39bn profit after tax in 2024 | [S061] |
| FairMoney | Profitable (unaudited) | ₦5.85bn profit after tax in 2024 | [S055] |
| PalmPay | Reported profitable | Per people familiar with its finances; no published accounts | [S051] |
| Chipper Cash | Cash flow positive | First quarter without cash burn | [S056] |
| Flutterwave | Not yet, profitability "in sight" | Monthly margin doubled vs 2024 average by June 2025; UK unit lost £2.27m in 2024 | [S045], [S043] |
| Kuda | Loss-making, narrowing | $5.83m loss in 2024 vs $35.11m in 2023 | [S054] |
| Jumia | Loss-making | $66.0m operating loss in 2024 | [S063] |
| MTN Nigeria | Loss in 2024 on FX | ₦400.4bn loss after tax despite ₦3.36tn revenue | [S074] |
| Tier one banks | Highly profitable | Zenith ₦1.03tn and GTCO ₦1.02tn profit after tax, 2024 | [S077], [S078] |

## Patterns in how the winners make money

1. **Lend to the customers you already process for.** OPay's filing says payment data helps it assess lending risk ([S037]); Moniepoint lends to its merchants and reports their transaction value rose 36% after receiving loans ([S033]).
2. **Sell to government.** Interswitch's fastest growing line is government and enterprise infrastructure ([S040]).
3. **Own the licence.** Paystack's MFB ([S049]) and the CBN's national MFB upgrades ([S084]) both turn payment firms into deposit takers that can earn interest margins.
4. **Charge for cash.** Agents and platforms earn more per naira on cash access than on any digital transfer ([S168]).
5. **Earn in dollars where you can.** Flutterwave's enterprise and cross-border focus ([S044]) and LemFi's diaspora model ([S057]) are partly a hedge against naira revenue.

## What we could not size

* The total revenue pool from NIP fees across all institutions.
* The total merchant service charge pool and its split.
* Total agent cash-out fee revenue.
* FX spread income on remittance corridors.
* Revenue of Paystack, Flutterwave, Moniepoint and PalmPay from audited Nigerian accounts.
* Total digital lending book size across FCCPC-registered lenders.

If you have a public, citable source for any of these, see [`../../CONTRIBUTING.md`](../../CONTRIBUTING.md).

Related files: [`players_competition.md`](players_competition.md), [`losses_and_leaks.md`](losses_and_leaks.md), [`SOURCES.md`](SOURCES.md).

<!-- reference links: generated by scripts/build_deep_dive_refs.py -->
[S001]: https://nairametrics.com/2025/01/29/e-payment-transactions-in-nigeria-hit-all-time-high-of-n1-07-quadrillion-in-2024/
[S016]: https://interswitchgroup.com/news/verve-hits-100-million-cards-issued-reinforcing-leadership-in-africas-card/
[S017]: https://interswitchgroup.com/news/interswitch-named-firs-access-point-provider-for-mandatory-e-invoicing/
[S027]: https://ncc.gov.ng/sites/default/files/2025-04/USSD-DETERMINATION-2025.pdf
[S030]: https://nairametrics.com/2025/06/19/banks-clear-95-of-n180-billion-ussd-debt-3-lenders-still-owing-alton/
[S031]: https://moniepoint.com/blog/moniepoint-has-raised-usdollar110-million
[S033]: https://techpoint.africa/news/moniepoint-2025-report/
[S036]: https://www.sec.gov/Archives/edgar/data/2103076/000119312526418812/d56487df1.htm
[S037]: https://nairametrics.com/2026/10/13/opay-earns-more-from-lending-than-payments-as-profit-hits-90-9-million/
[S038]: https://www.techcityng.com/opay-ipo-filing-nyse/
[S040]: https://moneycentral.com.ng/exclusive/article/interswitch-navigates-fx-headwinds-moves-to-n14-7-billion-profit-after-prior-year-loss/
[S041]: https://moneycentral.com.ng/companies/article/interswitch-reports-n1-67bn-loss-in-2024-on-exchange-rate-movement-charge-back-fraud/
[S043]: https://techpoint.africa/news/flutterwave-uk-2024-financial-result/
[S044]: https://flutterwave.com/us/blog/building-for-the-long-term-2024-in-review
[S045]: https://flutterwave.com/us/blog/scaling-with-purpose-h1-2025-at-flutterwave
[S047]: https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring
[S048]: https://paystack.com/pricing
[S049]: https://techcabal.com/2026/01/14/paystack-becomes-a-microfinance-bank-nigeria/
[S051]: https://techcrunch.com/2025/06/05/profitable-african-fintech-palmpay-is-in-talks-to-raise-as-much-as-100m/
[S054]: https://businessday.ng/technology/article/breaking-kuda-cuts-losses-to-5-8m-as-fintech-shifts-focus-to-profitability/
[S055]: https://www.tekedia.com/fairmoney-revenue-surges-to-n121-9-billion-in-2024-amid-shift-to-customer-deposit-funded-lending/
[S056]: https://techcabal.com/2026/01/21/chipper-cash-posts-first-quarter-without-cash-burn/
[S057]: https://www.highlandeurope.com/lemfi-has-secured-53m-in-series-b-funding-led-by-highland-europe/
[S061]: https://doclib.ngxgroup.com/Financial_NewsDocs/43535_E-TRANZACT_INTERNATIONAL_PLC-_QUARTER_5_-_FINANCIAL_STATEMENT_FOR_2024_FINANCIAL_STATEMENTS_MARCH_2025.pdf
[S063]: https://www.sec.gov/Archives/edgar/data/1756708/000175670825000005/jumia-ex991q42024.htm
[S071]: https://naicom.gov.ng/annual/
[S072]: https://www.chainalysis.com/blog/subsaharan-africa-crypto-adoption-2025/
[S074]: https://doclib.ngxgroup.com/Financial_NewsDocs/43207_MTN_NIGERIA_COMMUNICATIONS_PLC-MTN_NIGERIA_FY_2024_EARNINGS_RELEASE_CORPORATE_ACTIONS_FEBRUARY_2025.pdf
[S076]: https://businessday.ng/companies/article/zenith-uba-lead-nigerian-banks-with-trillion-naira-net-interest-income/
[S077]: https://nairametrics.com/2025/03/28/breaking-gtco-reports-record-n1-trillion-profit-after-tax-for-2024-fy/
[S078]: https://nairametrics.com/2025/03/27/zenith-bank-post-record-n1-trillion-profit-after-tax/
[S084]: https://guardian.ng/business-services/money/cbn-upgrades-licences-of-major-fintechs-mfbs-to-national-status/
[S087]: https://nairametrics.com/2024/02/04/cbn-stops-outbound-international-money-transfer-transactions-limits-inflow-payouts-to-naira/
[S092]: https://www.thecable.ng/banks-to-start-charging-senders-n50-stamp-duty-on-transfers-above-n10k-from-january/
[S114]: https://businessday.ng/business-economy/article/cbn-limits-daily-cash-withdrawals-via-agent-banking-to-n100000/
[S117]: https://nairametrics.com/2025/12/03/cbn-revises-cash-withdrawal-rules-effective-january-2026-ends-special-authorisation/
[S127]: https://www.cbn.gov.ng/Out/2022/CCD/Guide%20to%20Charges%20by%20Banks%20Other%20Financial%20and%20Non-Financial%20Institutions%20eff%20Jan%201%202020.pdf
[S163]: https://www.ceicdata.com/en/nigeria/foreign-exchange-rates-annual/official-exchange-rate-period-average-local-currency-to-usd
[S164]: https://www.vanguardngr.com/2026/05/diaspora-remittances-stabilises-at-21-8bn-in-2025-amid-global-pressures/
[S168]: https://techpoint.africa/insight/pos-withdrawal-charges-rise-as-agents-lament-cash-scarcity-and-rising-costs/
[S175]: https://nairametrics.com/2026/08/13/opay-swings-to-profit-in-fy2025-as-revenue-surges-161-to-536-3-million/
[S177]: https://www.streetinsider.com/Reuters/SoftBank-backed+OPay+reveals+revenue+rise+in+US+IPO+filing/27171098.html
