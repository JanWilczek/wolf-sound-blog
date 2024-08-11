---
id: 379
title: What is data alignment?
description: "Learn what is data alignment in C and C++ languages and what are the available functions in the STL library to handle it."
date: 2020-04-09T14:00:35+00:00
author: Jan Wilczek
layout: post
guid: https://thewolfsound.com/?p=379
permalink: /what-is-data-alignment/
themify_used_global_styles:
  - 'a:1:{i:0;s:0:"";}'
tbp_custom_css:
  - ""
content_width:
  - default_width
hide_post_title:
  - default
unlink_post_title:
  - default
hide_post_date:
  - default
hide_post_image:
  - default
unlink_post_image:
  - default
header_wrap:
  - solid
background_repeat:
  - fullcover
background: /wp-content/uploads/2020/04/thumbnail.png
categories:
  - C/C++
tags:
  - c
  - cpp
discussion_id: 2020-04-09-what-is-data-alignment
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/tyw6_B0-QZA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>

So you want to speed up your software so that it is capable of running even the most sophisticated audio algorithms in real time. How to achieve that? This question has multiple answers, but one of them is definitely data alignment, the topic of today&#8217;s article.

Today I want to explain how to take advantage of proper data alignment. To present the full picture, I will introduce the relevant C++ features.

To understand the concept of alignment we first have to differentiate between _address alignment_ and _datum alignment_.

## Address alignment

Let&#8217;s imagine that computer&#8217;s memory consists of drawers. Each drawer is of the same size in bytes which is equal to a power of 2, and we can somehow choose which power it is. For example, the whole memory could be made up of 4-byte blocks. We still can address every byte, but only the first address in each block is &#8220;aligned&#8221;. That is the address alignment. 

![](https://thewolfsound.com/wp-content/uploads/2020/04/memory_aligned-300x263.png)

## Datum alignment

Now, if a 4-byte variable is placed completely in one of these 4-byte blocks (it fills all 4 bytes of a block) it is said to be _aligned_. That is datum alignment.

![](https://thewolfsound.com/wp-content/uploads/2020/04/int_in_memory-300x263.png)

Now, how would it look like, if such a 4-byte variable would not be aligned? It would occupy more than one block (it would cross the block boundary). It could be placed, for example, at address 4n + 1 (where n is a nonnegative integer) and would hence take addresses 4n+1, 4n+2, 4n+3 and 4n+4 = 4(n+1) + 0. 

![](https://thewolfsound.com/wp-content/uploads/2020/04/bad_int_in_memory-300x263.png)

That means, that in order to read out the variable the processor would need two read operations: one from the first 4-byte block and another one from the second. That in turn is, of course, slightly slower, but may as well be prone to race condition (one thread reads part of the variable, another thread modifies the whole variable and then the first thread reads the other part of the variable; in effect, the retrieved value is completely incorrect).

## Address vs. datum alignment

So address alignment with respect to some power of 2 relates to this address modulo 2 to that power. On the other hand, datum alignment relates to whether a particular datum lies at an aligned address. A 1-byte variable (typically a `char` in C/C++) is always aligned. A 2-byte variable (typically a `short` in C/C++) in order to be aligned must lie at an address divisible by 2. A 4-byte variable (typically an `int` in C/C++) must lie at an address divisible by 4 and so on. This specification of a particular type is called _alignment requirement_(&#8216;what&#8217;s the size of the box the type should be placed in in order to be aligned&#8217;).

## Handling alignment

How to ensure that your data is aligned? Well, in most programming languages (including C and C++) the compiler does that for you. That, however, may mean, that your structures take more space than is required, because of additional padding inserted to make your `struct`&#8216;s data members aligned. That results in (potentially unnecessary) increased usage of memory.

Of course, one could argue, that in modern computers such microoptimization is unnecessary. Well, let&#8217;s look at an example, shall we?

Consider the following structure:

```cpp
struct A {
    char c1;
    short s1;
    int i1;
    char c2;
};
```

In memory the structure looks rather like the following (due to data alignment done by the compiler):

```cpp
struct A {
    char c1;
    // 1-byte padding
    short s1;
    int i1;
    char c2;
    // 3-byte padding
};
```

On my computer, `sizeof(A)` returns 12, what means that due to additional padding `struct`&#8216;s size is 4 bytes larger than the sum of its data members&#8217; sizes (on my machine, running gcc 7.2.0, `char` is 1 byte, `short` is 2 bytes and `int` is 4 bytes long).

#### Why the difference in size?

The alignment of `A` is 4 because of the `int` data member: `int`&#8216;s alignment is 4 what determines the alignment of the whole structure. In other words, the `int` data member must lie at a 4-byte boundary to be aligned.

This layout of `A` results in 4 bytes wasted per each variable of type `A`. That means, that having an array of 1024 `A`s wastes 4 Kb of memory. It may seem an artificial example, but it is worth keeping in mind.

#### Reducing size

What can we do, to get rid of the padding? We could use some nasty implementation-specific preprocessor directives, &#8220;which I will not utter here&#8221;. As already mentioned, forcing data members to be unaligned can increase their access time. However, in this case, we can simply reorder data members of the `struct` in the following way:

```cpp
struct B {
    int i1;
    short s1;
    char c1;
    char c2;
};
```

In struct B `int` is at a 4-byte boundary, `short` at a 2-byte boundary and of course both `char`s at 1-byte boundaries. It is worth mentioning that although `B`&#8216;s alignment requirement is the same as `A`&#8216;s, its size is 4 bytes smaller.

#### The general rule for padding minimization

A simple rule to follow in data member order declaration to minimize additional padding is to declare data members in descending order of size (as returned by the `sizeof` operator). We then get the best alignment we could possibly ever get with any ordering. Sometimes a loss is inevitable, as in the following `struct`:

```cpp
struct C {
    int i1;
    short s1;
    short c1;
    char c2;
    // 3-byte padding
};
```

If we wanted to pack variables of type `C` in an array in a way, that uses no additional space beyond the sum of `C` members&#8217; sizes multiplied by the number of the array members, the only option left is to use the preprocessor directives.

## **C++ alignment support**

Along with the development of C++ more and more alignment features are part of the standard (rather than implementation-specific extensions). To these belong the operators: `alignof`, `alignas`, functions: `std::alignment_of` and `std::aligment_of_v`, `std::align`, `std::aligned_storage`, `std::aligned_union`, types: `std::align_val_t` and implementation-specific `std::max_align_t`.

Let&#8217;s take a quick look at each one of these in turn:

#### Keywords

`alignof`: returns the alignment requirement of a type in form of a value of type `std::size_t`; how the address of the variable of given type has to be aligned so that this variable is aligned.

`alignas`: allows to specify the alignment requirement of a type or particular class data member; how it should be positioned in memory by the compiler to make it aligned. It comes in handy when we want to align structs, for example, for using intrinsic vector instructions, where data has to be 16-, 32- or 64-bytes aligned [3]. Mind you, that the specified alignment can only be a power of 2 and, unless it&#8217;s greater than the &#8216;natural&#8217; alignment, it will be ignored by the compiler. 

#### Templates

`std::alignment_of<T>`: class template that provides similar information to the `alignof` keyword. The difference is, that it can be used in metaprogramming facilities [5].

`std::alignment_of_v<T>`: helper template for `std::alignment_of<T>` that directly returns the value of alignment (so that `std::alignment_of<T>()`, `std::alignment_of_v<T>` and `alignof(T)` are always equal).

#### Functions

`std::align`: allows the user to ensure that given pointer points to an aligned address with respect to given alignment, number of bytes and indicated available space.

#### Data structures

`std::aligned_storage`: a simple wrapper providing uninitialized aligned storage space. As with any uninitialized storage, it requires construction at an explicit address and explicit destructor invocation at that address. May be used for a container type implementation.

`std::aligned_union`: as the above with the difference, that the alignment suitable for all given types is chosen and the size of the allocated space is such that it can hold any of the objects of those types.

#### Types

`std::max_align_t`: an implementation-dependent type whose alignment requirement is at least as strict as that of any scalar type. Typically as large as `long double`&#8216;s.

`std::align_val_t`: used to indicate an alignment requirement using `new` and `delete` functions if it is greater than `__STDCPP_DEFAULT_NEW_ALIGNMENT__`. It allows to supply an argument for correct function overloading, rather than `std::size_t` argument which is used to specify the address at which to allocate memory.

One interesting note: There seems to be a debate whether unaligned data incurres a run time performance loss. Tests have been reported showing that it is, in fact, possible. To further complicate the matters, SIMD commands for Intel processors operating on unaligned data contain a speed-up trick that turns them into their aligned equivalents if the data they are operating on is aligned [3]. It is therefore quite a tricky task to perform &#8216;impartial&#8217; experimental evaluation of the aligned vs. unaligned performance. I think, it is best to do speed or memory measurements on the concrete system, where it can actually matter and then to decide whether to go for speed or memory efficiency.

## Summary

In this article we&#8217;ve looked at data alignment and what tools can we use to take advantage of it in C++ programming language. Its meaning and purpose should be now clear and ready for mindful application!

_Note: Please be reminded, that_ `int` _does not have to necessarily be 4 bytes in size. It was picked as an example, which often occurs in practice but it is in fact platform-specific._

## Reference:

[1] Article about alignment in Microsoft Docs: <https://docs.microsoft.com/en-us/cpp/cpp/alignment-cpp-declarations?view=vs-2019> Access: 09.04.2020

[2] <https://en.cppreference.com/w/cpp/language/object#Alignment> Access: 09.04.2020 

[3] Excerpt from the &#8220;Power and Performance in Enterprise Systems&#8221; 2015, Pages 263-273: <https://www.sciencedirect.com/topics/computer-science/alignment-requirement> Access: 09.04.2020 

[4] Alignment optimality discussion: <https://lemire.me/blog/2012/05/31/data-alignment-for-speed-myth-or-reality/> Access: 09.04.2020 

[5] `std::alignment_of<T>` vs. `alignof`: <https://stackoverflow.com/questions/36981968/stdalignment-of-versus-alignof> Access: 09.04.2020 
