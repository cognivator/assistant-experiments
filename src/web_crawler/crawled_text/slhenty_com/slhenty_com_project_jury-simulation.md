> https://slhenty.com/project/jury-simulation?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Jury Simulation: Constraint satisfaction
networks](/_next/image?url=%2Fimages%2Fjury-simulation.hero.png&w=3840&q=75)

Jury Simulation: Constraint satisfaction networks

ai / ml

### The Project

In the late 1990s, Arizona contemplated a rule change for jurors that would
allow them to **deliberate before all the evidence of a trial was presented**
, the intent being to reach verdicts quicker and make jury duty more
interesting. This project was a **simulation of the jury decision-making
process** to investigate the possible effects on verdict outcomes.

> This project was an **exemplar for research projects** in the distributed
> cognition curriculum **for a decade**.

### My Role

**Principle Investigator** and **ML Engineer** , working as an undergraduate
**under the mentorship of Edwin Hutchins, PhD** , the leading researcher in
the field of distributed cognition.

### Interesting Challenges

The primary challenge for any simulation is **selecting a suitable modeling
paradigm**. For this project, the system being simulated was the
**psychological biases and persuasive susceptibility of a group of human
actors**. At the level of individual actors, a well-known phenomenon called
**'confirmation bias'** is known to operate on an individual’s perception of
real-world evidence. At the level of a group of actors, a **hypothetical
phenomenon coined 'group confirmation bias'** was presumed to operate, and was
the intended focus of the simulation.

In order to simulate individual confirmation bias, a **programming paradigm
called 'constraint-satisfaction network'** was employed. Network nodes
arranged into a small communicating group are allowed to influence each other,
both positively and negatively, until the activation level of the nodes
settles to an equilibrium. For this simulation, the **initial activations
modeled the a priori biases of an individual actor** , and **external
signals** fed into the network **simulated trial evidence**.

To simulate deliberation among individuals, a **collection of constraint
satisfaction networks was connected in a mesh network** to allow each
network’s current activation level to affect the others. For this simulation,
the **timing of inter-network communication was varied** as either early-onset
while evidence was being fed to the individual networks, or late-onset
following the evidence feed.

### Results

The simulation results indicated a **statistically significant main effect of
increased likelihoods of guilty verdicts** when only the timing of jury
deliberation onset was varied, while holding the sequence and content of trial
evidence constant.

This project was **awarded a spot in the 2000 Undergraduate Research
Conference** , where **I presented the research methodology and results** to a
peer group of other similarly-awarded undergraduates and their mentors.

My mentor subsequently used this project and its results as an **exemplar for
research projects** in his distributed cognition curriculum **into the early
2010's**.

## Skills

LISP

cognitive psychology

ANOVA statistical analysis

## Demos / Artifacts

Slide Presentation

The slides presented at the 2000 Undergraduate Research Conference.

[View slides](/docs/Henty-juryShort.pdf)

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

