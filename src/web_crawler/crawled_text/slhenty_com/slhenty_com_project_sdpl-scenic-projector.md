> https://slhenty.com/project/sdpl-scenic-projector?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![San Diego Public Library: Scenic projector
integration](/_next/image?url=%2Fimages%2Fsdpl.hero.jpeg&w=3840&q=75)

San Diego Public Library: Scenic projector integration

dev

> Also see the related _[DESIGN](sdpl-app-design?a=true&n=99)_ project
> covering the back-office management app.

### The Project

A free-standing kiosk, a scenic projector, and a back office computer
connected in an isolated network. The projector **displays a list of donor
names on an architectural pillar** , and the kiosk allows selection of a name
from the master list for temporary display of the associated signature of the
donor on the pillar. The back office computer provides donor names and
signature file upload to the kiosk, **selection of day- or night-time color
scheme for the projection** , and **real-time control of the projector
lamps**. The kiosk hosts all functions including web, web socket, data, and
scheduler services **using node-windows to run the node processes as Windows
services**.

### My Role

**Interaction Designer** and **Full-stack developer**. Originally engaged as a
sub-contractor to provide integration of a custom projection app with the
kiosk hardware, the role grew to cover the **entire infrastructure**
comprising kiosk software customization, network design, data access services,
inter-app communication services, and the back office web app.

### Interesting Challenges

The system involved **real-time signaling** among kiosk hardware, a scenic
projector, and a back office computer **via web sockets**. Unfortunately, the
custom display software, _Construct 2_ , only supported plain vanilla web
sockets which prevented the use of a robust library like primus.io to
communicate with the display app. This meant I had to **devise a message
format** to handle the varying signals between the apps. Thankfully, the
signaling to the back office computer could use all primus.io has to offer,
including **events, channel multiplexing, and automatic connection retries**.
The projector, on the other hand, used **TCP socket communication** and a
specialized signaling format, so the web socket services handled the
**translation from web sockets to TCP and back** when projector communication
was required. The projector was not available for most of the development
cycle, so I **built a mock projector service** as a stand-in during
development. Additionally, I had to learn the custom app IDE, _Construct 2_ ,
and the kiosk software, _Sitekiosk_ , to complete the integration.

### Results

The art installation remained in service for **three confirmed years** *,
during which time it was active for **daily public use.** It was also a
**signature feature for VIP events** hosted at the library.

* _It may still be in service._

## Skills

Modified MEAN stack: ExpressJS, AngularJS, NodeJS

WebSockets, REST

Javascript, LESS/CSS, HTML/Jade

Browserify

AxureRP

## Demos / Artifacts

San Diego Public Library

The installation may still be live at the San Diego Public Library, Central
Library location.

Video

A video of the installation in action.

[View full-size video](https://iframe.mediadelivery.net/play/177094/a8815fae-
ec06-4a91-8b4e-8492fdb0505e)

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

