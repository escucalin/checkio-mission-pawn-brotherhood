"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": ["b4", "d4", "f4", "c3", "e3", "g5", "d2"],
            "answer": 6,
            "explanation": ["d2"]
        },
        {
            "input": ["b4", "c4", "d4", "e4", "f4", "g4", "e5"],
            "answer": 1,
            "explanation": ["b4", "c4", "d4", "e4", "f4", "g4"]
        },
    ],
    "Edge": [
        {
            "input": ["e4"],
            "answer": 0,
            "explanation": ["e4"]
        },
        {
            "input": ["e8"],
            "answer": 0,
            "explanation": ["e8"]
        },
        {
            "input": ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"],
            "answer": 7,
            "explanation": ["a1"]
        },
        {
            "input": ["a8", "b7", "c6", "d5", "e4", "f3", "g2", "h1"],
            "answer": 7,
            "explanation": ["h1"]
        },
        {
            "input": ["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"],
            "answer": 7,
            "explanation": ["a1"]
        },
        {
            "input": ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"],
            "answer": 0,
            "explanation": ["a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2"]
        },
        {
            "input": ["a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"],
            "answer": 0,
            "explanation": ["a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"]
        },
    ],
    "Extra": [
        {
            "input": ["b4", "c4", "d4", "e4", "f4", "g4", "e3"],
            "answer": 2,
            "explanation": ["b4", "c4", "e4", "g4", "e3"]
        },
        {
            "input": ["e7", "e6", "d5", "f5", "c4", "e4", "g4", "e8"],
            "answer": 3,
            "explanation": ["e8", "e7", "c4", "e4", "g4"]
        },
        {
            "input": ["a2", "b4", "c6", "d8", "e1", "f3", "g5", "h8"],
            "answer": 0,
            "explanation": ["a2", "b4", "c6", "d8", "e1", "f3", "g5", "h8"]
        },
        {
            "input": ["b6", "a7", "b8", "c7", "g1", "f2", "h2", "g3"],
            "answer": 6,
            "explanation": ["b6", "g1"]
        },




    ]
}
