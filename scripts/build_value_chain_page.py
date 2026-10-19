"""Render data/value_chain_edges.csv as docs/dashboard/value_chain.html.

Usage: python3 scripts/build_value_chain_page.py
The page draws the graph with Mermaid (loaded from jsDelivr) and lists
every edge with its sources. No build step or server needed.
"""
import csv
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
rows = list(csv.DictReader(open(ROOT / "data" / "value_chain_edges.csv")))

ids = {}
def node(name):
    if name not in ids:
        ids[name] = "n" + str(len(ids))
    return ids[name]

lines = ["graph LR"]
for r in rows:
    a, b = node(r["Source"]), node(r["Target"])
    label = re.sub(r"[^A-Za-z0-9 ,.]", " ", r["Relationship"])[:40].strip()
    lines.append(f'  {a}["{r["Source"]}"] -->|{label}| {b}["{r["Target"]}"]')
graph = "\n".join(lines)

trs = []
for r in rows:
    links = " ".join(f'<a href="{html.escape(u.strip())}">src</a>' for u in r["Source_URLs"].split(";") if u.strip())
    trs.append(f"<tr><td>{html.escape(r['Source'])}</td><td>{html.escape(r['Target'])}</td><td>{html.escape(r['Relationship'])}</td><td>{html.escape(r['Layer'])}</td><td>{links}</td></tr>")

page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Nigeria tech landscape: value chain graph</title>
<style>
body {{ margin:0; font-family: ui-sans-serif, system-ui, sans-serif; background:#0b1220; color:#e8eefc; }}
header, main, footer {{ padding:16px 24px; }}
p {{ color:#9aa8c7; max-width:75ch; line-height:1.45; }}
a {{ color:#93c5fd; }}
.graph {{ background:#fff; border-radius:10px; padding:12px; overflow:auto; }}
table {{ width:100%; border-collapse:collapse; font-size:.9rem; margin-top:16px; }}
th, td {{ text-align:left; padding:8px; border-bottom:1px solid #243049; }}
th {{ color:#9aa8c7; }}
</style></head><body>
<header><h1>Value chain: who depends on whom</h1>
<p>Generated from <code>data/value_chain_edges.csv</code> ({len(rows)} edges). Each edge links to the sources behind it. Read the full analysis in <a href="../deep_dive/value_chain.md">docs/deep_dive/value_chain.md</a>. Back to the <a href="index.html">ranked dashboard</a>.</p></header>
<main><div class="graph"><pre class="mermaid">
{html.escape(graph)}
</pre></div>
<table><thead><tr><th>Source</th><th>Target</th><th>Relationship</th><th>Layer</th><th>Sources</th></tr></thead>
<tbody>
{chr(10).join(trs)}
</tbody></table></main>
<footer>Built by scripts/build_value_chain_page.py. Blanks over guesses.</footer>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs";
mermaid.initialize({{ startOnLoad: true }});
</script>
</body></html>
"""
(ROOT / "docs" / "dashboard" / "value_chain.html").write_text(page)
print("ok", len(rows), "edges")
