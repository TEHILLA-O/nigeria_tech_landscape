# Major players and how they compete

Last verified: **2026-10-19**. Metrics are the latest public figures we could cite, with their dates. Blank or "not disclosed" means we looked and found nothing defensible. Many Nigerian fintechs are private and publish little, so treat every row as a floor, not a full picture.

## The big picture in five sentences

1. Retail payments are now led by two wallet companies, OPay and Moniepoint, that started as payments firms and became lenders with banking licences.
2. Online checkout is a two horse race between Paystack and Flutterwave, both of which are moving into banking or data to escape thin payment margins.
3. Banks lost the everyday transfer but kept the balance sheet, and they still earn far more money than any fintech.
4. Price wars on transfers and POS are mostly over: the survivors are raising prices and earning on credit instead.
5. Consolidation is happening through small acquisitions and licence purchases, not big mergers.

## Segment by segment

### Consumer wallets and digital MFBs

| Company | Licences | Users | Volume | Revenue and profit | Funding (from this repo) |
|---|---|---|---|---|---|
| OPay | MMO and MFB ([S036]) | 50.1m monthly, 26.8m daily (31 Jul 2026) ([S038]) | $358bn gross transaction value in 2025 ([S175]), $558bn in 12 months to Jun 2026 ([S038]) | First monthly profit announced May 2024 ([S039]); revenue $205.7m in 2024 with $50.8m net loss; $536.3m in 2025 with $72.5m profit; H1 2026 revenue $467.1m, profit $90.9m ([S036], [S037]) | $570m disclosed (see `data/ranked_disclosed.csv`) |
| PalmPay | MMO and MFB | 16m monthly active in 2024 ([S052]); 35m registered in Q1 2025 ([S053]) | 15m daily transactions in Q1 2025 ([S053]) | About $64m revenue in 2023 and described as profitable by 2025 by people familiar with its finances ([S051]) | $140m |
| Kuda | MFB | Not disclosed in sources we used | Not disclosed | 2024 group revenue $18.34m, loss $5.83m, down from $35.11m loss in 2023; Nigerian revenue ₦21.2bn ([S054]) | See ranked sheet |
| MoMo PSB (MTN) | PSB | 2.7m active wallets in H1 2025 ([S062]) | Not disclosed | Not disclosed | Corporate |
| FairMoney | MFB | Not disclosed | Loan book ₦68.5bn (2024) | Revenue ₦121.9bn, profit after tax ₦5.85bn, loan impairments ₦59.4bn (2024, unaudited) ([S055]) | See ranked sheet |

**What OPay's F-1 tells us about the whole segment.** This is the first time a top Nigerian wallet has had to publish audited numbers in full, so it is worth reading closely:

* In H1 2026, OPay earned $236.1 million from loans it issued, $130.6 million from payment services, $41.6 million from loan facilitation (mostly Indonesia) and $50.6 million in short-term investment interest ([S037], [S036]). Loans were 50.6% of revenue and payments only 27.9% ([S037]).
* Its credit loss expense was $118.4 million in H1 2026, 25.3% of revenue, up from 19.3% a year earlier. It wrote off $113.2 million in six months, more than the $70.0 million it wrote off in all of 2025 ([S037]).
* About 85% of OPay's credit income comes from Nigeria ([S037]), and Nigeria produced 88.1% of 2025 revenue ([S038]).
* Average transaction size in the year to June 2026 was about $6.19 ([S038], calculated by TechCity from F-1 totals). This is a micro-payment business.

The lesson is general: **the wallet is a customer acquisition channel for lending.** Payment revenue covers the cost of being the default app, and credit pays for the profit. That is also why credit losses are now the swing factor for the whole segment.

### Merchant acquiring, agents and POS

| Company | Position | Metrics |
|---|---|---|
| Moniepoint | Largest merchant acquirer | 2025: ₦412 trillion processed, 14 billion+ transactions, 6 million+ businesses, 16 million+ individuals, ₦1 trillion+ credit disbursed; says 8 in 10 in-person transactions ran through it ([S033]). 2024: 800 million+ transactions a month, over $17 billion monthly value, profitable, revenue CAGR above 150% ([S031], [S032]). Raised a $200 million Series C completed October 2025 ([S034]) |
| OPay | Second large agent and POS network | Ecofin estimates OPay had over 563,000 agents by mid-2023, about 37% of all agents, but this is a press estimate, not a filing ([S073]) |
| PalmPay | Agent network | Ecofin estimates 500,000+ agents; treat as an estimate ([S073]) |
| Paystack Terminal | SME and enterprise terminals | Terminal card fee 0.5% capped at ₦1,000; device price ₦100,000 ([S048]) |

**Moat.** In acquiring, the moat is distribution: thousands of field staff, terminal logistics, agent float credit and the MFB licence to hold merchant balances. Software is copyable; a field network that keeps 6 million businesses live is not ([S033]).

**The POS "war" ended in price rises.** OPay moved from free terminals to outright sales of about ₦10,000 for a mini device to ₦60,000 for a smart terminal, and Moniepoint charged a ₦21,500 package with daily volume targets for agents, according to agent reporting ([S170]). Device prices rose 30% to 100% between 2023 and 2025 ([S006]). Agents responded by raising cash-out fees, which moved toward ₦200 to ₦300 per ₦10,000 withdrawal in 2025 ([S168]).

### Online payments and gateways

| Company | Position | Metrics |
|---|---|---|
| Paystack (Stripe) | SME to mid-market online checkout | Claimed more than half of Nigerian online transactions in 2024 ([S050]); group profitable from February 2025 ([S047]); bought Ladder MFB and relaunched it as Paystack MFB ([S049]) |
| Flutterwave | Enterprise and cross-border | Enterprise payments 90% of revenue (2024) ([S044]); monthly margin doubled by June 2025 vs 2024 average, enterprise TPV up about 20% ([S045]); bought Mono (January 2026) ([S046]). Flutterwave UK lost £2.27m in 2024 on turnover of £6.6m ([S043]). Group revenue not disclosed |
| Interswitch | Switching, Verve, Quickteller, government | Revenue ₦137.5bn, profit after tax ₦14.7bn, year to March 2025 ([S040]) |
| eTranzact | Switching, NGX listed | Revenue ₦29.9bn, profit after tax ₦3.39bn in 2024 ([S061]) |

**Moat.** For Paystack, developer experience plus Stripe's balance sheet. For Flutterwave, multi-country licences and enterprise integrations (it says enterprise is 90% of revenue ([S044])). For Interswitch, Verve's issuance base of over 70 million Nigerian cards ([S016]) and government contracts ([S017]).

**Where they are heading.** Both big gateways are buying their way out of pure payments: Paystack into banking via an MFB ([S049]), Flutterwave into account data and account-to-account payments via Mono ([S046]). That tells you list-price checkout fees alone do not make a great business.

### Banks

| Bank | 2024 net interest income | 2024 profit after tax |
|---|---|---|
| Zenith | ₦1.73 trillion ([S076]) | ₦1.03 trillion ([S078]) |
| UBA | ₦1.53 trillion ([S076]) | not cited here |
| First Holdco | ₦1.40 trillion ([S076]) | not cited here |
| Access | ₦1.26 trillion ([S076]) | not cited here |
| GTCO | ₦1.06 trillion ([S076]) | ₦1.02 trillion ([S077]) |

For scale: OPay's best half year (H1 2026) was $467.1 million of revenue ([S037]). At an illustrative ₦1,385/$ (our conversion using the 2026 average in [S163]) that is about ₦647 billion, still well below Zenith's net interest income alone. **Banks are not losing money to fintechs; they are losing customers' daily attention.**

### Credit and BNPL

| Company | Metric |
|---|---|
| OPay | $927.6m of new Nigerian loans in H1 2026, up from $305.1m a year earlier; quarterly unique borrowers rose from 3.5m to 6.7m ([S037]) |
| Moniepoint MFB | ₦1 trillion+ disbursed in 2025 ([S033]) |
| FairMoney | ₦68.5bn loan book, ₦59.4bn impairments (2024) ([S055]) |
| Lidya | Shut down October 2025 after raising $16.45m ([S146], [S147]) |

**How they compete.** Speed of approval and data. A wallet that sees a merchant's daily flows can lend against them; a standalone lender cannot. Lidya's closure in 2025 ([S146]) and Okra's closure (an open banking data supplier) the same year ([S145]) show what happens to firms without their own transaction data.

### Remittance and cross-border

| Company | Metric |
|---|---|
| LemFi | $53m Series B (Jan 2025), total about $85m, more than $1bn monthly volume, doubled users and revenue in two years ([S057]) |
| Chipper Cash | First quarter without cash burn after restructuring (reported Jan 2026) ([S056]) |
| Grey | Seed-stage cross-border accounts for freelancers; metrics are company claims only, not cited here |
| Moniepoint (MonieWorld) | UK remittance arm; Moniepoint GB lost £1.2m in 2024 in set-up costs and spent $2.5m on the Bancom acquisition ([S035]) |

The structural problem here is that formal flows are small relative to total remittances. Formal diaspora remittances were about $21.8 billion in 2025 ([S164]) but IMTO flows were only $2.07 billion in H1 2025 ([S165]). The CBN's 2024 rule that inbound payouts must be in naira ([S087]) removed the dollar payout option that some users wanted.

### Savings and wealth

PiggyVest is the clear leader by disclosed activity: ₦835 billion paid out in 2024 and ₦1.3 trillion in 2025 with over 6 million users ([S060], [S059]). It also co-led the 2024 Brass acquisition with Paystack ([S058]). Cowrywise, Risevest and Bamboo do not publish assets under management in sources we could cite, so their rows in this repo stay blank on size.

### Crypto

Binance spent 2024 in a standoff with the government: an executive was detained until October 2024 ([S101]) and the tax authority filed an $81.5 billion claim ([S102]). Local exchanges entered the SEC's ARIP pathway ([S096]). Bundle Africa closed its exchange in July 2023 ([S154]). The SEC raised minimum capital for digital asset exchanges and custodians to ₦2 billion in January 2026 ([S097], [S098]), which favours the larger, better funded players.

### Mobility, commerce and energy

* **Mobility.** Uber ended Nigerian operations on 2 September 2026 ([S065]) amid fuel, financing and fare pressure ([S066]). Moove, whose model depended on Uber, then exited Nigeria and transferred about ₦35 billion of vehicles to drivers ([S064]). Bolt and inDrive stay. Gokada filed for Chapter 11 in October 2024 ([S153]).
* **E-commerce.** Jumia cut its 2024 operating loss by 10% to $66.0 million while revenue fell 10% to $167.5 million, largely on the naira ([S063]).
* **Energy.** Sun King's $80 million naira-denominated receivables facility ([S068]) and d.light's ₦10 billion securitisation ([S070]) show the winners are those who can borrow in naira and match it to naira repayments.

## The price wars

| War | What happened | Who won | Source |
|---|---|---|---|
| Free transfers | PalmPay kept promoting zero-fee transfers in 2024 while OPay and Moniepoint moved to small charges or limited free tiers | Nobody "won" on price; the winners were the apps with the most reliable uptime and credit offers | [S169], [S073] |
| Government levy pass-through | From December 2024 wallets began deducting the ₦50 Electronic Money Transfer Levy on inflows of ₦10,000 or more ([S093]); from January 2026 this became a ₦50 stamp duty paid by the sender ([S092]) | Neutral across players, negative for users | [S093], [S092] |
| POS terminals | Free or subsidised terminals ended; prices and agent targets rose | Moniepoint, which kept its share while raising prices ([S033], [S170]) | [S006], [S170] |
| Agent cash-out fees | Association price lists and rising fees; FCCPC warning on price fixing | Agents in the short term | [S168], [S131] |
| Online checkout | List prices are now similar (Paystack 1.5% plus ₦100 capped at ₦2,000) | Volume discounts matter more than list price | [S048] |

## Consolidation and M&A (2024 to 2026)

| Year | Deal | Why it matters | Source |
|---|---|---|---|
| 2024 | Paystack, PiggyVest, P1 Ventures and Ventures Platform buy Brass | Rescue of an SME bank by its peers | [S058] |
| 2024 to 2025 | Moniepoint GB buys Bancom (UK e-money firm) | Licence acquisition for diaspora remittance | [S035] |
| 2026 | Flutterwave buys Mono, all-stock, reported $25m to $40m | Payments firm buys data and account-to-account rails | [S046] |
| 2026 | Paystack buys Ladder MFB, becomes Paystack MFB | Gateway becomes a bank | [S049] |
| 2026 | CBN upgrades Moniepoint, OPay, Kuda and other MFBs to national status | Regulator formalises fintechs as banks | [S084] |

The pattern: **buy a licence, not a competitor.** Licences take years to get, so acquiring a small licensed entity is the fastest route into deposit-taking or a new market.

## Banks vs fintechs

* **Fintechs took the daily transaction.** Mobile money operators processed ₦71.5 trillion in 2024 ([S004]), and Moniepoint says it handles most in-person payments ([S033]).
* **Banks kept the balance sheet.** Tier one banks earned trillions in net interest income ([S076]) and now carry recapitalised capital bases ([S083]).
* **The two are converging.** Fintechs now hold MFB licences and lend; banks are rebuilding cores and apps ([S073]).
* **Regulators treat big fintechs like banks.** The 2024 onboarding pause ([S088]), reported ₦1 billion fines on Moniepoint and OPay (OPay denied it) ([S128]) and the 2026 national licence upgrades ([S084]) all point the same way.

## Who is winning, who is losing, and why

| Winning | Why |
|---|---|
| OPay | Scale in micro payments turned into a lending book; swung to profit in 2025 ([S036]) |
| Moniepoint | Distribution moat in in-person payments plus SME credit ([S033]) |
| Paystack | Profitable and buying a bank licence ([S047], [S049]) |
| Interswitch | Back to profit; diversifying into government plumbing ([S040], [S017]) |
| Tier one banks | Record net interest income ([S076]) |

| Losing or retreating | Why |
|---|---|
| Ride hailing (Uber, Moove) | Fuel, financing and fare pressure ([S065], [S066], [S064]) |
| Standalone lenders and data aggregators (Lidya, Okra) | No proprietary transaction data, expensive dollar costs ([S146], [S145]) |
| Telco PSBs (MoMo PSB) | Far below targets in active wallets ([S062]) |
| USD-funded startups with naira revenue | Devaluation (see [`losses_and_leaks.md`](losses_and_leaks.md)) |

## What we could not find

* Paystack and Flutterwave group revenue for 2024 or 2025. Third-party estimates exist, but none from a filing.
* Moniepoint's audited revenue and profit. It says it is profitable ([S031]) but publishes no figures we could cite.
* PalmPay's audited 2024 or 2025 accounts.
* NIBSS participant-level rankings of NIP inflows by institution.
* Card scheme market shares by value in Nigeria.

Related files: [`value_chain.md`](value_chain.md), [`money_flows.md`](money_flows.md), [`SOURCES.md`](SOURCES.md).

<!-- reference links: generated by scripts/build_deep_dive_refs.py -->
[S004]: https://nairametrics.com/2025/02/02/mobile-money-palmpay-opay-others-process-n71-5-trillion-transactions-in-2024/
[S006]: https://nairametrics.com/2025/09/30/pos-terminals-cost-jumps-30-100-in-nigeria-over-two-years/
[S016]: https://interswitchgroup.com/news/verve-hits-100-million-cards-issued-reinforcing-leadership-in-africas-card/
[S017]: https://interswitchgroup.com/news/interswitch-named-firs-access-point-provider-for-mandatory-e-invoicing/
[S031]: https://moniepoint.com/blog/moniepoint-has-raised-usdollar110-million
[S032]: https://www.reuters.com/technology/google-among-investors-putting-110-million-into-nigerias-moniepoint-2024-10-29/
[S033]: https://techpoint.africa/news/moniepoint-2025-report/
[S034]: https://www.moniepoint.com/blog/moniepoint-announces-successful-completion-of-usdollar200-million-series-c-round-to-power-financial-inclusion
[S035]: https://nairametrics.com/2025/10/08/moniepoint-clarifies-uk-units-2024-loss-spends-2-5-million-on-bancom-acquisition/
[S036]: https://www.sec.gov/Archives/edgar/data/2103076/000119312526418812/d56487df1.htm
[S037]: https://nairametrics.com/2026/10/13/opay-earns-more-from-lending-than-payments-as-profit-hits-90-9-million/
[S038]: https://www.techcityng.com/opay-ipo-filing-nyse/
[S039]: https://www.prnewswire.com/news-releases/opay-announces-its-first-monthly-profit-with-nearly-10-million-daily-active-trading-users-302142052.html
[S040]: https://moneycentral.com.ng/exclusive/article/interswitch-navigates-fx-headwinds-moves-to-n14-7-billion-profit-after-prior-year-loss/
[S043]: https://techpoint.africa/news/flutterwave-uk-2024-financial-result/
[S044]: https://flutterwave.com/us/blog/building-for-the-long-term-2024-in-review
[S045]: https://flutterwave.com/us/blog/scaling-with-purpose-h1-2025-at-flutterwave
[S046]: https://techcrunch.com/2026/01/05/flutterwave-buys-nigerias-mono-in-rare-african-fintech-exit/
[S047]: https://www.semafor.com/article/01/20/2026/paystack-eyes-growth-beyond-payments-with-restructuring
[S048]: https://paystack.com/pricing
[S049]: https://techcabal.com/2026/01/14/paystack-becomes-a-microfinance-bank-nigeria/
[S050]: https://newtelegraphng.com/paystack-focuses-on-building-best-payments-growth-tools-for-african-businesses-akinlade/
[S051]: https://techcrunch.com/2025/06/05/profitable-african-fintech-palmpay-is-in-talks-to-raise-as-much-as-100m/
[S052]: https://businessday.ng/technology/article/palmpay-served-10-million-monthly-active-users-in-2024-nwosu/
[S053]: https://nairametrics.com/2025/05/08/palmpay-hits-15-million-daily-transactions-in-q1-2025/
[S054]: https://businessday.ng/technology/article/breaking-kuda-cuts-losses-to-5-8m-as-fintech-shifts-focus-to-profitability/
[S055]: https://www.tekedia.com/fairmoney-revenue-surges-to-n121-9-billion-in-2024-amid-shift-to-customer-deposit-funded-lending/
[S056]: https://techcabal.com/2026/01/21/chipper-cash-posts-first-quarter-without-cash-burn/
[S057]: https://www.highlandeurope.com/lemfi-has-secured-53m-in-series-b-funding-led-by-highland-europe/
[S058]: https://techpoint.africa/news/paystack-and-piggyvest-join-forces-in-brass-acquisition/
[S059]: https://techpoint.africa/news/piggyvest-2025-payouts/
[S060]: https://techpoint.africa/news/piggyvest-disburses-billions-users/
[S061]: https://doclib.ngxgroup.com/Financial_NewsDocs/43535_E-TRANZACT_INTERNATIONAL_PLC-_QUARTER_5_-_FINANCIAL_STATEMENT_FOR_2024_FINANCIAL_STATEMENTS_MARCH_2025.pdf
[S062]: https://www.tekedia.com/momo-psb-hits-2-7-million-wallets-as-growth-and-strategy-rebound-in-h1-2025/
[S063]: https://www.sec.gov/Archives/edgar/data/1756708/000175670825000005/jumia-ex991q42024.htm
[S064]: https://punchng.com/moove-exits-nigeria-transfers-n35bn-vehicles-to-customers/
[S065]: https://www.bbc.com/news/articles/c86xpv8l9y9o
[S066]: https://www.aljazeera.com/news/2026/9/11/why-is-uber-pulling-out-of-some-african-markets
[S068]: https://www.ifc.org/en/pressroom/2025/sun-king-ifc-and-stanbic-ibtc-bank-close-80-million-debt-facility-to-expand-solar-
[S070]: https://chapelhilldenham.com/d-light-and-chapel-hill-denham-close-n10-billion-in-securitised-financing-to-fund-off-grid-solar-expansion-in-nigeria/
[S073]: https://www.ecofinagency.com/insights/0809-48489-in-nigerian-bank-technology-failures-pushed-opay-and-palmpay-to-leadership-in-daily-payments
[S076]: https://businessday.ng/companies/article/zenith-uba-lead-nigerian-banks-with-trillion-naira-net-interest-income/
[S077]: https://nairametrics.com/2025/03/28/breaking-gtco-reports-record-n1-trillion-profit-after-tax-for-2024-fy/
[S078]: https://nairametrics.com/2025/03/27/zenith-bank-post-record-n1-trillion-profit-after-tax/
[S083]: https://www.thisdaylive.com/2026/04/02/cbn-33-of-37-banks-met-new-capital-requirements-raised-n4-65trn/
[S084]: https://guardian.ng/business-services/money/cbn-upgrades-licences-of-major-fintechs-mfbs-to-national-status/
[S087]: https://nairametrics.com/2024/02/04/cbn-stops-outbound-international-money-transfer-transactions-limits-inflow-payouts-to-naira/
[S088]: https://nairametrics.com/2024/06/03/cbn-clears-opay-kuda-others-to-resume-new-customer-onboarding-this-week/
[S092]: https://www.thecable.ng/banks-to-start-charging-senders-n50-stamp-duty-on-transfers-above-n10k-from-january/
[S093]: https://www.legit.ng/business-economy/industry/1628352-fg-begins-n50-electronic-transfer-levy-charges-opay-palmpay-companies-send-messages/
[S096]: https://www.sec.gov.ng/about/resources/checklists/accelerated-regulatory-incubation-program-arip-checklist-for-vasp-onboarding/
[S097]: https://techcabal.com/2026/01/16/sec-2-billion-minimum-capital-for-exchanges/
[S098]: https://www.sec.gov.ng/for-investors/keep-track-of-circulars/revised-minimum-capital-mc-for-regulated-capital-market-entities/
[S101]: https://apnews.com/article/nigeria-cryptocurrency-binance-da2f52ba457492e6a9c7733f646f5b2e
[S102]: https://www.reuters.com/world/africa/nigeria-seeks-815-bln-economic-losses-back-tax-against-binance-court-document-2025-02-19/
[S128]: https://techcabal.com/2024/12/10/cbn-fines-moniepoint-and-opay/
[S131]: https://fccpc.gov.ng/update-on-potential-anti-competitive-conduct-in-association-of-pos-operators-statement-of-setting-prices-for-services/
[S145]: https://technext24.com/news/okra-blames-shutdown-on-market-challenge/
[S146]: https://nairametrics.com/2025/10/24/fintech-startup-lidya-shuts-down-after-nine-years/
[S147]: https://techpoint.africa/insight/lydia-shuts-down/
[S153]: https://cdn.pacermonitor.com/pdfserver/D3XGTLY/199916559/Gokada_Inc__debke-24-12377__0001.0.pdf
[S154]: https://techcabal.com/2023/07/21/bundle-africa-shuts-down/
[S163]: https://www.ceicdata.com/en/nigeria/foreign-exchange-rates-annual/official-exchange-rate-period-average-local-currency-to-usd
[S164]: https://www.vanguardngr.com/2026/05/diaspora-remittances-stabilises-at-21-8bn-in-2025-amid-global-pressures/
[S165]: https://nairametrics.com/2025/12/26/nigerias-imto-inflows-drop-11-78-to-2-07-billion-in-h1-2025/
[S168]: https://techpoint.africa/insight/pos-withdrawal-charges-rise-as-agents-lament-cash-scarcity-and-rising-costs/
[S169]: https://punchng.com/palmpay-sustains-zero-fee-transfer-to-drive-financial-inclusion/
[S170]: https://thewhistler.ng/hike-in-terminal-charge-by-opay-moniepoint-is-turning-pos-business-into-unattractive-venture-operators/
[S175]: https://nairametrics.com/2026/08/13/opay-swings-to-profit-in-fy2025-as-revenue-surges-161-to-536-3-million/
