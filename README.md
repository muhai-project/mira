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

Research questions for social history research, such as from social demography, commonly include (i) descriptive questions, (ii) comparative questions, and (iii) explanatory questions. Here, each question is based on the output from the previous one. Preferably, these questions are all derived from one another, and from the dataset. See the image below. The MIRA ontology thus links datasets to questions, preferably as linked open data according to the RDF Data Cube Vocabulary. An example is shown in the figure below.

![Example annotation](./figures/data-explanations.png)

The ontology is populated by structured research questions on health inequality, queriable via a [SPARQL endpoint](
https://api.druid.datalegend.net/datasets/lisestork/MIRA-KG/services/MIRA-KG/sparql).

This github contains the ontology, example annotations, scripts to produce structured annotations automatically from paper abstracts (but only the explanatory questions and their evidence), and SHACL shapes for the validation of generated annotations.

### Prerequisites

1. clone the project
```
git clone https://github.com/muhai-project/mira.git
```

2. set up an environment (like anaconda) from the requirement.txt file
```
pip install -r requirements.txt
```

### Usage

The semantify.py script turns research paper abstracts of papers on social demography into RDF according to the MIRA ontology. It does so by: (i) prompting a Large Language Model to annotate paper abstracts, (ii) mapping concepts to terms from NCBO BioPortal ontologies and Geonames. An example annotation is shown in the figure below:

![Example annotation](./figures/example-annotation.png)
```
python semantify.py --paper_file paper_file.pkl --api_key "api key" --output output_graph.ttl --max 1 --print True

```

The location of the input file, the openAI api key, and the output file are required arguments. Max and print are optional and indicate how many papers to process, and whether to print the serialised RDF after each step. _To check whether all works as expected, we recommend to first set these to 1 and True, before processing a large batch._

The --paper_file argument expects the location of a pickle file (.pkl) which consists of a list of dictionaries with the following keys:
dict_keys(['paperId','title','abstract','year','publicationDate','authors','references'])
These can, for instance, be retrieved from Semantic Scholar:

```
from semanticscholar import SemanticScholar

sch = SemanticScholar()
results = sch.search_paper('',year=, fields_of_study=[''])
papers = [sch.get_paper(result.paperId) for result in results]
```

You can use the validate.py script to validate the set against a set of SHACL shapes, developed according to a set of data quality criteria.

```
python validate.py --batch_file batch_file.ttl --shacl_file shacl_file.ttl --validation_output validation_results.ttl --verbose True

```
## License

This project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

## Acknowledgments
This work was funded by the European MUHAI project (Horizon 2020 research and innovation program) under grant agreement
number 951846. We thank Tobias Kuhn and Inès Blin for the insightful discussions that contributed to this work.

---
