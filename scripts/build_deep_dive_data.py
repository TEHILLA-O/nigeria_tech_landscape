"""Write the structured CSVs behind docs/deep_dive.

Usage: python3 scripts/build_deep_dive_data.py
Values are copied from the deep dive Markdown, which cites each source.
Blank cells mean not disclosed. Rows marked Estimate=Yes are our arithmetic.
"""
import csv
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
URL = {s[0]: s[4] for s in __import__("deep_dive_sources").SOURCES}


def urls(ids):
    return " ; ".join(URL[i] for i in ids.split())


def write(name, header, rows):
    with open(DATA / name, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for r in rows:
            r = list(r)
            r[-1] = urls(r[-1])
            w.writerow(r)
    print(name, len(rows))


# value chain edges: source, target, relationship, layer, source ids
EDGES = [
    ("CBN", "NIBSS", "supervises and co-owns; NIP settles on CBN RTGS", "rails", "S007 S009"),
    ("CBN", "Deposit money banks", "licenses and sets capital", "regulation", "S082"),
    ("CBN", "Wallets and digital MFBs", "licenses MMO and MFB; national upgrades 2026", "regulation", "S084"),
    ("CBN", "Switches and processors", "licenses switching and processing", "regulation", "S079"),
    ("CBN", "Payment service banks", "licenses PSBs", "regulation", "S081"),
    ("CBN", "IMTOs and remittance firms", "licenses IMTOs; naira-only payout", "regulation", "S086 S087"),
    ("CBN", "Agents and POS", "agent banking caps and geofencing", "regulation", "S114 S115"),
    ("NIBSS", "Deposit money banks", "NIP clearing, deferred net settlement", "rails", "S007"),
    ("NIBSS", "Wallets and digital MFBs", "NIP access for transfers", "rails", "S001 S004"),
    ("NIBSS", "KYC vendors", "BVN verification", "identity", "S018"),
    ("NIMC", "KYC vendors", "NIN verification", "identity", "S019 S020"),
    ("KYC vendors", "Wallets and digital MFBs", "onboarding checks", "identity", "S021"),
    ("KYC vendors", "Lenders and BNPL", "onboarding checks", "identity", "S021"),
    ("Deposit money banks", "Payment gateways", "sponsor bank and settlement accounts", "payments", "S048"),
    ("Deposit money banks", "Card schemes", "card issuing", "payments", "S016"),
    ("Card schemes", "Switches and processors", "authorisation and switching", "payments", "S040"),
    ("Switches and processors", "Payment gateways", "processing", "payments", "S040"),
    ("Payment gateways", "Merchants and real economy", "online checkout, transfers, terminals", "payments", "S048"),
    ("Wallets and digital MFBs", "Agents and POS", "terminals, float, settlement", "distribution", "S006 S033"),
    ("Agents and POS", "Merchants and real economy", "cash in and cash out for a fee", "distribution", "S168"),
    ("Wallets and digital MFBs", "Lenders and BNPL", "credit funded from own MFB balance sheet", "credit", "S037 S033"),
    ("Credit bureaus", "Lenders and BNPL", "credit reports", "credit", "S022"),
    ("FCCPC", "Lenders and BNPL", "registers consumer lending apps", "regulation", "S111"),
    ("NCC", "Telcos", "licenses and sets USSD pricing", "regulation", "S027"),
    ("Telcos", "Deposit money banks", "USSD and SMS channels", "channels", "S029 S030"),
    ("Telcos", "Wallets and digital MFBs", "USSD and SMS channels", "channels", "S027"),
    ("Telcos", "Payment service banks", "parent companies of PSBs", "channels", "S062"),
    ("IMTOs and remittance firms", "Deposit money banks", "naira payout", "cross-border", "S087"),
    ("IMTOs and remittance firms", "Wallets and digital MFBs", "naira payout", "cross-border", "S035 S057"),
    ("SEC Nigeria", "Crypto VASPs", "regulates under ISA 2025; ARIP; capital rules", "regulation", "S094 S096 S098"),
    ("SEC Nigeria", "Savings and wealth apps", "regulates fund managers", "regulation", "S098"),
    ("Crypto VASPs", "Deposit money banks", "designated settlement accounts", "crypto", "S099 S100"),
    ("Savings and wealth apps", "Deposit money banks", "customer funds held and invested", "savings", "S059"),
    ("NAICOM", "Insurers and insurtech", "licenses and sets capital", "regulation", "S121"),
    ("NDPC", "Wallets and digital MFBs", "data protection enforcement", "regulation", "S109"),
    ("Merchants and real economy", "Lenders and BNPL", "borrow working capital", "credit", "S033"),
    ("Switches and processors", "FIRS", "e-invoicing access point", "government", "S017"),
    ("Ride-hailing platforms", "Mobility finance", "driver earnings fund vehicle repayments", "real economy", "S064 S065"),
    ("Wallets and digital MFBs", "PAYG solar", "mobile money repayments", "real economy", "S068"),
]
write("value_chain_edges.csv", ["Source", "Target", "Relationship", "Layer", "Source_URLs"], EDGES)

POOLS = [
    (1, "Bank net interest income", "Five tier one banks: NGN 6.98tn (2024)", 6980000000000, "", "2024", "High", "High", "No", "Sum of five banks (our calc)", "S076 S077 S078"),
    (2, "Fintech consumer and SME lending", "OPay loan income USD 236.1m (H1 2026); Moniepoint NGN 1tn+ disbursed (2025); FairMoney revenue NGN 121.9bn (2024)", "", 236100000, "H1 2026", "Medium", "High for OPay, medium for others", "No", "Credit losses about 50% of OPay loan income (our calc)", "S037 S033 S055"),
    (3, "Payment and transaction fees", "OPay USD 130.6m (H1 2026); Interswitch core processing about NGN 53.6bn (FY to Mar 2025); eTranzact NGN 29.9bn (2024)", 53600000000, 130600000, "2024 to 2026", "Low to medium", "High for filers, low for Paystack, Flutterwave, Moniepoint", "Yes", "Interswitch line is 39% of NGN 137.5bn (our calc)", "S037 S040 S061"),
    (4, "Card scheme fees", "Verve about NGN 44.0bn (FY to Mar 2025)", 44000000000, "", "FY to Mar 2025", "Medium to high", "Medium", "Yes", "32% of Interswitch revenue (our calc)", "S040 S016"),
    (5, "Float and treasury income", "OPay short-term investment interest USD 50.6m (H1 2026)", "", 50600000, "H1 2026", "High", "Medium", "No", "Only OPay discloses", "S036 S037"),
    (6, "Government and enterprise infrastructure", "Interswitch non-transaction revenue NGN 34.3bn (FY to Mar 2025)", 34300000000, "", "FY to Mar 2025", "Medium to high", "Medium", "No", "Includes FIRS e-invoicing and pensions", "S040 S017"),
    (7, "Insurance premiums", "Gross written premiums NGN 1.5587tn (2024)", 1558700000000, "", "2024", "Varies", "High", "No", "Whole industry", "S071"),
    (8, "Cross-border FX spread and fees", "Revenue not disclosed; flows about USD 21.8bn formal remittances (2025)", "", "", "2025", "Medium", "Low", "No", "Flow, not revenue", "S164 S057 S087"),
    (9, "Agent cash-out fees", "NGN 200 to 300 per NGN 10,000 (2025); pool not disclosed", "", "", "2025", "High per transaction", "Low", "No", "2% to 3% effective (our calc)", "S168 S114"),
    (10, "Telco USSD session fees", "NGN 6.98 per session (2025); pool not disclosed", "", "", "2025", "Medium", "Medium", "No", "Arrears of about NGN 180bn by 2025", "S027 S030"),
    (11, "Crypto trading and on-ramps", "Revenue not disclosed; USD 92.1bn value received (Jul 2024 to Jun 2025)", "", "", "2024 to 2025", "Unknown", "Low", "No", "Flow, not revenue", "S072"),
    (12, "Merchant software and SaaS", "Not disclosed", "", "", "2025", "Potentially high", "Low", "No", "Often bundled free", "S033"),
]
write("revenue_pools.csv", ["Rank", "Pool", "Disclosed_Size_Text", "Size_NGN", "Size_USD", "As_Of", "Margin", "Certainty", "Estimate", "Notes", "Source_URLs"], POOLS)

LOSSES = [
    (1, "FX devaluation", "MTN Nigeria net FX loss (2024); ten listed firms FX losses (2024)", 925400000000, 602900000, "2024", "Accounting loss", "No", "USD at NGN 1,535 (our calc); ten firms NGN 2.17tn", "Naira debt matched to naira revenue; dollar revenue lines", "S074 S075 S006"),
    (2, "Credit losses", "OPay credit loss expense H1 2026; FairMoney impairments 2024; bank NPL ratio 5.76% Jun 2025", 59400000000, 118400000, "2024 to 2026", "Realised and expected", "No", "NGN is FairMoney; USD is OPay", "Cash-flow underwriting; compliant collections; GSI", "S037 S055 S156"),
    (3, "Power and diesel", "Manufacturers alternative energy spend 2024", 1110000000000, 723100000, "2024", "Operating cost", "No", "Manufacturing proxy; no tech sector figure", "PAYG solar financed in naira", "S158"),
    (4, "Failed startups capital", "Amounts raised by eight failed startups", "", 173350000, "2023 to 2025", "Capital lost or returned", "Yes", "Lower bound sum of raises (our calc)", "Governance, naira-cost matching, partner diversification", "S143 S144 S145 S147 S155 S148 S150 S149"),
    (5, "Regulatory fines", "Meta USD 220m; CBN, NDPC naira fines", 19672000000, 220000000, "2024 to 2025", "Fines imposed", "Yes", "Naira sum includes fines OPay denies (our calc)", "NDPA consent tooling; AML case management", "S105 S106 S129 S130 S128 S107 S108"),
    (6, "USSD debt", "Banks' USSD arrears to telcos, revised", 180000000000, 118400000, "2024 to 2025", "Disputed receivable", "No", "Telcos first claimed NGN 250bn; 95% recovered", "End-user billing now in place", "S029 S030"),
    (7, "Payment fraud", "NIBSS reported losses 2024 (2025: NGN 25.85bn)", 52260000000, 34000000, "2024", "Cash lost", "No", "NGN 31.1bn of 2024 was one incident", "Insider monitoring; cross-institution reporting", "S132 S133 S134"),
    (8, "Processor operational losses", "Interswitch chargeback operating loss; Flutterwave 2023 glitch exposure", 11450000000, "", "2023 to 2024", "Operating loss and exposure", "No", "Flutterwave exposure NGN 21.2bn, NGN 7.2bn preserved", "Real-time reconciliation; chargeback evidence", "S041 S042 S138 S139 S137"),
    (9, "Mobility collapse", "Moove vehicles transferred to drivers on exit", 35000000000, 25300000, "2026", "Asset write-down", "Yes", "Company-stated transfer value (our USD calc)", "Multi-platform driver finance", "S064 S065"),
    (10, "POS hardware treadmill", "Replacement value of deployed POS fleet", 501500000000, 330000000, "2025", "Capex", "Yes", "Upper bound: 5.90m x NGN 85,000; lower NGN 126.85bn (our calc)", "Leasing, refurbishment, redeployment", "S005 S006"),
    (11, "Cybersecurity breaches", "Patricia hack", "", 2000000, "2022", "Cash lost", "No", "Police linked NGN 607m diverted", "Hot wallet controls", "S141 S142"),
    (12, "Funding drought", "Fall in Nigerian startup funding 2024 to 2025", "", 67000000, "2025", "Capital not raised", "No", "USD 410m to 343m (Africa: The Big Deal)", "Revenue-first models", "S160 S173"),
]
write("losses.csv", ["Rank", "Hole", "Measure", "Size_NGN", "Size_USD", "As_Of", "Type", "Estimate", "Notes", "Possible_Fix", "Source_URLs"], LOSSES)

TIMELINE = [
    ("2021-02-05", "CBN", "Banks barred from serving crypto exchanges", "Crypto moves to P2P", "S100"),
    ("2021", "CBN", "Consolidated payment licence categories and capital", "Capital floors still in use", "S079"),
    ("2021-10", "CBN", "eNaira launched", "Low adoption", "S014"),
    ("2023-01-26", "CBN; NIBSS", "AfriGO domestic card scheme launched", "Scheme competition", "S011"),
    ("2023-02", "CBN", "Naira redesign cash crunch", "POS fees spike; failed transfers", "S166 S167"),
    ("2023-03", "CBN", "Open banking operational guidelines", "Not live as of Oct 2025", "S024 S025"),
    ("2023-06-16", "CBN", "FX windows unified", "Sharp devaluation", "S162"),
    ("2023-12-22", "CBN", "Crypto bank ban reversed for SEC-licensed VASPs", "Licensed exchange path", "S099"),
    ("2024-01-31", "CBN", "Revised IMTO guidelines", "Naira-only payouts; USD 1m capital", "S086 S087"),
    ("2024-03-01", "CBN", "Accounts without BVN or NIN restricted", "KYC clean-up", "S118"),
    ("2024-03-28", "CBN", "Bank recapitalisation circular", "NGN 4.65tn raised by 2026", "S082 S083"),
    ("2024-04", "CBN", "Onboarding pause on OPay, PalmPay, Kuda, Moniepoint, Paga", "Lifted early June 2024", "S088 S089"),
    ("2024-05", "CBN; FG", "Cybersecurity levy issued then suspended", "Policy whiplash", "S090 S091"),
    ("2024-05", "NDIC", "Deposit insurance raised", "NGN 5m banks and MMOs; NGN 2m MFBs and PSBs", "S120"),
    ("2024-08", "NDPC", "Fidelity Bank fined NGN 555.8m", "NDPA enforcement", "S107"),
    ("2024-09-14", "NCC", "Final NIN-SIM linkage deadline", "Unlinked lines barred", "S119"),
    ("2024-10", "FG", "Binance executive released", "Tax case continues", "S101"),
    ("2024-12", "FIRS", "Wallets begin deducting NGN 50 EMTL", "Higher cost on inflows", "S093"),
    ("2025-02", "FIRS", "USD 81.5bn suit against Binance", "Unresolved", "S102"),
    ("2025-03", "NCC", "USSD determination: NGN 6.98 per session", "Billing moves to airtime", "S027 S028"),
    ("2025-04-25", "FCCPC", "Tribunal upholds USD 220m Meta fine", "Largest tech fine", "S105"),
    ("2025", "National Assembly", "Investments and Securities Act 2025", "SEC powers over VASPs", "S094"),
    ("2025-07", "NDPC", "Multichoice fined NGN 766.2m", "NDPA enforcement", "S108"),
    ("2025-07-21", "FCCPC", "DEON digital lending regulations in force", "Lenders must register", "S111"),
    ("2025-07-31", "NAICOM", "NIIRA 2025 capital levels take effect", "Insurer recapitalisation", "S121"),
    ("2025-10", "CBN", "Agent banking guidelines: caps and geofencing", "Agent economics reset", "S114 S115 S116"),
    ("2025-10-31", "CBN", "ISO 20022 compliance deadline", "Rail upgrade", "S008"),
    ("2026-01-01", "CBN", "New cash policy", "Deposit limits removed; 3% and 5% excess withdrawal fees", "S117"),
    ("2026-01-01", "Tax reform", "NGN 50 stamp duty paid by sender", "Cost shifts to payer", "S092"),
    ("2026-01-05", "FCCPC", "Digital lending compliance deadline", "Enforcement", "S112 S113"),
    ("2026-01-16", "SEC", "New minimum capital for capital market operators", "NGN 2bn for crypto exchanges", "S097 S098"),
    ("2026-01-27", "CBN", "Fintech MFBs upgraded to national licences", "Fintechs regulated as banks", "S084"),
    ("2026-03-31", "CBN", "Bank recapitalisation deadline", "33 of 37 banks compliant", "S083"),
    ("2026-04-01", "CBN", "Agent location and exclusivity rules apply", "Agents tied to one place", "S115"),
]
write("regulatory_timeline.csv", ["Date", "Regulator", "Event", "Effect", "Source_URLs"], TIMELINE)
