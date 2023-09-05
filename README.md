# MIRA - Mechanisms of Inequality: A Knowledge Graph for Social Demography Hypotheses and Findings.

This github presents the MIRA-KG, a knowledge graph designed to capture hypotheses and findings in social demography research. The resource aids researchers in understanding the trends and patterns revealed in social demography, and use them to discover biases, discover knowledge, and derive novel questions.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The ontology links datasets, structured as instances of qb:DataSet, to research questions in the domain of social demography. The ontology is populated by structured research questions on health inequality, queriable via a [SPARQL endpoint](
https://api.druid.datalegend.net/datasets/lisestork/MIRA-KG/services/MIRA-KG/sparql).

This github contains the ontology, example annotations, scripts to produce structured annotations automatically, and SHACL shapes for validation of their structure.

## Getting Started

Requirements can be found in
by: (i) prompting a Large Language Model to annotate paper abstracts, (ii) mapping concepts to terms from NCBO BioPortal ontologies, Geonames, and CauseNet for capturing causal pathways, and (iii) refining the final graph by a set of SHACL constraints, developed according to a set of data quality criteria.

### Prerequisites

git clone https://github.com/muhai-project/mira.git

pip install -r requirements.txt


### Usage

python semantify.py --paper_file paper_file.txt --output graph.ttl


## Data



## Results


## Contributing


## License


## Acknowledgments


---
