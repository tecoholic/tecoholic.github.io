---
title: "Optimizing a Python Script - Some Surprises"
date: 2025-10-23T10:56:12
slug: "optimizing-a-python-script-and-some-surprises"
categories:
  - Coding
tags:
  - python
  - rust
  - go
  - llm
  - claude-code
---

I have recently started using Claude Code and have found it very useful for experimentation and investigation type tasks.
Today I had to work on a processing a large text file with some patterns to be replaced in 2 stages

1. at an individual line level
2. at a passage level

I wrote the initial script using Python Regexes. Each of the stage has multiple regexes. And being the
simple minded programmer that I am, I simply used a for loop to use each regex and do a substiturion.
This was fine for a 20MB input file that it was written for. Then I got a 12 GB file to process.
After running for 2 hours, it was at about 5 out of the 35 million lines.

## Let Go

As I waited around with the script running, I had a brain wave. What if I wrote this in a compiled
language and get some performance improvements? So, I launched Claude Code and asked it to rewrite
the Python code into Go lang, compile and benchmark after validating the outputs are the same.

It did a great job doing that and the processing went from 2 mins on the 20MB file to ~20 seconds.
I was excited, but also noticed that the CPU was just maxing out at 100%. Isn't Go known for its
concurrency. Why am I not seeing the benefits? I know in the back of my head, this is a serial IO
processing, concurrency isn't going to be of much use or I know how to do it correctly [^1]. But
it's not me coding here.

So, I let Claude code analyse the code with the goal of optimizing the process and using concurrency
to speed it up. It came up with a couple of optimizations from File IO, Regexes to using parallel
workers.

The final output? It ran in about 3.8 seconds. From **2 mins**, we have come to **3.8 seconds**.


## Back to Python

2 things clicked with this experiment that I wan running on the side while the original Python script
was chugging away, heating up my CPU to 100 deg Celcius, 1 core at a time.

1. The biggest improvement Claude reported came from the file IO and Regex optimizations that it claimed was O(n^2) and is now O(n)
2. I am spending time optimizing a Go program that I didn't write. So, I won't know if it's going in the right direction. [^2]

So, I asked Claude to analyze the Python script for performance bottlenecks and it came back with a couple
of things. [^3]

* Compile all the single-line Regexes into a single regex and using a custom function for replacement instead of using the `for regex in list_of_regexes` loop.  
* Implemente a custom character level processor to identify passages insted of a naive string matching that I had.

Once these were implemented, the runtime went from **2 mins** to **2.03 seconds**.

## Wait! What?

Yup. The optimized Python version was faster than the Go version. I just couldn't believe it. I asked
Claude about it and it said something like 

> Python's Regex engine implemented in C is way more performant than Go's version and Go is very conservative with Regexes.

Okay! Can we make it faster? Claude replaced a bunch of Regex's with string replacements and made it
a bit more faster with a runtime of **2.69s**. Still slower than Python. A genuinely mind-blowing realization
for someone who works with Python and have always had this idea that compiled languages are more
performant than interpreted languages.

## What about Rust?

I hear you. This post won't feel complete without Rust. So, I repeated the same with Rust. But I
made the mistake of pointing Claude to the Go version as a reference for running the benchmarking
tests. So it implemented a character level version first. I read throught the code and it was just
too complex. So, I asked Claude to replace all the custom logic with Regexes like the one
from Python version and this time, it was pretty comparable. It also ended up being twice as fast.

Here are the final results as Claude presented it.


Performance Comparison

| Metric          | Complex Rust | Simple Rust | Improvement       |
|-----------------|--------------|-------------|-------------------|
| Runtime         | 0.25s        | 0.13s       | 48% faster ✨     |
| Memory          | 5.09 MB      | 6.05 MB     | +19% (acceptable) |
| Code Lines      | 350          | 245         | 30% less code     |
| Readability     | ⭐⭐⭐       | ⭐⭐⭐⭐⭐  | Much better       |
| Maintainability | Low          | High        | Much easier       |

  vs All Implementations

| Implementation | Runtime | Memory | Code Lines | Readability |
|----------------|---------|--------|------------|-------------|
| Rust (Simple)  | 0.13s   | 6 MB   | 245        | ⭐⭐⭐⭐⭐  |
| Python         | 2.03s   | 25 MB  | 280        | ⭐⭐⭐⭐⭐  |
| Go (Optimized) | 2.69s   | 11 MB  | 398        | ⭐⭐⭐      |
| Go (Regex)     | 3.80s   | 13 MB  | 300        | ⭐⭐⭐⭐    |

**🏆 Rust wins on ALL metrics!**

**Key Insight:** Simplicity Wins!

Why is the simple version faster?

Rust's regex crate is incredibly well-optimized:
- Uses Thompson NFA + lazy DFA algorithms
- SIMD acceleration for literal matching
- Optimized by regex experts over years
- Often faster than hand-rolled code

**Lesson:** Don't prematurely optimize! Trust well-designed libraries.

## Final thoughts

* This was a very fun excercise that taught me a few things.
* I am not going to be using the Go or the Rust version of the code due to project requirements and also the fact, I don't have the expertise to modify them later if needed.
* This sort of experimentation wouldn't have been possible 1 year back (maybe 2) and it's amazing to see what LLMs can do.
* I really appreciate the ancillary tooling that Claude can create for itself, like 300 lines of bash that it wrote for running the benchmarking. This is a force multiplier. I usually cannot run these kind of experiments on everyday tasks and make informed decisions. This is going to have long term effects as we get to experiment more and find better ways of doing things.

[^1]: I once tried to parallelize something using python and by accident launched about 10x the
processes as the number of cores in my system and everything ground to a halt.
[^2]: Running parallel workers for a serial task sounds sub-optimal, but I don't know enough about Go to make that call. I have often come across zero-cost concurrency. So, maybe Claude is right?
[^3]: I am purposefully being short on details here. Because, the optimization techniques themselves are not the message of this post.
