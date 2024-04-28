> https://slhenty.com/project/wrapped-components-highcharts?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Wrapped Components: Highcharts](/_next/image?url=%2Fimages%2Fwrapped-
chart.png&w=3840&q=75)

Wrapped Components: Highcharts

dev

### The Project

A satellite monitoring system **displays time-series data** in a **set of
stacked charts**. For consistency with legacy monitoring systems, the charting
engine selected was **Highcharts** , which **does not offer a Polymer
integration**. The solution was to write a **wrapper for the Highcharts
component** with a simplified contract tailored to display time-series data.

### My Role

**Sr. Application Developer** and **UI Architect** who designed and
implemented the Polymer Behavior wrapper.

### Interesting Challenges

The challenge in this project was getting to the **right level of
abstraction** when wrapping the Highcharts component for use with Polymer. The
abstraction ultimately settled on was a **Polymer Behavior implementation**.
The Behavior encapsulates the 'uninteresting' aspects of Highcharts
initialization, configuration, and rendering while **exposing a couple of data
preparation methods** intended to be overridden for specific time series. This
use of **Template Method pattern** allowed a simple injection of raw data for
typical time series charts, while offering a way to provide specialized data
set preparation when necessary.

The complexity of the Highcharts configuration was also largely hidden behind
a **properly-configured default** configuration in the Polymer Behavior. When
necessary, the configuration can be **enhanced or completely overridden** in
much the same way as the data preparation.

### Results

The Polymer Behavior was used to **create a dozen or more charts** over the
course of a **few short development sprints**.

> Even when unusual chart configurations are required, the architecture
> **avoids the need to modify the Behavior itself**.

## Skills

Javascript

Highcharts

Polymer

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

