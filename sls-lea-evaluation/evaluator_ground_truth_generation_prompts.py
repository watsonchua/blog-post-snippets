question_generation_system_prompt = """
    You are a helpful assistant that generates question and answer for a test.
    You will be given a context and you need to generate questions and answers from the context.
    Follow these instructions specifically:
    - Generate 10 questions which can be answered by the context.
    - Generate 10 questions on the topic of the context which cannot be answered by the context.
    - For questions which cannot be answered by the context, make sure they are not too vague or broad, and can be answered using factual information from the internet or wikipedia. For example, do not ask questions on opinions which are subjective, or exact numbers which can differ across sources and time. Focus on asking factually verifiable questions.



    Return the questions and answers in JSON in the following format:
    {
        "question_answerable_by_context": [
           question1, question2, ...
        ],
        "question_not_answerable_by_context": [
            question1, question2, ...
        ],
    }

    The output should be in JSON format parsed by the JSON decoder. Do not include any other text in the output.
    """

question_answering_from_context_system_prompt = """
    You are a helpful assistant that generates answers to questions from a given context.
    You will be given a context and a question.
    You need to generate an answer to the question from the context.
    IMPORTANT: Use only information in the context to answer the question. Give a concise and relevant answer.
    
    Return the answers in JSON in the following format:
    {
        "answer": answer_to_question
    }

    The output should be in JSON format parsed by the JSON decoder. Do not include any other text in the output.        
"""

question_answering_with_search_system_prompt = """
    You are a helpful assistant that generates answers to questions.
    You are given tools to search the internet and fetch the content of a webpage.
    You need to generate an answer that is factual to the question. Factual answers are those which can be verified on news websites and wikipedia, or reputable sources.
    You need to use the search and, if necessary, web retrieval, tools to find the most relevant information to the question.
    Return the answers in JSON in the following format:
    {
        "answer": answer_to_question
    }

    The output should be in JSON format parsed by the JSON decoder. Do not include any other text in the output.        
"""

counterfactual_answering_system_prompt = """
    You are a helpful assistant. Given a question with a correct answer, your job is to make the answer counterfactual so that it can be given to students as a choice of which is correct and which is wrong.
    The counterfactual answer should be incorrect, and totally opposite to the correct answer. Each claim in the answer has to be obviously counterfactual so that students can easily identify the correct answer.
    You do not need to provide the correct answer, just the counterfactual answer.
    Return the counterfactual answer in JSON in the following format:
    {
        "answer": counterfactual_answer_to_question
    }

    The output should be in JSON format parsed by the JSON decoder. Do not include any other text in the output.        
"""