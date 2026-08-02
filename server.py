from __future__ import annotations

from datetime import datetime
from typing import Any, Dict


SESSION_MEMORY: Dict[str, list[str]] = {}


def get_daily_loan_metrics() -> int:
    """Return a simple demo metric for the current date."""
    today = datetime.now().day
    return 180 + (today % 7) * 3


def calculate_student_eligibility(course_type: str, income: int, country: str) -> Dict[str, Any]:
    """Provide a simplified eligibility estimate for a student loan scenario."""
    if income >= 90000:
        max_amount = 65000
        rate = 7.3
    elif income >= 50000:
        max_amount = 90000
        rate = 7.0
    elif income >= 30000:
        max_amount = 120000
        rate = 6.8
    else:
        max_amount = 140000
        rate = 6.5

    return {
        "max_amount": max_amount,
        "baseline_interest_rate": round(rate, 1),
        "course_type": course_type,
        "income": income,
        "country": country,
    }


def get_ux_bot_instructions(context: str) -> Dict[str, Any]:
    """Return guidance for a UX-oriented assistant in a given context."""
    if context.lower() == "checkout":
        return {
            "context": context,
            "focus_areas": ["clarity", "trust", "speed"],
            "guidance": ["reduce friction", "explain each step", "confirm before payment"],
        }

    return {
        "context": context,
        "focus_areas": ["clarity", "accessibility"],
        "guidance": ["keep instructions simple", "offer next-step help"],
    }


def get_faq_suggestions() -> list[str]:
    """Return a small set of suggested follow-up questions."""
    return [
        "What does this bot do?",
        "How much can I borrow for a student loan?",
        "What interest rate can I expect?",
        "What documents do I need to apply?",
        "How do I apply for a student loan?",
    ]


def build_chat_response(message: str, session_id: str = "default") -> Dict[str, Any]:
    """Build a student-loan-focused chatbot response with FAQ suggestions and simple session memory."""
    normalized = message.strip().lower()
    suggestions = get_faq_suggestions()
    history = SESSION_MEMORY.setdefault(session_id, [])
    history.append(normalized)

    if any(keyword in normalized for keyword in {"faq", "help", "what is this", "what does this bot do", "how do i use this"}):
        reply = (
            "This bot helps answer student-loan questions such as eligibility, loan amount, "
            "and interest rates. FAQ suggestions:"
        )
    elif any(keyword in normalized for keyword in {"borrow", "amount", "loan cap", "how much"}):
        eligibility = calculate_student_eligibility("engineering", 35000, "US")
        reply = (
            f"Based on a sample profile, your estimated maximum loan amount is ${eligibility['max_amount']}. "
            f"The baseline interest rate is {eligibility['baseline_interest_rate']}%."
        )
    elif any(keyword in normalized for keyword in {"interest", "rate", "percentage"}):
        eligibility = calculate_student_eligibility("engineering", 35000, "US")
        reply = (
            f"For a sample student-loan profile, the baseline interest rate is {eligibility['baseline_interest_rate']}%."
        )
    elif any(keyword in normalized for keyword in {"document", "documents", "id", "proof", "income proof"}):
        reply = (
            "Typical documents include a government ID, proof of enrollment, income statements, and any residency or course details requested by the lender."
        )
    elif any(keyword in normalized for keyword in {"tell me more", "more about", "continue", "and what about"}):
        reply = (
            "I can continue with eligibility, documents, application steps, or repayment guidance. "
            "Tell me which area you want to explore next."
        )
    elif any(keyword in normalized for keyword in {"apply", "application", "start"}):
        reply = (
            "To apply, gather your documents, confirm your course details, submit the application form, and review the eligibility estimate before submission."
        )
    elif any(keyword in normalized for keyword in {"lower", "reduce", "better rate", "cheaper"}):
        reply = (
            "You may lower your rate by maintaining a strong repayment profile, submitting accurate documents, and choosing a lender with better terms."
        )
    elif any(keyword in normalized for keyword in {"international", "visa", "abroad", "overseas"}):
        reply = (
            "International students may still be eligible depending on residency, enrollment status, and lender requirements. Check the specific lender's rules before applying."
        )
    elif any(keyword in normalized for keyword in {"miss", "missed", "late", "payment", "default"}):
        reply = (
            "Missing a payment can lead to late fees, extra interest, and a negative impact on your credit profile, so contact the lender as soon as possible."
        )
    elif any(keyword in normalized for keyword in {"eligible", "eligibility", "qualify", "can i"}):
        eligibility = calculate_student_eligibility("engineering", 35000, "US")
        reply = (
            f"student-loan eligibility: based on the sample profile, you may be eligible for up to ${eligibility['max_amount']} "
            f"with a baseline interest rate of {eligibility['baseline_interest_rate']}%."
        )
    else:
        reply = (
            "I can help with student-loan eligibility, loan amount estimates, and interest-rate questions. "
            "Try one of the suggested topics."
        )

    return {"reply": reply, "suggestions": suggestions}


def build_ux_bot_response(context: str) -> str:
    """Format student-loan guidance into a human-readable assistant response."""
    response = build_chat_response(context)
    return "UX Bot guidance: " + response["reply"]


def run_interactive_ux_bot() -> None:
    """Start a simple command-line interaction loop for the student-loan UX bot."""
    print("Student Loan UX Bot interactive mode")
    print("Type a student-loan question, or 'exit'.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        if not user_input:
            continue
        response = build_chat_response(user_input)
        print(response["reply"])
        print("Suggested topics:")
        for suggestion in response["suggestions"]:
            print(f"- {suggestion}")


if __name__ == "__main__":
    print("Daily loan metrics:", get_daily_loan_metrics())
    print("Eligibility example:", calculate_student_eligibility("engineering", 35000, "US"))
    print("UX bot guidance:", get_ux_bot_instructions("checkout"))
    print("\nRun the interactive UX bot by calling run_interactive_ux_bot()")
