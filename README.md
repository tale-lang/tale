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

And that's the thing! There are no messages, objects, sending, etc. These are just metaphors we use to describe internal state of the program inside some paradigm. The only metaphor of Tale is a code itself.

Though it may contain something we call _generics_, _type classes_, _structs_, _pattern matching_, _lambdas_ and so on, but only as things that allow to write more elegant and clean, we may say, _text_.

Sounds good? Let's dive right into the syntax!
