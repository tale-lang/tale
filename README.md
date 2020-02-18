<div align="center">
    <img src="https://github.com/tale-lang/tale/blob/master/images/logo.png" alt="Tale Logo" width="128" height="128"></img>
</div>

<h1 align="center">The Tale</h1>

<p align="center">
    <i>A programming language for writing code that reads like English but still is strict, formal, and executes blazingly fast.</i>
</p>

<div align="center">
    <img src="https://github.com/tale-lang/tale/blob/develop/images/syntax.png" alt="Tale Syntax"></img>
</div>

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

In the first case it seems like `(2 + 2)` is an object and `should be` is a method (or a message), but, on the other hand, the second case looks like we're sending message `add:to` to nothing.

And that's the thing! You can write expression of any form and the only difference is whether to put `:` character or not.
There are no messages, objects, sending, etc. These are just metaphors we use to describe internal state of the program inside some paradigm. The only metaphor of Tale is the code itself.

Though it may contain something we call _generics_, _type classes_, _structs_, _pattern matching_, _lambdas_ and so on, but only as things that allow to write more elegant and clean **text**.

## Status
The language is on very pre-pre-pre alpha stage. It has ideological foundation, syntax design for a bunch of features and approximate roadmap.

## Install
There is no way to install the language yet as it's not implemented.

## Language

### Background
The background of the Tale is a simple idea that we can take any particular language and use its underlying paradigm to write English-like (or any other natural language) sentences.

Consider this example of C# code:
``` c#
100.Minutes()
```

From the paradigm perspective of view, there is the integer object `100` and the `Minutes` method call.
_(Let's ignore the fact that usually `Minutes` is implemented as an extension method, because this is just a feature of C#.)_
One could argue that in terms of paradigm, any method should be a verb (common mistake!), so the expression `100.Minutes()` should be changed to `TimeSpan.GetFromMinutes(100)`.

But from the _reader_ perspective of view, `100.Minutes()` looks like "100 minutes", a regular English phrase.
And like any other English phrase it has meaning, which is very similar to one represented by `TimeSpan.GetFromMinutes(100)` code.

Seems like there is a conflict between how things work and how they look. What is more important? Is there one?
The Tale's answer is both: readable code is for humans, but responsive applications are also for humans.

Thus, the language should _enfroce_ declarative and fluent style of programming while allowing considerable performance.

### Syntax
The syntax of the Tale is a mix of Python tiny and elegant feel, Haskell expressiveness and Smalltalk keyword messages.

#### Comments
``` tale
-- A one-line comment.

a = 1 -- Another one.

---
A multi-line comment. Can be used to document any kind of stuff.
Here is an example of doc-comment for some addition expression.

Accepts:
    x: First addend.
    y: Second addend.

Represents: A sum of the two numbers.
---
```

#### Assignments
In the Tale everything is an expression, and expressions can have names.

Consider a simple example:
``` tale
author = "Oscar Wilde"
```

Here we have two expresions: `"Oscar Wilde"`, which is a constant string literal, and `author`, which is a _name_.
_(The `=` sign is used to assign a name.)_

It's also possible to assign a name to other name:
``` tale
x = author
```

But what is a name actually? Just a bunch of characters that correspond to something. So, when we see the `author` somewhere in
the code, we know that it's associated with one and only one expression -- `"Oscar Wilde"`.

Actually, the `"Oscar Wilde"` is a name as well, but a constant one, it doesn't point to somewhere, but kinda points to itself.

Let's motivate our next step with this example:
``` tale
1 squared = 1
2 squared = 4
3 squared = 9
4 squared = 16
...
```

Here we have a _group_ of names, where each represents a squared number. This group of names is very different from just random names,
because they have something similar: the meaning of squared number and the word `squared`. And because any number can be squared, we don't want to write `(x) squared`
for every possible `x`.

It'd be much more useful if we were able to define something like name template or form, and that's exactly what the Tale can do!

#### Unary forms
Consider this name:
``` tale
(x) squared = x * x
```

Two things are going on here. First of all, `(x) squared` is also a name, but it doesn't match exactly one set of characters.
Instead, it takes into account every possible way of writing `... squared`: `1 squared`, `2 squared`, `100 squared`, `"Oscar Wilde" squared`, `author squared`, etc.

Second, every `... squared` corresponds to a different expression: `1 squared` to `1 * 1`, `2 squared` to `2 * 2`, and so on.
This is achieved by the variable part `(x)`: the name `(x) squared` kinda _captures_ first part of the expression and associates it with `x` name.

That's the Tale's view on functions, procedures and methods.

#### Binary forms
Let's take a look at the `x * x` part of the `(x) squared` name. What is `*` here?
Knowing the concept of forms, it's reasonable to suppose, that somewhere a form `(x) * (y) = ...` is defined and
it represents the multiplication operation.

In this way many of mathematical and logical operations are implemented, but can we have a `(x) or (y)` form?
Unfortunately, no. The Tale allows defining binary forms only with special symbols between arguments (like `+`, `\`, `-`, `;`, `.`, `>=`).
This is where the language should respect formal nature of programs.

Consider this code:
``` tale
(x) or = x
(x) or (b) = b
(x) two = x

one = 1
two = 2

-- `x` is either 1 or 2.
x = one or two
```

Here the compiler would have too many options of how to interpret the `one or two` expression.
To solve this problem, the Tale uses Smalltalk syntax of keyword messages.

#### Keyword forms
Beyond simple forms is the only one kind: keyword forms. Combined with unary ones they allow developers to write any kind of sentences.

Here is a simple example of a few keyword forms:
``` tale
print: (x) = ...
(x) and: (y) = ...
add: (x) to: (y) = ...
add: (x) to: (y) at: (i) = ...
```

As you can see, the only difference is a `:` character after each _"keyword"_. It helps the compiler to think about code more accurately.

It's also worth mentioning one invalid way of defining keyword forms:
``` tale
print: (x) async = ...
```

Because the compiler processes code from left to right, it'd be hard for it to decide, is `async` an unary form or not.

To elaborate more on that, let's talk about brackets and precedence rules.

#### Brackets and precedence
There are some rules of how we can compose expressions of different forms. These rules help compiler as well as programmers
to process code unambigiously.

First of all, keyword expressions. They are executed in pretty simple way.

Let's take a look at this example:
``` tale
put: item to: list
```

Here the compiler will lookup a `put:to:` name. But what if we've defined only tricky names:
``` tale
put: (x) = ...
(x) to: (y) = ...

-- Error:
put: item to: list
```

This is a compilation error, because _composed keyword expressions should be in brackets_. Thus, instead of writing `put: item to: list`,
we need to explicitly add brackets: `(put: item) to: list`.

How about mixing keyword expressions with unary ones?
``` tale
print: 2 squared
-- Same as:
print: (2 squared)
```

So, unary expressions have higher precedence over keyword ones.

Here is another example that demonstrates this rule:
``` tale
2 squared or: 3 squared
-- Same as:
(2 squared) or: (3 squared)
```

Operators are in between:
``` tale
2 squared == 3 squared
-- Same as:
(2 squared) == (3 squared)

x == y or: y == z
-- Same as:
(x == y) or: (y == z)

-- In total:
x squared == y squared or: y squared == z squared
-- Same as:
((x squared) == (y squared)) or: ((y squared) == (z squared))
```

Everything seems cool and looks really like a small modification of Smalltalk syntax, but there is a problem.

Consider this example of C# code:
``` c#
var x = 2.Squared().Multiplied(by: 2).ToString();
```

Here we have a chain of 3 method calls: `Squared`, `Multiplied` and `ToString()`. Let's see how this looks in Tale:
``` tale
x = 2 squared multipliedBy: 2 toString
```

Which by rules of precedence should be written as:
``` tale
x = (2 squared) multipliedBy: (2 toString)
```

But we want:
``` tale
x = ((2 squared) multipliedBy: 2) toString
```

Thus, the brackets should be explicit. Imagine we now want to convert the resulting string to UTF-8 bytes array.

In C# we only need to put a new method call at the end of the chain:
``` c #
var x = 2.Squared().Multiplied(by: 2).ToString().AsUTF8Bytes();
```

But in Tale (and Smalltalk as well) you need to wrap everything in brackets:
``` tale
x = (((2 squared) multipliedBy: 2) toString) asUTF8Bytes
```

Which is pretty LISP.

### Architecture
...

## Roadmap
First version of the Tale will be my Bachelor's degree in the topic _"Programming language with expressions of free form"_.

Then the Tale will evolve slowly, especially in performance. Right now I have no clue, whether to just write an interpreter for it or maybe to use LLVM backend or even to implement compiler myself.

But let's look at the roadmap!

### 0.0: Preparation
This patch is all about initial documentations, repos setup, etc. Nothing special here.

### 0.1: Basic syntax
In this patch basic syntax things like assignments, expressions, pattern matching on values, blocks, Unicode characters, etc. will be added. It's expected that after some version like `0.1.X`, the language will be able to handle simple tasks like any scripting one does.

### 0.2: Types
In this patch I hope I'll be able to add static typing: generics, pattern matching on types, types inference.

### 0.3: Packages
In this patch an import system will be added and the evolution of standard library will be started.

### 0.4: Performance
In this patch the performance and speed will become main focus.

## License
The package is licensed under the [MIT](https://github.com/tale-lang/tale/blob/master/LICENSE) license.
