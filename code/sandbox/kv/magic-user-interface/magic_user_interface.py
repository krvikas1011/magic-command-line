from input_manager.command_input_manager import init_all_commands


class MagicUserInterface:
    """
    Used to handle user interactions. This involves the input/output management and handling all errors.
    Entry point for Magic UI.
    """

    @staticmethod
    def _init_input_management():
        """
        Used to initialize the listeners for input commands.
        :return: None
        """
        init_all_commands()

    @staticmethod
    def _init_output_management():
        """
        Used to initialize the output libraries.
        :return: None
        """
        pass

    @staticmethod
    def _init_command_processor_interface():
        """
        Used to initialize processors.
        :return: None
        """
        pass

    @staticmethod
    def _setup_error_boundary():
        """
        Used to setup error boundary.
        :return:
        """
        pass

    @staticmethod
    def init_magic_ui():
        MagicUserInterface._init_input_management()
        MagicUserInterface._init_output_management()
        MagicUserInterface._init_command_processor_interface()
        MagicUserInterface._setup_error_boundary()


if __name__ == '__main__':
    MagicUserInterface.init_magic_ui()
