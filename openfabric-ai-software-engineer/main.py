import openai

############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:
    output = []

    # Iterate over each input text from the request
    for text in request.text:
        # Step 1: Parse the input text
        parsed_text = parse_input(text)

        # Step 2: Generate a response
        response = generate_science_response(parsed_text)

        # Append the response to the output list
        output.append(response)

    # Step 3: Return the formatted output
    return SchemaUtil.create(SimpleText(), dict(text=output))


def parse_input(text):
    """
    Basic parsing: Converts text to lowercase for uniformity.
    You can expand this function to include more sophisticated NLP techniques,
    like named entity recognition (NER), intent classification, etc.
    """
    return text.lower()


def generate_science_response(parsed_text):
    """
    Generate a response based on the parsed input.
    This function currently handles a few hardcoded science concepts.
    You can extend it with more concepts or integrate a more dynamic approach.
    """

    if "gravity" in parsed_text:
        return "Gravity is a force by which a planet or other body draws objects toward its center. It is what keeps us grounded on Earth!"
    elif "photosynthesis" in parsed_text:
        return "Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll."
    elif "evolution" in parsed_text:
        return "Evolution is the process by which different kinds of living organisms are thought to have developed and diversified from earlier forms during the history of the earth."
    elif "quantum mechanics" in parsed_text:
        return "Quantum mechanics is a fundamental theory in physics that provides a description of the physical properties of nature at the scale of atoms and subatomic particles."
    else:
        # Generic fallback response using a hypothetical model (like OpenAI GPT)
        return ask_science_model(parsed_text)


def ask_science_model(query):
    """
    This function could integrate with an external API like OpenAI's GPT-3 or a custom model.
    For simplicity, this example simulates a model response.
    """
    # Simulated model response:
    return f"I'm still learning, but here's what I think: {query.capitalize()} is an interesting topic!"


# Hypothetical classes that might be part of your project setup

class SimpleText:
    def __init__(self, text=None):
        self.text = text or []

class Ray:
    pass  # Placeholder for any attributes/methods Ray might have

class State:
    pass  # Placeholder for any attributes/methods State might have

class SchemaUtil:
    @staticmethod
    def create(simple_text, data):
        simple_text.text = data.get("text", [])
        return simple_text
