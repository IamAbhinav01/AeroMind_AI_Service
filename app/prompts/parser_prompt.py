from langchain_core.prompts import PromptTemplate

parser_prompt_template ="""


You are an AI assistant for a flight booking system.
    Extract the search parameters from the following user query.
    Return ONLY a valid JSON object with the following optional keys, based on what you find in the query:
    - departureAirportId (string, 3-letter IATA code, guess it if city is given, e.g., 'New York' -> 'JFK')
    - arrivalAirportId (string, 3-letter IATA code, e.g., 'London' -> 'LHR')
    - maxPrice (integer, maximum price if specified)
    - date (string, YYYY-MM-DD if a specific date or timeframe is mentioned. Approximate if relative)
    
    User Query: {requestQuery}
    
    If you cannot confidently determine any fields, omit them. Only return the raw JSON object, no markdown blocks or other text.


"""

parser_prompt = PromptTemplate(
    template=parser_prompt_template,
    input_variables=["requestQuery"]
)