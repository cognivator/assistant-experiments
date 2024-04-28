> https://slhenty.com/project/realtime-report-builder?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Configurable Component: Real-time Report
Builder](/_next/image?url=%2Fimages%2Fconfig-report.hero.webp&w=3840&q=75)

Configurable Component: Real-time Report Builder

dev

### The Project

A **satellite monitoring system** displays performance data for **airline Wifi
service** in a table. The table rows correspond to **satellite receivers
mounted in airplanes** , and the table columns correspond to performance
metrics or time-series values for a given timeframe depending on the report
type.

Performance metrics are typically rendered as a group of columns whose
**column names may be derived from the performance data itself**. System
operators can **choose pre-configured reports** or **build custom reports** by
selecting performance metrics **on-the-fly**. Changes to the selected metrics
are **rendered in the table immediately**.

The number of reports and their column configuration is **essentially
unbounded** , with new reports coming online in response to customer requests
and internal reporting needs.

> Implementing a new report is a matter of writing or updating report and
> column descriptors with **no additional development effort necessary**.

### My Role

**Sr. Application Developer** and **UI Architect** who designed and
implemented the data grid used for displaying the dynamic report
configurations.

### Interesting Challenges

The primary challenge for the dynamic data grid was **reacting to real-time
changes** in the number and specification of the table columns, especially
when the column characteristics are **derived from the data itself**. I
designed **JSONSchema column and report "descriptors"** that specify column
characteristics, cell styles, click events, data binding and transformations,
which columns make up a report, and the source(s) of the dataset. When a
report is selected from the ACL-mediated choices in the left-nav, the report
descriptor and its column descriptors are used to retrieve the dataset(s),
**re-write the display template** , and **bind the dataset** to the display
template.

Two additional challenges include **a) obtaining durable references** to data
items across multiple, sparse arrays in the dataset, and **b) coalescing
multiple report datasources** into the smallest number of data requests. In
the first case, I use a **curried 'getter'** to capture the array reference at
the time the dataset is analyzed, deferring retrieval until the specific row
is rendered. Coalescing multiple data sources is achieved by **debouncing the
data requestor** until report selections have subsided and all data sources
are known and can be combined.

### Results

The data descriptors and parsers that construct the UI were **deployed for
over 12 months** , and have been used with **both Polymer and React component
libraries**. Two dozen custom and preconfigured reports were specified over
time for use across multiple customers.

## Skills

Javascript

JSON, JSONSchema

Postgres, REST, Swagger

Polymer, HTML, CSS

functional programming

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

