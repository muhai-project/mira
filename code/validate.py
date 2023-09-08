import argparse
from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.namespace import SKOS, RDF, RDFS, XSD
from pyshacl import validate


def validate_graph(batch,shacl_file,validation_output):
    shacl_graph = Graph()
    shacl_graph.parse(shacl_file, format="ttl")
    batch_graph = Graph()
    batch_graph.parse(batch_file, format="ttl")
    print(batch_graph.serialize(format='turtle'))
    r = validate(batch_graph,
          shacl_graph=shacl_graph)
    conforms, results_graph, results_text = r

    if conforms:
        print("Validation successful. No violations found.")
    else:
        print("Validation failed. Violations found.")

        # Extract the violations from the results_graph
        violations = list(results_graph.triples((None, None, None)))

        # Print the number of violations
        print(results_graph.serialize(format='turtle'))
    if validation_output:
        results_graph.serialize(validation_output,format='turtle')

def main(batch_file, shacl_file):

    validate_graph(batch_file,shacl_file,validation_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validating an RDF graph according to the MIRA ontology.")

    parser.add_argument("shacl_file", type=str, required=True, help="Path to shacl file for validation.")
    parser.add_argument("batch_file", type=str, required=True, help="Path to .ttl file for the batch to be validated.")
    parser.add_argument("validation_output", type=str, required=False, help="Path to .ttl file for storing the output graph.")

    args = parser.parse_args()
    main(args.batch_file,args.shacl_file,args.validation_output)
