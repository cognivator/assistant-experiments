> https://slhenty.com/project/ui-telemetry-spec?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![UI Telemetry Specification: Lightweight UI usage
metrics](/_next/image?url=%2Fimages%2Fui-telemetry.png&w=3840&q=75)

UI Telemetry Specification: Lightweight UI usage metrics

design

### The Project

Define an appropriate payload for UI usage telemetry. The goal was to **allow
virtually any UI usage or domain workflow-related question** to be posed and
analyzed using the existing telemetry data **without re-instrumenting the
code**.

### My Role

**UI Architect** responsible for defining the proper payload to **balance the
needs of UX design** with the **application performance** and development
**maintenance overhead**.

### Interesting Challenges

It was obvious early on that **typical “web analytics” providers** , a la
Google Analytics (GA), are predisposed to sales and advertising conversion
metrics and **not wholly appropriate for web application workflow metrics**.
The most glaring example of this predisposition is how GA, for example, treats
long delays between requests as “abandonment” rather than workflow delays or
workflow hand-offs between actors. On the other hand, GA natively captures
much useful information about user-agent, geocoding, etc. Therefore, **the
client-side telemetry needed to accommodate multiple collection endpoints** :
GA for what it does well, and additional endpoints for custom workflow
analysis, reconciliation with other service activity and performance logging,
etc. For this reason, **the Angulartics project was chosen as the client-side
instrumentation** for its support of multiple endpoints via extensions, and
its integration with the AngularJS http interceptor architecture.

Additionally, the payload necessary to pose and analyze workflow-related
questions required **domain-specific data to properly re-construct the
workflow** across real-world interruptions, multi-actor collaboration, multi-
day processing, etc. Here again Angulartics supports custom payloads as part
of the UI event stream.

### Results

The resulting payload consists of a **UI element ID, User ID, job / entity ID,
and timestamp**. In combination with the native GA metrics around user-agent
and geocoding, any **workflow path** or **UI element usage histogram** of
interest can be reconstructed during **post-hoc analysis** , including
investigating differences across organizations, regulatory jurisdictions, etc.

## Skills

AngularJS / Angulartics, Google Analytics

UX design, Axure RP

workflow / domain knowledge

## Demos / Artifacts

Axure Prototype

Live Axure drill-down diagram of the UI metrics payload spec.

[View on Axshare](https://ojnwzf.axshare.com/home.html)

Medium Article

[User Interface Telemetry: Motivation, Goals,
Methods](https://slhenty.medium.com/user-interface-telemetry-ebf0498fc307)

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

