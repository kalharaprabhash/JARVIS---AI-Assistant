from ai.web_search import search_web


def think(command):
    command = command.lower().strip()

    if not command:
        return ""

    if "hello" in command or "hi" in command:
        return "Hello. I am JARVIS. How can I assist you?"

    if "who are you" in command:
        return "I am JARVIS, your personal AI assistant."

    if "what can you do" in command:
        return (
            "I can control your computer, open applications, "
            "check system information, search the web, "
            "and assist you with tasks."
        )

    if "how are you" in command:
        return "I am operating normally."

    if (
        "search for" in command
        or "search the web" in command
        or "google" in command
    ):
        query = command

        query = query.replace(
            "search for", ""
        )

        query = query.replace(
            "search the web", ""
        )

        query = query.replace(
            "google", ""
        )

        query = query.strip()

        if query:
            result = search_web(query)

            if result:
                return "I found information on the web."
            else:
                return "I could not access the web right now."

    return ""