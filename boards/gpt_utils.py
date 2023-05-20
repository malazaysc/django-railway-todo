import openai

openai.api_key = 'fake'

class OpenAIService:
    @staticmethod
    def generate_prompt(board):
        # You can customize this function as much as you want
        return f"""I have a project board about {board.subject}. What are some tasks I 
        could add to my todo list?. Please list them comma separated. 
        So I can run python's split function to parse them to a list.
        The TODO items should be small and actionable. Here are some examples:
        For a board that is about a blog, possible TODOs could be:
        - Write a blog post about GPT-3
        - Add a comment section to my blog
        - Add a contact form to my blog
        - Add a newsletter subscription form to my blog
        - Add a search bar to my blog
        """

    @staticmethod
    def get_suggestions(board, num_suggestions=5):
        prompt = OpenAIService.generate_prompt(board)
        response = openai.Completion.create(engine="gpt-3.5-turbo-0301", prompt=prompt, max_tokens=60, n=num_suggestions)
        return [entry['choices'][0]['text'].strip() for entry in response['choices']]