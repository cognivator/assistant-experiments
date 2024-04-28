> https://slhenty.com/project/exploratory-prototyping?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Exploratory Prototyping: Mediator pattern in Axure](/images/mediator-
axure.svg)

Exploratory Prototyping: Mediator pattern in Axure

design / dev

> Also see the related _[Iterative Prototyping](iterative-
> prototyping?a=true&n=99)_ project which formed the basis of this exploratory
> prototpying pattern.

### The Project

Design and implement a **reusable method in Axure RP** to allow more robust,
exploratory usability and concept testing. Prototypes using this pattern are
**not limited to pre-built combinations of UI element states** , and **can
respond to un-scripted user actions** in a more robust, believable way.

### My Role

**Sr. Interaction Designer** using prototyping tools to **enhance research
possibilities** beyond scripted click-through prototypes.

### Interesting Challenges

The challenge of any partly-functional or click-through prototype is
**responding to un-planned user actions in a believable way**. This is
normally accomplished in functional UI’s via controllers, view models,
eventing frameworks or similar that update the UI, none of which are available
in Axure RP. While Axure does have **limited eventing** for use in bubbling up
through a hierarchy of master components, the **events are not directly
visible to sibling elements or elements on other pages**.

The solution I evolved to is an implementation of the **Mediator pattern**. On
an Axure page, any given element can update global workflow or UI state
variables and then send a next-state event to a reusable, invisible Mediator
panel. The Mediator panel state change causes a show event on other dynamic
panels on the page, which those panels can use to select a different state. To
achieve cross-page updates, each page load event calls the refresh UI method.

While the use of global variables is a necessary ugliness, the Mediator panel
achieves the **useful decoupling among UI elements** that change workflow
state vs. those that respond to the change.

### Results

The exploratory prototypes using this pattern were **more robust and
believable** than the scripted prototypes they replaced.

The **Mediator pattern** was published as an .rplib master component that
allows an **arbitrary number of UI elements** in an Axure prototype to
**respond individually** to changes in the UI or simulated workflow state.
This master component is **reusable** across multiple prototypes, and **easy
to implement** in new prototypes.

### Notes

> #### Usage notes for Axure prototype
>
> The design example in the prototype is a workflow for a property insurance
> adjuster. The adjuster is assigned a claim, and then must complete an
> estimate for the claim. The estimate is then reviewed by a supervisor, and
> then the adjuster must complete a final bill for the claim. The adjuster can
> then send the estimate and final bill to the customer, and then close the
> claim.
>
> Accept the defaults on the opening configuration screen.
>
> Generally, the active hotspots are signaled with a cursor change, and
> include (in rough order of appearance):
>
>   1. Accept Assignment button
>   2. List entry for Vickie Owens
>   3. Overview and Estimate tabs
>   4. Native Estimating button
>   5. Final Bill checkbox
>   6. Commit & Print button
>   7. dialog action buttons
>   8. Send... button
>   9. Open Estimate button
>   10. Jobs button in the top-level ribbon
>

## Skills

Axure

mediator pattern

## Demos / Artifacts

Axure prototype

Live Axure mediator pattern to allow multiple, unscripted paths through the
mockup.

[View on Axshare](https://l229me.axshare.com/RCE_Workflow_Fixes.html)

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

