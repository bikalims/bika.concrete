## bika.concrete

**Concrete & Cement Testing LIMS Add-on for Bika and Senaite LIMS**

An add-on for professional open-source Laboratory Information Management Systems, specifically designed for **concrete manufacturing**, **ready-mix plants**, **cement laboratories**, and **concrete research institutions**.

### Overview

`bika.concrete` extends **Senaite** (the modern core of Bika LIMS) with industry-specific functionality for the concrete and construction materials testing sector.

It helps labs manage:
- Concrete mix designs
- Raw material testing (aggregates, cement, admixtures, water)
- Batch production and sampling
- Time-series results and graphs for e.g. Compression testing over weeks
- Quality control
- Certificates of Analysis (COA) for concrete batches

### Features

- Dedicated **Concrete Mix** and **Batch** management
- Support for standard concrete tests (compressive strength, slump, air content, density, etc.)
- Time-based result tracking (e.g., 7-day, 28-day, 56-day strength)
- Materials library for aggregates, binders, and admixtures
- Automated calculations and trend analysis
- Full audit trail and ISO-compliant workflows

### Requirements

- **Senaite** (recommended latest version) or **Ingwe Bika LIMS 4**
- Plone 5 / Python 3 environment
- Bika Lab Systems professional support (optional but recommended for production use)

### Installation

#### Using Buildout (Classic Plone/Senaite)

Add the following to your `buildout.cfg`:

cfg
[buildout]
eggs =
    ...
    bika.concrete

Then run:
Bashbin/buildout

#### Docker (Recommended for Ingwe Bika LIMS 4)

Add bika.concrete to your custom add-ons list in the Docker-based Ingwe Bika distribution.

### User Manual

[Bika Concrete user Manual](https://www.bikalims.org/new-manual/bika-concrete)

### License
This project is licensed under the GNU General Public License v2.0 (GPL-2.0).

Support & Professional Services
[Bika Lab Systems](www.bikalabs.com) offers professional implementation, training, custom development, and support for bika.concrete.

Website: [https://www.bikalims.org](https://www.bikalims.org)
Email: info@bikalims.org (or contact Lemoene directly)

Made with ❤️ in Cape Town, South Africa
