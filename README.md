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
There is no way to install the language yet as it's not implemented. But you can play with the latest version using these steps.

### Preparation
- Download latest (3.8.1) version of the Python [here](https://www.python.org/downloads/).
- Clone the repository using `git clone "git@github.com:tale-lang/tale.git"` command.
- Go to the source directory -- `cd tale/src`.
- Set up virtualenv -- `virtualenv venv` (if `virtualenv` is not installed, use `pip3 install virtualenv`).
- Activate virtual environment (if not activated) -- `source venv/bin/activate` (or `venv/Scripts/activate` on Windows).
- Install required packages -- `pip install -r requirements.txt`.

### Usage
- Go to the source directory -- `cd tale/src`.
- Activate virtual environment (if not activated) -- `source venv/bin/activate` (or `venv/Scripts/activate` on Windows).
- Execute any program file -- `python cli.py PROGRAM` (e.g. `python cli.py examples/helloworld.tale`).

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
Here is an example of doc-comment for `+` operator.

Accepts:
    x: First addend.
    y: Second addend.

Represents: A sum of the two numbers.
---
(x: Int) + (y: Int) = ...
```

#### Assignments
In the Tale everything is an expression, and expressions can have names.

Consider a simple example:
``` tale
author = "Oscar Wilde"
```

Here we have two expressions: `"Oscar Wilde"`, which is a constant string literal, and `author`, which is a _name_.
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
Instead, it takes into account every possible way of writing `... squared`: `1 squared`, `2 squared`, `100 squared`, `"Oscar Wilde" squared`, `author squared`, etc. _(We'll talk about types and type signatures later)._

Second, every `... squared` corresponds to a different expression: `1 squared` to `1 * 1`, `2 squared` to `2 * 2`, and so on.
This is achieved by the variable part `(x)`: the name `(x) squared` kinda _captures_ first part of the expression and associates it with `x` name.

That's the Tale's view on functions, procedures and methods.

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

#### Operator forms
One special thing needed to mention is _operator_ forms: they're just simple forms
like unary or keywords, only they consist of special symbols like `+|%&#!><=` etc.
(including bunch of nice Unicode stuff like `∑`, `√`).

##### Unary operators
The first type of operator forms are unary operators: they're prefix version of regular
unary forms.

For example, famous `!` (boolean inversion) symbol can be defined as:
``` tale
!(x) = not: x
-- And used like:
alive = !dead
```

The main rule here: unary operators must be _connected_ to an identifier without
any spaces in between. _(In this way the lexer of the language will be able to correctly
process code.)_

_(It's also worth mentioning that there are no **postfix** version of unary operators)._

##### Binary operators
There is also a binary operator forms, like `+` or `-`.

Consider this example of definition of such an operator:
``` tale
(x) + (y) = ...
-- And used like:
x = 2 + 2
```

The main rule for binary operators is the opposite of the rule for unary ones:
there _must_ be a space before and after an operator, so the compiler will be
able to understand expressions like `2 + ++2`.

Knowing basic blocks of the language, let's now talk about brackets and precedence rules.

#### Brackets and precedence
There are some rules of how we can compose expressions of different forms. These rules help compiler as well as programmers
to process code unambigiously.

##### Keyword forms
Let's talk a bit about keyword forms first. They are executed in pretty simple way.

Consider this example:
``` tale
put: item to: list
```

Here the compiler will lookup only a `put:to:` name. If we instead define only tricky names:
``` tale
put: (x) = ...
(x) to: (y) = ...

-- Error:
put: item to: list
```

That would be a compilation error, because _composed keyword expressions should be in brackets_.
Thus, instead of writing `put: item to: list`, we need to explicitly add brackets: `(put: item) to: list`.

##### Unary operators
Another rule is about combining unary operators:
``` tale
!!something   -- Apply `!!` operator to `something`.
!(!something) -- Apply `!` operator to `something` twice.
```

##### Precedence
The general precedence order is like that:
Unary Operators > Unary Forms > Binary Operators > Keyword Forms.

For example:
``` tale
print: 2 squared
-- Same as:
print: (2 squared)

print: -2 squared
-- Same as:
print: ((-2) squared)

-- With keyword form:
2 squared or: 3 squared
-- Same as:
(2 squared) or: (3 squared)
```

Binary operators are in between:
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

#### Chaining
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
``` c#
var x = 2.Squared().Multiplied(by: 2).ToString().AsUTF8Bytes();
```

But in Tale (and Smalltalk as well) you need to wrap everything in brackets:
``` tale
x = (((2 squared) multipliedBy: 2) toString) asUTF8Bytes
```

To solve this problem Tale introduces a few rules about indentation. Let's check them first.

**Rule 1:** If line is indented, it's automatically attached to previous one with lower indentation level and they both wrapped in brackets.
``` tale
...
  ...
  ...
-- Same as:
(...) (...) (...)
```

So when we write, for example:
``` tale
2 multipliedBy: 4
  multipliedBy: 2
  toString
```

We get:
``` tale
(2 multipliedBy: 4) (multipliedBy: 2) (toString)
```

Which results in:
``` tale
(((2 multipliedBy: 4) multipliedBy: 2) toString)
```

**Rule 2:** If line ends with `;`, it'll cancel the next newline character and any indentation after.
``` tale
...;
...;
 ...
-- Same as:
... ... ...
```

This feature is pretty useful when you have a keyword form and you want to span it over several lines:
``` tale
if: x > 0;
  then: (print: "Greater");
  else: (print: "Less or equal")
-- Same as:
if: x > 0 then: (print: "Greater") else: (print: "Less or equal")
```

**Rule 3:** If a line ends with `x:`, then the `x` identifier is automatically considered as a keyword one,
and compiler automatically expects next line (or lines) to be indented more than the current.
These lines are treated as block. More on blocks later, but in short they're like lambdas.

Using this rule you can write nice expressions:
``` tale
if: x > 0;
  then:
    print: "Greater"
    print: "Than zero";
  else:
    print: "Less or equal"
    print: "Than zero"
-- Same as:
if: x > 0 then: [|print: "Greater". print: "Than zero"|] else: [|print: "Less or equal". print: "Than zero"|]
```

Cycles are also implemented like that. Consider this example:
``` tale
5 times do:
  print: "Hello, world"
-- Same as:
(5 times) do: [|print: "Hello, world"|]
```

_(Note: strange brackets `[|` and `|]` are just for inner compiler usage,
they're not available in regular code.)_

**Remark:** _All rules were created for the sake of readability in different popular scenarios,
especially in methods chaining, and because the rules are a bit specific, there are
many ways to misuse them, for example:_
``` tale
-- ✘
print: 2
  asString
-- ✔
print: 2 asString
-- ✔
print: (2
  asString)

-- ✘
asString
  print: "2"

-- ✘
asString;
  multipliedBy: 2

-- ✘
print:
  "Hello, world"
  print: "x"
-- ✔
print:
  "Hello, world"

-- ✘
print:;
  "Hello, world"
  print: "x"
-- ✔ (ugly)
print:;
  "Hello, world"

-- ✘
if x > 0
  then: ...
  else: ...
-- ✔
if x > 0;
  then: ...;
  else: ...
```

#### Blocks
Another powerful feature of the Tale is a concept of blocks. They're pretty similar to anonymous functions in other languages,
but here they represent a small version of a program with its own scope and variables.

Let's look at the simple example of a block:
``` tale
wait: 5 seconds then:
  print: "Hello, world!"
```

As you remember, because of **Rule 3**, this code is equal to:
``` tale
wait: (5 seconds) then: [|print: "Hello, world!"|]
```

Here the `wait:then` keyword form captures not only seconds argument, but also a whole block of code.
The definition of the form looks like that:
``` tale
wait (x) then: [|block|] =
    sleep: x
    block call
```

Here is a C# alternative:
``` c#
Wait(TimeSpan span, Action then) { ... }

// Which may be called:
Wait(5.Seconds(), then: () => Console.WriteLine("Hello, world!"));
```

Note that there are two version of blocks:
``` tale
-- Brackets are used to inline blocks with only one expression.
after: 5 seconds do: (print: "Hello, world!")

-- Third rule of indentation:
after: 5 seconds do:
    print: "Hello, world!"
```

How about blocks with arguments? Blocks with arguments are implemented a bit more interesting than
in C# or Smalltalk.

Let's look at this example:
``` tale
for: i in: items do:
   print: i
```

Here we have the `for:in:do` keyword form that captures `i`, `items` and block `[|print: i|]`. What's interesting here is that
`i` is captured a bit differently that any other argument, because the only thing captured is a name. Even if you have:
``` tale
i = 0
for: i in: items do:
   print: i
```

The `i` part of the `for:in:do` form will be different for each `[|print: i|]` block execution. This is very similar to lambda form: `i => print: i`,
only `i` is defined as a part of the expression.

Here is how the syntax of the loop definition looks like:
``` tale
for: [(i)] in: (sequence) do: [|block|] =
    ... -- Something like `while` loop here.
        block call: current -- `current` is a current item of a collection.
```

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
