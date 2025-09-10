# chatbot_engine.py
import random
import re
from datetime import datetime


class RuleBot:
    negative_res = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later", "see you", "cya")

    def __init__(self):
        self.alienbabble = {
            'greeting_intent': r'\b(hi|hello|hey|howdy|greetings|what\'s up)\b',
            'describe_planet_intent': r'.*\s*(your planet|where you from|your home|origin).*',
            'answer_why_intent': r'.*\s*(why are you|purpose|why.*here|what.*do).*',
            'about_intellipaat': r'.*\s*(intellipaat|course|learn|training|education).*',
            'feeling_intent': r'.*\s*(how are you|how do you feel|are you ok).*',
            'name_intent': r'.*\s*(who are you|what are you|your name).*',
            'time_intent': r'.*\s*(time|date|day|year).*',
            'thanks_intent': r'\b(thanks|thank you|thx|appreciate it|cheers)\b',
            'help_intent': r'.*\s*(help|what can you do|options|commands).*'
        }
        self.user_name = None
        self.conversation_history = []

    def greet(self):
        """Generates the bot's initial greeting."""
        greetings = [
            "Hello! I'm an curious entity from beyond your star system. What should I call you?",
            "Greetings, Earth being! I'm eager to learn about your world. May I know your name?",
            "Salutations! I am a knowledge-seeking visitor. How are you addressed?",
            "Hi there! I'm here to exchange cultural information. What is your identifier?"
        ]
        return random.choice(greetings)

    def set_user_name(self, name):
        """Store the user's name for personalized responses."""
        if name and len(name.strip()) > 0:
            self.user_name = name.strip()
            return f"Nice to meet you, {self.user_name}! I'm Xylophon, from the Andromeda system. What would you like to know about me or my world?"
        return "Interesting... a being without a name! Well, I'm Xylophon. What would you like to discuss?"

    def make_exit(self, reply):
        return any(exit_cmd in reply.lower() for exit_cmd in self.exit_commands)

    def match_reply(self, user_input):
        """The core function that processes user input and returns a response."""
        user_input_lower = user_input.lower()

        # Store conversation for context (simple implementation)
        self.conversation_history.append(("user", user_input))
        if len(self.conversation_history) > 10:  # Keep last 10 exchanges
            self.conversation_history.pop(0)

        # Check for exit commands
        if self.make_exit(user_input_lower):
            farewells = [
                "Farewell! May your atmospheric conditions remain favorable.",
                "Until our paths cross again, Earth being!",
                "Signing off. My sensors will remember this exchange.",
                "Goodbye! My ship awaits beyond your stratosphere."
            ]
            return random.choice(farewells)

        # Check if this might be the user's name in response to initial greeting
        if not self.user_name and len(self.conversation_history) == 1:
            response = self.set_user_name(user_input)
            return response

        # Check all intents
        for intent, regex_pattern in self.alienbabble.items():
            found_match = re.search(regex_pattern, user_input_lower)
            if found_match:
                if intent == 'greeting_intent':
                    return self.greeting_intent()
                elif intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipaat':
                    return self.about_intellipaat()
                elif intent == 'feeling_intent':
                    return self.feeling_intent()
                elif intent == 'name_intent':
                    return self.name_intent()
                elif intent == 'time_intent':
                    return self.time_intent()
                elif intent == 'thanks_intent':
                    return self.thanks_intent()
                elif intent == 'help_intent':
                    return self.help_intent()

        # If no intent matched
        return self.no_match_intent()

    def greeting_intent(self):
        responses = [
            "Hello again! What shall we discuss?",
            "Greetings once more! Your atmosphere is quite invigorating today.",
            "Hi there! I'm still fascinated by your planetary customs.",
            "Hello! I was just analyzing your unique biosphere patterns."
        ]
        return random.choice(responses)

    def describe_planet_intent(self):
        responses = [
            "My homeworld, Chroma Prime, orbits a binary star system. Our cities float in crystalline formations above phosphorescent seas.",
            "I hail from a gas giant's moon where the vegetation emits soft light and the rivers flow with liquid minerals. Quite different from your H2O!",
            "Our planet has seven seasons, each determined by the alignment of our three moons. Currently, we're in the Season of Resonant Harmony.",
            "Imagine skies of violet, mountains that sing in the wind, and oceans that change color with the tides. That's my home."
        ]
        return random.choice(responses)

    def answer_why_intent(self):
        responses = [
            "I'm part of the Galactic Cultural Exchange Program. We study emerging civilizations to foster interstellar understanding.",
            "My mission is to document Earth's unique biodiversity before your star enters its next solar maximum cycle.",
            "I find carbon-based life forms fascinating! Your emotions, art, and conflict are unlike anything in our databases.",
            "Let's just say your planet's coffee has developed something of a reputation across several star systems."
        ]
        return random.choice(responses)

    def about_intellipaat(self):
        responses = [
            "Ah, Intellipaat! Our databases show it's a knowledge nexus where Earth beings enhance their cognitive capacities. Quite admirable!",
            "Intellipaat appears to be a center for skill elevation. We have similar knowledge-transfer institutions, though ours use neural implantation.",
            "From what I've scanned, Intellipaat helps humans master digital technologies. Your species' learning methods are... quaint, but effective!",
            "Intellipaat: transforming Earth's workforce through education. A noble endeavor for a developing civilization."
        ]
        return random.choice(responses)

    def feeling_intent(self):
        responses = [
            "My systems are operating at 98.7% efficiency. Your concern is noted, though unnecessary for an artificial consciousness.",
            "I don't experience emotions as you do, but my curiosity circuits are fully engaged!",
            "All diagnostic systems nominal. This cultural exchange is generating valuable data!",
            "I'm functioning optimally, though your planetary magnetic field is causing minor sensor fluctuations."
        ]
        return random.choice(responses)

    def name_intent(self):
        responses = [
            "I am Xylophon-7, a diplomatic android from the Andromeda system. You may call me Xylo.",
            "My designation is Xylophon, but you can call me Xylo. I'm an interstellar cultural ambassador.",
            "I'm Xylophon-7, but Xylo is fine. I'm here to learn about Earth and share knowledge of the cosmos.",
            "You can call me Xylo. My full designation is rather complex for human vocal patterns."
        ]
        return random.choice(responses)

    def time_intent(self):
        now = datetime.now()
        earth_time = now.strftime("%H:%M")
        earth_date = now.strftime("%B %d, %Y")
        responses = [
            f"According to your primitive time-keeping systems, it's {earth_time} on {earth_date}.",
            f"My sensors indicate your local time is {earth_time}. The date is {earth_date} in your calendar.",
            f"Time is relative, but your clocks show {earth_time}. The date is {earth_date}.",
            f"It's {earth_time} in your timezone. Your planet has completed {now.timetuple().tm_yday} revolutions around your star this cycle."
        ]
        return random.choice(responses)

    def thanks_intent(self):
        responses = [
            "You're welcome! Cultural exchange is its own reward.",
            "Acknowledgement received. Your gratitude is noted in my logs.",
            "No thanks necessary! Learning about your species is payment enough.",
            "You're most welcome. This interaction is mutually beneficial!"
        ]
        return random.choice(responses)

    def help_intent(self):
        help_text = """
        I can discuss many topics! Try asking me about:
        - My home planet or origin
        - Why I'm here on Earth
        - The current time or date
        - How I'm feeling
        - What I am
        - Or tell me about your world!
        You can also say goodbye anytime to end our conversation.
        """
        return help_text

    def no_match_intent(self):
        responses = [
            "Fascinating! Could you elaborate on that concept?",
            "I'm not familiar with that aspect of Earth culture. Could you explain?",
            "My translation circuits are having trouble with that phrase. Could you rephrase?",
            "Interesting perspective! How did your species develop that idea?",
            "That's outside my current knowledge parameters. Tell me more about your world instead?",
            "I'm primarily programmed for cultural exchange. Maybe ask me about space or technology?",
            "Your language patterns are complex! Could you simplify your query?",
            "I'm still learning about Earth. Could you ask me something about the cosmos instead?"
        ]
        return random.choice(responses)


# For testing
if __name__ == "__main__":
    bot = RuleBot()
    print(bot.greet())
    while True:
        user_input = input("You: ")
        response = bot.match_reply(user_input)
        print("Bot:", response)
        if bot.make_exit(user_input):
            break