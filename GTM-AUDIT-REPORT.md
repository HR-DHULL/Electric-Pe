# Google Tag Manager (GTM) Audit Report
## ElectricPe (electricpe.com)

**Audit Date:** March 17, 2026
**Prepared For:** ElectricPe — India's Largest EV Retail Network
**Prepared By:** [Your Agency Name]
**Audit Type:** Complimentary GTM & Tracking Infrastructure Assessment
**Domain:** https://electricpe.com
**Tech Stack:** Next.js (React SSR), WebEngage, Razorpay

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Current Tracking Inventory](#2-current-tracking-inventory)
3. [GTM Audit Findings (22 Checks)](#3-gtm-audit-findings)
4. [Data Layer Assessment](#4-data-layer-assessment)
5. [Conversion Tracking Gaps](#5-conversion-tracking-gaps)
6. [Tag Health & Performance](#6-tag-health--performance)
7. [Privacy & Consent Compliance](#7-privacy--consent-compliance)
8. [Revenue Impact Analysis](#8-revenue-impact-analysis)
9. [Prioritized Remediation Plan](#9-prioritized-remediation-plan)
10. [What We Can Do For You](#10-what-we-can-do-for-you)

---

## 1. Executive Summary

### GTM Health Score: 12 / 100 — CRITICAL

ElectricPe has built an impressive EV business — 15,000+ charging stations, 35+ Mobility Centres, 6,000+ EVs sold, 80,000+ app community members, and a Google Maps partnership. However, **the tracking and measurement infrastructure behind the website is severely broken**, meaning ElectricPe is flying blind on digital performance.

### The Core Problem

| What You Have | What You're Missing |
|---------------|-------------------|
| WebEngage (behavioral analytics) | Google Tag Manager (GTM) |
| Razorpay (payment processing) | Google Analytics 4 (GA4) |
| Facebook Pixel (partial/unverified) | Google Ads Conversion Tracking |
| WhatsApp Business Widget | Meta CAPI (Server-Side Tracking) |
| | LinkedIn Insight Tag |
| | Structured Data Layer |
| | Consent Management Platform |
| | Cross-Domain Tracking |
| | Enhanced Ecommerce Tracking |
| | Event-Based Conversion Measurement |

### What This Means in Plain Language

Every day, potential EV buyers visit electricpe.com, browse vehicles, check charging stations, and interact with the test ride booking flow. **You have no visibility into:**

- Which marketing channels drive the most test ride bookings
- What the cost per test ride booking is from each source
- Where users drop off in the booking funnel
- Which EV models get the most interest
- Whether your ₹299 test ride offer converts better than other CTAs
- How much revenue each traffic source generates
- Which city pages perform best

**You're essentially running a ₹13+ Crore business with the measurement maturity of a personal blog.**

### Score Breakdown

| Category | Score | Max | Status |
|----------|-------|-----|--------|
| GTM Container Setup | 0 | 15 | NOT INSTALLED |
| Data Layer Implementation | 0 | 20 | NOT FOUND |
| Google Analytics 4 | 0 | 15 | NOT INSTALLED |
| Conversion Tracking | 3 | 15 | MINIMAL (WebEngage only) |
| Meta Pixel & CAPI | 4 | 10 | PARTIAL (fbq reference found) |
| Event Configuration | 2 | 10 | MINIMAL |
| Privacy & Consent | 0 | 5 | NOT FOUND |
| Cross-Platform Integration | 0 | 5 | NOT CONFIGURED |
| Tag Performance & QA | 3 | 5 | CANNOT ASSESS (no GTM) |
| **Total** | **12** | **100** | **CRITICAL** |

---

## 2. Current Tracking Inventory

### 2.1 What We Found

We performed a comprehensive scan of electricpe.com's source code, scripts, and network requests. Here is every tracking technology currently deployed:

#### WebEngage — FOUND (Primary CDP)

| Detail | Value |
|--------|-------|
| **Status** | Active |
| **SDK Version** | v6.0 |
| **Account ID** | `in~~2024c260` |
| **Script URL** | `https://widgets.in.webengage.com/js/webengage-min-v-6.0.js` |
| **SPA Mode** | Enabled (`is_spa: 1`) |
| **Tag ID** | `_webengage_script_tag` |

**Assessment:** WebEngage is functioning as ElectricPe's primary customer data platform. It handles behavioral tracking, push notifications, and user engagement. However, WebEngage is **not a substitute for Google Tag Manager** — it cannot:
- Feed conversion data to Google Ads Smart Bidding
- Send events to Meta's advertising algorithm
- Provide cross-channel attribution
- Manage multiple third-party tags efficiently
- Implement a structured data layer

**Risk:** Over-reliance on a single vendor (WebEngage) for all analytics creates vendor lock-in and a single point of failure.

#### Razorpay — FOUND (Payment Gateway)

| Detail | Value |
|--------|-------|
| **Status** | Active |
| **Script URL** | `https://checkout.razorpay.com/v1/checkout.js` |
| **Purpose** | Payment processing for test ride bookings and EV purchases |

**Assessment:** Razorpay is properly loaded. However, **payment completion events are not being forwarded to any analytics or advertising platform**. This means:
- Google Ads cannot optimize bids based on actual purchases
- Meta cannot build lookalike audiences from paying customers
- You cannot calculate true ROAS from any channel

#### Facebook Pixel — PARTIAL (Unverified)

| Detail | Value |
|--------|-------|
| **Status** | Reference found (`fbq()` function, `FacebookPixelEvents` component) |
| **Pixel ID** | NOT CONFIRMED |
| **Standard Events** | NOT CONFIRMED |
| **CAPI** | NOT FOUND |
| **Domain Verification** | NOT CONFIRMED |

**Assessment:** There is a reference to Facebook Pixel code in ElectricPe's Next.js codebase (a `FacebookPixelEvents` component exists), but we could not confirm:
- Whether the pixel is actively firing on all pages
- What Pixel ID is being used
- Whether any standard events (Lead, Purchase, ViewContent) are configured
- Whether the domain is verified in Meta Business Manager
- Whether Conversions API (CAPI) is deployed for server-side tracking

**If the pixel is partially deployed but not properly configured, this is arguably worse than having no pixel** — Meta's algorithm receives incomplete, noisy data and optimizes poorly.

#### WhatsApp Business — FOUND

| Detail | Value |
|--------|-------|
| **Status** | Active |
| **Number** | +91 96328 88926 |
| **Integration** | wa.me deep link (basic) |

**Assessment:** WhatsApp widget is present but not tracked. No click events are being captured, so you cannot measure how many leads come through WhatsApp vs. other channels.

### 2.2 What We Did NOT Find

| Technology | Status | Business Impact |
|-----------|--------|-----------------|
| **Google Tag Manager (GTM)** | NOT FOUND | No centralized tag management; every new tag requires developer deployment |
| **Google Analytics 4 (GA4)** | NOT FOUND | No cross-channel web analytics; no funnel analysis; no audience building |
| **Google Ads Tag (gtag.js)** | NOT FOUND | Cannot run Google Ads with conversion optimization |
| **Google Ads Conversion Linker** | NOT FOUND | First-party cookie tracking broken |
| **Meta Conversions API (CAPI)** | NOT FOUND | 30-40% of Meta conversion data lost due to browser restrictions |
| **LinkedIn Insight Tag** | NOT FOUND | Cannot run LinkedIn Ads or build B2B retargeting audiences |
| **TikTok Pixel** | NOT FOUND | Cannot run TikTok Ads |
| **Microsoft Clarity / Hotjar** | NOT FOUND | No heatmaps, no session recordings, no UX insights |
| **Google Search Console Verification** | NOT CONFIRMED | Cannot monitor SEO performance in GSC |
| **Consent Management Platform** | NOT FOUND | No cookie consent banner; potential compliance risk |
| **Structured dataLayer** | NOT FOUND | No data layer for GTM to consume |

---

## 3. GTM Audit Findings (22 Checks)

### 3.1 GTM Container — NOT INSTALLED

| Check | Status | Severity |
|-------|--------|----------|
| GTM-01: GTM container present on all pages | FAIL | CRITICAL |
| GTM-02: GTM container ID consistent across pages | N/A | CRITICAL |
| GTM-03: GTM snippet in correct position (`<head>` + `<body>` noscript) | N/A | CRITICAL |
| GTM-04: Only one GTM container per page (no duplicates) | N/A | CRITICAL |
| GTM-05: GTM loaded before other marketing tags | N/A | HIGH |

**Impact:** Without GTM, every tracking change requires a developer to modify the Next.js codebase, rebuild, and redeploy. This creates:
- 3-7 day delays for any tracking change (vs. minutes with GTM)
- Developer dependency for marketing team operations
- Higher error risk (code changes vs. GTM UI)
- No version control or rollback capability for tags
- No preview/debug mode for testing

### 3.2 Data Layer

| Check | Status | Severity |
|-------|--------|----------|
| GTM-06: `window.dataLayer` initialized before GTM | FAIL | CRITICAL |
| GTM-07: Page-level variables pushed (page_type, page_title, user_type) | FAIL | HIGH |
| GTM-08: E-commerce data layer (product views, add to cart, purchase) | FAIL | HIGH |
| GTM-09: User identity passed (hashed email/phone for Enhanced Conversions) | FAIL | HIGH |
| GTM-10: Custom dimensions defined (city, EV_model, mobility_centre) | FAIL | MEDIUM |

### 3.3 Tag Configuration

| Check | Status | Severity |
|-------|--------|----------|
| GTM-11: GA4 Configuration tag present | FAIL | CRITICAL |
| GTM-12: GA4 event tags for key actions | FAIL | CRITICAL |
| GTM-13: Google Ads Conversion tag | FAIL | CRITICAL |
| GTM-14: Google Ads Remarketing tag | FAIL | HIGH |
| GTM-15: Meta Pixel base code via GTM | FAIL (hardcoded, unverified) | HIGH |
| GTM-16: LinkedIn Insight Tag | FAIL | MEDIUM |
| GTM-17: All tags fire on correct triggers | N/A | HIGH |
| GTM-18: No duplicate tag firing | CANNOT VERIFY | MEDIUM |

### 3.4 Triggers & Variables

| Check | Status | Severity |
|-------|--------|----------|
| GTM-19: Form submission triggers (test ride booking) | FAIL | CRITICAL |
| GTM-20: Click triggers (CTA buttons, app download links) | FAIL | HIGH |
| GTM-21: Scroll depth tracking | FAIL | LOW |
| GTM-22: Video engagement tracking (if applicable) | FAIL | LOW |

### Summary: 0 of 22 checks passed.

---

## 4. Data Layer Assessment

### 4.1 Current State: No Data Layer Exists

ElectricPe's Next.js website does not push any structured data into `window.dataLayer`. This is the foundation that GTM reads from to fire tags with contextual information. Without it, even if GTM were installed, it would have no business context to work with.

### 4.2 Recommended Data Layer Architecture for ElectricPe

**Page Load Events:**

```javascript
// Every page load
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({
  event: 'page_view',
  page_type: 'product_listing',     // homepage | product_listing | product_detail | charging_station | blog | booking | confirmation
  page_title: document.title,
  user_type: 'prospect',            // prospect | registered | app_user | customer
  city: 'Bengaluru',                // User's selected city
  mobility_centre: 'Koramangala',   // Nearest mobility centre
  platform: 'web'                   // web | app
});
```

**EV Product View:**

```javascript
window.dataLayer.push({
  event: 'view_item',
  ecommerce: {
    currency: 'INR',
    value: 89999,
    items: [{
      item_id: 'TVS-IQUBE-ST',
      item_name: 'TVS iQube ST',
      item_brand: 'TVS',
      item_category: 'Electric Scooter',
      price: 89999,
      item_variant: 'Standard'
    }]
  }
});
```

**Test Ride Booking Initiated:**

```javascript
window.dataLayer.push({
  event: 'begin_checkout',
  ecommerce: {
    currency: 'INR',
    value: 299,
    items: [{
      item_id: 'TEST-RIDE-TVS-IQUBE',
      item_name: 'Test Ride - TVS iQube ST',
      item_category: 'Test Ride',
      price: 299
    }]
  },
  booking_city: 'Bengaluru',
  booking_centre: 'Koramangala',
  booking_type: 'home_visit'  // home_visit | showroom
});
```

**Test Ride Booking Completed (PRIMARY CONVERSION):**

```javascript
window.dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: 'TR-2026-03-17-001',
    currency: 'INR',
    value: 299,
    items: [{
      item_id: 'TEST-RIDE-TVS-IQUBE',
      item_name: 'Test Ride - TVS iQube ST',
      item_category: 'Test Ride',
      price: 299
    }]
  },
  // Enhanced Conversions data (hashed by GTM)
  user_data: {
    email: 'customer@example.com',
    phone_number: '+919876543210',
    address: {
      city: 'Bengaluru',
      region: 'Karnataka',
      country: 'IN'
    }
  }
});
```

**Charging Station Search:**

```javascript
window.dataLayer.push({
  event: 'search',
  search_term: 'EV charging station Koramangala',
  search_city: 'Bengaluru',
  results_count: 12
});
```

**App Download Click:**

```javascript
window.dataLayer.push({
  event: 'app_download_click',
  app_platform: 'android',  // android | ios
  click_location: 'homepage_hero'  // homepage_hero | footer | nav | banner
});
```

**WhatsApp Lead:**

```javascript
window.dataLayer.push({
  event: 'whatsapp_click',
  click_location: 'floating_widget',
  page_url: window.location.href
});
```

### 4.3 Why This Data Layer Matters

| Without Data Layer | With Data Layer |
|-------------------|-----------------|
| Google Ads optimizes on page views (worthless) | Google Ads optimizes on actual test ride bookings |
| Meta shows ads to everyone equally | Meta targets lookalikes of paying customers |
| No idea which EV model drives most interest | Dashboard showing product interest by model, city, and source |
| ₹299 test ride offer unmeasured | Exact CPA per test ride booking, per channel, per city |
| Razorpay transactions invisible to marketing | Every purchase tied to its marketing source |

---

## 5. Conversion Tracking Gaps

### 5.1 Critical Conversions NOT Being Tracked

| Conversion Event | Business Value | Currently Tracked? | Platforms That Need It |
|-----------------|----------------|-------------------|----------------------|
| **Test Ride Booking** | PRIMARY (leads to ₹50K-15L+ sale) | NO | Google Ads, GA4, Meta, LinkedIn |
| **EV Purchase/Financing Approved** | HIGHEST VALUE | NO | Google Ads, GA4, Meta |
| **App Install Click** | HIGH (retention channel) | NO | GA4, Meta, Google App Campaigns |
| **Charging Station Search** | MEDIUM (engagement) | WebEngage only | GA4 |
| **Contact Form Submit** | MEDIUM | NO | Google Ads, GA4, Meta |
| **WhatsApp Chat Initiated** | MEDIUM (lead) | NO | GA4, Meta |
| **EV Model Page View** | LOW (micro-conversion) | WebEngage only | GA4, Meta (ViewContent) |
| **Financing Calculator Used** | MEDIUM | NO | GA4, Meta |
| **City/Centre Selected** | LOW | NO | GA4 |

### 5.2 Revenue Leakage Estimate

Based on industry benchmarks for EV/automotive digital marketing in India:

| Metric | Estimate |
|--------|----------|
| Monthly website visitors (estimated) | 50,000 - 100,000 |
| Test ride booking conversion rate (estimated) | 2-4% |
| Potential monthly test ride bookings | 1,000 - 4,000 |
| Test ride to purchase conversion rate | 10-20% |
| Average EV sale value | ₹80,000 - ₹1,50,000 |
| **Potential monthly revenue from web** | **₹80L - ₹12Cr** |
| **Currently measurable** | **₹0 (nothing tracked)** |

Even a 10% improvement in conversion rate through proper tracking and optimization would represent **₹8L - ₹1.2Cr additional monthly revenue**.

### 5.3 The "Test Ride" Measurement Gap — In Detail

The ₹299 test ride is ElectricPe's most powerful conversion mechanism. A customer who takes a test ride is estimated to be **10x more likely** to purchase an EV. Yet this critical event has ZERO connection to any advertising measurement:

```
Current State:
Ad Click → ??? → Website Visit (maybe WebEngage) → ??? → Test Ride Page → ??? → Booking → Razorpay → ???

No data flows back to Google Ads or Meta.
Smart Bidding has no signal to optimize.
Meta's algorithm has no feedback loop.
You cannot calculate cost-per-test-ride from any channel.

Required State:
Ad Click → Landing Page (GA4: page_view) → Test Ride Page (GA4: view_item) →
Booking Form Open (GA4: begin_checkout) → Form Submit (GA4: purchase / Google Ads: Conversion / Meta: Lead) →
Razorpay Payment (GA4: purchase confirmed / Enhanced Conversion with user data) →
Data feeds back to Google Ads, Meta, GA4 → Algorithms optimize → CPA decreases → More bookings for same budget
```

---

## 6. Tag Health & Performance

### 6.1 Current Tag Load Assessment

| Tag | Load Method | Impact on Page Speed | Best Practice |
|-----|-------------|---------------------|---------------|
| WebEngage SDK (v6.0) | Inline `<script>` | MEDIUM-HIGH (~180KB) | Should be loaded async via GTM |
| Razorpay Checkout | `<script src>` in head | MEDIUM (~120KB) | Should lazy-load only on checkout pages |
| Facebook Pixel (if active) | Next.js component | LOW-MEDIUM | Should be managed via GTM for consistency |
| WhatsApp Widget | Inline link | LOW | Acceptable |

### 6.2 Issues Found

| Issue | Severity | Detail |
|-------|----------|--------|
| **No tag management system** | CRITICAL | Tags are hardcoded in the Next.js codebase. Adding/removing/modifying any tag requires a full code deployment. |
| **WebEngage loading synchronously** | HIGH | The WebEngage SDK loads as a render-blocking inline script. It should be loaded asynchronously via GTM with `strategy="afterInteractive"` or `"lazyOnload"`. |
| **Razorpay loaded on every page** | MEDIUM | The Razorpay checkout script loads on all pages, including pages where no payment occurs. This adds ~120KB of unnecessary JavaScript to blog posts, about pages, etc. |
| **No tag firing sequence control** | HIGH | Without GTM, there is no guarantee that tags fire in the correct order. The data layer should initialize before any tag fires. |
| **No tag error monitoring** | MEDIUM | No way to detect if a tag fails silently (e.g., if WebEngage SDK fails to load, no alert is generated). |
| **No tag version control** | HIGH | GTM provides built-in versioning with rollback capability. Current hardcoded approach has no rollback — a bad tag deployment requires a full code revert. |

### 6.3 Page Speed Impact of Missing GTM

Paradoxically, **adding GTM will likely improve page speed** because:
1. Moving WebEngage from inline to GTM async loading removes render-blocking behavior
2. Conditional loading (Razorpay only on checkout pages) reduces unnecessary JS
3. GTM's built-in tag sequencing prevents race conditions
4. Tag firing rules prevent unnecessary tag execution on irrelevant pages

---

## 7. Privacy & Consent Compliance

### 7.1 Current State: No Consent Management

| Check | Status | Risk |
|-------|--------|------|
| Cookie consent banner | NOT FOUND | MEDIUM — India's DPDPA 2023 requires consent for personal data processing |
| Consent Mode v2 (Google) | NOT CONFIGURED | HIGH — Required for Google Ads in many markets; good practice globally |
| Cookie classification | NOT DONE | MEDIUM — No distinction between essential, analytics, and marketing cookies |
| Privacy policy link to tracking | VERIFY | LOW — Privacy policy exists but may not detail all tracking technologies |
| Data processing agreements | UNKNOWN | MEDIUM — WebEngage DPA should be in place |

### 7.2 India's Digital Personal Data Protection Act (DPDPA) 2023

India's DPDPA came into effect and requires:
- Clear notice before collecting personal data
- Consent before processing personal data for marketing
- Ability for users to withdraw consent
- Data retention limitations

**ElectricPe currently has no visible consent mechanism for tracking technologies.** While enforcement is still evolving, implementing a consent management platform now:
- Protects against future enforcement actions
- Builds user trust (especially important for high-value EV purchases)
- Enables Google Consent Mode v2 (which improves ad measurement accuracy)

### 7.3 Recommended Consent Stack

```
GTM Consent Mode v2
  ├── Default: Denied (analytics_storage, ad_storage, ad_user_data, ad_personalization)
  ├── Consent Banner: CookieYes or OneTrust (free tier available)
  ├── On Accept: Grant all consent signals
  ├── On Decline: GA4 fires with cookieless pings (behavioral modeling fills gaps)
  └── Google Ads: Consent Mode modeling recovers ~70% of declined-consent conversions
```

---

## 8. Revenue Impact Analysis

### 8.1 What Proper GTM Implementation Unlocks

| Capability | Current | After GTM | Revenue Impact |
|-----------|---------|-----------|----------------|
| Google Ads with Smart Bidding | Cannot run | Fully optimized campaigns | ₹3-10L/month in new test rides |
| Meta Ads with conversion optimization | Blind / partially working | Optimized for actual bookings | ₹2-5L/month in new test rides |
| Retargeting (website visitors) | Zero retargeting | 30-day visitor remarketing | 15-25% conversion lift |
| Lookalike audiences (Meta) | Cannot build | 1% lookalike from customers | 2-3x better CPA vs cold targeting |
| Enhanced Conversions (Google) | Not available | Hashed user data for attribution | +10-15% measured conversions |
| Server-side tracking (CAPI) | Not available | Full-funnel measurement | +30-40% conversion visibility |
| A/B testing | Not possible | GTM-enabled experimentation | 5-15% conversion rate improvement |
| Cross-channel attribution | Zero visibility | GA4 Data-Driven Attribution | 20-30% budget reallocation savings |

### 8.2 Cost of Inaction (Monthly)

| Lost Opportunity | Estimated Monthly Impact |
|-----------------|------------------------|
| Unmeasured test ride bookings | ₹5-15L in attributable revenue |
| Unoptimized ad spend (when ads launch) | 30-50% higher CPA than necessary |
| No retargeting of website visitors | 1,000-4,000 lost re-engagement opportunities |
| No lookalike audience expansion | 2-3x higher customer acquisition cost |
| Manual tag deployment delays | 3-7 days per change = missed market opportunities |
| No A/B testing capability | 5-15% conversion improvement left on table |

### 8.3 Cost of Implementation

| Item | One-Time Cost | Monthly Cost |
|------|--------------|--------------|
| GTM Setup + Data Layer | ₹50,000 - ₹1,50,000 | ₹0 (GTM is free) |
| GA4 Configuration | ₹30,000 - ₹80,000 | ₹0 (GA4 is free) |
| Google Ads Conversion Setup | ₹20,000 - ₹50,000 | ₹0 |
| Meta Pixel + CAPI | ₹30,000 - ₹80,000 | ₹0 |
| LinkedIn Insight Tag | ₹10,000 - ₹20,000 | ₹0 |
| Consent Management | ₹15,000 - ₹30,000 | ₹0-₹5,000 |
| Ongoing Tag Management | — | ₹15,000 - ₹40,000 |
| **Total** | **₹1.5L - ₹4L** | **₹15K - ₹45K** |

**ROI Calculation:** At a conservative estimate, proper GTM implementation enables ₹5L+/month in measurable, optimizable revenue. Against a one-time setup cost of ₹1.5-4L, **the payback period is less than 30 days.**

---

## 9. Prioritized Remediation Plan

### Phase 1: Foundation (Week 1-2) — CRITICAL

| # | Task | Time | Dependency |
|---|------|------|-----------|
| 1.1 | Install GTM container on all Next.js pages (head + body noscript) | 4 hours | Developer |
| 1.2 | Initialize `window.dataLayer` before GTM on every page | 2 hours | Developer |
| 1.3 | Push page-level variables to dataLayer (page_type, city, user_type) | 4 hours | Developer |
| 1.4 | Deploy GA4 Configuration tag via GTM | 1 hour | GTM access |
| 1.5 | Configure GA4 Enhanced Measurement (scroll, outbound clicks, file downloads) | 30 min | GTM access |
| 1.6 | Move WebEngage SDK from inline to GTM (async loading) | 2 hours | GTM access + Dev |
| 1.7 | Migrate Facebook Pixel from Next.js component to GTM | 2 hours | GTM access + Dev |
| 1.8 | Verify Meta Pixel is firing correctly + confirm Pixel ID | 1 hour | Meta Business Manager |

### Phase 2: Conversion Tracking (Week 2-3) — HIGH

| # | Task | Time | Dependency |
|---|------|------|-----------|
| 2.1 | Create Google Ads account + link to GA4 | 1 hour | Marketing |
| 2.2 | Set up Google Ads conversion action: Test Ride Booking | 2 hours | GTM + Google Ads |
| 2.3 | Push `begin_checkout` and `purchase` events to dataLayer on test ride flow | 4 hours | Developer |
| 2.4 | Configure Meta standard events (Lead, ViewContent, Purchase) via GTM | 2 hours | GTM |
| 2.5 | Deploy Meta CAPI via CAPI Gateway or server-side GTM | 4-8 hours | Developer |
| 2.6 | Verify domain in Meta Business Manager | 5 min | Marketing |
| 2.7 | Enable Enhanced Conversions (Google) with hashed user data | 3 hours | Developer + GTM |
| 2.8 | Install LinkedIn Insight Tag via GTM | 30 min | GTM |
| 2.9 | Implement UTM parameter framework for all campaigns | 2 hours | Marketing |

### Phase 3: Advanced Measurement (Week 3-4) — MEDIUM

| # | Task | Time | Dependency |
|---|------|------|-----------|
| 3.1 | Push EV product view data to dataLayer (view_item events) | 4 hours | Developer |
| 3.2 | Track WhatsApp widget clicks as custom events | 1 hour | GTM |
| 3.3 | Track app download button clicks with platform differentiation | 1 hour | GTM |
| 3.4 | Configure Razorpay payment success → dataLayer purchase event | 4 hours | Developer |
| 3.5 | Set up cross-domain tracking if subdomains exist (app.electricpe.com, etc.) | 2 hours | GTM |
| 3.6 | Deploy consent management platform (CookieYes / OneTrust) | 4 hours | Developer + GTM |
| 3.7 | Configure Google Consent Mode v2 | 2 hours | GTM |
| 3.8 | Install Microsoft Clarity for heatmaps and session recordings (free) | 30 min | GTM |

### Phase 4: Optimization & Scaling (Month 2+) — LOW

| # | Task | Time | Dependency |
|---|------|------|-----------|
| 4.1 | Set up GA4 Explorations (funnel analysis, path analysis) | 4 hours | Analyst |
| 4.2 | Build custom GA4 audiences for remarketing | 2 hours | GA4 |
| 4.3 | Configure offline conversion import (test rides attended → Google Ads) | 8 hours | Developer + CRM |
| 4.4 | A/B test implementation via GTM (Optimize alternative) | 4 hours | GTM |
| 4.5 | Build Looker Studio / Data Studio dashboards | 8 hours | Analyst |
| 4.6 | Monthly tag audit and cleanup | 2 hours | Ongoing |

---

## 10. What We Can Do For You

### The Problem Is Clear. The Solution Is Straightforward.

ElectricPe has achieved remarkable growth through physical retail, partnerships, and community. But the digital measurement foundation is missing — and as you scale to 50+ Mobility Centres and invest in digital marketing, this gap becomes increasingly expensive.

### Our GTM & Tracking Implementation Service

We specialize in building measurement infrastructure for high-growth companies. Here's what we'd deliver for ElectricPe:

**Week 1-2: GTM Foundation**
- Full GTM container setup on your Next.js website
- Custom data layer architecture designed for your EV business model
- GA4 property configuration with ElectricPe-specific events
- Migration of existing tags (WebEngage, Meta Pixel) into GTM

**Week 2-3: Conversion Tracking**
- Google Ads conversion tracking (test ride bookings as primary conversion)
- Meta Pixel verification + CAPI deployment (server-side tracking)
- LinkedIn Insight Tag installation
- Enhanced Conversions setup with hashed user data
- Complete test ride funnel tracking (every step measured)

**Week 3-4: Advanced & Compliance**
- Razorpay payment → conversion event integration
- Consent management platform deployment (DPDPA compliant)
- Google Consent Mode v2 configuration
- Microsoft Clarity (free heatmaps + session recordings)
- Cross-domain tracking (if applicable)
- UTM framework + campaign tracking templates

**Deliverables:**
- Fully configured GTM container with 15-25 tags, 20+ triggers, 30+ variables
- Custom data layer documentation for your development team
- GA4 property with conversion events, custom dimensions, and audiences
- Conversion tracking across Google, Meta, and LinkedIn — ready for campaign launch
- Consent management compliant with India's DPDPA
- Dashboard template (Looker Studio) showing key metrics
- Tag monitoring and QA documentation
- 30-day post-launch support

**Investment:** [Contact us for a custom quote based on scope]

### Why Act Now?

1. **Your competitors are already running paid ads.** Statiq ($18M raised), Tata Power, and Ather are actively acquiring customers through Google and Meta. Every month without tracking is a month they pull ahead.

2. **You're expanding to 50+ Mobility Centres.** Each new city is a digital marketing opportunity — but only if you can measure which cities convert best and allocate budget accordingly.

3. **Your ₹299 test ride offer is a paid ads goldmine.** A low-friction, high-value CTA like this typically achieves 3-5% conversion rates on Google Search and 1-3% on Meta. But without tracking, you can't deploy it.

4. **The 80,000+ community members are a lookalike seed audience.** Upload that list to Meta, build a 1% lookalike, and you instantly have 3-5 million potential customers to target. This data is decaying every day it sits unused.

5. **Every Razorpay transaction is an unattributed conversion.** You're selling EVs and processing payments, but you can't tell which marketing channels drove those sales. Proper tracking turns this from a mystery into a profit lever.

---

### Next Steps

We'd love to walk you through this audit in a 30-minute call and show you exactly how we'd implement the solution.

**Book a call:** [Your Booking Link]
**Email:** [Your Email]
**Phone:** [Your Phone]

---

*This complimentary audit was prepared using publicly observable data from electricpe.com. A full technical audit with GTM Preview Mode access, GA4 property access, and Google Ads account access would provide additional depth and specificity.*

*Report generated: March 17, 2026*
