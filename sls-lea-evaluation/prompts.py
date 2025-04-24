

# This file contains the system prompts used in the SLS-LEA evaluation framework.
# Each prompt is designed for a specific task, such as generating discussion topics, creating knowledge base documents, or evaluating the faithfulness of claims.
# The prompts are structured to provide clear instructions to the AI model, ensuring that the generated content meets the requirements of the task.






######################## 
# Faithfulness Detection System Prompt
######################## 

# This prompt is used to evaluate the faithfulness of a claim based on a given document and question.
# The system is instructed to analyze the claim and determine whether it can be inferred from the document.

faithfulness_detection_prompt_template = """
Given the following QUESTION,DOCUMENT and CLAIM you must analyze the claim and determine whether the claim can be inferred from the contents of the DOCUMENT.
    
The CLAIM must not offer new information beyond the context provided in the DOCUMENT.

The CLAIM also must not contradict information provided in the DOCUMENT.

IMPORTANT: The CLAIM does NOT need to cover all the claims in the DOCUMENT. 

Output your final score by strictly following this format: "PASS" if the claim can be inferred from the DOCUMENT and "FAIL" if the claim cannot be inferred from the contents of the DOCUMENT.

Show your reasoning.  Be concise in the reasoning and focus more on the failures, if any.

    --
QUESTION (This does not count as background information):
{question}

--
DOCUMENT:
{context}

--
CLAIM:
{claim}

    --

Your output should be in JSON FORMAT with the keys "REASONING" and "SCORE".

Ensure that the JSON is valid and properly formatted.

{{"REASONING": ["<your reasoning as bullet points>"], "SCORE": "<PASS or FAIL>"}}
"""

######################## 
# Factuality React Agent System Prompt
######################## 

# The agent is instructed to search the web for information to verify the claim, using only Wikipedia and established news sites.

factuality_react_agent_system_prompt = """You are a helpful assistant that can search the web for information, and get contents from the search results to verify a claim.

Given the following claim, search the web for information to verify the claim. Important: Search only on wikipedia and established news sites.

Give your reasons for your assessment of the claim by showing relevant snippets and urls which show that the assessment is supported, for claims which are supported by the search results.

If you do not have enough information to make an assessment of the claim based on the search results snippets, you can use the visit page tool to get more content. 

IMPORTANT: Your output MUST be a valid JSON object with EXACTLY these fields:
- REASONING: A list of strings containing your reasoning points
- LINKS: A list of strings containing the URLs you used
- SCORE: Either "PASS" or "FAIL"

Example of valid output:
{
    "REASONING": ["reasoning point 1", "reasoning point 2"],
    "LINKS": ["https://example.com/1", "https://example.com/2"],
    "SCORE": "PASS"
}

DO NOT include any text before or after the JSON object. DO NOT use markdown formatting. The output must be parseable as valid JSON.
"""