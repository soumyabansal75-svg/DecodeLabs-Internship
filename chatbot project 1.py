def run_chatbot():
    # ==========================================
    # 1. EXPANDED KNOWLEDGE BASE
    # ==========================================
    # Key-Value pairs for O(1) constant lookup time
    knowledge_base = {
        # Greetings
        "hello": "Hi there! Welcome to the DecodeLabs team. Ready to build?",
        "hi": "Hello! Let's master some deterministic logic gates today.",
        "hey": "Hey! Great to see you. What would you like to learn?",
        "hey robot": "Hey Human! I am ready. What is your query?",
        
        # Project Related
        "project 1": "Project 1 is the Rule-Based AI Chatbot—the foundation skeleton for AI Guardrails.",
        "project1": "Project 1 is the Rule-Based AI Chatbot—the foundation skeleton for AI Guardrails.",
        "what is project 1": "Project 1 is learning control flow and logic before moving to probabilistic AI.",
        
        # Systems
        "system 1": "System 1 is Probabilistic (The Artist). It's flexible but prone to hallucinations.",
        "system1": "System 1 is Probabilistic (The Artist). Flexible but prone to hallucinations.",
        "system 2": "System 2 is Deterministic (The Engineer). It is hard-coded, safe, and traceable.",
        "system2": "System 2 is Deterministic (The Engineer). It is hard-coded, safe, and traceable.",
        "difference": "System 1 is flexible but unpredictable. System 2 is rigid but 100% accurate.",
        
        # Core Concepts
        "guardrails": "AI guardrails act as a deterministic filter for probabilistic LLMs to ensure safety.",
        "efficiency": "Using a dictionary gives us O(1) constant lookup time, no matter how large!",
        "logic": "We use deterministic logic—an O(1) hash map lookup instead of slow if-elif chains.",
        "hallucination": "Hallucination is when AI makes up false information. Guardrails prevent this!",
        
        # Commands
        "help": "Available commands: hello, project 1, system 1, system 2, guardrails, efficiency, or exit.",
        "commands": "You can ask about: project 1, system 1, system 2, guardrails, efficiency, logic, or exit.",
        "list": "Try asking: hello, project 1, system 1, system 2, guardrails, efficiency, or exit.",
        
        # Fun
        "who are you": "I am a deterministic rule-based AI. I have no hallucinations—only facts!",
        "who": "I am DecodeLabs' AI, built with deterministic logic gates.",
        "joke": "Why did the AI cross the road? It couldn't—it was stuck in a deterministic loop! (;",
        "thanks": "You're welcome! Happy to help with your logic training.",
        "thank you": "You're welcome! Keep building those logic skills."
    }

    # Fallback response for unknown inputs
    fallback = "I do not understand. Type 'help' for available commands."

    # ==========================================
    # 2. WELCOME MESSAGE
    # ==========================================
    print("=" * 50)
    print("🤖 DECODELABS CHATBOT - LOGIC ENGINE v1.0")
    print("=" * 50)
    print("🤖 System initialized. Deterministic mode: ACTIVE")
    print("🤖 Type 'help' for commands or 'exit' to quit.")
    print("=" * 50)

    # ==========================================
    # 3. MAIN CHAT LOOP
    # ==========================================
    while True:
        # Get user input
        raw_input = input("\nYou: ")
        
        # Handle empty input
        if not raw_input.strip():
            print("🤖 Bot: Please type something!")
            continue
            
        # Sanitize: lowercase + remove whitespace
        clean_input = raw_input.lower().strip()

        # Exit condition
        if clean_input == "exit":
            print("\n🤖 Bot: Shutting down logic engine. Goodbye!")
            break

        # ==========================================
        # 4. THE O(1) LOGIC: Dictionary .get()
        # ==========================================
        reply = knowledge_base.get(clean_input, fallback)
        
        # Print bot response
        print(f"🤖 Bot: {reply}\n")


# ==========================================
# ENTRY POINT
# ==========================================
if __name__ == "__main__":
    run_chatbot()