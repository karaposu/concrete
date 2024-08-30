from llm_handler import  LLMHandler
from stage import  Stage

class Concrete:
    def __init__(self):
        self.llm_handler = LLMHandler()
        self.stages = {
            "idea_refinement": Stage(name="Idea Refinement", llm_handler=self.llm_handler),
            "understanding": Stage(name="Understanding", llm_handler=self.llm_handler),
            "high_level_user_stories": Stage(name="High-Level User Stories", llm_handler=self.llm_handler),
        }
        self.current_stage = "idea_refinement"

    def set_stage(self, stage_name):
        if stage_name in self.stages:
            self.current_stage = stage_name
            return f"Stage set to {stage_name}"
        else:
            raise ValueError(f"Stage {stage_name} does not exist.")

    def get_current_stage(self):
        return self.stages[self.current_stage]

    def pour_idea(self, idea):
        # Delegate the idea pouring to the current stage
        stage = self.get_current_stage()
        return stage.pour_idea(idea)

    def refine_idea(self):
        stage = self.get_current_stage()
        return stage.refine_idea()

    def backpropagate(self):
        stage = self.get_current_stage()
        return stage.backpropagate()

    def compile_document(self):
        # Logic to compile documents from all stages
        documents = [stage.compile_document() for stage in self.stages.values()]
        return "Concrete document compiled from all stages."

    def export_document(self):
        # Logic to export the compiled document
        return f"Document exported for {self.current_stage} stage."
