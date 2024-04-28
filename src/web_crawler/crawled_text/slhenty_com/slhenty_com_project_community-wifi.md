> https://slhenty.com/project/community-wifi?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Community Wifi: Local wifi for underserved
communities](/_next/image?url=%2Fimages%2Fcomm-wifi.hero.webp&w=3840&q=75)

Community Wifi: Local wifi for underserved communities

dev

### The Project

Use **airborne data channels** \- satellite, LTE, etc. - to provide local
**wifi access to underserved communities**. Make internet access available via
a captive portal in **hyper-local access points** using pre-paid codes sold by
local vendors and partners.

### My Role

**Sr. Software Engineer** and **Frontend Architect** responsible for
evaluation of the extant technology stack, and for the **design and
implementation of the captive portal**.

### Interesting Challenges

#### Architecture

The primary architectural challenge was providing a **partner-branded
experience at each hyper-local captive portal** while maintaining a single
codebase. Anticipating dozens of regional partners and thousands of vendor
host sites, the solution needed to be **scalable and maintainable**.

The **"partnerization" assets** \- logos, pricing models, app feature flags,
legal notices, etc. - were stored in a **headless CMS**. The captive portal
code had **site identifiers injected during provisioning**. The web app used
the identifiers to retrieve the CMS assets. This solution allowed **unlimited
onboarding** of new partner and vendor host sites over time with **no code
changes or deployment**.

#### Technical

A persistent technical challenge was the **high latency** of the satellite or
LTE links. The captive portal and web app needed to be fast and responsive
when accessed using **budget or low compute-power devices**. It also needed to
be **branded** for the partner site. The solution used NEXT.js to provide
**server-side rendering** (SSR) of the initial page load, and then client-side
rendering for subsequent page loads. While fine in theory, the initial SSR was
**not considered static** by NEXT.js and **could not be cached** , either at
the server or the captive portal host.

> A better solution might have been to use a single-page app so the page
> assets could be cached at the captive portal after the first device request.
> This would have required a significant rewrite of the existing codebase with
> no time or budget available.

Another technical challenge was providing a **seamless, no-login experience
for returning devices** on subsequent visits to the vendor. The solution used
**mac address cookies** to identify returning devices with remaining usage
credits and automatically log them in to the captive portal.

### Results

In spite of the implementation difficulties noted above, **dozens of sites**
were successfully onboarded in the **first 12 months** of operation across
**Mexico, Guatemala, Brazil, and Nigeria**.

## Skills

NextJS, React

graphQL, Apollo

captive portal, RADIUS

CPE (Customer Premises Equipment), satellite

network engineering

Salesforce Apex and Lightning components

AWS

## Demos / Artifacts

Built with[![Next.js](/_next/static/media/nextjs-logotype-dark-
background.84e239c2.svg)](https://nextjs.org/)by Steve Henty.Hosted
by[![Vercel](/_next/static/media/vercel-logotype-
light.079985bd.svg)](https://vercel.com).

Theme: [![Solarized](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsolarized-
yinyang.529358b9.png&w=1080&q=75)solarized](https://en.wikipedia.org/wiki/Solarized)
(Why? - [Ethan Schoonover](https://ethanschoonover.com/solarized/) |
[WIRED](https://www.wired.com/story/very-mathematical-history-perfect-color-
combination/))

© 2015-2024 Steve Henty

