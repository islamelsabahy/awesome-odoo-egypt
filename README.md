# Awesome Odoo Egypt

**EN** — A short, honest, curated list of resources for running Odoo in Egypt: official Odoo localization docs, the Egyptian Tax Authority (ETA) e-invoicing / e-receipt SDK, community code, and implementation material for real estate companies. Every link below was opened on **2026-10-12** unless it is marked otherwise; items I could not fully verify are marked.

**AR** — قائمة مختصرة وموثوقة لمصادر تشغيل Odoo في مصر: توثيق Odoo الرسمي للتوطين المصري، وبوابة مطوري الفاتورة الإلكترونية والإيصال الإلكتروني من مصلحة الضرائب (ETA)، وكود المجتمع، ومواد تنفيذ مناسبة لشركات التطوير العقاري. كل لينك اتفتح بتاريخ 2026-10-12 إلا اللي متعلّم غير كده، وأي حاجة مقدرتش أتأكد منها بالكامل متعلّمة.

## Contents / المحتويات

- [Official Odoo documentation](#official-odoo-documentation)
- [Egyptian e-invoicing and e-receipt (ETA)](#egyptian-e-invoicing-and-e-receipt-eta)
- [Community and source code](#community-and-source-code)
- [Implementation material](#implementation-material)
- [Third-party commercial modules](#third-party-commercial-modules)
- [Practical checklists in this repo](#practical-checklists-in-this-repo)

## Official Odoo documentation

| Resource | Notes |
|---|---|
| [Egypt fiscal localization](https://www.odoo.com/documentation/18.0/applications/finance/fiscal_localizations/egypt.html) | Official page exists under Finance → Fiscal localizations. *Page body did not load in my automated check, so read it directly for the exact module list and e-invoicing steps.* |
| [Egypt payroll localization](https://www.odoo.com/documentation/18.0/applications/hr/payroll/payroll_localizations/egypt.html) | Official page exists under Payroll localizations. *Body not verified, same caveat.* Note that Odoo's canonical link for these pages points at the 19.0 docs, so check the version that matches your database. |

## Egyptian e-invoicing and e-receipt (ETA)

All pages below belong to the Egyptian Tax Authority SDK portal and were opened successfully.

| Resource | What it is |
|---|---|
| [eInvoicing & eReceipt SDK portal](https://sdk.invoicing.eta.gov.eg) | Documentation home for the APIs that ERP and POS systems use to register documents with ETA |
| [Getting started](https://sdk.invoicing.eta.gov.eg/start/) | One-time setup and the everyday integration flow (see the checklist below) |
| [API reference](https://sdk.invoicing.eta.gov.eg/api/) | Common, eInvoicing and eReceipt APIs, plus governance and rate limiting |
| [Release notes](https://sdk.invoicing.eta.gov.eg/release-notes/) | API and solution changes: watch this before upgrades |
| [Integration toolkit](https://sdk.invoicing.eta.gov.eg/toolkit/home/) | Utilities for integrating with the eReceipt platform |
| [FAQ](https://sdk.invoicing.eta.gov.eg/faq/) | Integration practices and receipt issuance questions |
| [Contacts](https://sdk.invoicing.eta.gov.eg/contacts/) | How to reach the SDK team |
| [Egyptian Tax Authority](https://www.incometax.gov.eg/) | Linked from the SDK portal as the authority's main site |

Unofficial tools (not affiliated with ETA):

| Resource | What it is |
|---|---|
| [einvoice-validator](https://github.com/islamelsabahy/einvoice-validator) ([try it in the browser](https://islamelsabahy.github.io/einvoice-validator/)) | Offline pre-flight check for ETA e-invoice JSON (v1.0 layout): missing fields, wrong enums, dates and arithmetic, in English and Arabic. Runs as a CLI or fully client-side in the browser |

> The SDK home page showed a "last updated" date of 2022-12-08. Always cross-check the release notes for current behavior.

## Community and source code

| Resource | Notes |
|---|---|
| [odoo/odoo](https://github.com/odoo/odoo) | Odoo Community source (OCB below is a backport fork of it) |
| [OCA on GitHub](https://github.com/OCA) | Odoo Community Association: open-source addons and tooling around Odoo |
| [OCA/OCB](https://github.com/OCA/OCB) | Odoo Community Backports |
| [OCA/OpenUpgrade](https://github.com/OCA/OpenUpgrade) | Community upgrade path between Odoo versions, useful when planning a version jump |

I searched for an OCA Egypt localization repository and did not find one. If you know of one, please open an issue or PR.

## Implementation material

| Resource | Notes |
|---|---|
| [odoo-real-estate-addons](https://github.com/islamelsabahy/odoo-real-estate-addons) | Odoo 17 add-ons for real estate developers: units catalog and installment plans with generated payment schedules, plus a local staging setup |
| [cheque-tracker-odoo](https://github.com/islamelsabahy/cheque-tracker-odoo) | Odoo 17 module for post-dated cheques (received/deposited/cleared/bounced) that links to installment lines and marks them paid on clearing. Tested on the official Odoo 17 image in CI |
| [Installment schedule calculator](https://islamelsabahy.github.io/odoo-real-estate-addons/) | Browser version of the `re_installment` schedule logic with PDF/CSV export; checked against the Python module on shared test vectors |
| [arabic-contract-clause-checker](https://github.com/islamelsabahy/arabic-contract-clause-checker) ([browser version](https://islamelsabahy.github.io/arabic-contract-clause-checker/)) | First-pass checklist review of Arabic sale/lease contracts: missing clauses and risky wording. Not legal advice |
| [odoo-implementation-playbook](https://github.com/islamelsabahy/odoo-implementation-playbook) | Business-first Odoo implementation framework from discovery to hypercare, with UAT libraries for Finance, CRM & Sales, HR & Payroll, Purchase & Inventory and a real estate extension. Documentation and templates, no code |

## Third-party commercial modules

Listed for awareness only. They are commercial products from a third party that I have **not** tested or endorsed. Evaluate any vendor's module on a staging database and read its support terms first.

| Resource | Notes |
|---|---|
| [Ecosire: Egypt ETA E-Invoice & E-Receipt for Odoo (docs)](https://docs.ecosire.com/odoo-modules/egypt-eta-einvoicing) | Vendor documentation for a paid ETA connector. *Appeared in a web search; I did not open the page, so its content is unreviewed* |

## Practical checklists in this repo

- [ETA e-invoicing integration checklist (EN/AR)](docs/eta-integration-checklist.md)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Short version: open the link yourself, state what you confirmed, keep descriptions factual.

## License

[CC0 1.0](LICENSE): do whatever you like with the list.
