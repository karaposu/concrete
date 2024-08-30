from langchain import OpenAI


class LLMHandler:
    def __init__(self, model_name="gpt-4"):
        self.model_name = model_name
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        # Initialize the LLM using LangChain's OpenAI wrapper
        return OpenAI(model_name=self.model_name)

    def refine_idea(self, idea_text):
        # Use the LLM to refine the given idea
        prompt = self._create_refinement_prompt(idea_text)
        return self.llm(prompt)

    def generate_content(self, context, task):
        # Use the LLM to generate content based on a given context and task
        prompt = self._create_generation_prompt(context, task)
        return self.llm(prompt)

    def professionalize_idea(self, idea_text):
        # Rephrase the idea in a professional way
        prompt = self._create_professional_prompt(idea_text)
        return self.llm(prompt)

    def detail_idea(self, idea_text):
        # Rewrite the idea with more details
        prompt = self._create_detailer_prompt(idea_text)
        return self.llm(prompt)

    def convert_to_markdown(self, idea_text):
        # Convert the idea to markdown format
        prompt = self._create_markdown_prompt(idea_text)
        return self.llm(prompt)

    def summarize_idea(self, idea_text):
        # Summarize the idea
        prompt = self._create_sum_prompt(idea_text)
        return self.llm(prompt)

    # Internal prompt creation methods
    def _create_refinement_prompt(self, idea_text):
        return f"Refine the following idea: {idea_text}"

    def _create_generation_prompt(self, context, task):
        return f"Given the context: {context}, perform the following task: {task}"

    def _create_professional_prompt(self, idea_text):
        return f"Rephrase the following idea in a professional way: {idea_text}"

    def _create_detailer_prompt(self, idea_text):
        return f"Rewrite the following idea with more details: {idea_text}"

    def _create_markdown_prompt(self, idea_text):
        return f"Convert the following idea to markdown: {idea_text}"

    def _create_sum_prompt(self, idea_text):
        return f"Summarize the following idea: {idea_text}"
