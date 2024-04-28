> https://slhenty.com/project/fineuploader-modal?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Re-usable Component: Refactor FineUploader modal
lightbox](/_next/image?url=%2Fimages%2Ffineuploader.png&w=3840&q=75)

Re-usable Component: Refactor FineUploader modal lightbox

dev

### The Project

Fine Uploader, a JQuery plugin that manages file transfers, had been wrapped
by another development team into an AngularJS directive, leaving the native
Fine Uploader UI elements unchanged. This project involved **re-styling the
Fine Uploader UI** to match the existing product style guide, and **moving the
elements** from a sliding drawer animated panel **into a modal lightbox**.

### My Role

**Lead UI Developer** tasked with modifying the UI elements, while laying the
groundwork for a **separation of the Fine Uploader file transfer progress
content from the modal lightbox framework** intended for broad re-use
throughout the application.

### Interesting Challenges

This project presented a few challenges. The first was the **UI’s dependency
on a back end data indexing service**. The service was not fully CORS-
compliant, which meant accessing it from a local development environment
**failed the CORS pre-flight handshake for POST**. Given the nature of the
service and the need for issuing XHR progress events to properly test the UI
styles during file transfers, the effort to mock the service seemed not worth
the time. Instead, I **configured nginx as a reverse proxy to handle the CORS
pre-flight** headers directly, and passed only the actual GET and POST
requests through to the service.

Another challenge was refactoring the HTML structure and CSS styles for the
Angular directive template to **keep the modal framework separate from the
Fine Uploader UI content**. The separation was achieved two ways. First, I
**name-spaced the CSS styles separately** , which provided an obvious
separation in the markup. Then, I **structured the HTML into distinct modal
Header, Content, and Footer containers** , with the file transfer elements in
the Content container and the modal display controls in the header and footer.

### Results

Creating the reusable modal directive was not part of this project, but the
above refactor **set the stage for a modal directive** with default,
configurable header and footer, and transcluded content. The header, footer,
and content can **optionally be injected as custom html partials via directive
attributes**.

## Skills

AngularJS, Javascript

Fine Uploader

LESS, CSS, HTML

nginx, CORS

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

