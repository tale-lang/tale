<div align="center">
    <img src="https://github.com/tale-lang/tale/blob/master/images/logo.png" alt="Tale Logo" width="128" height="128"></img>
</div>

<h1 align="center">The Tale</h1>

<p align="center">
    <i>A programming language for writing code that reads like English but still is strict, formal, and executes blazingly fast.</i>
</p>

<br>

## Introduction
Many programming languages are described by a primary programming paradigm they support, but Tale is not. Tale is about _form_ and _beauty_.

It enforces programmers to think not about objects, functions or messages, but expressions and _words_. This is achieved by allowing to write any kind of expression using special syntax, similar to Smalltalk [keyword messages](http://pharo.gforge.inria.fr/PBE1/PBE1ch5.html).

For example, one could write in Tale:
```
(2 + 2) should be: 4
```

Or even:

```
add: 1 to: 10
```

In the first case it seems like `(2 + 2)` is an object and `should be` is a message, but, on the other hand, the second case looks like we're sending message `add:to` to nothing.

And that's the thing! There are no messages, objects, sending, etc. These are just metaphors we use to describe internal state of the program inside some paradigm. The only metaphor of Tale is the code itself.

Though it may contain something we call _generics_, _type classes_, _structs_, _pattern matching_, _lambdas_ and so on, but only as things that allow to write more elegant and clean, we may say, _text_.

## Status
The language is on very pre-pre-pre alpha stage. It has ideological foundation, syntax design for a bunch of features and approximate roadmap.

## Install
There is no way to install the language yet as it's not implemented.

## Language
...

### Background
...

### Philosophy
...

### Syntax
...

### Architecture
...

## Roadmap
First version of the Tale will be my Bachelor's degree in the topic _"Programming language with expressions of free form"_.

Then the Tale will evolve slowly, especially in performance. Right now I have no clue, whether to just write an interpreter for it or maybe to use LLVM backend or even to implement compiler myself.

But let's look at the roadmap!

### 0.0.0: Preparation
This version is all about initial documentations, repos setup, etc. Nothing special here.

### 0.1.0: Basic syntax
In this version basic syntax things like assignments, expressions, pattern matching on values, blocks, Unicode characters, etc. will be added. It's expected that after some version like `0.1.X`, the language will be able to handle simple tasks like any scripting one do.

### 0.2.0: Types
In this version I hope I'll be able to add static typing: generics, pattern matching on types, types inference.

### 0.3.0: Packages
In this version an import system will be added and the evolution of standard library will be started.

### 0.4.0: Performance
In this version the performance and speed will become main focus. 

## License
The package is licensed under the [MIT](https://github.com/tale-lang/tale/blob/master/LICENSE) license.
