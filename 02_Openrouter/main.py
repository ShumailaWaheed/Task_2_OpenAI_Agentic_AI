import random
import time

class Agent:
    # A simple Agent class that can send messages to other agents and reply
    def __init__(self, name):
        self.name = name
        self.moods = ["Happy", "Excited", "Curious", "Serious"]
        self.message_types = {
            "Friendly": [
                "Hey there! How are you?",
                "Hello friend! Long time no see!",
                "Hi! Hope everything is good?"
            ],
            "Serious": [
                "We need to talk about something important.",
                "Can you spare a minute? It's urgent.",
                "I have something to discuss, please listen."
            ],
            "Casual": [
                "Yo! What's up?",
                "Just chilling?",
                "Just checking in — hope all's well."
            ]
        }

    def send_message(self, other_agent):
        # Send a random mood and message to another agent
        mood = random.choice(self.moods)
        message_type = random.choice(list(self.message_types.keys()))
        message = random.choice(self.message_types[message_type])

        self._simulate_typing()
        print(f"{self.name} [{message_type}] says: {message}")
        other_agent.receive_message(self, message, mood)

    def receive_message(self, sender_agent, message, mood):
        # Print the received message and reply
        print(f"{self.name} received a message from {sender_agent.name} ({mood}): {message}")
        reply = f"Thanks for reaching out, {sender_agent.name}! I'm feeling {random.choice(self.moods)} today."
        print(f"{self.name} replies: {reply}")

    def _simulate_typing(self):
        # Simulate a typing animation
        print(f"{self.name} is typing...", end="", flush=True)
        time.sleep(1)
        print("\r", end="")

if __name__ == "__main__":
    agent1 = Agent("Agent_Alpha")
    agent2 = Agent("Agent_Beta")

    agent1.send_message(agent2)
    print()
    agent2.send_message(agent1)

    agent2.send_message(agent1)
