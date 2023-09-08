import argparse
from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.namespace import SKOS, RDF, RDFS, XSD
from pyshacl import validate


def validate_graph(batch_file,shacl_file,validation_output=None,verbose=False):
    shacl_graph = Graph()
    shacl_graph.parse(shacl_file, format="ttl")
    batch_graph = Graph()
    batch_graph.parse(batch_file, format="ttl")
    # print(batch_graph.serialize(format='turtle'))
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
    if validation_output != None:
        results_graph.serialize(validation_output,format='turtle')
    return results_graph

def main(batch_file, shacl_file,validation_output,verbose=False):

    results_graph = validate_graph(batch_file,shacl_file,validation_output)
    if verbose:
        print(results_graph.serialize(format='turtle'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validating an RDF graph according to the MIRA ontology.")

    parser.add_argument("--shacl_file", type=str, help="Path to shacl file for validation.")
    parser.add_argument("--batch_file", type=str, help="Path to .ttl file for the batch to be validated.")
    parser.add_argument("--validation_output", type=str, help="Path to .ttl file for storing the output graph.")
    parser.add_argument("--verbose", type=int, help="Print the shacl validations as a serialised graph.")

    args = parser.parse_args()
    main(args.batch_file,args.shacl_file,args.validation_output,args.verbose)
