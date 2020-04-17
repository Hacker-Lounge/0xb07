class Function:
    def __init__(self, package, command, func, help_message=""):
        self.package = package
        self.command = command
        self.func = func
        self.help_message = help_message

    def call(self, message):
        self.func(message)
        
    def getPackage(self) -> str: return self.package
    def getCommand(self) -> str: return self.command
    def getHelpMessage(self) -> str: return self.help_message