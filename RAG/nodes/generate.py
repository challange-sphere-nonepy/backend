from RAG.agents.generate import rag_chain
from langchain_core.messages import AIMessage


def generate(state):
    """
    Generate answer

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): New key added to state, generation, that contains LLM generation
    """
    print("---GENERATE---")
    question = state["question"]
    # question = state["contextualized_question"]
    web_documents = state["web_search_documents"]
    namal_vector_documents = state["namal_vector_search_documents"]
    ranil_vector_documents = state["ranil_vector_search_documents"]
    sajith_vector_documents = state["sajith_vector_search_documents"]
    # chat_history = state["chat_history"]
    # print(chat_history)
    # RAG generation
    generation = rag_chain.invoke(
        {
            "web_context": web_documents,
            "namal_context": namal_vector_documents, 
            "ranil_context": ranil_vector_documents, 
            "sajith_context": sajith_vector_documents, 
            "question": question,
            # "chat_history": chat_history
        }
    )

    # state["chat_history"].append(AIMessage(content=generation))
    generated_count = state.get("generated_count", 0) + 1

    return {
        "question": state["question"],
        "contextualized_question": question, 
        "generation": generation,
        "generated_count": generated_count,
        "state": state
    }