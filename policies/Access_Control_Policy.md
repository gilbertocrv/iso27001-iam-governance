---
title: "Da Arquitetura ao Controle: Access Control Policy na ISO/IEC 27001"
series: "ISO 27001 IAM Governance"
episode: 1
date: 2025
controls: ["5.15", "5.18"]
document: Access Control Policy
---

# Da Arquitetura ao Controle: Access Control Policy

> **Série:** ISO 27001 IAM Governance · **Episódio 1 de 7**  
> **Controles:** 5.15 – Access Control · 5.18 – Access Rights  
> **Artefato:** [`Access_Control_Policy.md`](../01_policies/Access_Control_Policy.md)

---

## Contexto da série

Na série anterior, explorei como a ISO/IEC 27001 estrutura os controles de IAM dentro de um SGSI e como eles formam uma cadeia lógica:

```
Política → Identidade → Credencial → Permissão → Privilégio → Informação → Autenticação
```

Esta série avança um passo: mostra como esses controles se materializam em **documentos, processos e evidências** utilizados na governança e nas auditorias de segurança da informação.

---

## O documento raiz: Access Control Policy

O primeiro artefato da estrutura documental de IAM é a **Access Control Policy**.

Ela está diretamente relacionada ao controle **5.15 – Access Control**, que exige que a organização estabeleça regras formais para controle de acesso à informação e aos sistemas.

### Por que ela é o documento raiz?

Sem essa política, os processos de IAM surgem de forma fragmentada — dependentes de ferramentas ou fluxos operacionais sem base normativa comum.

É comum encontrar organizações com:
- Soluções de IGA implantadas
- Workflows de aprovação configurados
- Automações de provisionamento ativas

...mas sem nenhum documento que formalize *por que* e *como* esses controles existem.

Quando a política existe, ela funciona como fundação normativa para todos os procedimentos derivados.

---

## Estrutura típica da Access Control Policy

| Seção | Conteúdo |
|---|---|
| Objetivo | Propósito e justificativa do documento |
| Escopo | Usuários, sistemas e ambientes cobertos |
| Princípios | Least privilege, need-to-know, SoD, rastreabilidade |
| Responsabilidades | Information Owner, gestor, usuário, TI, auditoria |
| Governança de concessão | Fluxo: solicitação → aprovação → implementação → registro |
| Revisão de acessos | Frequências mínimas por tipo de acesso |
| Referências normativas | ISO 27001:2022, ISO 27701, LGPD |

---

## Frequências de revisão (controle 5.18)

| Tipo de acesso | Frequência mínima |
|---|---|
| Acessos comuns | Semestral |
| Acessos privilegiados | Trimestral |
| Acessos a dados pessoais (LGPD) | Trimestral |
| Contas de serviço | Semestral |

---

## Controles ISO 27001:2022 relacionados

```
5.15 – Access Control          → define os princípios e regras
5.18 – Access Rights           → governa concessão, revisão e revogação
```

A política opera no cruzamento dos dois: estabelece os princípios (5.15) e define a governança de direitos (5.18).

---

## Procedimentos derivados desta política

A partir da Access Control Policy surgem os procedimentos operacionais que detalham como as regras são aplicadas:

1. [`Identity_Lifecycle_Procedure.md`](../02_procedures/Identity_Lifecycle_Procedure.md) — 5.16
2. [`Authentication_Standard.md`](../02_procedures/Authentication_Standard.md) — 5.17
3. [`Access_Provisioning_Procedure.md`](../02_procedures/Access_Provisioning_Procedure.md) — 5.18
4. [`Privileged_Access_Procedure.md`](../02_procedures/Privileged_Access_Procedure.md) — 8.2
5. [`Access_Review_Procedure.md`](../02_procedures/Access_Review_Procedure.md) — 5.18 · 8.2

---

## Estrutura do repositório

```
iso27001-iam-governance-templates/
├── 00_articles/
│   └── 01-access-control-policy.md        ← este arquivo
├── 01_policies/
│   └── Access_Control_Policy.md
├── 02_procedures/
│   ├── Identity_Lifecycle_Procedure.md
│   ├── Authentication_Standard.md
│   ├── Access_Provisioning_Procedure.md
│   ├── Privileged_Access_Procedure.md
│   └── Access_Review_Procedure.md
└── 03_governance_artifacts/
    ├── SoD_Matrix.xlsx
    ├── Access_Review_Register.xlsx
    └── Privileged_Access_Register.xlsx
```

---

## Próximo episódio

**Episódio 2:** Identity Lifecycle Management Procedure — como identidades são criadas, movidas e desativadas (Joiner / Mover / Leaver) — controle 5.16.

---

*Conteúdo educacional. Não contém informações corporativas reais.*  
*Autor: Gilberto Gonçalves · [LinkedIn](https://linkedin.com) · [GitHub](https://github.com)*
