> https://slhenty.com/project/genai-exploration?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![LLM / Generative AI \(WIP\): Experiments in
Prompting](/_next/image?url=%2Fimages%2Fgenai-exploration.webp&w=3840&q=75)

LLM / Generative AI (WIP): Experiments in Prompting

ai / ml

This page has three main sections:

  * _Reproducing Results_
  * _Explorations_
  * _Insights_

The first two sections are collections of projects and explorations in the
field of Generative AI prompting. The third is a collection of insights and
best practices that I have developed or observed in the course of these
projects.

_Unless noted, all AI prompt explorations used the OpenAI ChatGPT interface
with the GPT-4 model and python-based code analysis plugins in the mid-2023 to
late-2023 timeframe._

### Reproducing Results

* * *

A first step to exploring and expanding knowledge of a topic is to reproduce
known results. The following examples are the results I strove to reproduce.

> With a few exceptions where noted, I originally encountered these projects
> during 1:1 Workshops with [Eric Elliott](http://medium.com/@_ericelliott).

##### Fact-checker - climate change

My first encounter with RAG (Resource Assisted Generation), this is a system
explored by a generative AI research team that ingests a large body of
knowledge and uses it to fact-check claims. Rather than ingest separate
resources, I directed the AI to consider only scholarly climate-science
sources and to provide citations to support its verdict.

##### Generating an LLM prompting language - design SudoLang

Followed Elliott's original article chronicling the development of what he
dubbed, 'SudoLang', a language for prompting a sufficiently-advanced
Generative AI.

##### Subject Matter Expert (SME) Tutor

This is the 'Hello, World' of LLM prompting, described by many sources across
the internet.

##### Interactive storyteller - whispers

A project by Elliott to generate a choose-your-own-adventure story from a
description of the target world.

##### Resource Assisted Generation (RAG) - Holy Grail ingestion

A variation on RAG by Elliott, ingesting the script for Monty Python's, The
Holy Grail, and asking the AI to recount portions of the script based on
inexact prompts. Explores the AI's inference and semantic capabilities.

##### Code assistance - Redux for compost monitor

Working from Elliott's 'autoredux' project, I directed the AI to generate a
Redux state reducer for a web admin interface to a compost monitor (see
_Arduino Maker_ in Explorations below).

### Explorations

* * *

The projects below are novel explorations in Generative AI prompting
techniques — learned or informed by _Reproducing Results_ above — that are
intended to mitigate LLM hallucination and increase reliability. They evolved
from a collection of specific prompts into generalized "personas".

The two generalized personas are described first, followed by a list of the
specific explorations that either gave rise to or exercised the personas.

#### Generalized Personas

##### Consultant Persona

This exploration is a generalization of the role a "Consultant" with a
"Specialty" would play when designing a solution to a project specification.

> Best of class from AWS, Arduino Maker, and Interactive Storyteller

The Consultant portion is general and unchanging, empowered and constrained
to:

  * evaluate and select available components and services
  * design the integration and interaction of the components and services
  * evaluate the suitability of the design for the given project
  * evaluate its own performance and completeness
  * manage its own use of resources to conduct the consultation

The Specialty portion is a separate markdown document that identifies the
domain and the project goals and constraints. The Specialty may also provide a
description of the domain if it is not widely known, but for common domains
simply naming it is usually sufficient.

The Consultant expects a Specialty to be provided, and can then carry out a
"consultation."

##### Tutor Persona

This exploration is a generalization of the role a "Tutor" with a "Subject"
would play when teaching the subject to a student.

> Best of class from Interactive Storyteller, GPT Tutor, and General
> Consultant

The Tutor portion is general and unchanging, empowered and constrained to:

  * generate a lesson plan
  * present topics appropriate for the student's expertise level
  * evaluate the student's understanding with quizzes and exercises
  * manage its own use of resources to conduct the tutoring

The Subject portion is a separate markdown document that identifies the domain
and the specific topics of interest in the domain. The Subject may also
provide a description of the domain if it is not widely known, but for common
domains simply naming it is usually sufficient.

The Tutor expects a Subject to be provided, and can then plan and administer a
course of study.

#### Exploratory Prompts

The following explorations are specific prompts that either led to the
Generalized Personas above, or were used to test and refine the Generalized
Personas.

##### Code Assistant

A prompt to generate Typescript-ready JSDocs from source code comprising
either bare function signatures or explicit type definitions. Achieved
reasonable success and ported several Node.js modules to JSDoc Typescript with
a small amount of hand-tuning.

##### CV / Resume Writer

> This exploration and others lead to the evolution of the Generalized
> Consultant persona

A prompt to write cover letters, resume bullets from a LinkedIn profile.
Ultimately not used or refined - existing tools already do this - but started
the foundation for the Generalized Consultant persona.

##### Arduino Maker

> This exploration and others lead to the evolution of the Generalized
> Consultant persona

A prompt to select Arduino components, design the circuits, and evaluate the
design for completeness based on a "customer spec". The Specification is a
Compost Monitor to measure and track temperature and moisture level of a
compost pile. The AI generated a complete design, wiring diagram, and
microcontroller code that matched my own research into the topic.

##### Amazon Web Services (AWS) Consultant

> This exploration solidified the Generalized Consultant persona

A prompt to recommend AWS services suited to a "cutomer spec," including the
IaC (Infrastructure as Code) necessary to deploy the services. The AI
struggled to generate a complete IaC script, but gave a good start point. The
two specs attempted were a web host and an email service.

This exploration led directly to the Generalized Consultant persona.

##### Structural Design - Specialty for the General Consultant

A Specialization for the Consultant persona to design a replacement for a
wooden stoop. Part of the specification was to take measurements from an image
of the existing stoop.

The AI struggled to properly analyze the image, which led to failures of the
rest of the process. This was, however, before the AI had proper access to
image analysis tools.

##### YouTube Consultant - Specialty for the General Consultant

A Specialization for the Customer persona to advise on tools for the video
production process suitable for YouTube. The AI generated a select list of
tools and a brief description of each.

##### GPT Tutor

> This exploration and others let to the evolution of the Generalized Tutor
> persona

A prompt to explain the concept of Generative AI and give examples of its use.
The response was customized and made appropriate for various lay audiences,
such as: teacher, grandparent, child, etc.

##### Next.js Tutor - Subject for the General Tutor

A Subject for the Tutor persona to teach the Next.js framework at varying
levels of expertise. The AI generated a lesson plan and some rudimentary
exercises, providing a starting point for a technically savvy student.

### Insights

* * *

Successful prompting exhibits the following characteristics, in some
combination.

`>` Declarative over Imperative: _**describe**_ the problem space, resources,
and desired outcome, rather than instructing action

`>` Constraint and Example based: guide outcomes (reliability) and limit
irrelevance (hallucination) using _**constraints**_ and _**examples**_

`>` Implicit over Explicit: apply the _**minimum amount**_ of constraint and
specific guidance necessary to achieve outcomes

`>` "Coaching" vs. "Commanding": use _**encouraging language**_ and tone to
maximize completeness and accuracy

## Skills

LLM / GenAI Prompting

Declarative Programming

Constraint Satisfaction

GenAI 'Psychology'

## Demos / Artifacts

WIP - Git Repo

Experiments with various approaches to LLM / GenAI prompting.

[GitHub](https://github.com/cognivator/ai-whisp/tree/main)

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

