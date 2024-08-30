class Stage:
    def __init__(self, name, llm_handler):
        self.name = name
        self.version = "1.0"
        self.timestamp = None
        self.idea_input = None
        self.refined_output = None
        self.history = []
        self.llm_handler = llm_handler

        # Shortcut prompts
        self.shortcut_prompt_professional = False
        self.shortcut_prompt_fix_grammar = False
        self.shortcut_prompt_sum = False
        self.shortcut_prompt_detailer = False
        self.shortcut_prompt_markdown = False

    def pour_idea(self, idea):
        self.idea_input = idea
        self.timestamp = self._get_current_timestamp()
        self.history.append(("Poured", idea, self.timestamp))
        return f"Idea '{idea}' has been poured in stage '{self.name}'."

    def refine_idea(self):
        if not self.idea_input:
            raise ValueError("No idea to refine. Please pour an idea first.")
        refined = self.llm_handler.refine_idea(self.idea_input)
        self.refined_output = refined
        self.history.append(("Refined", refined, self.timestamp))
        return f"Refined output for stage '{self.name}': {self.refined_output}"

    def backpropagate(self):
        if len(self.history) > 1:
            self.history.pop()  # Remove last step
            last_state = self.history[-1]
            self.idea_input, self.refined_output = last_state[1], None
            return f"Reverted to previous state: {self.idea_input} in stage '{self.name}'."
        else:
            return "No previous state to revert to."

    def compile_document(self):
        if not self.refined_output:
            raise ValueError("No refined output to compile.")
        compiled_document = f"Compiled document based on '{self.refined_output}' in stage '{self.name}'."
        self.history.append(("Compiled", compiled_document, self.timestamp))
        return compiled_document

    def _get_current_timestamp(self):
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%y %H:%M:%S")

    def return_previous_version(self):
        if len(self.history) > 1:
            previous_state = self.history[-2]
            return f"Previous version in stage '{self.name}': {previous_state[1]}"
        else:
            return "No previous version available."

    def pull_refiner_to_raw(self):
        if self.refined_output:
            self.idea_input = self.refined_output
            self.refined_output = None
            self.timestamp = self._get_current_timestamp()
            self.history.append(("Pulled to Raw", self.idea_input, self.timestamp))
            return f"Refined output has been pulled back to raw input in stage '{self.name}'."
        else:
            return "No refined output available to pull."

    def apply_shortcut_prompt(self):
        if not self.idea_input:
            raise ValueError("No idea to refine. Please pour an idea first.")

        refined = self.idea_input

        if self.shortcut_prompt_professional:
            refined = self.llm_handler.professionalize_idea(refined)
        if self.shortcut_prompt_fix_grammar:
            refined = self.llm_handler.refine_idea(refined)  # Assuming the refine method also fixes grammar
        if self.shortcut_prompt_sum:
            refined = self.llm_handler.summarize_idea(refined)
        if self.shortcut_prompt_detailer:
            refined = self.llm_handler.detail_idea(refined)
        if self.shortcut_prompt_markdown:
            refined = self.llm_handler.convert_to_markdown(refined)

        self.refined_output = refined
        self.timestamp = self._get_current_timestamp()
        self.history.append(("Shortcut Applied", refined, self.timestamp))
        return f"Shortcut prompts applied to the idea in stage '{self.name}'. Refined output: {self.refined_output}"
