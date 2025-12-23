from intent.predict import predict_intent
from orchestrator import handle_intent

def main():
    print("Connext AI started. Type 'exit' to quit.\n")

    while True:
        user_input = input(">> ")

        if user_input.lower() in ["exit", "quit"]:
            break

        intent = predict_intent(user_input)
        result = handle_intent(intent, user_input)

        print(f"[{intent}] → {result}\n")

if __name__ == "__main__":
    main()