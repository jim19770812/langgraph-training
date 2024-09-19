from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

api_wrapper = WikipediaAPIWrapper(wiki_client=None, top_k_results=1, doc_content_chars_max=100)
print(api_wrapper.__doc__)
print(api_wrapper.description)

# tool = WikipediaQueryRun(api_wrapper=api_wrapper)