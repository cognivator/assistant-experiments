> https://slhenty.com/project/climate-change-bias?a=true&n=99



Steve Henty

![Steve
Henty](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2FProfile_close_square.f71e0d71.jpg&w=3840&q=75)

UI Development

UX Design

AI / ML Adoption

[Projects](/?a=true&n=99#projects)

![Climate Change: Detecting bias in news
reporting](/_next/image?url=%2Fimages%2Fclimate-model.webp&w=3840&q=75)

Climate Change: Detecting bias in news reporting

ai / ml

### The Project

Create and publish an AI / ML model that **fact checks** climate-related
claims and **detects bias** in news reporting on climate change. The model is
used to analyze and score news articles on demand. The implementation goal is
to be **simple enough for "someone's grandmother" to use**.

### My Role

**Team Leader** and **ML Engineer** for the model selection and training phase
of the project.

### Interesting Challenges

The biggest challenge was **obtaining model training data**. Having identified
BERT base models trained on sentence- and document-length data as the models
of choice, we could rely on **transfer learning** to fine tune the models to
our task. Unfortunately, effective fine-tuning requires a large amount of
**labeled training data** that **simply didn't exist** for the climate domain.

We had access only to a **small climate-specific dataset** for fine-tuning,
but it was not in a format that could be used directly. We wrote code to
**convert the dataset** to fine-tune our **sentence- and document-based BERT
base models** for comparison with models that had been fine-tuned on
scientific, albeit non-climate related datasets - e.g. medical research,
environmental reports, etc. The performance of our fine-tuned models was
**slightly better** than the base models, but **not as good** as the models
**trained on large scientific datasets**.

In the end we used **BERT base models fine-tuned on scientific datasets**
which provided reasonable performance for our climate domain.

### Results

The team published a **chrome extension** that uses both sentence- and
document-based models to score news articles. The extension can **harvest the
entire article** , or work from **selected text**.

A **web site** that allows **greater control over the model operation** was
also made available, primarily for the team's use **during model development**
, or for **other researchers and interested parties**.

The team wrapped up the project by presenting the research, modeling, and
development activities, and **live demos** of the chrome extension and web
site to the Omdena organization.

## Skills

Python, Jupyter

HuggingFace

BERT, Transformers

Dataset preparation

## Demos / Artifacts

Omdena Presentation

Project summary and demo presented to Omdena organization.

[Omdena Cologne Presentation
(LinkedIn)](https://www.linkedin.com/events/areal-worldaiprojectwalk-
throug7067127135664021504/about/)

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

