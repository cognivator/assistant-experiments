> https://slhenty.com/project/css-refactor?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Tiger Team: CSS refactoring](/_next/image?url=%2Fimages%2Fcss-
refactor.webp&w=3840&q=75)

Tiger Team: CSS refactoring

design / dev

### The Project

The CSS ecology for an existing web application shell had conflicting global
classes, multiple _and_ duplicate versions of Bootstrap LESS sources, and
inconsistent naming conventions which caused serious integration problems for
separately-developed functional modules. This project used a **dedicated,
five-person ‘tiger team’ of development leads from two product groups and UX**
, myself included, to **completely rewrite the CSS framework**. The goals of
the project were to re-evaluate our choice of CSS preprocessor, establish a
CSS naming convention using BEM, define standardized styles for re-usable
components, and thus ensure the web application shell provided a known,
consistent context for integrating additional modules.

### My Role

**Lead UI Developer** and primary **UX representative**. I provided guidance
in areas of likely UI style variations when the team needed to determine
**which aspects of the style should be configurable** during development **vs.
immutable** in the name of UI consistency.

### Interesting Challenges

One challenge we faced was porting LESS to SASS sources. The syntax itself is
similar enough that the bulk of the transfer could be handled with a series of
Find-and-Replace’s. More difficult was **finding the implicit use of class
selectors** as mixing allowed by LESS and **converting them to explicit @mixin
declarations** required by SASS. The **most disappointing aspect of SASS as
implemented by libsass** , however, is its **simplistic handling of the
@import dependency graph**. We were used to LESS’ ability to walk the entire
graph and import each dependency once, whereas libsass handles `@import` much
like C headers, resulting in a lot of unintentional duplication of common
code. While we found a technique in use that promised to avoid this problem
using `@export`, our timeframe was too short to adopt it fully, and we opted
for hand-optimization instead.

**Another surprise with SASS is its handling of variable scoping**. We were
used to LESS hoisting variables, even across multiple @imports, which enabled
late overriding of variables for control over theming. With SASS, we had to
use a combination of `!default` in the primary theme variables definition
file, and then `@import` the primary theme **after** any overrides, but
**before** the use of those variables.

## Skills

SASS, LESS, CSS, HTML

Interaction Design

AngularJS

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

