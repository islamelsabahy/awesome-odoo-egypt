# ETA e-invoicing integration checklist / قائمة تشيك لربط ERP بالفاتورة الإلكترونية

Source: the "Getting started" page of the ETA SDK portal, checked on 2026-10-12: <https://sdk.invoicing.eta.gov.eg/start/>.
This checklist restates that page as a project plan. It does not replace it, and ETA can change requirements, so confirm each step against the portal and the [release notes](https://sdk.invoicing.eta.gov.eg/release-notes/).

المصدر: صفحة Getting started في بوابة ETA SDK بتاريخ 2026-10-12. القائمة دي إعادة ترتيب للصفحة كخطة مشروع، ومش بديل عنها، ومصلحة الضرائب ممكن تغيّر المتطلبات، فراجع كل خطوة مع البوابة.

## Phase 1: one-time setup / التجهيز لمرة واحدة

| # | Step | الخطوة | Owner | Done |
|---|---|---|---|---|
| 1 | Register a digital profile with ETA (gives access to the web app for managing representatives and systems) | تسجيل الملف الرقمي للمنشأة لدى ETA | Finance / Tax | ☐ |
| 2 | Accept the invitation to register the taxpayer administrator account | قبول دعوة تسجيل حساب مسؤول الممول | Finance / Tax | ☐ |
| 3 | Invite other representatives and register each ERP / POS system that will call the APIs | دعوة باقي الممثلين وتسجيل كل نظام ERP أو POS سيتصل بالـ API | IT + Finance | ☐ |
| 4 | Obtain API access credentials and configure them in the ERP | الحصول على بيانات الدخول للـ API وإعدادها في النظام | IT | ☐ |
| 5 | Obtain an eSeal X.509 certificate and configure it in the submitting system (documents must be digitally signed) | الحصول على شهادة الختم الإلكتروني X.509 وإعدادها لتوقيع المستندات | IT | ☐ |

## Phase 2: everyday integration / التكامل اليومي

| # | Requirement | المتطلب | Done |
|---|---|---|---|
| A | Authenticate against the identity system to get a session (access) token, reuse it for API calls | الحصول على access token واستخدامه في الطلبات | ☐ |
| B | Submit documents, retrieve documents and retrieve notifications through the APIs | إرسال واسترجاع المستندات والإشعارات عبر الـ API | ☐ |
| C | Optional: receive document status and package-processing notifications as REST callbacks (the endpoint must be reachable from the ETA side) | اختياري: استقبال إشعارات الحالة عبر callback يمكن الوصول له من ETA | ☐ |
| D | Use TLS for every API call | استخدام TLS في كل الاتصالات | ☐ |
| E | Digitally sign every submitted document as the issuer | توقيع كل مستند رقمياً | ☐ |

## Open questions to settle with ETA / أسئلة لازم تتأكد منها مع ETA

The Getting started page did not mention a pre-production (test) environment, so ask the SDK team via the [contacts page](https://sdk.invoicing.eta.gov.eg/contacts/):

- Is there a test environment, and how do we get test credentials?
- Which document types and tax codes apply to our activity? See the "Types" and "Codes" sections of the SDK.
- Where should the eSeal certificate and its PIN be stored, and who owns renewal?
- What are the rate limits for our expected daily volume? See "APIs Governance & Rate Limiting" in the API section.

## Suggested internal roles / الأدوار المقترحة

| Role | Responsibility |
|---|---|
| Finance / Tax owner | Digital profile, representatives, tax codes, filing accountability |
| IT manager | ERP registration, credentials, certificate custody, callback endpoint, monitoring |
| ERP vendor / partner | Connector configuration and testing |
| Backup owner | Certificate renewal calendar and credential rotation |
