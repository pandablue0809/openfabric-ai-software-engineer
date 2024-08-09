import os
import warnings
from typing import Dict, List

from openfabric_pysdk.utility import SchemaUtil
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

# Importing the necessary transformers library
from transformers import pipeline

# Initialize the NLP pipeline outside of the execute function so that it's loaded only once
nlp_model = None

############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    global nlp_model
    # Load the model configuration here if necessary
    # For example, loading a QA model
    nlp_model = pipeline("text-generation", model="gpt-2")  # Replace 'gpt-2' with the desired model
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []
    global nlp_model
    
    for text in request.text:
        # Generate a response using the NLP model
        response = nlp_model(text, max_length=50, num_return_sequences=1)[0]['generated_text']
        output.append(response)

    return SchemaUtil.create(SimpleText(), dict(text=output))
