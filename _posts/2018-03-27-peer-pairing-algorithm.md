---
layout: post
title: "Peer Pairing Algorithm"
date: 2018-03-27
categories: Coding
tags: python coding
---

## Problem Statement

A class has **N** number of students. When the students submit an assignment, they are assigned **K** peers to review their assignments and provide feedback such that _0 < K < N_. Now, if given the input **N** and **K**, return a _dict_ (Python) _Object_ (JavaScript) or something equivalent in other languages in the format, `student: [list of reviewers]` adhering to the following rules:

1. Each student should be assigned **K** reviewers.
2. The student cannot review his/her own work.
3. There shouldn't be multiple reviews by the same person. Each reviewer assigned should be unique.

I should return 0/False if there is an error in the input conditions such _K >= N_

#### Example:

_Input:_ N=3, K=1

_Output:_
```
{
    0: [1],
    1: [2],
    2: [0]
}
```
_Input:_ N=3, K=2

```
{
    0: [1,2],
    1: [2,0],
    2: [0,1]
}
```

## Solution

```python
def generate_peer_pairs(N, K):
    """A function that provides unique peers for reviewing.
    The generated matches follow the following rules:
        1. The no.of reviews/rounds of review is less than total no.of users.
        2. The user won't be reviewing his/her own work
        3. All the reviewers assigned would be unique.
        4. Each user will have equal no.of reviews to give and receive.

    :param N: Total no.of student for whom the matching is to be done.
    :param K: The no.of reviews each student is supposed to receive.
    :returns: a dictionary of graders and their peers { grader_id: [peer_1, peer_2, ...]}
    """
    if K >= N:
        return False

    available_offsets = list(range(1, N))
    offsets = []

    while len(offsets) < rounds:
        offset = random.choice(available_offsets)
        offsets.append(offset)
        available_offsets.remove(offset)

    students = list(range(N))
    random.shuffle(students)

    allocations = {}
    for idx, student in enumerate(students):
        allocations[student] = [students[(idx + offset) % N] for offset in offsets])

    return allocations
```

## Notes

The problem is an interesting one. I started out with the idea that the peers should be arranged in a random way and wrote an algorithm by selecting a random recipient while looping over each grader. It was completely non-roboust and failed to make the right pairs more times that it worked.

The solution if you had noticed, is completely a position shifting algorithm. What appears a non-repeating random order for the grader and the recipient is not really that random.
