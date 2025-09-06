from src.module5.files_exceptions import gather_lines, save_notes, build_report, speak_text


def main():
    try:
        lines = gather_lines()
        if not lines:
            print("NO input provided.  Exiting.")
            return
        save_notes(lines)
        report = build_report()

        print("\n--- Report ---\n" + report)

        print("Speaking report via Azure Text-to-Speech...")
        speak_text(report)

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
