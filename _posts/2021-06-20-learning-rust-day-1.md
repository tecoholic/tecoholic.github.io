---
layout: post
title: "Learning Rust - Day 1"
date: 2021-06-20 16:53:32
category: Coding
tags: rustlang
---

Dev notes from learning Rust.




*Official Website:* https://www.rust-lang.org


* Installed the tool from the official website https://www.rust-lang.org/tools/install
* Started learning from the official Rust Book - https://doc.rust-lang.org/book/
* Completed the Chapter 1 and learnt about the 2 methods of compilation - using the direct `rustc` compiler and the `cargo` package manager


Notes
-----


* Rust is a compiled language - different from my daily drivers Python and JavaScript both interpreted languages.
* Compiled means re-learning the difference between passing by reference and passing by value
* Rust has mutability at the core of data management - so being conscious about immutable and mutable data
* Errors are handled as a part of the `Result` of functions. Doesn't need an explicit `try...except` (at least at this point)
* Packages are called `crates` and there are binary crates & library crates
* https://crates.io/ is the package registry
* `Cargo.lock` file acts as the record of dependencies for Reproducible builds
* `cargo update` updates the packages to the most recent bugfix version
* there is something called Traits which provide access to functions of a crate.





![](/img/wp-content/uploads/2021/08/guessing_game_1.png?w=937)

