# iso27001-iam-governance

Projeto de estudo independente sobre Gestão de Identidades e Acessos (IAM) baseado nos controles públicos da ISO/IEC 27001:2022, com aplicação à ISO 27701 e LGPD.

**GitHub Pages:** `https://gilbertocrv.github.io/iso27001-iam-governance`

---

## Estrutura

```
iso27001-iam-governance/
│
├── index.html                              # Página principal — mapa de controles e ferramentas
│
├── controles/                              # Deep dives por controle ISO 27001
│   ├── 5.15.html                           # Access Control Policy ✅
│   ├── 5.16.html                           # Identity Management (em breve)
│   ├── 5.17.html                           # Authentication Information (em breve)
│   ├── 5.18.html                           # Access Rights (em breve)
│   ├── 8.2.html                            # Privileged Access Rights (em breve)
│   ├── 8.3.html                            # Information Access Restriction (em breve)
│   └── 8.5.html                            # Secure Authentication (em breve)
│
├── ferramentas/                            # Ferramentas interativas
│   ├── policy-builder.html                 # Gerador modular de rascunho de política
│   ├── sod-simulator.html                  # Simulador de conflitos de Segregação de Funções
│   └── horizon-scanning.html               # Dashboard de monitoramento regulatório e de mercado
│
├── policies/                               # Documentos de referência
│   ├── Access_Control_Policy.html          # Política renderizada (acessível via GitHub Pages)
│   └── Access_Control_Policy.md            # Fonte Markdown (download via GitHub)
│
├── data/
│   └── scanning.json                       # Entradas do Horizon Scanning (manual + RSS automático)
│
├── .github/
│   ├── workflows/
│   │   └── scanning.yml                    # GitHub Actions: atualiza feeds RSS diariamente
│   └── scripts/
│       └── fetch_feeds.py                  # Script de coleta e merge dos feeds
│
├── _config.yml                             # Configuração GitHub Pages
└── README.md                               # Este arquivo
```

---

## Status do conteúdo

### Deep dives — Controles ISO 27001:2022

| Arquivo | Controle | Título | Status |
|---|---|---|---|
| `controles/5.15.html` | 5.15 | Access Control Policy | ✅ Publicado |
| `controles/5.16.html` | 5.16 | Identity Management | 🔜 Em breve |
| `controles/5.17.html` | 5.17 | Authentication Information | 🔜 Em breve |
| `controles/5.18.html` | 5.18 | Access Rights | 🔜 Em breve |
| `controles/8.2.html` | 8.2 | Privileged Access Rights | 🔜 Em breve |
| `controles/8.3.html` | 8.3 | Information Access Restriction | 🔜 Em breve |
| `controles/8.5.html` | 8.5 | Secure Authentication | 🔜 Em breve |

### Ferramentas

| Arquivo | Descrição | Status |
|---|---|---|
| `ferramentas/policy-builder.html` | Gerador modular de política de acesso | ✅ Publicado |
| `ferramentas/sod-simulator.html` | Simulador de conflitos SoD | ✅ Publicado |
| `ferramentas/horizon-scanning.html` | Dashboard de monitoramento regulatório | ✅ Publicado |

### Documentos

| Arquivo | Descrição | Status |
|---|---|---|
| `policies/Access_Control_Policy.html` | Access Control Policy — visualização web | ✅ Publicado |
| `policies/Access_Control_Policy.md` | Access Control Policy — fonte Markdown | ✅ Publicado |

---

## Horizon Scanning — como funciona

O dashboard em `ferramentas/horizon-scanning.html` lê o arquivo `data/scanning.json` e exibe as entradas com filtros por categoria e status.

**Fontes automáticas (via GitHub Actions — diariamente às 08h UTC):**
- NIST — `nist.gov/news-events/cybersecurity/rss.xml`
- OWASP — `owasp.org/blog/feed.xml`
- Microsoft Security — `microsoft.com/en-us/security/blog/feed/`
- AWS Security — `aws.amazon.com/blogs/security/feed/`
- Google Cloud Security — `cloudblog.withgoogle.com/products/identity-security/rss/`

**Fontes manuais (editar `data/scanning.json` diretamente):**
- ANPD, TCU, TCM, Tribunais de Contas Estaduais
- ISO, CIS Controls

**Para adicionar uma entrada manual**, edite `data/scanning.json` seguindo o modelo:

```json
{
  "id": "anpd-002",
  "date": "2026-03-12",
  "source": "ANPD",
  "category": "Regulação",
  "title": "Título da publicação",
  "url": "https://...",
  "impact": ["Privacidade", "Acesso"],
  "action": "Ação sugerida nos controles",
  "status": "novo",
  "notes": "Entrada manual"
}
```

Valores válidos para `status`: `novo` · `em-analise` · `monitorando` · `incorporado`
Valores válidos para `impact`: `IAM` · `GRC` · `Acesso` · `Privacidade`
Valores válidos para `category`: `Regulação` · `Framework` · `Mercado`

---

## Como publicar no GitHub Pages

1. Faça upload de todos os arquivos para o repositório `iso27001-iam-governance`
2. Vá em **Settings → Pages**
3. Em *Source*, selecione **Branch: main** / pasta **/ (root)**
4. Clique em **Save**
5. Aguarde ~1 minuto — o site estará disponível em `https://gilbertocrv.github.io/iso27001-iam-governance`

**Para ativar o GitHub Actions (Horizon Scanning automático):**
Settings → Actions → General → Allow all actions → Save

---

*Conteúdo educacional. Baseado em normas públicas. Não contém informações corporativas.*
*Autor: Gilberto Gonçalves · [github.com/gilbertocrv](https://github.com/gilbertocrv)*
