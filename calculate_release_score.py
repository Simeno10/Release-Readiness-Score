#!/usr/bin/env python3

import json
import sys

MAX_SCORE = 100

WEIGHTS = {
    "unit_tests": 25,
    "ui_tests": 20,
    "coverage": 20,
    "release_blockers": 20,
    "build_stability": 15,
}


def calculate_score(data):
    score = 0

    # Unit Tests
    if data["unit_tests_passed"]:
        score += WEIGHTS["unit_tests"]

    # UI Tests
    if data["ui_tests_passed"]:
        score += WEIGHTS["ui_tests"]

    # Coverage
    coverage = data["coverage"]

    if coverage >= 80:
        score += WEIGHTS["coverage"]
    elif coverage >= 70:
        score += int(WEIGHTS["coverage"] * 0.75)
    elif coverage >= 60:
        score += int(WEIGHTS["coverage"] * 0.5)

    # Release blockers
    blockers = data["release_blockers"]

    if blockers == 0:
        score += WEIGHTS["release_blockers"]
    elif blockers <= 2:
        score += int(WEIGHTS["release_blockers"] * 0.5)

    # Build stability
    stability = data["successful_builds_last_10"]

    score += round(
        WEIGHTS["build_stability"] * (stability / 10)
    )

    return score


def recommendation(score):
    if score >= 90:
        return "READY FOR PRODUCTION"
    elif score >= 75:
        return "READY FOR RC"
    elif score >= 60:
        return "NEEDS REVIEW"
    else:
        return "NOT READY"


def main():
    if len(sys.argv) != 2:
        print("Usage: python calculate_release_score.py release.json")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        data = json.load(f)

    score = calculate_score(data)

    print("=" * 40)
    print(f"Release Readiness Score: {score}/{MAX_SCORE}")
    print("=" * 40)
    print(f"Recommendation: {recommendation(score)}")
    print()

    print("Details:")
    print(f"Unit Tests: {'PASS' if data['unit_tests_passed'] else 'FAIL'}")
    print(f"UI Tests: {'PASS' if data['ui_tests_passed'] else 'FAIL'}")
    print(f"Coverage: {data['coverage']}%")
    print(f"Release Blockers: {data['release_blockers']}")
    print(
        f"Successful Builds (last 10): "
        f"{data['successful_builds_last_10']}/10"
    )


if __name__ == "__main__":
    main()
