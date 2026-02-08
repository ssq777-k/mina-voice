class CommandProcessor:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, handler):
        """
        Register a command with a handler.
        :param command_name: The name of the command.
        :param handler: The function that handles the command.
        """
        self.commands[command_name] = handler

    def process_command(self, voice_input):
        """
        Process the given voice input by matching it with registered commands.
        :param voice_input: The voice command input from the user.
        """
        best_match = None
        highest_similarity = 0

        for command in self.commands:
            similarity = self._fuzzy_match(command, voice_input)
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = command

        if best_match:
            self.commands[best_match]()  # Execute the best matching command
        else:
            print("Command not recognized.")

    def _fuzzy_match(self, command, voice_input):
        """
        A simple fuzzy matching implementation based on the length of the match.
        :param command: Command string to match.
        :param voice_input: Input string from the user.
        :return: A similarity score between 0 and 1.
        """
        command_len = len(command)
        input_len = len(voice_input)
        # Simple matching based on common length
        common_length = len(set(command.lower()) & set(voice_input.lower()))
        return common_length / max(command_len, input_len)
