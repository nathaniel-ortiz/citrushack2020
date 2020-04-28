# Citrus Hack 2020

## [Galacta](https://devpost.com/software/galacta)

Galacta was our submission to Citrus Hack 2020, and won Best Domain!

## What it does
Galacta is a simple web interface to map the galaxy using Aladin and AstroPy. It allows to you see a visual map of where each celestial body is, and calculate the coordinates and distance from relative to your position on earth. Galacta is a Google Cloud-based Website, hosting astronomical survey data in addition to companion Python scripts. The Galacta team identified the opportunity to develop an educational and interactive celestial platform as a way to bridge casual space enthusiasts and hardcore astronomers. This was accomplished by creating a sleek, user-friendly website under the .space domain to house a variety of feature-packed libraries and APIs. At the core of the Galacta domain is the Aladin Lite astronomical survey data map, a rich Javascript-enabled Python program that allows users to explore far beyond their own solar system. This toolkit, developed at the University of Saulsburg, allows for survey data selection, enabling users to finely control their level of detail. In addition, users are able to plot data points, interact with a wide array of imaging maps, and scale in a projected 3D environment. Another of Galacta’s core features is a celestial countdown timer array, powered by Google Cloud’s Wordpress one-stop integration modules. The array displays visual countdowns to the next Haley’s Comet passing, Mercury Transit, and total solar and lunar eclipses
## How we built it
We build Galacta on AstroPy, Wordpress and Aladin. We used AstroPy to calculate the coordinates of each body, and then serialize it with JSON. Wordpress hosts the site, and Aladin maps everything. We also deployed the site using the Google Cloud Platform Wordpress deployment.

We also attempted to incorporate weather functionality, but we were not able to integrate it into the site.
## Challenges we ran into
Serializing the data into a JSON format was actually very difficult, as there is no way to individually access each element in a SkyCoord object, the data format the coordinates are returned in.

Setting up our Python virtual environments was also difficult, as well as finding the necessary libraries.
## Accomplishments that we're proud of
Getting the output serialized into JSON. This is also our first hackathon, and our first project outside of the learning environment.
