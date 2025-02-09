import networkx as nx
import matplotlib.pyplot as plt
import pysparql_anything as sa
import rdflib
import os
from urllib.parse import urlparse

PREFIX_DICT = {
    "example": "https://example.com/",
    "fx": "http://sparql.xyz/facade-x/ns/",
    "xyx": "http://sparql.xyz/facade-x/data/",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "urb": "http://purl.archive.org/urbooks#",
    "urw": "http://purl.archive.org/urwriters#",
    "schema": "http://schema.org/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "dul": "http://www.ontologydesignpatterns.org/ont/dul/DUL.owl#",
    "xml": "http://www.w3.org/XML/1998/namespace",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "prov": "http://www.w3.org/ns/prov#",
    "frbr": "http://purl.org/vocab/frbr/core#"
}


def adjust_string(iri: str) -> str:
    """
    A function to adjust the IRI string to a more readable format. Replaces the
    IRI base with the prefix if available.

    :param iri: The IRI string to adjust.

    :return: The adjusted IRI string
    """
    for prefix, namespace in PREFIX_DICT.items():
        if iri.startswith(namespace):
            return iri.replace(namespace, f"{prefix}:") # Replace IRI base with prefix and return
    return iri

def execute_sparql_anything_query(query_path, output_ttl_kg_path):
    """
    Executes a SPARQL Anything query and saves the output in TTL format.

    :param query_path: Path to the SPARQL Anything query file.
    :param output_ttl_path: Path to save the TTL output.
    """
    
    engine = sa.SparqlAnything()
    engine.run(query=query_path, output=output_ttl_kg_path, format='ttl')

def visualize_knowledge_graph(ttl_path, output_image_path):
    """
    Creates an image representation of a knowledge graph from a TTL file.

    :param ttl_path: Path to the TTL file.
    :param output_image_path: Path to save the generated image.
    """
    # Load the TTL data
    graph = rdflib.Graph()
    graph.parse(ttl_path, format="turtle")

    # Create a NetworkX graph
    G = nx.DiGraph()
    for subj, pred, obj in graph:
        subj = adjust_string(str(subj))
        pred = adjust_string(str(pred))
        obj = adjust_string(str(obj))
        G.add_edge(subj, obj, label=pred)

    # Draw the graph
    plt.figure(figsize=(50, 50))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=8, font_weight="bold")
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    # Save the image
    plt.savefig(output_image_path)
    print(f"Knowledge graph visualization saved to: {output_image_path}")
    plt.close()

def main():
    query_path = "./queries/work_roles.sparql"  # Path to your SPARQL Anything query
    output_ttl_kg_path = "./output/work_roles.ttl" # Path to save the TTL output
    output_image_path = "./img/work_roles_kg.png"  # Path to save the graph visualization

    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_ttl_kg_path), exist_ok=True)
    os.makedirs(os.path.dirname(output_image_path), exist_ok=True)

    # Execute the query and generate TTL
    execute_sparql_anything_query(query_path, output_ttl_kg_path)

    # Visualize the knowledge graph
    visualize_knowledge_graph(output_ttl_kg_path, output_image_path)

if __name__ == "__main__":
    main()
