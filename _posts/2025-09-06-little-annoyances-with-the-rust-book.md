---
layout: post
title: "Little Annoyances With the Rust Book"
date: 2025-09-06
category: Books
tags: Rust
---

## Background 

I have been wanting to write some software in a compiled language. Since my primary language has been Python for the
last decade, I settled on Rust after I discovered Rust & Python work well together. I really wanted to learn Go, because
it's supposed to be simpler and used in all the devops stuff that I work with, but being able to use Rust & Python
together seems like a big plus.

Anyway, in the age of LLM assisted development, I bought a paperback copy of **"The Rust Programming Language"** 2nd edition by *Steve
Klabnik* and *Carol Nichols*, and started working through this week.

> *"Why buy a paperback, when its [available online](https://doc.rust-lang.org/book/) for free?"*, you ask.
> 
> I have tried the online book at least 5 times before. I end up just copy pasting code after a while or get
> distracted switching between my editor and the browser. A physical book really keeps me focused.


## Why this post?

As I go through the book, I noticed some things that kind of bother me the way they are presented. Now, if they were
genuine errors, I could create Github issues and offer corrections in Pull Requests. These are not them. These are
editorial choices, that the authors have made which I don't agree with. Bothering them with these is, probably, a waste
of everyone's time.

But, I can't keep them bottled up as well. So, this blog will be my dumping ground.

## Annoyances

Now to those annoyances themselves. 


### Chapter 2 - Programmning a Guessing Game

#### Converting String to Integer

In page 25, this bit of code is added to convert the `String` read using a `io::stdin().read_line()` in to a `u32` integer value.

```rust
let guess: u32 = guess
  .trim()
  .parse()
  .except("Please type a number!");
```

I was really stumped for a minute when I read this line. **How does `parse()` know to parse an integer here? Why not a boolean or a float?**.
Yes, I get that the compiler knows to use `parse()` in a way compatible with the expected value `u32` based on the type annotation.
But why not explicity tell that to parse? If the compiler "knows" to do it correctly, why bother with calling `parse` at all? Wouldn't
it be simpler to just write `let guess: u32 = guess` and call it a day? *I know, that wouldn't be practical. We need error handling, a-la `except()`.*

To make it worse, we are introduced to this line in the preceeding pages:

```rust
let mut guess = String::new();
```

Here the type is inferred from the assignment. But now, is the assignment inferred from the type?

##### The "turbofish"

Thankfully, RustRover's quick doc feature cleared my confusion - quickly, when I put my cursor over parse. Here is the docs for `parse()`

> Parses this string slice into another type.
> 
> Because parse is so general, it can cause problems with type inference. As such, parse is one of the few times you'll see the syntax
> affectionately known as the 'turbofish': `::<>`. This helps the inference algorithm understand specifically which type you're trying
> to parse into.
> 
> `parse` can parse into any type that implements the `FromStr` trait

So, the more explicit/consistent way to write this would be

```rust
let guess = guess
  .trim()
  .parse::<u32>()
  .excpet("Please type a number!");
```

Now I know exactly what's going on and don't have to rely on "compiler magic". In my opinion, this is more straightforward to understand
and reason about. I wish the authors have used the 'turbofish' here and introduced the simplified version (is this called syntactic sugar?)
later at some point. Maybe they thought this was a "simpler" version and putting `::<>` before the `()` would scare people, I don't know.
It feels inconsistent and confusing for me.

### Chapter 3 - Common Programming Concepts

#### "don't think you are not a good programmer"

While explaning about *Variables and Mutability*, I came across this passage:

> This example shows how the compiler helps you find errors in your programs. Compiler errors can be frustrating, but really they only
> mean your program isn’t safely doing what you want it to do yet; they do not mean that you’re not a good programmer! Experienced
> Rustaceans still get compiler errors.

Why would I think I am not a good programmer because of a compiler error? Especially, when this is the instruction I received:

> Save and run the program using `cargo run`. You should receive an error message regarding an immutability error, as shown in this output:

The book goes on...

> You received the error message cannot assign twice to immutable variable `x` because you tried to assign a second value to the immutable x variable.
>
> It’s important that we get compile-time errors when we attempt to change a value that’s designated as immutable because this very situation can lead to bugs.

Notice the shift from "you" to "we" here? You did all the wrong stuff and we are here to tell you about all the right stuff. It just irritates
me to no end when authors write like this. I just ran the code you gave me and asked me to run. Now English is my second language.
So, this change of "you" and "we" could be a minor nothing. But coupled with the *"don't think you are not good"*, it's really grating to read.

