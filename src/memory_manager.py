class ConversationMemoryManager:
    def __init__(self, max_turns: int = 5):
        """
        In-Memory Context Buffer Queue.
        Preserves rolling chat history for multi-turn local interactions.
        """
        self.max_turns = max_turns
        self.chat_history = []  # Payload schema: [{"role": "user/assistant", "content": "..."}]

    def append_message(self, role: str, content: str):
        """Appends a new conversation node and maintains context window limits."""
        self.chat_history.append({"role": role, "content": content})
        
        # Evicting oldest memory turns if limit is breached to maintain strict context space
        if len(self.chat_history) > (self.max_turns * 2):
            self.chat_history.pop(0)
            self.chat_history.pop(0)

    def get_formatted_history(self) -> str:
        """Transforms structured rolling memory arrays into readable training context."""
        formatted_string = ""
        for message in self.chat_history:
            role_label = "User" if message["role"] == "user" else "Assistant"
            formatted_string += f"{role_label}: {message['content']}\n"
        return formatted_string

    def clear_memory(self):
        """Resets active context history grid completely."""
        self.chat_history = []