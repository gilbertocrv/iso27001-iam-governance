# iso27001-iam-governance

Projeto de estudo independente sobre Gestão de Identidades e Acessos (IAM) baseado nos controles públicos da ISO/IEC 27001:2022, com aplicação à ISO 27701 e LGPD.

**GitHub Pages:** `https://gilbertocrv.github.io/iso27001-iam-governance`

---

## Estrutura

```
iso27001-iam-governance/
│
├── index.html                                      # Página principal — mapa de controles e ferramentas
│
├── controles/                                      # Deep dives por controle ISO 27001
│   ├── 5.15.html                                   # Access Control Policy ✅
│   ├── 5.16.html                                   # Identity Management ✅
│   ├── 5.17.html                                   # Authentication Information ✅
│   ├── 5.18.html                                   # Access Rights ✅
│   ├── 8.2.html                                    # Privileged Access Rights ✅
│   ├── 8.3.html                                    # Information Access Restriction (em breve)
│   └── 8.5.html                                    # Secure Authentication (em breve)
│
├── ferramentas/                                    # Ferramentas interativas e artefatos operacionais
│   ├── policy-builder.html                         # Gerador modular de rascunho de política ✅
│   ├── sod-simulator.html                          # Simulador de conflitos de Segregação de Funções ✅
│   ├── horizon-scanning.html                       # Dashboard de monitoramento regulatório ✅
│   ├── authentication-standard.html                # Padrão técnico 5.17 + 8.5 — checklist interativo ✅
│   ├── authentication-standard-builder.html        # Gerador de Authentication Standard com score ✅
│   ├── access-provisioning.html                    # Procedimento de provisionamento 5.18 — RACI + SLAs ✅
│   └── privileged-access-standard.html             # Padrão PAM 8.2 — tiers + vault + checklist ✅
│
├── policies/                                       # Documentos de referência
│   ├── Access_Control_Policy.html                  # Política renderizada (acessível via GitHub Pages)
│   └── Access_Control_Policy.md                    # Fonte Markdown (download via GitHub)
│
├── data/
│   └── scanning.json                               # Entradas do Horizon Scanning (manual + RSS automático)
│
├── .github/
│   ├── workflows/
│   │   └── scanning.yml                            # GitHub Actions: atualiza feeds RSS diariamente
│   └── scripts/
│       └── fetch_feeds.py                          # Script de coleta e merge dos feeds
│
├── _config.yml                                     # Configuração GitHub Pages
└── README.md                                       # Este arquivo
```

---

## Status do conteúdo

### Deep dives — Controles ISO 27001:2022

| Arquivo | Controle | Título | Status |
|---|---|---|---|
| `controles/5.15.html` | 5.15 | Access Control Policy | ✅ Publicado |
| `controles/5.16.html` | 5.16 | Identity Management | ✅ Publicado |
| `controles/5.17.html` | 5.17 | Authentication Information | ✅ Publicado |
| `controles/5.18.html` | 5.18 | Access Rights | ✅ Publicado |
| `controles/8.2.html` | 8.2 | Privileged Access Rights | ✅ Publicado |
| `controles/8.3.html` | 8.3 | Information Access Restriction | 🔜 Em breve |
| `controles/8.5.html` | 8.5 | Secure Authentication | 🔜 Em breve |

### Ferramentas e artefatos operacionais

| Arquivo | Descrição | Controles | Status |
|---|---|---|---|
| `ferramentas/policy-builder.html` | Gerador modular de política de acesso | 5.15 · 5.18 | ✅ Publicado |
| `ferramentas/sod-simulator.html` | Simulador de conflitos SoD | 5.18 · 8.2 | ✅ Publicado |
| `ferramentas/horizon-scanning.html` | Dashboard de monitoramento regulatório e de mercado | — | ✅ Publicado |
| `ferramentas/authentication-standard.html` | Padrão técnico de autenticação — parâmetros, MFA, vault e checklist de auditoria | 5.17 · 8.5 | ✅ Publicado |
| `ferramentas/authentication-standard-builder.html` | Gerador interativo de Authentication Standard com score de aderência e download em Markdown | 5.17 · 8.5 | ✅ Publicado |
| `ferramentas/access-provisioning.html` | Procedimento de provisionamento — fluxo de aprovação, RACI, SLAs e checklist | 5.18 | ✅ Publicado |
| `ferramentas/privileged-access-standard.html` | Padrão PAM — classificação por tier, controles obrigatórios, vault e checklist | 8.2 | ✅ Publicado |

### Documentos de política

| Arquivo | Descrição | Status |
|---|---|---|
| `policies/Access_Control_Policy.html` | Access Control Policy — visualização web | ✅ Publicado |
| `policies/Access_Control_Policy.md` | Access Control Policy — fonte Markdown | ✅ Publicado |

---

## Arquitetura de controles

A série segue a lógica de confiança progressiva — cada camada depende da anterior:

```
5.15 Governança → 5.16 Identidade → 5.17 Credencial → 5.18 Autorização → 8.2 Privilégio → 8.5 Autenticação
```

Cada controle publicado inclui: conceito central, ciclo de vida, avaliação de maturidade (N0–N4), riscos associados, evidências para auditoria e artefatos relacionados.

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

## Próximos passos

| Prioridade | Item | Tipo |
|---|---|---|
| Alta | `controles/8.3.html` — Information Access Restriction | Deep dive |
| Alta | `controles/8.5.html` — Secure Authentication | Deep dive |
| Média | `ferramentas/access-recertification.html` — Procedimento de revisão periódica | Artefato |
| Média | `ferramentas/sod-matrix.html` — Matriz SoD completa exportável | Artefato |
| Baixa | `policies/Identity_Lifecycle_Procedure.html` — Procedimento JML renderizado | Documento |

---

*Conteúdo educacional. Baseado em normas públicas. Não contém informações corporativas.*  
*Autor: Gilberto Gonçalves · [github.com/gilbertocrv](https://github.com/gilbertocrv)*
