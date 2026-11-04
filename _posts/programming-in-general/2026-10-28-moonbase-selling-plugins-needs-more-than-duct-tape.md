---
title: "Selling plugins needs more than duct tape"
description: "Licensing, store, email, and analytics held together with duct tape cost you plugins. Learn how to offer one-click activation, loyalty pricing, and emails that earn their place."
date: 2026-10-28
author: Moonbase
layout: post
permalink: /selling-plugins-needs-more-than-duct-tape/
background: /assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/Thumbnail.webp
categories:
  - Programming In General
tags:
  - plugin
  - career
discussion_id: 2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape
---
Nobody gets into plugins because they love setting up payment providers.

_Disclaimer from Jan: This is a sponsored guest post by [Moonbase](/moonbase). Thanks a lot for sponsoring the blog! And to you dear reader, make sure to check them out!_

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/00-cover.png", "Selling plugins needs more than duct tape: four tool cards, Store, Licensing, Email and Analytics, held together with strips of duct tape" %}

We certainly didn't, but when we started selling our own many years ago, it came with the job: picking products from different vendors to solve different needs. Licensing, e-commerce, email marketing and much more: some we bought, some we built.

Then you duct tape them together, so a sale in one tool becomes a license in another and a subscriber in a third, and so the numbers you need end up somewhere you can see them.

Every new idea after that means more tape: a bundle, a subscription option, a loyalty discount for existing customers.

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/01-more-tape.png", "The same tools held together with duct tape, in three stages. First plugin: Store and Licensing joined by one strip. A newsletter: Store, Licensing and Email taped together in a triangle. Bundles, subscriptions, loyalty pricing: the same three tools buried under layers of overlapping, patched-up tape." %}
*Every new idea means more tape, and every strip is something you have to keep working.*

None of it is what you got into plugins for, and every hour spent on the glue is an hour not spent on the next plugin.

Here is what worked best for us.

## Building loyal fans

Plugins are an indie business, and in an indie business nothing beats a raving fan. Most of us can't outspend the big brands, so growth comes from the customers who recommend us on forums, in YouTube comments and to whoever is in the studio with them.

A great plugin is what makes someone a fan, but it isn't enough on its own. Everything around it counts too: how the plugin is activated, what they pay for the next one, and what lands in their inbox.

For us, that comes down to three things:

1. **Activation has to be painless.** One click from installed to working, even for someone who doesn't own the plugin yet.
2. **Loyalty has to pay.** Existing customers get the best price on new plugins, and never pay twice for what they already own when they move up to a bundle.
3. **Every email has to earn its place.** Email fatigue is real, so we send less, and make what we send precise.

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/02-fan-flywheel.png", "A loop of five steps around a raving fan: tries a plugin, activates in one click, buys the next one at an owner's price, gets only the emails meant for them, and recommends you to someone new, who then tries a plugin." %}
*Every good experience along the way makes a fan, and every fan brings in the next customer.*

## DRM that doesn't suck

Activation is usually the first thing a customer does with your plugin, so it sets the tone for everything after it.

What worked best for us is a single sign-on style flow: the plugin opens our store in the browser, where the customer is usually already signed in.

One click takes them from installed to activated. No copying keys out of emails, and no typing passwords into a plugin window their password manager can't see.

If they aren't signed in, or don't own the plugin yet, the browser is the right place to handle that too: they can sign in, buy it or start a trial, and go straight back to making music.

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/03-one-click-screens.png", "Three screens. A Fjord Verb plugin window with an Activate button. A browser page asking \"Activate Fjord Verb on this computer?\", showing the customer is already signed in as alex@example.com, with an Activate button. The plugin window again, now showing \"Licensed to Alex\" with a check mark." %}
*No license key and no password: the customer is already signed in.*

Two more things matter as much as that first activation:

- **Studios go offline.** Plenty of studio computers are kept off the internet on purpose. Offer an offline activation path, and let an activated plugin keep working without a connection.
- **A failed check is not a revoked license.** If the plugin can't reach your server, that tells you nothing about the license. Only deactivate when the server actually says the license was revoked or has expired. Get this wrong, and paying customers re-activate every time their Wi-Fi drops, which is exactly the kind of DRM that sends people looking for a cracked copy.

## Pricing that understands customers

The second thing was making loyalty pay, and this is where the duct tape shows the most.

Most plugin companies grow the same way. One plugin, then a second, then a third, and at some point a bundle of all of them. Every one of those launches raises the same question: what should the people who already bought from you pay?

If your store doesn't know what each customer owns, the answer is "the same as everyone else". Your most loyal customer, the one who bought your first two plugins at full price, sees the new bundle at the same price as someone who has never heard of you. They can pay again for plugins they already own, or they can wait. Neither builds a fan, and next time you launch a plugin, they will remember to wait for the bundle.

Here is what worked for us:

- **Loyalty pricing on new releases.** When we launch a plugin, owners of our related plugins get a better price than the general public, without typing anything. Not a coupon code mailed to a list, but a discount that applies because the store knows who they are when they sign in. Shared codes leak: give it a week and it is on a deal forum, and your loyalty discount has become a public sale.
- **Bundles that count what you already own.** If a customer owns some of the plugins in a bundle, they pay for the rest, not for the whole thing again. We price it by each plugin's share of the bundle's value: owning a $29 plugin from a bundle worth $247 in total takes about 12% off a $99 bundle, so they pay $87.38. Buying a single plugin today should never be something a customer regrets tomorrow.
- **Upgrades and crossgrades.** A version 2 worth charging for should still cost less for version 1 owners, and someone moving from the lite edition to the full one should get credit for what they already paid.
- **More than one way to pay.** Some customers would rather pay monthly than up front. Rent-to-own, where a subscription becomes a perpetual license after a set number of payments, lowers the price of entry without anyone feeling they are renting forever.

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/04-bundle-tiles.png", "The Fjord Collection: five plugins worth $247, sold together for $99. Alex already owns Fjord Verb ($29), so the other four, $218 of the $247, are still to buy. The bundle costs Alex $87.38 instead of $99." %}
*Alex already owns one plugin in the bundle, so they pay only for the rest.*

Every one of these depends on the same thing: knowing what a customer owns at the moment they are about to pay. That knowledge usually lives in your licensing system, while your prices live in your store. When the two don't talk, each idea above turns into a manual project: export the owners, generate codes, send them out, and hope they don't leak.

## Running campaigns that make sense

The third thing was making every email earn its place. In practice, that mostly means sending fewer emails, to the right people.

Plugin customers are some of the most heavily emailed people around. Most of them have bought a plugin or two from a dozen companies, and every one of those companies is having its biggest sale ever, every month, and twice in November. You don't stand out by shouting louder. You stand out by sending the email that is obviously meant for them.

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/05-inbox.png", "A customer's inbox in November: rows of loud sale emails from plugin companies, such as \"Biggest sale ever: 90% off everything\", \"Last chance!!\" and \"Black Friday starts NOW\", all grayed out. One stands out, from Fjord: \"Alex, your owner's price on Fjord Bus. Because you own Fjord Verb and Fjord EQ.\"" %}
*In a November inbox, the email that stands out is the one written for the reader.*

What that looks like for us:

1. **Segment by what people own and do, not only by who subscribed.** A new mixing compressor goes first to the people who own our other mixing plugins, and to those who trialled one of them and never bought. The general newsletter hears about it later, if at all.
2. **Never pitch a plugin to someone who already owns it.** Nothing makes a fan feel foolish faster than a 50% off email for the plugin they bought at full price last week. If your email tool doesn't know who owns what, this will happen to you. It is only a question of when.
3. **Make offers personal.** A single-use code per recipient, or a discount that applies when they sign in, can't end up on a deal site, and it makes the email feel written for them. Because it was.
4. **Treat product updates as marketing.** "Version 1.4 is out, and here is what's new" is an email owners actually want to read. It shows you are still working on what they paid for, and it is the most natural place to mention what is coming next.
5. **Respect the opt-in.** Keep transactional email (receipts, license emails, password resets) apart from marketing, and only send marketing to people who asked for it. It keeps you on the right side of GDPR, and more importantly, it keeps your list full of people who want to hear from you.

Finally, judge campaigns by sales, not open rates. Opens have been unreliable since Apple's Mail Privacy Protection started loading every email on people's behalf, and a campaign that sold to a hundred owners beats one with a great open rate that sold nothing.

## Understanding our customers

All three of those rest on one thing: knowing your customers. That is hard when every tool only knows a slice of them.

When sales live in one tool, licenses in another and email in a third, simple questions turn into an afternoon of joining CSV exports in a spreadsheet:

- How many people who trialled our reverb last month went on to buy it?
- Which customers own three or more of our plugins, but not the newest one?
- Which plugin versions and operating systems are our customers actually running?

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/06-one-customer.png", "Three tools each know a slice of the same customer. The store knows 2 orders, $78. Licensing knows 3 activations on macOS. Email knows alex@example.com opens product updates. Put together in one profile: Alex owns Fjord Verb and Fjord EQ, trialled Fjord Comp 12 days ago and didn't buy, runs Fjord EQ 1.4 on a Mac with Apple silicon, and opens every product update. Next: an owner's price on Fjord Comp." %}
*Each tool knows a slice of the customer. Put together, the slices tell you what to do next.*

A few things we learned to treat as non-negotiable:

**Your licensing is your best analytics.** Every activation and every license check tells you something: which plugin, which version, which platform, how often it is opened. That is usage data most software companies have to build tracking for, and you get it from the DRM you already have. It tells you when it is safe to drop an old macOS version, and whether a Windows on ARM build is worth the effort. But only if it sits somewhere you can look at it next to your sales. (Keep it to what licensing needs, though; plugin users are rightly wary of software that phones home.)

**Follow the whole funnel.** Download, trial, purchase, activation. Where people drop off tells you what to fix. Lots of downloads but few trials? Look at your installer and your activation flow. Lots of trials but few purchases? It is the product, or the price. Purchases that never activate? Your support inbox is about to tell you why.

**Know your fans by name.** The customers who own most of your catalogue, open every product update and buy on launch day are the ones to talk to before a launch, the ones to give early access, and the ones never to take for granted. You can only find them if ownership, email and sales live in the same place.

## Less glue, more plugins

Looking back, none of these ideas is complicated on its own. One-click activation, a fair bundle price, a launch email that reaches the right people, a chart of trial conversions. What made them hard for us was that every one of them crossed the line between two or three tools, and every crossing was more glue to write and keep working.

That is the real cost of duct tape. It isn't the subscription fees. It is the campaigns you never run because the data isn't where it needs to be, and the weeks you spend on plumbing instead of plugins.

{% image "assets/img/posts/programming-in-general/2026-10-28-moonbase-selling-plugins-needs-more-than-duct-tape/07-checklist.png", "Before you sell your first plugin: a checklist in four cards. Activation has to be painless: one click, through the browser; works offline; a failed check is not a revoked license. Pricing has to make loyalty pay: owners get the best price; bundles count what they own; no shared codes to leak. Email has to earn its place: segment by what people own and do; never pitch what they already own; judge by sales, not opens. Data has to live in one place: licensing is your analytics; follow the whole funnel; know your fans by name." %}
*The short version.*

Eventually we stopped gluing, and put licensing, the store, email and analytics into one system. That system became [Moonbase](/moonbase), which now runs the business side for other plugin developers too. If you are about to sell your first plugin, or you are tired of maintaining your own glue, come and have a look.

And whatever you end up using: decide early what experience you want your customers to have, and pick tools that share what they know about them. That way, the next good idea you have is a setting, not a project.
