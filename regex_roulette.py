#!/usr/bin/env python3
"""
Regex Roulette - Because regex debugging should feel like gambling!

Spin the wheel, test your pattern, and discover which edge cases
will haunt you in production at 3 AM.
"""

import re
import random
from typing import List, Tuple

def generate_edge_cases() -> List[Tuple[str, str, str]]:
    """
    Generate test cases that will make you question your life choices.
    Returns: [(test_string, should_match, description), ...]
    """
    return [
        # The classics
        ("hello world", r"hello\s+world", "Basic sanity check (you'll fail this)"),
        ("hello\nworld", r"hello.world", ". doesn't match newline (surprise!"),
        ("foo bar baz", r"foo.*baz", "Greedy vs non-greedy? Who knows!"),
        ("123-456-7890", r"\d{3}-\d{3}-\d{4}", "Phone number (works until international)"),
        ("user@example.com", r"\w+@\w+\.\w+", "Email (ignores 99% of real emails)"),
        # The fun ones
        ("", r"^.*$", "Empty string (your regex's existential crisis)"),
        ("a" * 1000, r"a{5,10}", "Long strings: where greed goes to die"),
        ("café", r"cafe", "Unicode: because bytes have feelings too"),
        ("  spaces  ", r"^spaces$", "Whitespace: the silent regex killer"),
        ("price: $19.99", r"\$\d+", "Special chars escaping (did you remember?)"),
    ]

def test_pattern(pattern: str, verbose: bool = False) -> None:
    """
    Test your regex against our carefully crafted torture devices.
    Returns: Nothing, just shame and disappointment.
    """
    print(f"\n🔫 Testing pattern: {pattern}")
    print("Spinning the regex roulette wheel...\n")
    
    try:
        compiled = re.compile(pattern)
    except re.error as e:
        print(f"💥 Syntax error: {e}")
        print("Your regex doesn't even compile. Maybe try string matching?")
        return
    
    cases = generate_edge_cases()
    random.shuffle(cases)  # Because randomness = fairness
    
    passed = 0
    for test_str, expected_pattern, description in cases:
        should_match = bool(re.fullmatch(expected_pattern, test_str))
        actual_match = bool(compiled.fullmatch(test_str))
        
        if actual_match == should_match:
            passed += 1
            if verbose:
                print(f"✅ {description}")
        else:
            print(f"❌ {description}")
            print(f"   Test: '{test_str[:50]}{'...' if len(test_str) > 50 else ''}'")
            print(f"   Expected: {'match' if should_match else 'no match'}")
            print(f"   Got: {'match' if actual_match else 'no match'}")
    
    score = passed / len(cases)
    print(f"\n🎯 Score: {passed}/{len(cases)} ({score:.0%})")
    
    # Snarky feedback - because constructive criticism is overrated
    if score == 1.0:
        print("🎉 Perfect! (Did you test with real data? Probably not.)")
    elif score > 0.7:
        print("👍 Not terrible! (It'll fail in production, but gracefully.)")
    elif score > 0.3:
        print("🤔 Room for improvement! (Like, all the rooms.)")
    else:
        print("💀 Oof. Maybe use a string method instead?")

def main() -> None:
    """Main function where dreams go to die."""
    print("=== Regex Roulette ===")
    print("Test your regex against edge cases that will break in production!\n")
    
    while True:
        pattern = input("Enter regex pattern (or 'quit' to cry): ").strip()
        if pattern.lower() == 'quit':
            print("\n🏃💨 Running away: the best debugging strategy!")
            break
        
        verbose = input("Verbose mode? (y/n): ").strip().lower() == 'y'
        test_pattern(pattern, verbose)
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()
