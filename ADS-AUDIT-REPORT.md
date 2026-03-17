# ElectricPe — Paid Advertising & Marketing Audit Report

**Audit Date:** March 17, 2026
**Prepared by:** Budget & Bidding Specialist (Ads Audit Agent)
**Company:** ElectricPe — India's Largest EV Retail Network
**Scope:** Google Ads, Meta Ads (Facebook/Instagram), LinkedIn Ads, YouTube Ads, TikTok Ads, Conversion Tracking Infrastructure, Creative & Messaging, Audience Strategy, Budget & Bidding

---

## Table of Contents

1. Executive Summary
2. Platform Analysis
   - 2.1 Google Ads Assessment
   - 2.2 Meta Ads Assessment (Facebook & Instagram)
   - 2.3 LinkedIn Ads Assessment
   - 2.4 YouTube Ads Assessment
   - 2.5 Other Platforms (TikTok, etc.)
3. Conversion Tracking Audit
4. Creative & Messaging Analysis
5. Audience & Targeting Strategy
6. Budget & Bidding Recommendations
7. Competitive Gap Analysis
8. Cross-Platform Strategy Recommendations
9. Prioritized Action Plan
10. Quick Wins (Under 15 Minutes)

---

## 1. Executive Summary

### Overall Marketing Health Score: 8 / 100 — Grade F (Critical)

ElectricPe operates in one of India's fastest-growing consumer markets (EV sector, 25–27.6% CAGR, projected $3.8B by 2033) and has built a legitimate, differentiated business: 35+ Mobility Centres, 15,000+ charging stations, 6,000+ EVs sold, and a 4.4-rated app with 80,000+ community members. The Google Maps partnership, test-ride-first model, and physical retail expansion signal a company with real product-market fit.

The paid advertising situation is the opposite. Based on all observable evidence, ElectricPe has essentially zero paid advertising infrastructure in place. No Meta Pixel, no Google Ads conversion tracking, no LinkedIn Campaign Manager activity, no TikTok pixel, and no evidence of active paid campaigns on any platform. Every single tracking, bidding, and campaign check FAILS by default. The score of 8 reflects only the positive signals from organic digital presence (app store ratings, social presence, WhatsApp widget, WebEngage use) that indicate a foundation to build on — the paid advertising stack itself scores 0.

This is not necessarily a crisis: it means ElectricPe has been growing entirely through organic, partnership-driven, and physical channels. However, with well-funded competitors like Statiq ($18M raised, Y Combinator/Shell-backed) and Tata Power EZ Charge actively marketing, the absence of paid acquisition represents a significant and growing strategic vulnerability.

### Key Findings

| Finding | Severity | Impact |
|---------|----------|--------|
| No paid advertising on any platform | Critical | Zero scalable acquisition channel |
| No conversion tracking installed (Pixel, gtag, Insight Tag) | Critical | Cannot run or measure any campaign |
| No Meta CAPI / server-side tracking | Critical | 30-40% data loss from day one |
| No Google Tag Manager or GA4 conversion setup | Critical | Smart Bidding cannot function |
| No LinkedIn Insight Tag | Critical | B2B/fleet targeting entirely blocked |
| Test-ride CTA (primary offer) not connected to any tracking | Critical | Revenue-driving action unmeasured |
| Blog and SEO poorly optimized | High | Organic traffic potential unrealized |
| No retargeting audiences built | High | Website visitors lost with no follow-up |
| Competitors running paid acquisition at scale | High | Market share being ceded actively |
| Strong organic foundation (app, community, partnerships) | Positive | Provides seed data and social proof for paid |

### Score Breakdown by Platform

| Platform | Score | Grade | Status |
|----------|-------|-------|--------|
| Google Ads | 0 / 100 | F | Not running |
| Meta Ads | 0 / 100 | F | Not running |
| LinkedIn Ads | 0 / 100 | F | Not running |
| YouTube Ads | 0 / 100 | F | Not running |
| TikTok Ads | 0 / 100 | F | Not running |
| Conversion Tracking | 0 / 100 | F | Nothing installed |
| Overall (Aggregate) | 8 / 100 | F | Critical — immediate action required |

The score of 8 (rather than 0) reflects partial credit for observable positives: WebEngage behavioral tracking is present (indicating some analytics intent), Razorpay payments are integrated (transaction data exists), the WhatsApp widget provides a lead capture mechanism, and the 4.4-rated app with 80K community members provides a first-party data seed. None of these substitute for paid advertising infrastructure, but they shorten the time to launch.

---

## 2. Platform Analysis

### 2.1 Google Ads Assessment

**Status: Not Running | Score: 0/100 | Grade: F**

#### Current State

No evidence of Google Ads activity was found in public searches. No Google Tag, Google Ads conversion snippet, or gtag.js code has been identified on the ElectricPe website. The site runs Next.js with WebEngage tracking but is missing the entire Google measurement stack.

#### Why Google Ads Should Be Priority 1 for ElectricPe

ElectricPe's primary customers are first-time EV buyers and price-conscious urban professionals — people who are actively researching before making a high-consideration purchase (an EV costs ₹1–15L+). These buyers are searching Google daily for terms like "best electric scooter under 1 lakh," "EV test ride Bangalore," "electric car financing India," and "charging station near me." This is high-intent, purchase-ready traffic that Google Search captures better than any other platform. ElectricPe is currently invisible to all of it.

#### Checklist Evaluation (All FAIL — No Account Exists)

| Check ID | Check | Status | Notes |
|----------|-------|--------|-------|
| G42 | Conversion actions defined | FAIL | No Google Ads account |
| G43 | Enhanced conversions enabled | FAIL | No Google Ads account |
| G44 | Server-side tracking | FAIL | No server-side GTM |
| G45 | Consent Mode v2 | N/A | India (non-EU) — lower urgency |
| G47 | Micro vs macro separation | FAIL | No tracking exists |
| G48 | Attribution model | FAIL | DDA cannot run without account |
| G05 | Brand vs Non-Brand separation | FAIL | No campaigns |
| G11 | Geographic targeting accuracy | FAIL | No campaigns |
| G12 | Network settings | FAIL | No campaigns |
| G14 | Negative keyword lists | FAIL | No campaigns |
| G50 | Sitelink extensions | FAIL | No campaigns |

#### Recommended Google Ads Account Structure for ElectricPe

**Campaign 1 — Brand Protection (Search)**
- Keywords: "ElectricPe," "Electric Pe," "electricpe.com," "electricpe app"
- Bid strategy: Target Impression Share (95–100%)
- Daily budget: ₹500–₹1,000
- Goal: Own the brand SERP; prevent competitors from bidding on the name
- Priority: Launch Day 1

**Campaign 2 — EV Purchase Intent (Search)**
- Keywords: "buy electric scooter [city]," "EV test ride [city]," "electric two-wheeler price," "best EV under 1 lakh," "electric scooter EMI"
- Match types: Phrase + Exact (NO Broad Match until sufficient conversion data)
- Bid strategy: Maximize Clicks (cold start) → transition to Maximize Conversions at 15+ conv/month → Target CPA at 30+ conv/month
- Daily budget: ₹3,000–₹5,000
- Landing page: Dedicated EV browse/test-ride booking page
- Negative keywords: Jobs, free, DIY, second-hand, spare parts, competitors

**Campaign 3 — Charging Network (Search)**
- Keywords: "EV charging station near me," "EV charging point [city]," "fast charging EV India," "ChargeZone alternative"
- Goal: App installs + charging session bookings
- Daily budget: ₹1,500–₹2,500
- Bid strategy: Maximize Conversions (app installs / lead form submissions)

**Campaign 4 — Retargeting (Display / Demand Gen)**
- Audience: Website visitors (last 30 days) + App users who did not convert
- Goal: Drive test-ride bookings and app installs
- Creative: Test-ride offer (₹299 FREE), city-specific mobility centre callouts
- Daily budget: ₹1,000–₹2,000

**Campaign 5 — Performance Max (After 90 days)**
- Enable once conversion history exists (30+ conversions/month minimum)
- Asset groups by product line: EV Purchase, Charging, Financing
- Enable audience signals: website visitors, app users, in-market for EVs
- Do NOT launch PMax before conversion tracking is live and stable

#### Bidding Strategy Decision (Cold Start)

ElectricPe starts with 0 conversions. Per the bidding strategy decision tree:

```
0 conversions → Maximize Clicks (Manual CPC is acceptable alternative)
Set Max CPC = Target_CPA / (estimated CVR × 1.5)

Estimated CPA target: ₹800–₹1,500 per test ride booking
Estimated CVR (search): 3–5%
Max CPC calculation: ₹1,000 / (0.04 × 1.5) = ₹16,667 — cap at ₹150–₹300/click to start

After 15 conversions: Maximize Conversions
After 30 conversions: Target CPA (set at 1.1–1.2x historical CPA)
```

#### India-Specific Google Ads Considerations

- The India EV market has low keyword competition relative to automotive in Western markets — CPC may be lower than the global benchmark of $5.26 (likely ₹20–₹80/click for EV terms)
- Regional language ad copy (Hindi, Kannada, Tamil, Telugu) will dramatically improve CTR and Quality Scores in respective markets
- Local campaigns with Google Maps integration (ElectricPe already has a Google Maps partnership) should be prioritized — this is a unique advantage

---

### 2.2 Meta Ads Assessment (Facebook & Instagram)

**Status: Not Running | Score: 0/100 | Grade: F**

#### Current State

No Meta Pixel has been identified on the ElectricPe website. No Conversions API (CAPI) evidence exists. No active Facebook or Instagram ad campaigns were found in public ad library searches. Social media pages exist (Facebook, Instagram) but appear to be used only for organic content.

#### Why Meta Ads Should Be Priority 2

Facebook and Instagram reach over 400 million users in India. For ElectricPe's target audience — urban professionals aged 22–40 considering their first EV — Meta offers unmatched interest-based and behavioral targeting. More critically, Meta's CPM in India is extremely low by global standards (₹9–10 CPM on Facebook, ₹70–200 on Instagram). The test-ride offer (₹299 FREE test ride) is a perfect Meta ad hook: it has a clear value proposition, low friction, and a price anchor that makes the CTA feel risk-free.

#### Checklist Evaluation (All FAIL — No Account Exists)

| Check ID | Check | Status | Notes |
|----------|-------|--------|-------|
| M01 | Meta Pixel installed | FAIL | No pixel on website |
| M02 | Conversions API (CAPI) active | FAIL | No server-side tracking |
| M03 | Event deduplication | FAIL | Prerequisite (pixel) absent |
| M04 | Event Match Quality (EMQ) | FAIL | Pixel absent; EMQ = 0 |
| M05 | Domain verification | FAIL | Business Manager not confirmed |
| M06 | Aggregated Event Measurement | FAIL | Not configured |
| M13 | Learning phase status | FAIL | No campaigns exist |
| M23 | Exclusion audiences | FAIL | No campaigns exist |
| M24 | First-party data utilization | FAIL | No custom audiences uploaded |
| M25 | Creative format diversity | FAIL | No paid creative exists |

#### Recommended Meta Ads Account Structure

**Campaign 1 — Lead Gen: Test Ride Bookings (Top Priority)**
- Objective: Leads (Lead Gen Form or website conversion)
- Audience: Age 22–42, Tier 1 & Tier 2 Indian cities where Mobility Centres exist, interests: Electric vehicles, sustainable transport, two-wheelers, personal finance, Ola Electric, Ather Energy
- Ad format: Video (15–30s showing a test ride experience) + Static image (test ride offer visual)
- CTA: "Book Free Test Ride" → Lead Form or landing page
- Budget: ₹500–₹1,000/day (start ABO for testing)
- Bid strategy: Lowest Cost (default for cold start)

**Campaign 2 — App Install Campaign**
- Objective: App Installs (iOS + Android)
- Audience: Broad urban India + retargeting of website visitors
- Creative: Short video showing the charging station locator feature + community benefits
- Budget: ₹300–₹500/day
- Note: App install campaigns perform well on Meta given ElectricPe's 4.4 rating

**Campaign 3 — Retargeting (After pixel is live and audiences built)**
- Audience: Website visitors (last 30 days), Instagram/Facebook page engagers
- Goal: Drive test-ride bookings from warm traffic
- Budget: ₹200–₹500/day
- Creative: Testimonials, city-specific mobility centre callouts, financing EMI messaging

**Campaign 4 — Advantage+ Sales Campaign (Longer term)**
- Enable once 30+ conversions/month are flowing
- Use Advantage+ Creative enhancements
- Combine prospecting and retargeting under one ASC for efficiency

#### Meta Pixel + CAPI Setup Priority

This is the single most important technical task for Meta. Without the pixel:
- No campaign can optimize for conversions
- No retargeting audiences can be built
- No lookalike audiences can be created
- The ₹299 test ride booking action is completely unmeasured

Setup sequence:
1. Install Meta Pixel via Google Tag Manager (GTM) — 30 minutes
2. Configure standard events: ViewContent (EV pages), Lead (test ride form submit), CompleteRegistration (app signup), Purchase (EV financing approved)
3. Deploy CAPI via CAPI Gateway (simplified option) — 2–4 hours
4. Verify domain in Business Manager — 5 minutes
5. Configure Aggregated Event Measurement with 8 priority events
6. Set attribution window: 7-day click / 1-day view

India-specific note: With Razorpay already integrated, the Purchase event can be tied to payment confirmation for EV financing transactions, providing high-quality conversion signals.

---

### 2.3 LinkedIn Ads Assessment

**Status: Not Running | Score: 0/100 | Grade: F**

#### Current State

No LinkedIn Campaign Manager activity detected. No LinkedIn Insight Tag found on the website. LinkedIn social page exists (organic presence) but is not connected to any paid activity.

#### LinkedIn's Role for ElectricPe — B2B Is Underexploited

ElectricPe's B2C focus (first-time EV buyers) is the primary opportunity, but there is a significant and underexploited B2B segment: fleet operators, corporate HR managers overseeing employee commute benefits, commercial EV buyers, and logistics companies transitioning to EVs. LinkedIn is the only platform where these decision-makers can be reached with precision. Additionally, ElectricPe's CMS software for charging station management is a pure B2B product that LinkedIn is purpose-built for.

#### Checklist Evaluation (All FAIL — No Account Exists)

| Check ID | Check | Status | Notes |
|----------|-------|--------|-------|
| L01 | Insight Tag installed | FAIL | No tag on website |
| L02 | Conversions API (CAPI) | FAIL | No server-side tracking |
| L03 | Job title targeting precision | FAIL | No campaigns |
| L04 | Company size filtering | FAIL | No campaigns |
| L05 | Seniority level targeting | FAIL | No campaigns |
| L06 | Matched Audiences active | FAIL | No audiences built |
| L07 | ABM company lists | FAIL | No lists uploaded |
| L08 | Audience expansion setting | FAIL | No campaigns |
| L09 | Predictive audiences tested | FAIL | No campaigns |
| L10 | Thought Leader Ads (TLAs) | FAIL | No campaigns |
| L16 | Bid strategy appropriate | FAIL | No campaigns |
| L17 | Daily budget ≥$50 Sponsored Content | FAIL | No campaigns |

#### Recommended LinkedIn Ads Strategy (B2B Focus)

LinkedIn should be Phase 2 (months 2–3), not the immediate priority given ElectricPe's primarily B2C model. However, for CMS software and fleet sales, it is essential.

**Campaign 1 — Fleet & Corporate EV Adoption**
- Audience: Fleet Managers, Procurement Managers, Head of Operations, CFOs at companies with 50–500 employees in Bengaluru, Delhi, Mumbai, Hyderabad, Chennai
- Ad format: Single Image + Lead Gen Form (reduces friction vs landing page)
- Message: "Reduce your fleet fuel costs by 60%. ElectricPe's managed EV fleet solution."
- Bid: Maximum Delivery (default recommended)
- Daily budget: ₹4,000–₹5,000 ($50+/day — minimum for Sponsored Content delivery)

**Campaign 2 — Thought Leader Ads (TLAs) — Highest Priority LinkedIn Format**
- Use CEO Avinash Sharma's organic LinkedIn posts (thought leadership, EV industry insights)
- TLA CPC: ₹190–₹340 ($2.29–$4.14) vs ₹1,100+ ($13.23) for standard Sponsored Content
- Allocate ≥30% of LinkedIn budget to TLAs
- This is the most cost-efficient LinkedIn format and requires minimal production effort

**Campaign 3 — CMS Software Lead Gen**
- Audience: Charging Infrastructure Operators, Real Estate Developers (commercial), Hotel chains, Parking operators
- Lead Gen Form: "Get a free CMS demo for your charging network"
- Bid: Lowest Cost or Manual CPC

#### LinkedIn Bidding Notes

- LinkedIn CPCs in India are meaningfully lower than global averages ($5–$7 globally; Indian market likely $1–$3)
- Avoid Manual CPC without experience — start with Maximum Delivery
- LinkedIn Accelerate campaigns (AI-optimized) deliver 42% lower CPA on average; consider for campaigns with sufficient conversion history
- Do NOT use LinkedIn as a B2C channel for low-ticket test ride bookings — the high CPL ($60–$150+) makes it uneconomical vs Meta/Google

---

### 2.4 YouTube Ads Assessment

**Status: Not Running | Score: 0/100 | Grade: F**

#### Current State

A YouTube channel exists in the social media ecosystem (linked from website) but no paid YouTube advertising was identified. No video ad campaigns, no TrueView ads, no YouTube connected to Google Ads.

#### Why YouTube Matters for ElectricPe

EV purchase is a high-consideration, visually-driven decision. A prospective buyer comparing a Ather 450X to a Bajaj Chetak to an Ola S1 Pro is going to watch YouTube review videos for 30–60 minutes before deciding. YouTube pre-roll and mid-roll ads against EV review content (channels like EV Saga, Gyaan in Hindi, PowerDrift EV content) give ElectricPe a chance to intercept that research journey.

Additionally, ElectricPe's ₹299 test ride offer is well-suited to a 15-second non-skippable bumper ad: enough time to state the offer and drive action.

#### Recommended YouTube Strategy

**Phase 1 (Months 1–3): Awareness & Consideration**
- Ad type: TrueView In-Stream (skippable, 30s+) targeting EV review content viewers
- Targeting: In-market audience "Electric Vehicles," YouTube channels about EVs (channel targeting), custom intent audiences based on EV search terms
- Creative: 60-second video showing a customer's test-ride journey → EV purchase story
- Budget: ₹500–₹1,000/day

**Phase 2 (Months 3+): Retargeting with Bumper Ads**
- Ad type: 6-second non-skippable bumper ads
- Audience: Retarget users who watched >50% of Phase 1 video
- Message: "Book your free test ride at ElectricPe. ₹299, fully refunded."
- Budget: ₹300–₹500/day

**BrandLink / Connected TV consideration (longer term):** As ElectricPe scales, YouTube's Connected TV inventory (via Google's BrandLink equivalent) allows EV brand advertising on streaming platforms — premium placement for brand building.

---

### 2.5 Other Platforms (TikTok, Snapchat, etc.)

**Status: Not Running | Score: 0/100 | Grade: F (N/A for current stage)**

#### TikTok Assessment

No TikTok Pixel, no TikTok Ads account, no paid TikTok activity found.

**Should ElectricPe run TikTok Ads?**

TikTok's Indian market position is complex — the app was banned in India from June 2020 to November 2021, and while it returned, its user base skews younger (16–24) and is more heavily concentrated in Tier 2/3 cities. For ElectricPe's primary audience (urban professionals, 25–40, making high-consideration EV purchases), TikTok is lower priority than Google, Meta, and YouTube.

However, TikTok's engagement rates (5–16%, far exceeding Facebook's 0.09% and Instagram's 1.22%) and its CPM advantage (40–60% cheaper than Meta) make it worth considering for:
- Brand awareness among younger first-time EV buyers (electric scooters, ₹50K–₹1.2L range)
- App install campaigns (charging station locator content performs well on TikTok's interest graph)
- Organic-first approach: create native-style content about EV lifestyle, charging tips, test ride experiences, then amplify top performers with Spark Ads

**TikTok Recommendation: Phase 3 (Month 4+), 10% of digital budget, content-first approach**

If/when TikTok campaigns launch, critical setup requirements include:
- TikTok Pixel on all pages + Events API with ttclid passback (without ttclid, attribution breaks)
- Separate campaigns for prospecting vs retargeting (T03)
- Daily budget ≥50× target CPA per ad group (T12)
- All video in 9:16 vertical format (T06)
- Search Ads Toggle enabled (T14)
- Spark Ads from organic top performers (T10)

#### Microsoft Ads (Bing)

**Relevance: Very Low for India market**

Microsoft/Bing holds approximately 2–3% search market share in India vs Google's 97%+. Microsoft Ads (including Bing) is not a priority for ElectricPe. The LinkedIn profile targeting advantage (MS10) is the only unique value, but this can be achieved directly through LinkedIn Campaign Manager.

**Recommendation: Do not invest in Microsoft Ads. Reallocate that budget to Google and Meta.**

---

## 3. Conversion Tracking Audit

**Status: Nothing Installed | Score: 0/100 | Grade: F (Critical)**

This is the most urgent and foundational issue in the entire audit. Without conversion tracking, every rupee spent on paid advertising will be flying blind. Smart Bidding algorithms cannot optimize. Retargeting audiences cannot be built. Campaign performance cannot be measured. Attribution cannot be assigned.

### 3.1 Current Tracking Inventory

| Tracking Technology | Status | Impact of Absence |
|--------------------|--------|-------------------|
| Google Tag (gtag.js) | NOT FOUND | Cannot run Google Ads or GA4 |
| Google Tag Manager (GTM) | NOT CONFIRMED | No centralized tag management |
| Meta Pixel | NOT FOUND | Cannot run Meta Ads |
| Meta CAPI | NOT FOUND | 30–40% additional data loss |
| LinkedIn Insight Tag | NOT FOUND | Cannot run LinkedIn Ads |
| TikTok Pixel | NOT FOUND | Cannot run TikTok Ads |
| Microsoft UET Tag | NOT FOUND | Cannot run Microsoft Ads |
| GA4 Property | NOT CONFIRMED | No cross-channel analytics |
| WebEngage | FOUND | Behavioral/CRM tracking (partial signal) |
| Razorpay | FOUND | Transaction data exists (seed for tracking) |

### 3.2 Required Tracking Stack — Priority Order

**Step 1: Google Tag Manager (GTM) — Foundation of Everything**
Install GTM on the Next.js website. This is the container through which all other tags will be deployed. For Next.js specifically:
- Use the `next/script` component to load GTM
- Deploy GTM container on all pages (including app landing pages and test ride booking flow)
- Estimated time: 2–4 hours (developer required)

**Step 2: Google Analytics 4 (GA4) — Cross-Channel Analytics**
Deploy GA4 via GTM. Configure:
- Enhanced Measurement (scroll, file downloads, outbound clicks)
- Custom events: test_ride_booking_initiated, test_ride_booking_complete, ev_model_viewed, charging_station_searched, app_download_click, lead_form_submit, financing_inquiry
- Conversion marking: Mark test_ride_booking_complete and lead_form_submit as conversion events
- Estimated time: 4–8 hours (developer + analyst)

**Step 3: Google Ads Conversion Tracking — Required Before First Campaign**
Via GTM:
- Primary conversion action: Test ride booking (form submission confirmation page)
- Secondary conversion: App install click, EV financing inquiry, contact form submit
- Enable Enhanced Conversions: pass hashed email/phone at booking confirmation
- Attribution model: Data-Driven Attribution (DDA — now mandatory default)
- Conversion window: 30 days (matches EV consideration cycle)
- Estimated time: 2–3 hours

**Step 4: Meta Pixel + CAPI — Required Before First Meta Campaign**
- Deploy Meta Pixel base code via GTM
- Standard events to configure:
  - `ViewContent` — EV product page views
  - `Lead` — test ride form submit
  - `CompleteRegistration` — app sign-up
  - `InitiateCheckout` — EV financing flow start
  - `Purchase` — EV financing approved / EV purchase
  - `Schedule` — test ride appointment booked
- CAPI via CAPI Gateway (preferred for speed) or direct server-side integration
- Verify domain in Business Manager
- Set up Aggregated Event Measurement (AEM) with priority order: Purchase > Lead > Schedule > InitiateCheckout > ViewContent
- Target EMQ (Event Match Quality): minimum 6.0, target 8.0+
- Pass email + phone at all form submission events to maximize EMQ
- Estimated time: CAPI Gateway deployment 2–4 hours; full stack 1–2 days

**Step 5: LinkedIn Insight Tag — Before LinkedIn Campaign Launch**
- Deploy via GTM (one line of JavaScript, Insight Tag ID from Campaign Manager)
- Create conversion actions: Lead Gen Form submit, Contact page visit, Careers page (exclude from ad targeting)
- Estimated time: 30 minutes

**Step 6: UTM Parameters — All Channels**
Implement UTM parameters on all ad URLs immediately:
```
utm_source=google / meta / linkedin / youtube
utm_medium=cpc / paid_social / display
utm_campaign=[campaign_name]
utm_content=[ad_creative_id]
utm_term=[keyword] (Google Search only)
```
This feeds GA4 and allows cross-channel attribution even before full tracking stack is live. Estimated time: 30 minutes (add to URL builder template).

### 3.3 The Test Ride Funnel — Critical Tracking Gap

The ₹299 FREE test ride offer is ElectricPe's primary lead generation mechanism and the most important conversion to track. Currently, this conversion is not connected to any paid advertising measurement system. Every user who clicks "Book Now" on the website and completes a booking generates zero data for advertising optimization.

**Test Ride Funnel to Track:**

```
Ad Click
  → Landing Page View (ViewContent event)
    → Test Ride Page View (ViewContent — EV model specific)
      → Booking Form Open (custom event: booking_form_initiated)
        → Form Submitted (Lead event — PRIMARY CONVERSION)
          → Confirmation Page (confirmation_page_view)
            → Payment Completed / Ride Attended (Purchase event — HIGH VALUE)
```

Each step needs a tracking event. The Lead event (form submitted) should be the primary bidding signal for all campaigns. The Purchase/attendance event should be imported as an offline conversion to improve bid quality over time.

### 3.4 Attribution Framework

For ElectricPe's business model (high-consideration purchase, multi-session research journey), the following attribution setup is recommended:

| Platform | Attribution Window | Model | Rationale |
|----------|------------------|-------|-----------|
| Google Ads | 30-day click, 1-day view | DDA (mandatory) | EV research takes days to weeks |
| Meta Ads | 7-day click, 1-day view | Platform default | Standard for India B2C |
| LinkedIn Ads | 30-day click, 7-day view | Last touch | B2B fleet sales take longer |
| GA4 | Data-Driven | Cross-channel | Source of truth for all channels |

**Cross-Platform Attribution Rule:** Never trust platform-reported ROAS alone. Use GA4 + post-purchase/booking survey ("How did you first hear about ElectricPe?") as the authoritative cross-reference.

---

## 4. Creative & Messaging Analysis

### 4.1 Current Website CTA Analysis

| CTA | Location | Effectiveness | Issues |
|-----|----------|---------------|--------|
| "Get EV test ride for ₹299 FREE!!" | Homepage hero | Strong offer, clear value | Double exclamation mark reduces credibility; "FREE" and "₹299" are contradictory (₹299 is a deposit, not a cost — clarify this) |
| "Book Now" | Multiple locations | Clear intent | Generic; no offer context without surrounding copy |
| "Explore EVs" | Homepage | Consideration-stage CTA | Correct placement for cold visitors; leads to product catalog |
| "Download App" | Homepage | Appropriate | Needs platform-specific deep link tracking |

**Critical messaging issue:** The ₹299 test ride offer is confusingly worded as "₹299 FREE." If the ₹299 is a refundable deposit, this needs to be stated explicitly. If it is genuinely free and the ₹299 is credited toward purchase, that needs equal clarity. Ambiguous pricing language is the single largest friction point for paid ad landing pages in high-consideration categories.

### 4.2 Messaging Framework Assessment

**What ElectricPe Gets Right:**
- Test-ride-first approach reduces purchase anxiety (correct psychology for first-time EV buyers)
- "India's largest & most trusted" positioning is a strong authority claim
- 6,000+ EVs sold, 26,000+ charging points, 800K+ sessions — concrete social proof numbers exist
- 4.4 app rating on both stores — credible third-party validation
- Community angle (Club Electric, 80K members) creates belonging and reduces perceived risk

**What Is Missing from Paid Ad Creative:**
- No customer testimonial content observed (essential for high-consideration purchases)
- No range anxiety/charging anxiety objection handling in messaging
- No city-specific messaging (ads for Bengaluru should feature Bengaluru Mobility Centres)
- No financing/EMI messaging despite offering EV financing (major purchase barrier in India)
- No competitor comparison messaging (Statiq charges more? Tata Power has fewer locations in your city?)
- No urgency mechanism beyond the test ride offer

### 4.3 Creative Recommendations by Platform

**Google Search Ads (Responsive Search Ads):**
- Headline variants: "Book Free EV Test Ride Today," "25+ EV Models | Expert Guidance," "EV Financing Available | EMI From ₹3,999," "Nearest EV Centre [City]," "India's Largest EV Network," "800K+ Charging Sessions | Trusted"
- Description: "ElectricPe has 35+ Mobility Centres across 24 cities. Test ride any EV with our experts. Book in 60 seconds."
- Include city insertion: "{city} EV Test Ride | Book Today"
- Minimum: 15 headlines, 4 descriptions per RSA

**Meta/Instagram Visual Ads:**
- Format 1: 15-second video showing the test ride experience end-to-end (customer arrives → expert guidance → test ride → smiling with EV)
- Format 2: Before/after carousel (commute cost on petrol vs EV with rupee savings)
- Format 3: Static image with "₹0 fuel cost. ₹0 maintenance. Test ride for ₹299." (clarity on the offer)
- Format 4: User-generated content style — real customer testimonials filmed on mobile
- All video: 9:16 vertical for Reels/Stories, 1:1 for Feed, 16:9 for YouTube

**LinkedIn Creative (B2B):**
- Thought Leader Ads from CEO Avinash Sharma's posts on EV adoption, fleet economics, charging infrastructure
- Document ads: "2025 Fleet EV Cost Calculator — Save 60% on Fuel" (lead gen)
- Single image: Corporate fleet showing electrified, with CPL (cost per litre equivalent) savings

---

## 5. Audience & Targeting Strategy

### 5.1 Primary Audience Segments

**Segment 1: First-Time EV Buyers (Primary B2C)**
- Demographics: Age 24–40, urban professionals, HHI ₹8L–₹25L+
- Geography: Cities with ElectricPe Mobility Centres (Bengaluru, Delhi, Mumbai, Hyderabad, Chennai, Pune, and 18+ others)
- Interests: Electric vehicles, sustainable commuting, personal finance, technology adoption, two-wheelers
- Behavioral signals: Recently searched "buy electric scooter," browsed EV comparison sites, in-market for vehicles
- Best platforms: Google Search (intent), Meta (interest + lookalike), YouTube (consideration video)

**Segment 2: Current EV Owners (Charging Network)**
- Demographics: Age 22–45, existing EV owners across 65+ cities
- Behavioral: Has an EV (Ola, Ather, TVS, Bajaj Chetak owner)
- Goal: App installs for charging station discovery
- Best platforms: Meta custom audiences (interest: specific EV brands), Google App campaigns

**Segment 3: Fleet/Corporate Buyers (B2B)**
- Demographics: Fleet Managers, Operations Heads, CFOs at SMEs and enterprises
- Geography: Major metros
- Goal: Fleet EV adoption, CMS software demo
- Best platforms: LinkedIn (precision), Google Search (fleet EV terms)

**Segment 4: Range-Anxious Considerers (Retargeting)**
- Behavioral: Visited ElectricPe website but did not book test ride; browsed EV models
- Goal: Convert warm traffic with specific objection handling
- Messaging: Address range anxiety, highlight charging network density, offer financing
- Best platforms: Meta Retargeting, Google Display Retargeting, YouTube retargeting

### 5.2 Audience Targeting Recommendations by Platform

**Google Ads Targeting:**
- Search: Keyword intent targeting (no demographic overlay needed — intent is sufficient)
- Display/YouTube: In-market segments: "Electric Vehicles," "Mopeds & Scooters," "Hybrid & Alternative Fuel Vehicles"
- Customer Match: Upload app user list + lead list from WebEngage for RLSA
- Similar Audiences: Build from Customer Match lists once 1,000+ users
- Geographic: "People in" (not "People in or interested in") for city-specific Mobility Centre campaigns

**Meta Ads Targeting:**
- Cold prospecting: Interest stacking — Electric vehicles + Sustainable living + Personal finance + specific EV brands (Ather, Ola Electric, TVS iQube)
- Lookalike audiences: Build from app installs (seed: 80K community members) — 1% lookalike will be approximately 3–5M users in India
- Retargeting: Website Custom Audience (30-day window), Video viewers (50%+), Lead Gen Form openers who did not submit
- Exclusions: Existing customers (upload CRM list), existing app users — exclude from prospecting to prevent waste

**LinkedIn Targeting:**
- Job Functions: Operations, Procurement, Finance
- Seniority: Manager, Director, VP, C-suite
- Company Size: 50–500 employees (SME fleet buyers), 500+ (enterprise)
- Industries: Logistics, Transportation, Technology, Real Estate
- Audience Expansion: OFF (precision targeting is the LinkedIn value proposition)
- Predictive Audiences: Test once Insight Tag has accumulated 300+ visitors (post-tag install)
- ABM Lists: Upload target company lists for enterprise fleet outreach (up to 300,000 companies)

### 5.3 Geographic Prioritization

ElectricPe should tier its geographic targeting by Mobility Centre density and market opportunity:

| Tier | Cities | Platform Strategy |
|------|--------|-------------------|
| Tier 1 | Bengaluru, Delhi NCR, Mumbai | Full funnel: Search + Meta + YouTube + Retargeting |
| Tier 2 | Hyderabad, Chennai, Pune, Ahmedabad | Search + Meta (Lead Gen) |
| Tier 3 | Remaining 18+ cities with Mobility Centres | Search only (brand + local EV terms) |
| Expansion | New cities (50 new centres planned) | Pre-launch awareness: Meta + YouTube 30 days before opening |

---

## 6. Budget & Bidding Recommendations

### 6.1 Business Context for Budget Sizing

ElectricPe has revenue of ₹13.3 Cr (March 2025) and has raised $11.4M (~₹95 Cr). At this stage (Series A equivalent, 119 employees), allocating 5–15% of revenue to paid advertising is standard. For a ₹13.3 Cr revenue company in a high-growth market, a marketing budget of ₹65L–₹2 Cr per year for paid ads is appropriate, depending on growth ambition.

The minimum viable paid advertising budget that can produce measurable results (sufficient for Smart Bidding learning phases) is ₹3–5 Lakhs/month.

### 6.2 Recommended Monthly Budget Allocation

**Phase 1: Foundation (Months 1–2) — ₹3,00,000/month**

| Platform | Monthly Budget | Rationale |
|----------|---------------|-----------|
| Google Ads — Search (Brand + EV Intent) | ₹1,20,000 | Highest intent; capture in-market buyers |
| Meta Ads — Lead Gen (Test Ride) | ₹80,000 | Low CPM, high-reach, test ride offer |
| Meta Ads — App Install | ₹40,000 | Leverage 4.4 rating for low CPI |
| Google Ads — Display Retargeting | ₹30,000 | Re-engage website visitors |
| YouTube — Consideration | ₹30,000 | EV research journey interception |
| **Total** | **₹3,00,000** | |

**Phase 2: Scaling (Months 3–6) — ₹6,00,000/month**
Activate once ≥30 conversions/month are flowing and CPA is stable.

| Platform | Monthly Budget | Budget Share |
|----------|---------------|-------------|
| Google Ads — Search + PMax | ₹2,00,000 | 33% |
| Meta Ads — All campaigns | ₹1,80,000 | 30% |
| YouTube Ads | ₹80,000 | 13% |
| LinkedIn Ads (B2B fleet) | ₹1,00,000 | 17% |
| TikTok Ads (test) | ₹40,000 | 7% (10% experiment bucket) |
| **Total** | **₹6,00,000** | |

**Phase 3: Growth (Month 6+) — ₹10,00,000+/month**
Apply 70/20/10 rule once performance data exists:
- 70% to proven performers (platforms with CPA below target)
- 20% to scaling channels (platforms showing traction)
- 10% to experiments (new formats, new cities, new audience segments)

### 6.3 Bidding Strategy Roadmap

**Month 1 (Cold Start — 0 conversions):**
- Google Search: Maximize Clicks with Max CPC cap (₹150–₹300/click)
- Meta: Lowest Cost (no cap) — ABO structure for audience testing
- LinkedIn: Maximum Delivery
- Never use Smart Bidding with 0 conversion history

**Month 2 (15–30 conversions accumulated):**
- Google Search: Transition to Maximize Conversions
- Meta: Introduce Cost Cap at 1.2–1.5× observed CPA once CPA stabilizes
- Continue ABO until ₹5,000/day budget is reached, then test CBO

**Month 3+ (30+ conversions, stable CPA):**
- Google Search: Target CPA at 1.1–1.2× historical CPA
- Google PMax: Activate (30+ conversions required)
- Meta: Transition top-performing ad sets to CBO; test Advantage+ Leads campaigns
- LinkedIn: Accelerate campaigns (42% lower CPA vs manual)

### 6.4 CPA Targets by Conversion Type

| Conversion Event | Target CPA | Rationale |
|------------------|-----------|-----------|
| Test Ride Booking | ₹500–₹1,200 | High LTV event; converts to EV sale |
| App Install | ₹80–₹200 | Platform-level benchmark; 4.4 rating aids CVR |
| EV Lead (inquiry) | ₹300–₹800 | Broad lead; quality varies |
| Fleet/CMS Demo Request | ₹2,000–₹5,000 | B2B; high deal value justifies higher CPL |
| EV Purchase (attributed) | ₹3,000–₹8,000 | High-value conversion; downstream from test ride |

### 6.5 Scaling Rules (Apply When Campaigns Are Live)

**20% Rule:** Never increase any campaign budget by more than 20% at a time. Wait 3–5 days before next increase. Budget increases >20% reset Meta's learning phase.

**3x Kill Rule:** Pause any ad creative, ad set, or campaign that has spent 3× the target CPA with 0 conversions. Do not restart without changing the creative, audience, or landing page.

**Decreasing Returns Check:** If CPA increases >15% after a budget increase, roll back to the previous budget level and wait 7 days before attempting horizontal scaling (new audiences, new cities) instead of vertical scaling (more budget to same campaign).

---

## 7. Competitive Gap Analysis

### 7.1 Competitor Advertising Presence

| Competitor | Estimated Ad Spend | Platforms | Advantage |
|------------|------------------|-----------|-----------|
| Statiq | High ($18M raised) | Google, Meta, App stores | YC/Shell backing; 65+ cities |
| Tata Power EZ Charge | Very High | Google, Meta, YouTube, Display | Tata brand equity; unlimited budget |
| Ather Energy | Very High | Google, Meta, YouTube, Instagram | Premium brand; strong community |
| Ola Electric | Very High | Google, Meta, YouTube, TV | Massive brand spend |
| ChargeZone | Medium | Google, Meta | B2B charging focus |
| Jio-bp Pulse | Medium–High | Google, Meta | Reliance distribution |

**ElectricPe vs Competitors — Digital Advertising Gap:**
- All major competitors are actively running paid advertising
- Statiq (most direct competitor) has 65+ cities vs ElectricPe's 24+ and is backed by Y Combinator and Shell Ventures — likely spending aggressively on growth
- Tata Power EZ Charge benefits from Tata Group's existing brand campaigns that inherently include EZ Charge messaging
- Ather Energy is spending heavily on YouTube and Instagram for brand building among young urban buyers — exactly ElectricPe's target audience

### 7.2 Competitive Gaps ElectricPe Can Exploit

**Gap 1: Multi-Brand Dealer Advantage**
Ather, Ola, TVS iQube, Bajaj Chetak each only advertise their own brand. ElectricPe can run Google Ads targeting ALL of their brand keywords with messaging like "Compare 25+ EV models at one place." This competitor keyword strategy would be uniquely available to a multi-brand dealer.

**Gap 2: Physical Retail + Digital Integration**
Most charging-only competitors (Statiq, ChargeZone) do not sell EVs. Most EV brands (Ather, Ola) do not operate charging networks at scale. ElectricPe's combination of EV retail + charging network + financing is unique and can be exploited in ad copy: "Buy, charge, and finance your EV — all in one place."

**Gap 3: Community as Social Proof**
Club Electric with 80,000+ members is a significant asset that competitors likely do not have at this scale. User-generated content (member testimonials, charging session milestones, community stories) is a free creative source that would out-perform polished corporate ads on Meta and TikTok.

**Gap 4: Google Maps Partnership**
The real-time charging availability integration with Google Maps is a feature that can be used in Google Search ads and Display ads — "Find ElectricPe charging stations in real-time on Google Maps." This is a trust signal and convenience argument that competitors cannot match if they lack a similar partnership.

**Gap 5: Under-Competition in Hindi/Regional Language Search**
Most EV advertisers run English-language campaigns. Hindi, Kannada, Tamil, and Telugu search terms for EVs likely have significantly lower CPCs and less competition. ElectricPe, with a pan-India presence, is well-positioned to run regional language campaigns.

### 7.3 Competitor Strategy to Watch

**Statiq's YC network:** Statiq is likely leveraging YC's growth playbook (rapid experimentation, data-driven scaling, growth hacking). Expect Statiq to be running A/B tests across Google and Meta with significant budgets. ElectricPe needs to be in market to understand what is working.

**Tata Power's brand halo:** Any Tata brand advertising inadvertently lifts EZ Charge awareness. ElectricPe cannot compete on brand budget, but can compete on intent-based Google Search (lower funnel) and community-driven Meta content.

---

## 8. Cross-Platform Strategy Recommendations

### 8.1 Full-Funnel Architecture

ElectricPe's customer journey for an EV purchase typically spans 2–8 weeks and involves multiple touchpoints. The platform strategy should map to this journey:

```
AWARENESS (Weeks 1–2)
  → YouTube TrueView: "Is an EV right for me?" content
  → Meta Broad Prospecting: Lifestyle ads, range anxiety busters
  → Display: "India's EV revolution is here" brand ads

CONSIDERATION (Weeks 2–4)
  → Google Search: Actively searching for EV models, prices, test rides
  → Meta Retargeting: EV model comparisons, financing options
  → YouTube: Model-specific review content pre-rolls

INTENT / CONVERSION (Week 4+)
  → Google Search: "book test ride [city]," "EV test drive near me"
  → Meta Lead Gen: "Book your free test ride today" direct response
  → LinkedIn (B2B): "Fleet EV solution" specific to job title

POST-CONVERSION
  → App install push (Google App + Meta App Install)
  → WhatsApp automation via existing widget
  → Community onboarding (Club Electric)
  → Referral prompt (existing app + community)
```

### 8.2 The Test-Ride-First Paid Strategy

The test ride offer is ElectricPe's strongest paid advertising asset. Unlike most industries where the ad CTA is a remote digital action (sign up, download), ElectricPe's CTA bridges digital advertising to a physical, high-impact experience. A customer who takes a test ride has a 10× higher probability of purchasing than one who just browses the website. This means:

- All performance campaigns should optimize for test ride bookings (not just web clicks)
- The ₹299 test ride offer should be the primary creative message across all platforms
- Test ride confirmation should be tracked as the primary conversion event across Google and Meta
- Retargeting should be segmented: visitors who have NOT booked a test ride (push test ride offer) vs visitors who HAVE booked but not purchased (push financing and model comparisons)

### 8.3 App-First Strategy Integration

The ElectricPe App (4.4 stars, both stores) is an underexploited paid advertising asset:

- Google App Campaigns: Run universal app campaigns targeting EV owners and prospective buyers. The 4.4 rating is a powerful creative asset (competitive in app install campaigns)
- Meta App Install Campaigns: Target existing EV owners (Ola Electric, Ather, TVS iQube, Bajaj Chetak owners as interest groups) for the charging station locator feature
- Deep link all non-app-install campaigns to app-specific pages where possible (iOS/Android universal links) to capture app installs as a secondary conversion

### 8.4 Seasonal and Event-Based Advertising

| Period | Opportunity | Platform | Action |
|--------|-------------|----------|--------|
| Diwali (Oct–Nov) | Vehicle purchase season | Meta + Google | "Drive electric this Diwali" — heavy budget push |
| New Year (Jan) | New beginnings messaging | Meta | Lower CPMs post-holiday |
| Budget Day (Feb) | EV subsidy announcements | Google | Reactive search campaigns for EV subsidy news |
| World EV Day (Sep 9) | Awareness spike | YouTube + Meta | Brand content amplification |
| Financial Year End (Mar) | Corporate fleet budgets | LinkedIn | B2B fleet campaign push |
| City-specific EV Expo/Show | Local intent spike | Google Local + Meta | Event-targeted campaigns |

---

## 9. Prioritized Action Plan

### 9.1 Critical (Do This Week — Revenue Blocking)

| Priority | Action | Owner | Estimated Time | Impact |
|----------|--------|-------|---------------|--------|
| C1 | Install Google Tag Manager on Next.js website | Developer | 4 hours | Enables all tracking |
| C2 | Deploy GA4 via GTM with conversion events | Developer + Analyst | 8 hours | Cross-channel measurement |
| C3 | Install Meta Pixel via GTM + configure standard events | Developer | 4 hours | Meta campaigns can launch |
| C4 | Set up Google Ads account + brand campaign | Marketing | 4 hours | Protect brand SERP now |
| C5 | Create Meta Business Manager + verify domain | Marketing | 2 hours | Prerequisite for all Meta Ads |
| C6 | Configure Google Ads conversion tracking (test ride booking as primary) | Marketing | 3 hours | Smart Bidding foundation |
| C7 | Clarify "₹299 FREE" messaging on website — remove ambiguity | Content/Dev | 1 hour | Improves all ad CVR immediately |

### 9.2 High Priority (Do Within 2 Weeks)

| Priority | Action | Owner | Estimated Time | Impact |
|----------|--------|-------|---------------|--------|
| H1 | Deploy Meta CAPI via CAPI Gateway | Developer | 4–8 hours | Prevents 30-40% data loss |
| H2 | Launch Google Search — EV Purchase Intent campaign | Marketing | 8 hours | First paid traffic |
| H3 | Launch Meta Lead Gen — Test Ride Booking campaign | Marketing | 6 hours | First Meta leads |
| H4 | Install LinkedIn Insight Tag via GTM | Marketing | 30 minutes | Enables LinkedIn retargeting |
| H5 | Build website Custom Audiences in Meta (30-day visitors) | Marketing | 1 hour | Retargeting pool starts building |
| H6 | Upload existing customer/lead list to Meta Custom Audiences | Marketing | 2 hours | Lookalike seed audience |
| H7 | Add UTM parameters to all social media links + website CTAs | Marketing | 2 hours | Attribution data in GA4 |
| H8 | Create dedicated landing page for test ride bookings | Developer + Designer | 2–3 days | Improves CVR vs homepage |
| H9 | Launch Google App Campaign for ElectricPe app | Marketing | 4 hours | Leverage 4.4 rating |

### 9.3 Medium Priority (Do Within 30 Days)

| Priority | Action | Owner | Timeline | Impact |
|----------|--------|-------|----------|--------|
| M1 | Launch YouTube TrueView campaigns | Marketing | Week 3 | Awareness + consideration |
| M2 | Set up Google Display Retargeting | Marketing | Week 3 | Re-engage website visitors |
| M3 | Create city-specific landing pages for top 5 cities | Developer + Designer | Week 3–4 | Quality Score improvement + CVR |
| M4 | Launch Meta App Install campaign | Marketing | Week 3 | App user growth |
| M5 | Create video assets: test ride experience (15s, 30s, 60s) | Creative | Week 2–3 | Core Meta + YouTube creative |
| M6 | Set up Meta Retargeting campaign | Marketing | Week 4 | Re-engage non-converters |
| M7 | Implement Enhanced Conversions (Google) with hashed email | Developer | Week 3 | +10% measured conversions |
| M8 | Configure Aggregated Event Measurement (Meta AEM) | Marketing | Week 3 | iOS attribution |
| M9 | Create negative keyword lists for Google Ads | Marketing | Week 2 | Prevent wasted spend |
| M10 | Regional language ad copy (Hindi for North India campaigns) | Content | Week 3–4 | CTR improvement + lower CPC |

### 9.4 Low Priority (Month 2–3)

| Priority | Action | Owner | Timeline | Impact |
|----------|--------|-------|----------|--------|
| L1 | Launch LinkedIn Ads — B2B Fleet campaign | Marketing | Month 2 | Fleet sales pipeline |
| L2 | Launch Google Performance Max (once 30+ conv/month) | Marketing | Month 2–3 | Automated reach expansion |
| L3 | Test Thought Leader Ads on LinkedIn (CEO posts) | Marketing | Month 2 | Low-cost LinkedIn traffic |
| L4 | Test TikTok Ads — Spark Ads from top organic content | Marketing | Month 3+ | Young EV buyer awareness |
| L5 | Set up offline conversion import (test rides attended → Google Ads) | Developer + Marketing | Month 2 | Improve bid quality |
| L6 | Launch Meta Advantage+ Leads campaign | Marketing | Month 3 | Automated Meta lead gen |
| L7 | Incrementality test (geo-lift) on Meta campaigns | Marketing | Month 3–4 | True attribution validation |
| L8 | Build post-booking survey ("How did you hear about us?") | Developer + Marketing | Month 2 | Fill attribution gaps |

---

## 10. Quick Wins (Under 15 Minutes)

These items can be done immediately by the marketing team without developer support, and each has measurable impact.

| # | Action | Time | Impact | Platform |
|---|--------|------|--------|----------|
| 1 | Create Meta Business Manager account at business.facebook.com | 5 min | Prerequisite for all Meta Ads | Meta |
| 2 | Create Google Ads account and link to GA4 (if GA4 exists) | 10 min | Prerequisite for all Google Ads | Google |
| 3 | Verify ElectricPe domain in Meta Business Manager | 5 min | Required for pixel events to register | Meta |
| 4 | Create LinkedIn Campaign Manager account + link to company page | 5 min | Prerequisite for all LinkedIn Ads | LinkedIn |
| 5 | Add UTM parameters to all homepage CTAs ("Book Now," "Download App") | 10 min | Immediate attribution in GA4 | All |
| 6 | Update "₹299 FREE test ride" copy to clarify: "Book your test ride — ₹299 deposit, fully adjusted toward purchase" | 5 min | Removes purchase friction; improves ad CVR | All |
| 7 | Check if LinkedIn Insight Tag can be added via existing WebEngage/tag setup | 10 min | May not require developer | LinkedIn |
| 8 | Download existing lead/customer email list from CRM and upload to Meta as Custom Audience | 10 min | Starts building lookalike seed audience immediately | Meta |
| 9 | Create Google Ads brand campaign — add 10 brand keywords + 1 RSA with basic headlines | 10 min | Protects brand SERP from competitors | Google |
| 10 | Enable the LinkedIn Insight Tag on the website via GTM (if GTM is already installed) | 2 min | Starts building retargeting pool | LinkedIn |

---

## Appendix A — Platform Check Summary Table

### LinkedIn (24 Checks — Budget & Bidding Agent Scope)

| Check ID | Description | Status | Priority |
|----------|-------------|--------|----------|
| L03 | Job title targeting precision | FAIL — No campaigns | High |
| L04 | Company size filtering | FAIL — No campaigns | Medium |
| L05 | Seniority level targeting | FAIL — No campaigns | High |
| L06 | Matched Audiences active | FAIL — No tag installed | High |
| L07 | ABM company lists uploaded | FAIL — No account | Medium |
| L08 | Audience expansion setting | FAIL — No campaigns | Medium |
| L09 | Predictive audiences tested | FAIL — No campaigns | Medium |
| L16 | Bid strategy appropriate | FAIL — No campaigns | High |
| L17 | Daily budget ≥$50 Sponsored Content | FAIL — No budget | High |

### TikTok (8 Checks — Budget & Bidding Agent Scope)

| Check ID | Description | Status | Priority |
|----------|-------------|--------|----------|
| T03 | Separate campaigns: prospecting vs retargeting | FAIL — No account | High |
| T04 | Smart+ campaigns tested | FAIL — No account | Medium |
| T11 | Bid strategy matches goal | FAIL — No account | High |
| T12 | Daily budget ≥50× target CPA | FAIL — No account | High |
| T13 | Learning phase: ≥50 conversions/week | FAIL — No account | High |
| T14 | Search Ads Toggle enabled | FAIL — No account | High |
| T15 | Placement selection reviewed | FAIL — No account | Medium |
| T16 | Dayparting aligned | FAIL — No account | Low |

### Microsoft Ads (7 Checks — Budget & Bidding Agent Scope)

| Check ID | Description | Status | Priority |
|----------|-------------|--------|----------|
| MS04 | Search partner network reviewed | FAIL — No account | High |
| MS05 | Audience Network intentional | FAIL — No account | Medium |
| MS06 | Bid targets 20–35% lower than Google | N/A — Not recommended | N/A |
| MS07 | Target New Customers enabled (PMax) | N/A — Not recommended | N/A |
| MS08 | Campaign structure mirrors best practices | FAIL — No account | High |
| MS09 | Budget proportional to volume | N/A — Not recommended for India | N/A |
| MS10 | LinkedIn profile targeting for B2B | N/A — Use LinkedIn directly | N/A |

**Note on Microsoft Ads:** Given Bing's <3% search share in India, Microsoft Ads has been assessed as N/A for ElectricPe's Indian market. Budget that would go to Microsoft Ads should instead flow to Google and Meta where Indian users actually are.

---

## Appendix B — Minimum Viable Tracking Stack (Launch Checklist)

Before spending a single rupee on paid advertising, this stack must be in place:

```
MUST HAVE (Block campaign launch without these):
[ ] Google Tag Manager installed on all website pages
[ ] GA4 property created and linked
[ ] Meta Pixel base code firing on all pages
[ ] Meta Pixel: Lead event firing on test ride booking confirmation
[ ] Google Ads account created
[ ] Google Ads conversion action: Test Ride Booking (macro conversion)
[ ] Google Ads: gtag or GTM tag firing on conversion page
[ ] Meta Business Manager: domain verified
[ ] UTM parameters on all ad URLs

SHOULD HAVE (Deploy within first 2 weeks):
[ ] Meta CAPI via CAPI Gateway
[ ] Enhanced Conversions (Google)
[ ] LinkedIn Insight Tag
[ ] Aggregated Event Measurement (Meta AEM) — top 8 events prioritized
[ ] Custom Audiences built: Website visitors (30-day), Lead form openers

NICE TO HAVE (Month 2+):
[ ] Server-side GTM
[ ] Offline conversion import (test rides attended)
[ ] TikTok Pixel + Events API
[ ] Post-booking attribution survey
```

---

## Appendix C — India EV Market Context for Advertisers

| Metric | Value | Source |
|--------|-------|--------|
| India EV market CAGR | 25–27.6% | Industry reports |
| Market size by 2033 | $3.8 Billion | Research projections |
| Facebook CPM (India) | ₹9–10 | India benchmarks |
| Instagram CPM (India) | ₹70–200 | India benchmarks |
| Facebook CPC (India) | ₹0.50–₹2.26 | India benchmarks |
| Instagram CPC (India) | ₹2–₹6 | India benchmarks |
| Google Search CPC (EV terms) | ₹20–₹80 est. | Estimated (India market) |
| Recommended min spend (small biz) | ₹10K–₹50K/month | India benchmarks |
| Recommended spend (scaling) | ₹1L–₹5L/month | India benchmarks |
| ElectricPe recommended Phase 1 | ₹3L/month | This audit |

---

*End of Report*

**Report generated:** March 17, 2026
**Audit Agent:** Budget & Bidding Specialist
**Reference frameworks:** linkedin-audit.md (L03–L17), tiktok-audit.md (T03–T16), microsoft-audit.md (MS04–MS10), bidding-strategies.md, budget-allocation.md, benchmarks.md, scoring-system.md, google-audit.md, meta-audit.md, conversion-tracking.md
