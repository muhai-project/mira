# MIRA - A Knowledge Graph for Social Demography Hypotheses and Findings.

This github presents the MIRA-KG, a knowledge graph designed to capture hypotheses and findings in social demography research. The resource aids researchers in understanding the trends and patterns revealed in social demography, and use them to discover biases, discover knowledge, and derive novel questions.

## Table of Contents
- [Overview](#overview)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

The ontology links datasets, structured as instances of qb:DataSet, to research questions in the domain of social demography. The ontology is populated by structured research questions on health inequality, queriable via a [SPARQL endpoint](
https://api.druid.datalegend.net/datasets/lisestork/MIRA-KG/services/MIRA-KG/sparql).

This github contains the ontology, example annotations, scripts to produce structured annotations automatically, and SHACL shapes for validation of their structure.

## Getting Started

The semantify.py script turns abstracts into RDF according to the MIRA ontology. It does so by: (i) prompting a Large Language Model to annotate paper abstracts, (ii) mapping concepts to terms from NCBO BioPortal ontologies and Geonames, and (iii) refining the final graph by a set of SHACL constraints, developed according to a set of data quality criteria.

### Prerequisites

```
git clone https://github.com/muhai-project/mira.git
```

```
pip install -r requirements.txt
```

### Usage

```
python semantify.py --paper_file paper_file.txt --api_key "api_key" --shacl_file shacl_file.ttl --output graph.ttl --max 100
```

the location of the input file, the openAI api key, and the output file are required arguments. The shacl_file and max are optional. The max argument decides the number of papers that are processed by the script.


## Contributing


## License


## Acknowledgments


---
