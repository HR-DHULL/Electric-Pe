# GTM & GA4 Audit Checklist for ElectricPe (EV Marketplace)

> **Compiled**: March 2026
> **Scope**: Google Tag Manager container audit, GA4 configuration review, compliance assessment
> **Target**: ElectricPe — India's EV super app (charging, marketplace, test rides, community)

---

## Table of Contents

1. [GTM Container Health & Structure](#1-gtm-container-health--structure)
2. [Essential Tags for an EV Marketplace](#2-essential-tags-for-an-ev-marketplace)
3. [GA4 Ecommerce Event Tracking](#3-ga4-ecommerce-event-tracking)
4. [Engagement & Behavioral Events](#4-engagement--behavioral-events)
5. [GA4 Configuration Best Practices](#5-ga4-configuration-best-practices)
6. [Common GTM Mistakes to Check For](#6-common-gtm-mistakes-to-check-for)
7. [Industry Benchmarks & Performance Thresholds](#7-industry-benchmarks--performance-thresholds)
8. [Compliance & Privacy Requirements](#8-compliance--privacy-requirements)
9. [Server-Side Tagging Readiness](#9-server-side-tagging-readiness)
10. [Audit Scoring Template](#10-audit-scoring-template)

---

## 1. GTM Container Health & Structure

### 1.1 Container Inventory
- [ ] Document GTM container ID(s) in use (e.g., GTM-XXXXXXX)
- [ ] Confirm only ONE GTM container snippet is installed per page (check both `<head>` and `<noscript>` in `<body>`)
- [ ] Verify no duplicate GTM containers are loaded
- [ ] Confirm no direct GA4 snippet (gtag.js) is loaded alongside GTM — let GTM own the GA4 connection
- [ ] Count total tags, triggers, and variables in the container

### 1.2 Naming Conventions
- [ ] Tags follow a consistent naming pattern: `[Platform] - [Type] - [Description]`
  - Example: `GA4 - Event - EV Search Query`, `Meta - Pixel - Purchase`
- [ ] Triggers follow: `[Type] - [Description]`
  - Example: `Click - Book Test Ride CTA`, `PageView - Charger Listing`
- [ ] Variables follow: `[Type] - [Scope] - [Name]`
  - Example: `DLV - ecommerce - item_name`, `CSS - button - cta_text`

### 1.3 Container Hygiene
- [ ] No paused or unused tags remaining in the container
- [ ] No legacy Universal Analytics (UA) tags still present
- [ ] All Custom HTML tags reviewed for necessity — minimize these in favor of native tag templates
- [ ] Folders/organizational structure used to group related tags
- [ ] Container version notes are descriptive for every publish

### 1.4 Access & Permissions
- [ ] Admin access limited to authorized team members only
- [ ] Publish permissions restricted (not shared with third-party vendors)
- [ ] Two-factor authentication enabled on the Google account owning the container
- [ ] Workspace usage reviewed — no stale workspaces with unpublished changes

---

## 2. Essential Tags for an EV Marketplace

### 2.1 Core ElectricPe-Specific Events to Track

These events map to ElectricPe's core user journeys: charging, EV purchase, test rides, and community.

#### Charging Journey
- [ ] `charger_search` — user searches for a charging station (params: `search_term`, `city`, `charger_type`)
- [ ] `charger_view` — user views a specific charger/station detail page (params: `station_id`, `station_name`, `cpo_name`, `city`)
- [ ] `charger_filter_applied` — user applies filters (params: `filter_type`, `filter_value` e.g., fast charging, CCS2)
- [ ] `charger_directions_click` — user clicks "Get Directions" (params: `station_id`, `navigation_app`)
- [ ] `charging_session_start` — user initiates a charge via app (params: `station_id`, `charger_type`, `connector_type`)
- [ ] `charging_session_complete` — charge finishes (params: `station_id`, `duration`, `kwh_delivered`, `cost`)
- [ ] `qr_code_scan` — user scans charger QR code

#### EV Marketplace / Purchase Journey
- [ ] `ev_search` — user searches for an EV (params: `search_term`, `vehicle_type`)
- [ ] `ev_listing_view` (mapped to `view_item_list`) — user views EV listing page (params: `brand`, `category`)
- [ ] `ev_detail_view` (mapped to `view_item`) — user views specific EV detail (params: `vehicle_make`, `vehicle_model`, `price`, `range_km`)
- [ ] `ev_compare` — user compares EVs (params: `vehicles_compared[]`, `comparison_count`)
- [ ] `test_ride_booking` — user books a test ride (params: `vehicle_make`, `vehicle_model`, `booking_type: home/centre`, `city`)
- [ ] `purchase_inquiry` — user submits a purchase inquiry (params: `vehicle_make`, `vehicle_model`, `financing_interest: yes/no`)
- [ ] `financing_inquiry` — user explores financing options (params: `vehicle_model`, `loan_amount_range`)
- [ ] `insurance_inquiry` — user explores insurance options

#### App & Engagement
- [ ] `app_download_click` — user clicks app download CTA (params: `platform: ios/android`, `source_page`)
- [ ] `app_banner_click` — user clicks in-page app promotion banner
- [ ] `community_join_click` — user clicks to join community
- [ ] `subscription_plan_view` — user views charging subscription plans
- [ ] `subscription_plan_selected` — user selects a plan (params: `plan_name`, `plan_price`)

### 2.2 Automotive Standards Council (ASC) Aligned Events

Adapt the ASC framework (designed for automotive GA4) to ElectricPe's context:

- [ ] `asc_form_submission` — any lead form submitted (params: `form_type`, `lead_type`, `vehicle_model`)
- [ ] `asc_click_to_call` — phone number clicks (params: `phone_number`, `page_type`)
- [ ] `asc_chat_start` — chat widget interactions (params: `chat_source`)
- [ ] `asc_view_vehicle_details` — equivalent to EV detail view (params: `vehicle_year`, `vehicle_make`, `vehicle_model`)

---

## 3. GA4 Ecommerce Event Tracking

GA4 requires explicit implementation for ecommerce events (they are NOT automatic). Use Google's recommended event names exactly.

### 3.1 Full Ecommerce Funnel

| Funnel Stage | GA4 Event | ElectricPe Context | Status |
|---|---|---|---|
| Product Discovery | `view_item_list` | EV brand/model listing page | [ ] |
| Product View | `view_item` | Individual EV detail page | [ ] |
| Add to Wishlist | `add_to_wishlist` | "Save EV" or "Shortlist" action | [ ] |
| Add to Cart | `add_to_cart` | Select EV for inquiry/booking | [ ] |
| Begin Checkout | `begin_checkout` | Start test ride booking or purchase inquiry form | [ ] |
| Add Payment Info | `add_payment_info` | Wallet top-up, subscription payment | [ ] |
| Purchase | `purchase` | Charging session payment, subscription purchase, accessory purchase | [ ] |
| Refund | `refund` | Refund processed | [ ] |

### 3.2 Data Layer Requirements for Ecommerce

- [ ] Data layer pushes are implemented BEFORE the GTM container snippet
- [ ] Each ecommerce event includes mandatory parameters:
  - `currency` (e.g., "INR")
  - `value` (numeric transaction value)
  - `items[]` array with: `item_id`, `item_name`, `item_brand`, `item_category`, `price`, `quantity`
- [ ] Item-scoped custom dimensions registered in GA4:
  - `vehicle_type` (2-wheeler, 3-wheeler, 4-wheeler)
  - `vehicle_range_km`
  - `charger_type` (AC/DC)
  - `connector_type` (CCS2, CHAdeMO, Type 2, etc.)
- [ ] Use EXACT GA4 recommended event names — do NOT use custom names like `addProductToCart` instead of `add_to_cart`
- [ ] Transaction IDs are unique and non-repeating to prevent duplicate purchase tracking

### 3.3 Ecommerce Validation
- [ ] Revenue values are correctly passed (not null, not zero, not string)
- [ ] Currency is consistently "INR" across all events
- [ ] `items[]` array is properly structured JSON (not a string)
- [ ] Purchase events fire only once per transaction (no double-firing on thank-you pages)
- [ ] Test a full funnel in GTM Preview Mode to verify data layer pushes at each stage

---

## 4. Engagement & Behavioral Events

### 4.1 Scroll & Content Engagement
- [ ] `scroll` — GA4 enhanced measurement covers 90% scroll depth; consider adding 25%, 50%, 75% thresholds
- [ ] `video_play` — track EV review/demo video plays (params: `video_title`, `video_provider`, `video_percent`)
- [ ] `video_complete` — track video completion
- [ ] `file_download` — track brochure/spec sheet downloads (params: `file_name`, `file_extension`)

### 4.2 CTA & Click Tracking
- [ ] `cta_click` — track all primary CTAs (params: `cta_text`, `cta_location`, `destination_url`)
- [ ] `outbound_link_click` — track clicks to external sites (OEM websites, dealer sites)
- [ ] `social_share` — track social sharing actions
- [ ] `click_to_call` — track phone number clicks
- [ ] `click_to_whatsapp` — track WhatsApp chat clicks (common in India)
- [ ] `click_to_email` — track email link clicks

### 4.3 Form Tracking
- [ ] `form_start` — user begins filling a form (params: `form_id`, `form_name`)
- [ ] `form_submit` — user submits a form (params: `form_id`, `form_name`, `form_type`)
- [ ] `form_error` — form submission fails (params: `form_id`, `error_type`, `error_field`)
- [ ] Track form abandonment (started but not submitted)

### 4.4 Search Behavior
- [ ] `search` (GA4 enhanced measurement) — site search queries (params: `search_term`)
- [ ] `search_results_view` — search results displayed (params: `search_term`, `results_count`)
- [ ] `search_no_results` — zero results returned (params: `search_term`) — critical for UX insights

### 4.5 Error & Performance Tracking
- [ ] `page_error` — 404 pages, broken links (params: `page_url`, `referrer`)
- [ ] `javascript_error` — JS errors caught (params: `error_message`, `error_source`)
- [ ] `api_error` — API call failures (params: `api_endpoint`, `error_code`)
- [ ] `payment_error` — payment failures (params: `payment_method`, `error_type`)

---

## 5. GA4 Configuration Best Practices

### 5.1 Key Events (Conversions) to Configure

Mark these as key events (conversions) in GA4:

| Priority | Event | Why |
|---|---|---|
| P0 | `purchase` | Revenue tracking — subscriptions, charging, accessories |
| P0 | `test_ride_booking` | Primary lead generation action |
| P0 | `purchase_inquiry` | High-intent purchase signal |
| P1 | `app_download_click` | Core app growth metric |
| P1 | `charging_session_start` | Core product engagement |
| P1 | `form_submit` (qualified) | Lead capture |
| P1 | `subscription_plan_selected` | Monetization |
| P2 | `ev_compare` | High-intent research behavior |
| P2 | `charger_search` | Core engagement signal |
| P2 | `click_to_call` | Offline conversion signal |

### 5.2 Custom Dimensions to Register

**Event-scoped custom dimensions:**
- [ ] `vehicle_make` — EV manufacturer (Ola, Ather, TVS, etc.)
- [ ] `vehicle_model` — specific model name
- [ ] `vehicle_type` — 2W, 3W, 4W
- [ ] `city` — user's city
- [ ] `charger_type` — AC, DC, fast charging
- [ ] `connector_type` — CCS2, CHAdeMO, Type 2, GBT
- [ ] `cpo_name` — Charge Point Operator name
- [ ] `booking_type` — home test ride vs. centre visit
- [ ] `lead_type` — test ride, purchase inquiry, financing, insurance
- [ ] `form_name` — name of the form submitted
- [ ] `search_term` — what user searched for
- [ ] `error_type` — for error tracking events

**User-scoped custom dimensions:**
- [ ] `user_type` — new visitor, returning user, registered user, subscriber
- [ ] `subscription_status` — active subscriber, free user, expired
- [ ] `preferred_vehicle_type` — based on browsing behavior

**Item-scoped custom dimensions:**
- [ ] `vehicle_range_km` — EV range
- [ ] `vehicle_price_range` — price bracket
- [ ] `charging_speed` — kW rating
- [ ] `availability_status` — in stock, pre-order, out of stock

### 5.3 Custom Metrics
- [ ] `charging_kwh` — kWh delivered per session (sum metric)
- [ ] `charging_duration_minutes` — session duration
- [ ] `charging_cost_inr` — cost per session

### 5.4 Audience Segments to Build

Build these audiences in GA4 for remarketing and analysis:

| Audience | Definition | Use Case |
|---|---|---|
| EV Researchers | Viewed 3+ EV detail pages in 7 days | Retarget with test ride ads |
| Test Ride Leads | Completed `test_ride_booking` | Nurture toward purchase |
| Purchase Intent | Submitted `purchase_inquiry` OR `financing_inquiry` | High-priority retargeting |
| Charger Seekers | Used `charger_search` 3+ times | Promote charging subscriptions |
| Active Chargers | Completed 2+ `charging_session_complete` in 30 days | Upsell subscription plans |
| Lapsed Users | No session in 30+ days, previously active | Win-back campaigns |
| Subscription Prospects | Viewed subscription page but did not convert | Retarget with offers |
| High-Value Customers | Purchase value > INR 5000 in 90 days | Loyalty/VIP segments |
| City-Specific Users | Users in top 10 cities by traffic | Geo-targeted campaigns |
| App Download Abandoners | Clicked app CTA but no `first_open` event | Cross-platform retarget |
| EV Brand Enthusiasts | 3+ views of a specific brand (e.g., Ola, Ather) | Brand-specific campaigns |
| Comparison Shoppers | Triggered `ev_compare` event | Decision-stage nurturing |

### 5.5 Attribution Model Recommendations

- [ ] **Use Data-Driven Attribution (DDA)** as the primary model — GA4's default; uses machine learning to credit touchpoints based on actual conversion paths
- [ ] Set the **lookback window** appropriately:
  - Acquisition: 30 days (EV purchase is a considered decision)
  - Other conversions: 90 days (charging subscriptions, test rides may have longer cycles)
- [ ] Enable **Google Signals** for cross-device tracking (users research on mobile, convert on desktop, or vice versa)
- [ ] Compare DDA with **first-click attribution** periodically to understand which channels drive top-of-funnel awareness
- [ ] For paid campaigns, cross-reference GA4 attribution with platform-native attribution (Google Ads, Meta) to identify discrepancies
- [ ] Set up **conversion paths** report in GA4 to visualize multi-touch journeys

---

## 6. Common GTM Mistakes to Check For

### 6.1 Duplicate Tag Firing
- [ ] **No dual GA4 installation**: Confirm GA4 is loaded ONLY via GTM, not also via a direct gtag.js snippet
- [ ] **No duplicate GTM containers**: Only one GTM snippet per page
- [ ] **No duplicate event pushes**: Each business action pushes to dataLayer only once
- [ ] **One trigger per business event**: Follow the pattern "one signal -> one trigger -> one or more tags"
- [ ] **Purchase tag fires once**: Verify purchase/transaction tags cannot fire twice on confirmation pages (use tag firing options: "Once per event" or "Once per page")

### 6.2 Missing Cross-Domain Tracking
- [ ] Identify all domains/subdomains in ElectricPe's ecosystem (e.g., electricpe.com, app.electricpe.com, shop.electricpe.com, blog.electricpe.com)
- [ ] All domains use the SAME GA4 property
- [ ] Cross-domain measurement configured in GA4 Admin > Data Streams > Configure tag settings > Configure your domains
- [ ] Verify the `_gl` linker parameter appears in URLs when navigating between domains
- [ ] Subdomains under the same root domain should work automatically — verify this is happening
- [ ] If using third-party checkout or payment gateway domains, include them in cross-domain config
- [ ] Referral exclusion list updated to exclude own domains and payment gateways (Razorpay, PayTM, etc.)

### 6.3 No Consent Management
- [ ] A Consent Management Platform (CMP) is installed and functioning
- [ ] Google Consent Mode v2 is implemented (includes `ad_storage`, `analytics_storage`, `ad_user_data`, `ad_personalization` parameters)
- [ ] Default consent state is set BEFORE GTM loads
- [ ] Consent state updates when user makes a choice
- [ ] Tags respect consent signals — verify via GTM Preview Mode that tags fire/block based on consent
- [ ] Advanced Consent Mode implemented (sends cookieless pings for modeling when consent is denied) vs. Basic mode (blocks all tags when denied)
- [ ] Cookie banner is visible, clear, and not pre-checked

### 6.4 Tag Firing Order Issues
- [ ] GA4 Configuration tag fires BEFORE any GA4 Event tags
- [ ] Data layer is populated BEFORE GTM container loads (data layer snippet placed above GTM snippet)
- [ ] Tag sequencing is configured where dependencies exist (e.g., a conversion tag should fire only after the base pixel tag)
- [ ] Use tag priority or tag sequencing features in GTM for critical order dependencies
- [ ] No race conditions between consent management and tag firing

### 6.5 Missing Error Tracking
- [ ] JavaScript errors are captured and sent to GA4
- [ ] 404 page tracking is implemented
- [ ] Form validation errors are tracked
- [ ] Payment/transaction errors are tracked
- [ ] API timeout/failure events are tracked
- [ ] Tag firing failures are monitored (use GTM's built-in tag status monitoring)

### 6.6 No Data Layer Implementation
- [ ] A structured `dataLayer` object exists and is initialized before GTM
- [ ] Data layer variables are used instead of scraping the DOM with CSS selectors
- [ ] Ecommerce data is passed via the data layer (not hardcoded in tags)
- [ ] User attributes (login status, user type, subscription status) are in the data layer
- [ ] Page metadata (page type, category, content group) is in the data layer
- [ ] Data layer pushes use consistent event naming conventions

### 6.7 SPA / Next.js Pageview Issues
- [ ] If ElectricPe uses Next.js or any SPA framework:
  - [ ] Virtual pageviews are fired on client-side route changes (using `history.pushState` or Next.js router events)
  - [ ] GTM's default "All Pages" trigger is NOT also firing on route changes (avoid double pageviews)
  - [ ] The `page_location` and `page_title` parameters update correctly on virtual pageviews
  - [ ] Data layer is reset/updated appropriately on route changes
  - [ ] GTM is loaded once in the app shell (`_app.js` or layout component), NOT in individual page components
  - [ ] Scroll tracking resets on virtual page navigation
  - [ ] GA4's enhanced measurement "Page changes based on browser history events" setting is reviewed — it may cause duplicates if you also push manual pageviews

---

## 7. Industry Benchmarks & Performance Thresholds

### 7.1 GTM Tag Count Benchmarks

| Metric | Benchmark Range | Notes |
|---|---|---|
| Total tags in container | 15–40 tags | Typical for mid-size marketplace/ecommerce |
| GA4 tags | 1 config + 8–15 event tags | Use GA4 event tag for multiple events where possible |
| Advertising pixels | 3–6 (Google Ads, Meta, others) | Each with conversion + remarketing |
| Custom HTML tags | < 5 | Minimize — use native templates instead |
| Third-party tags | 3–8 (heatmaps, chat, CRM) | Audit for necessity quarterly |

### 7.2 Conversion Tracking Setup Benchmarks

| Metric | Typical Setup |
|---|---|
| Key events (conversions) marked | 5–10 events |
| Ecommerce events implemented | 6–8 events (full funnel) |
| Custom dimensions registered | 10–20 event-scoped, 3–5 user-scoped |
| Audiences configured | 8–15 segments |
| Conversion rate for test ride booking | 1–3% of EV detail page viewers (industry est.) |
| Conversion rate for purchase inquiry | 0.5–1.5% of EV detail page viewers (industry est.) |

### 7.3 Page Load Impact Thresholds

| Metric | Acceptable | Warning | Critical |
|---|---|---|---|
| GTM container load time | < 100ms | 100–300ms | > 300ms |
| Total tag execution time | < 500ms | 500ms–1s | > 1s |
| Impact on Largest Contentful Paint (LCP) | < 200ms added | 200–500ms | > 500ms |
| Impact on Time to Interactive (TTI) | < 300ms added | 300ms–1s | > 1s |
| Impact on Total Blocking Time (TBT) | < 200ms added | 200ms–500ms | > 500ms |
| Container size (compressed) | < 50KB | 50–100KB | > 100KB |

### 7.4 Performance Optimization Checklist
- [ ] Critical tags (GA4) fire on page load; non-critical tags (remarketing, heatmaps) fire on `Window Loaded` or `DOM Ready`
- [ ] Tag firing priority is used to ensure analytics fires before marketing tags
- [ ] Unused tags and triggers are removed (not just paused)
- [ ] Custom HTML tags are minimized and optimized
- [ ] Consider moving heavy tags to server-side GTM
- [ ] Run Lighthouse / PageSpeed Insights with and without GTM to measure actual impact
- [ ] Monitor Core Web Vitals specifically with GTM enabled

---

## 8. Compliance & Privacy Requirements

### 8.1 India's Digital Personal Data Protection Act (DPDPA) 2023

**Key Requirements:**

- [ ] **Consent is the ONLY legal basis** for cookie-based tracking under DPDPA — no "legitimate interest" exemption for cookies
- [ ] **Opt-in required**: Cookies must NOT fire before explicit user consent (no implied consent, no pre-checked boxes)
- [ ] Consent must be:
  - Freely given (no forced consent for accessing services)
  - Unconditional (not tied to service access)
  - Informed (clear description of data types, purposes, third parties)
  - Unambiguous (explicit action like clicking "Accept")
- [ ] **Consent withdrawal** must be as easy as giving consent
- [ ] Users (Data Principals) have the right to access, correct, and erase their data
- [ ] **Children's data**: Extra protections for users under 18 — no behavioral tracking/targeting of minors

**Key Timeline:**
- Consent manager registration opens: **November 13, 2026**
- All consent, privacy notice, and security provisions effective: **May 13, 2027**
- **Recommendation**: Implement compliant consent management NOW to be ready ahead of enforcement

**Penalties:**
- Up to INR 250 crore (approx. USD 30 million) per violation for significant non-compliance
- Data Protection Board of India has enforcement authority

### 8.2 Cookie Consent Implementation
- [ ] A consent banner is displayed on first visit, BEFORE any tracking cookies are set
- [ ] Banner provides clear Accept/Reject options (no dark patterns, no hidden reject button)
- [ ] Granular consent categories available:
  - Strictly Necessary (always on)
  - Analytics/Performance
  - Marketing/Advertising
  - Functional
- [ ] Consent choice is stored and persisted across sessions
- [ ] Consent can be modified at any time (accessible link in footer/settings)
- [ ] Consent records are logged with timestamp and user identifier for audit trail

### 8.3 Google Consent Mode v2 Integration
- [ ] Consent Mode v2 parameters implemented:
  - `ad_storage` — controls advertising cookies
  - `analytics_storage` — controls analytics cookies
  - `ad_user_data` — controls sending user data to Google for advertising
  - `ad_personalization` — controls personalized advertising
- [ ] Default consent state set to `denied` for Indian users (opt-in model)
- [ ] Consent state updates fire before page navigation
- [ ] **Advanced mode recommended**: Sends cookieless pings for Google's conversion modeling when consent is denied (recovers ~70% of measurement data)
- [ ] Use a Google-certified CMP (e.g., CookieYes, OneTrust, Cookiebot, Securiti.ai) — required by Google in 2026

### 8.4 Data Processing Agreements (DPAs)
- [ ] DPA signed with Google (for GA4, Google Ads data processing)
- [ ] DPA signed with Meta (if using Facebook Pixel/CAPI)
- [ ] DPAs with all third-party analytics/marketing vendors whose tags are in GTM
- [ ] DPA with CMP provider
- [ ] Data Processing Impact Assessment (DPIA) conducted for high-risk processing activities
- [ ] Data retention settings in GA4 reviewed (set to 14 months max, or shorter based on policy)
- [ ] IP anonymization confirmed (GA4 does this by default, but verify)
- [ ] Data sharing settings in GA4 reviewed — disable unnecessary data sharing with Google

### 8.5 Additional Compliance Checks
- [ ] Privacy policy updated to reflect all tracking technologies, purposes, and third-party data sharing
- [ ] Privacy policy is accessible from every page
- [ ] No personal data (email, phone, name) is sent to GA4 or advertising platforms in plain text
- [ ] User IDs, if used, are pseudonymized (hashed)
- [ ] PII scrubbing is in place — URL parameters with PII are filtered before sending to GA4
- [ ] Data deletion requests can be fulfilled (GA4 supports user data deletion via API)

---

## 9. Server-Side Tagging Readiness

Server-side GTM is becoming the standard for 2026 and beyond. Assess ElectricPe's readiness.

### 9.1 Benefits for ElectricPe
- **Performance**: Moves heavy tag processing from user's browser to server; documented 7%+ page load improvement
- **Data accuracy**: Bypasses ad blockers and iOS privacy restrictions; case studies show 28% increase in conversion accuracy
- **Privacy control**: Full control over what data is sent to third parties
- **Cookie longevity**: First-party cookies set server-side have longer lifespans than browser-set cookies

### 9.2 Readiness Checklist
- [ ] Evaluate if server-side GTM is deployed or planned
- [ ] If not deployed, assess priority:
  - High priority if: >30% traffic from Safari/iOS, significant ad blocker usage, Meta/Google Ads are major channels
  - Medium priority if: primarily app-based traffic (server-side less impactful for native app)
- [ ] Infrastructure assessment: Google Cloud Run or custom server for sGTM
- [ ] Subdomain configured for server-side endpoint (e.g., `data.electricpe.com`) for first-party context
- [ ] Meta Conversion API (CAPI) routed through server-side GTM
- [ ] Google Ads Enhanced Conversions configured via server-side
- [ ] Data deduplication logic in place between client-side and server-side events

---

## 10. Audit Scoring Template

Use this scoring matrix to rate each section during the audit.

| Section | Weight | Score (0-10) | Weighted Score | Notes |
|---|---|---|---|---|
| 1. Container Health & Structure | 10% | /10 | | |
| 2. Essential EV Marketplace Tags | 15% | /10 | | |
| 3. GA4 Ecommerce Tracking | 15% | /10 | | |
| 4. Engagement & Behavioral Events | 10% | /10 | | |
| 5. GA4 Configuration (dims, audiences, attribution) | 15% | /10 | | |
| 6. Common Mistakes Avoided | 10% | /10 | | |
| 7. Performance Within Benchmarks | 10% | /10 | | |
| 8. Compliance & Privacy | 10% | /10 | | |
| 9. Server-Side Tagging | 5% | /10 | | |
| **Total** | **100%** | | **/100** | |

**Rating Scale:**
- **90-100**: Excellent — production-grade, audit-ready
- **70-89**: Good — minor gaps, optimization opportunities
- **50-69**: Needs Work — significant gaps affecting data quality or compliance
- **Below 50**: Critical — major issues requiring immediate remediation

---

## Sources & References

- [GTM Audit Checklist 2025 — Wixpa](https://wixpa.com/google-tag-manager-audit-checklist/)
- [GTM Audit Checklist — Optimize Smart](https://www.optimizesmart.com/google-tag-manager-audit-checklist/)
- [GTM Best Practices 2026 — Stape](https://stape.io/blog/gtm-best-practices-and-tracking-tags)
- [GTM Checklist: 73 Ways — Analytics Mania](https://www.analyticsmania.com/post/google-tag-manager-checklist/)
- [How to Audit GTM Containers — TagStack](https://tagstack.io/blog/lucas-guide-to-successful-gtm-audits)
- [Year-End Web Analytics Checklist 2026 — Liquid](https://www.liquidint.com/blog/year-end-web-analytics-checklist-2026)
- [Common GTM Mistakes — Analytico Digital](https://www.analyticodigital.com/blog/common-mistakes-gtm-implementation-and-how-to-fix-them)
- [ASC for GA4 — Automotive Standards Council](https://automotivestandardscouncil.com/)
- [ASC GA4 Complete Guide — Generations Digital](https://www.generationsdigital.com/automotive-standards-council-for-ga4)
- [GA4 Recommended Events — Google](https://support.google.com/analytics/answer/9267735?hl=en)
- [GA4 Ecommerce Implementation — Google Developers](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce)
- [GA4 Ecommerce Events for D2C — FunnelFreaks](https://funnelfreaks.co/blog/ga4-ecommerce-events-d2c-brands)
- [GA4 Custom Dimensions — Analytics Mania](https://www.analyticsmania.com/post/a-guide-to-custom-dimensions-in-google-analytics-4/)
- [GA4 Audiences Guide — Measure School](https://measureschool.com/google-analytics-4-audiences/)
- [GA4 Attribution Models — MeasureMinds](https://measuremindsgroup.com/ga4-attribution-models)
- [GTM & Next.js Guide — Build with Matija](https://www.buildwithmatija.com/blog/nextjs-google-analytics-tag-manager-guide)
- [GTM Data Layer — Google Developers](https://developers.google.com/tag-platform/tag-manager/datalayer)
- [Data Layer Issues & Solutions — Analytics Mates](https://www.analyticsmates.com/post/gtm-data-layer-common-problems-and-viable-solutions)
- [India DPDPA Cookie Consent — Secure Privacy](https://secureprivacy.ai/blog/india-digital-personal-data-protection-act-dpdpa-cookie-consent-requirements)
- [DPDPA Cookie Banner Requirements — Secure Privacy](https://secureprivacy.ai/blog/india-dpdpa-cookie-banner)
- [India DPDPA 2025 Guide — CookieYes](https://www.cookieyes.com/blog/india-digital-personal-data-protection-act-dpdpa/)
- [Consent Mode v2 — Simo Ahava](https://www.simoahava.com/analytics/consent-mode-v2-google-tags/)
- [Google Consent Mode Setup — Google Developers](https://developers.google.com/tag-platform/security/guides/consent)
- [GTM Impact on Page Speed — Analytics Mania](https://www.analyticsmania.com/post/google-tag-manager-impact-on-page-speed-and-how-to-improve/)
- [Server-Side Tagging Benefits — Stape](https://stape.io/blog/benefits-server-side-tagging)
- [Server-Side GTM Explained — Analytify](https://analytify.io/gtm-server-side-tagging/)
- [Cross-Domain Tracking GA4 — Analytics Mania](https://www.analyticsmania.com/post/cross-domain-tracking-in-google-analytics-4/)
- [Cross-Domain Tracking Strategy — Usercentrics](https://usercentrics.com/guides/smarter-tagging-with-google-tag-manager/cross-domain-tracking/)
- [ElectricPe App](https://electricpe.com/electricpe-app)
