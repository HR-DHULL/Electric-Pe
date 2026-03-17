# ElectricPe Outreach Strategy - Multi-Channel

---

## CHANNEL 1: COLD EMAIL TO CEO (Avinash Sharma)

### Email #1 — The Hook

**Subject:** ElectricPe's ₹299 test ride bookings are invisible to Google — 40-hr audit inside

**To:** Avinash Sharma (avinash@electricpe.com / LinkedIn InMail)

---

Hi Avinash,

I'll keep this short — I spent 40+ hours doing an independent audit of ElectricPe's tracking, SEO, and growth infrastructure.

The findings surprised me. For a $52M-valued company, your digital infrastructure is running at seed-stage maturity.

**3 things that are costing you real money right now:**

1. **No Google Tag Manager installed** — every tracking change requires a developer deploy. Your Facebook Pixel fires late (15-30% data loss), you have zero Google Ads conversion tracking, and your 5 analytics tools run with no coordination.

2. **Your EV purchase funnel is a complete black box** — you've sold 6,000+ EVs but can't tell which marketing channel drove a single one. No GA4 ecommerce events, no funnel drop-off data, no remarketing for users who almost bought.

3. **www.electricpe.com shows a security warning** — your SSL cert doesn't cover the www subdomain. Anyone typing "www" bounces immediately. Your blog has 2 posts in 2+ years. Zero schema markup. Google barely knows you exist outside brand searches.

**Why this matters right now:** The Bolt.Earth + Statiq interoperability alliance is live. Your aggregator moat is under direct attack. You need to outcompete $106M-funded ChargeZone and $45.5M-funded Statiq by being smarter with data — but you can't even track a conversion today.

I've prepared a full Growth Blueprint showing how to take ElectricPe from INR 13.3 Cr to INR 35+ Cr in revenue. The tracking fix alone (2-4 weeks, INR 4-6 Lakh) would recover an estimated INR 2-5 Cr/year in wasted spend and lost conversions.

Worth a 30-minute call this week? I'll share all 6 audit reports on the call — 80+ pages of analysis, completely free.

Best,
Harsh Dhull
Growth & MarTech Strategist
work.samsolanki@gmail.com | www.sakshamsolanki.com

P.S. — Your 50,000 Club Electric members are being wasted. That community forum is overrun with loan scam spam that Google is indexing under your domain. It should be your #1 growth engine — a Meta lookalike audience from that list alone gives you 3-5 million targetable users.

---

### Email #2 — Follow-Up (Day 5, if no response)

**Subject:** Re: ElectricPe's ₹299 test ride bookings are invisible to Google

---

Hi Avinash,

Quick follow-up with one more finding I thought was worth sharing:

You have Razorpay integrated for payments, but no cross-domain tracking configured. This means:

- Every user who completes payment through Razorpay gets counted as a **new session** in analytics
- Razorpay shows up as a **referral source** instead of a payment step
- The original traffic source (whether it's organic, social, or any future paid campaign) is **lost after payment**
- You literally cannot calculate ROI on any marketing channel

This is a 3-4 hour fix once GTM is installed. It would immediately give you revenue attribution across every traffic source.

I also noticed your DPDPA exposure — 5 tracking tools firing without any cookie consent. Enforcement begins May 2027 (14 months). With investors like Blume and Green Frontier on your cap table, this is the kind of compliance risk that comes up during due diligence.

Happy to walk through everything whenever works.

Harsh

---

### Email #3 — Final Follow-Up (Day 12, if no response)

**Subject:** Last note on ElectricPe tracking

---

Hi Avinash,

Last follow-up — I don't want to be that person who keeps emailing.

One final data point: Kazam (your closest comp in the software/platform space) went from INR 11 Cr to INR 40 Cr revenue in one year — 3.5x growth. They did it largely through better product marketing and digital infrastructure, not more chargers.

Your super-app model (Buy + Charge + Finance + Service) is genuinely unique. No competitor has it. But a great product with broken tracking is like a Formula 1 car with no dashboard — you're fast, but you're driving blind.

The Growth Blueprint and all 6 audit reports are yours, no strings attached. If nothing else, share them with your marketing team — there's actionable stuff they can implement immediately.

All the best with the 50 new Mobility Centre rollout.

Harsh
work.samsolanki@gmail.com | www.sakshamsolanki.com

---

## CHANNEL 2: LINKEDIN DM SEQUENCE

### DM #1 — Connection Request Note

Hi Avinash — I'm a MarTech consultant who specializes in growth infrastructure for funded Indian startups. Did a deep dive on ElectricPe recently and found some interesting gaps. Would love to connect and share.

---

### DM #2 — After Connection Accepted

Hi Avinash, thanks for connecting!

I spent 40+ hours auditing ElectricPe's digital infrastructure — GTM, SEO, tracking, ads readiness, competitive positioning.

Quick headline: **Your growth readiness score came out at 23/100.**

Three critical findings:
- No GTM installed (every tag change needs a dev deploy)
- No Google Ads conversion tracking (ad optimization is impossible)
- www.electricpe.com has a broken SSL certificate (browsers show security warning)

I've prepared a full Growth Blueprint: INR 13.3 Cr → INR 35+ Cr revenue roadmap with specific implementation timelines.

The Phase 1 fix (2-4 weeks, INR 4-6 Lakh) would recover an estimated INR 2-5 Cr/year.

Would a 30-minute call work this week? Happy to share all 6 reports — 80+ pages, completely free.

---

### DM #3 — Follow-up (Day 5)

Hi Avinash — wanted to flag one more thing from the audit:

The Bolt.Earth + Statiq interoperability alliance means users can now charge across both networks without an aggregator. That's 110,000+ chargers combined.

Your super-app moat (Buy + Charge + Finance + Service) is strong, but it needs digital infrastructure to match. Right now your Instagram has 2,336 followers (vs Ather's 800K) and you have zero YouTube presence.

The full blueprint covers how to fix all of this. 30 minutes for a walkthrough?

---

## CHANNEL 3: LINKEDIN DM TO CTO / HEAD OF ENGINEERING

### DM #1

Hi [Name] — I did an independent technical audit of electricpe.com's tracking stack. Found some architecture-level gaps your engineering team would want to know about:

- GTM isn't installed — all 5 analytics tools (WebEngage, GA4/Firebase, Meta Pixel, Mixpanel, Clarity) are hardcoded into the Next.js webpack bundle
- Facebook Pixel is wrapped in React Suspense — it only fires after hydration, losing 15-30% of events
- No dataLayer implementation — when you do add GTM, it'll require significant backfill
- No cross-domain tracking with Razorpay — payment attribution is completely broken
- Firebase config exposed in client bundle (normal, but worth verifying security rules)

These are all straightforward fixes. The GTM migration would take 1-2 days and give your marketing team self-service tag management.

Happy to share the full technical report if useful.

---

## CHANNEL 4: LINKEDIN DM TO HEAD OF MARKETING / GROWTH

### DM #1

Hi [Name] — I run a growth consulting practice focused on funded Indian startups. Did a comprehensive audit of ElectricPe's marketing infrastructure.

Honest finding: you're operating at below seed-stage tracking maturity despite being a $52M company.

What jumped out:
- Zero paid ad campaigns running (Google Ads Transparency Center + Meta Ad Library show nothing)
- Blog has 2 posts in 2+ years
- Instagram: 2,336 followers (vs Ather's 800K+)
- No YouTube channel
- Club Electric forum is overrun with spam that Google is indexing
- No email marketing funnel despite WebEngage being installed
- Website missing: EV comparison tool, EMI calculator, pricing page, customer reviews

I've built a detailed playbook to take ElectricPe from INR 13.3 Cr → INR 35+ Cr revenue. Includes specific channel strategies, content calendars, and ROI projections.

Would love to share it over a 30-minute call. Completely free, no strings.

---

## CHANNEL 5: TWITTER/X DM (if accessible)

Short version for Twitter DMs:

Hey @ElectricPe team — did a 40-hour independent audit of your growth infrastructure. Found some critical gaps:

- Growth readiness score: 23/100
- No GTM, no Google Ads tracking, broken SSL on www
- Your 50K community forum is being indexed by Google as spam

Built a roadmap to take you from ₹13.3 Cr to ₹35+ Cr revenue. Happy to share — it's free.

DM me for the full report.

---

## SENDING STRATEGY

```
  DAY 1:  LinkedIn connection request to Avinash (CEO)
          LinkedIn connection request to CTO/Engineering Head
          LinkedIn connection request to Marketing/Growth Head

  DAY 2:  Email #1 to Avinash (after connection sent)

  DAY 3:  LinkedIn DM #2 to Avinash (after connection accepted)
          LinkedIn DM to CTO (after accepted)

  DAY 4:  LinkedIn DM to Marketing Head (after accepted)

  DAY 5:  If no response → Twitter DM to @ElectricPe

  DAY 7:  Email #2 to Avinash (follow-up)
          LinkedIn DM #3 to Avinash

  DAY 14: Email #3 to Avinash (final follow-up)

  DAY 21: If still no response → reach out to investors
          (Blume Ventures, Green Frontier Capital)
          with a value-add angle, not a pitch
```

---

## KEY TALKING POINTS FOR THE CALL

When you get the meeting, lead with these:

1. **Open with the scariest finding:** "www.electricpe.com shows a browser security warning right now. Did you know?"

2. **Show the competitive gap:** "Statiq is doing INR 280 Cr revenue with similar funding timeline. Kazam is at INR 40 Cr. The difference isn't product — it's digital infrastructure."

3. **Make it tangible:** "If you're spending even INR 5 Lakh/month on any ads, roughly INR 1.5-2.5 Lakh of that is wasted because Google has zero conversion data to optimize on."

4. **Create urgency:** "The Bolt.Earth + Statiq alliance launched in January. They now have 110,000+ interoperable chargers. Your aggregator moat is being undermined."

5. **Low-risk entry:** "Phase 1 is a one-time INR 4-6 Lakh fix over 2-4 weeks. If your tracking score doesn't go from 23 to 75+, you don't pay."

6. **End with the vision:** "Your super-app model is genuinely unique. No competitor combines Buy + Charge + Finance + Service. But right now it's like having a Ferrari engine in a car with no GPS. We add the GPS."
