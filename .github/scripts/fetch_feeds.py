"""
fetch_feeds.py
Busca entradas novas dos feeds RSS e merge com data/scanning.json.
Entradas manuais (notes = "Entrada manual") nunca são removidas.
"""

import json, hashlib, datetime, feedparser, re
from pathlib import Path

FEEDS = [
    {
        "source": "NIST",
        "category": "Framework",
        "url": "https://www.nist.gov/news-events/cybersecurity/rss.xml",
        "impact": ["GRC", "IAM"],
        "action": "Avaliar alinhamento com controles ISO 27001",
    },
    {
        "source": "OWASP",
        "category": "Framework",
        "url": "https://owasp.org/blog/feed.xml",
        "impact": ["Acesso", "IAM"],
        "action": "Verificar impacto em controles de acesso",
    },
    {
        "source": "Microsoft Security",
        "category": "Mercado",
        "url": "https://www.microsoft.com/en-us/security/blog/feed/",
        "impact": ["IAM", "Acesso"],
        "action": "Monitorar impacto em procedimentos de provisionamento",
    },
    {
        "source": "AWS Security",
        "category": "Mercado",
        "url": "https://aws.amazon.com/blogs/security/feed/",
        "impact": ["IAM", "GRC"],
        "action": "Avaliar relevância para controles de acesso",
    },
    {
        "source": "Google Cloud Security",
        "category": "Mercado",
        "url": "https://cloudblog.withgoogle.com/products/identity-security/rss/",
        "impact": ["IAM", "Acesso"],
        "action": "Referência para controles de autenticação",
    },
]

KEYWORDS_IAM = [
    "identity", "access", "iam", "authentication", "authorization",
    "privilege", "sso", "mfa", "zero trust", "acesso", "identidade",
    "autenticação", "privilegiado", "provisioning", "permission",
    "credential", "password", "oauth", "saml", "ldap", "active directory",
]

DATA_FILE = Path("data/scanning.json")
MAX_ENTRIES_PER_FEED = 10
MAX_AGE_DAYS = 90


def make_id(source, url):
    return hashlib.md5(f"{source}::{url}".encode()).hexdigest()[:12]


def is_relevant(entry):
    text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
    return any(kw in text for kw in KEYWORDS_IAM)


def parse_date(entry):
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        d = datetime.datetime(*entry.published_parsed[:3])
        return d.strftime("%Y-%m-%d")
    return datetime.date.today().strftime("%Y-%m-%d")


def load_existing():
    if DATA_FILE.exists():
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    return {"updated": "", "entries": []}


def save(data):
    data["updated"] = datetime.date.today().strftime("%Y-%m-%d")
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def fetch_feed(feed_cfg):
    print(f"  → {feed_cfg['source']}: {feed_cfg['url']}")
    try:
        parsed = feedparser.parse(feed_cfg["url"])
        new_entries = []
        cutoff = datetime.date.today() - datetime.timedelta(days=MAX_AGE_DAYS)
        for item in parsed.entries[:MAX_ENTRIES_PER_FEED]:
            if not is_relevant(item):
                continue
            date_str = parse_date(item)
            if datetime.date.fromisoformat(date_str) < cutoff:
                continue
            entry = {
                "id": make_id(feed_cfg["source"], item.get("link", item.get("id", ""))),
                "date": date_str,
                "source": feed_cfg["source"],
                "category": feed_cfg["category"],
                "title": re.sub(r"<[^>]+>", "", item.get("title", "")).strip(),
                "url": item.get("link", ""),
                "impact": feed_cfg["impact"],
                "action": feed_cfg["action"],
                "status": "novo",
                "notes": "Via RSS",
            }
            new_entries.append(entry)
        print(f"     {len(new_entries)} entradas relevantes encontradas")
        return new_entries
    except Exception as e:
        print(f"     ERRO: {e}")
        return []


def main():
    data = load_existing()
    existing_ids = {e["id"] for e in data["entries"]}
    added = 0

    for feed_cfg in FEEDS:
        new_entries = fetch_feed(feed_cfg)
        for entry in new_entries:
            if entry["id"] not in existing_ids:
                data["entries"].append(entry)
                existing_ids.add(entry["id"])
                added += 1

    data["entries"].sort(key=lambda e: e["date"], reverse=True)
    save(data)
    print(f"\nConcluído: {added} entradas novas adicionadas. Total: {len(data['entries'])}")


if __name__ == "__main__":
    main()
