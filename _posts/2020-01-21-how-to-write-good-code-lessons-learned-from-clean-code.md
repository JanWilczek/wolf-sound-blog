---
id: 333
title: 'How to write good code? Lessons learned from "Clean Code"'
date: 2020-01-21T17:40:22+00:00
author: Jan Wilczek
layout: post
guid: https://thewolfsound.com/?p=333
permalink: /how-to-write-good-code-lessons-learned-from-clean-code/
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
themify_used_global_styles:
  - 'a:1:{i:0;s:0:"";}'
tbp_custom_css:
  - ""
image: /wp-content/uploads/2020/01/thumbnail.png
background: /wp-content/uploads/2020/01/thumbnail.png
categories:
  - Programming in general
tags:
  - architecture
  - code
  - design
  - testing
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/5DFUH0zCn3Y" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/OR41NOATLhU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Today we are going to talk about THIS book:

![](//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0132350882&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL250_&tag=wolfsound-20)
*Click the image to view on Amazon.com*

It is the &#8220;Clean Code&#8221; by Robert C. Martin which is by some considered the ultimate book on &#8220;how to write good code&#8221;. Today I&#8217;d like to share with you my experience with the book and what I&#8217;ve learned from it.

This article is split into two parts: first covering the more general topics and the second devoted only to, spoiler alert, testing. So stick around if you find the topic interesting.

## My story

To motivate the need to write clean code let me share with you my story. As soon as I decided to develop myself further in the direction of software engineering I looked for resources which would guide me on how to solve problems with code, how to structure it, what makes it good for other programmers to reuse and so on. One of the best pieces of advice I got at that time was: &#8216;If you want to learn something just google &#8220;best book on &#8230;&#8221; and read the most recommended books.&#8217; So I did and I ended up reading &#8220;The Pragmatic Programmer&#8221; by Andy Hunt and Dave Thomas. While having a lot of useful information like the &#8216;Don&#8217;t Repeat Yourself&#8217; rule, &#8216;Everything is writing&#8217; and &#8216;Tracer bullets&#8217; especially, the book mostly deals with programmers as people and therefore is less practical than more code-oriented books. Also the version I read was from the early 2000s, so a lot of information seemed outdated. Still, the 20th Anniversary is out now, so maybe that&#8217;s worth looking at.

Another story that comes to my mind when thinking about clean code is when a colleague of mine did a peer review of my code at the company I was working at. He asked me through Slack &#8216;Have you read the Clean Code&#8217;?. &#8216;No.&#8217; I replied. His reaction was &#8216;One can see that.&#8217; As you can imagine it touched me deeply. Actually the recommendations to read &#8216;Clean Code&#8217; started coming from all sorts of different directions, so without hesitation I bought it and finally read it. I will share the most important lessons I&#8217;ve learned from it, one by one.

Should you read it as well? Wait and see until the end of the article.

## Part 1: Lessons learned from &#8220;Clean Code&#8221;

So without further ado, let&#8217;s start with number one, which is&#8230;

### 1. Aspects as a separation of concerns strategy.

Most programmers know the Single Responsibility Principle (SRP), namely, that one class should only do one thing, or, expressed differently, should have only one reason to change. But the sad reality is, that it is quite difficult to achieve. Very often you need additional class features like logging or database updating. That&#8217;s where aspect-oriented programming comes in.

Aspect-oriented programming let&#8217;s you write core business logic in the so-called Plain-Old Java Objects (POJO)s, as you normally would and then to define additional functionalities, so-called&nbsp; &#8216;aspects&#8217;, that are inserted between your method calls by a specialized framework. As you see, the functionalities are separated. 

<div class="wp-block-columns">
  <div class="wp-block-column">
![](https://thewolfsound.com/wp-content/uploads/2020/01/AspectOrientedProgammmingBefore-177x300.png)
*None*
    
    <p>
      SRP violation: <code>Account</code> stores information from user <strong>and </strong>handles database update.
    </p>
  </div>
  
  <div class="wp-block-column">
![](https://thewolfsound.com/wp-content/uploads/2020/01/AspectOrientedProgammmingAfter-1-1024x953.png)
*None*
    
    <p>
      Each aspect (here <code>DatabaseConnection</code> aspect) adds new logic to the POJO object independently.
    </p>
  </div>
</div>

In theory it is a simple and elegant solution, but in practice it heavily relies on the framework used. But it enables you to separate concerns efficiently and therefore enables smooth scalability of the system, since the modules are loosely coupled.

### 2. Encapsulating if condition in functions.

It is much more readable to replace a series of ors and ands with a named function, e.g. isEmpty() instead of size() == 0. It is a simple idea, yet it never occurred to me that extracting the condition as a function would improve readability. (I have to admit I usually put comments explaining the more complicated conditions). Simple but clever one!

```java
if (size() == 0)
{
   do_stuff();
}
```

Plain if condition. What was the original purpose?

```java
if (isEmpty())
{
   do_stuff();
}
```

Encapsulated if condition. It is clear that we want to operate within the &#8220;empty&#8221; state, whatever that means.

### 3. Write code that works first and then make it clean.

I too often get stuck trying to write perfect code instantly. This is, of course, impossible: writing good code is always an iterative process. The only thing to keep in mind, is that you need to know that your code works, which means: tests. We&#8217;ll come back to it in the later part of the article.

### 4. The Boy Scout Rule.

<blockquote class="wp-block-quote">
  <p>
    Always leave the campground cleaner than you found it.
  </p>
</blockquote>

Too often did I hear excuses from programmers (myself included) saying &#8220;but it is not my code!&#8221;. Don&#8217;t let that happen to you: if your task involves altering some module, always remember to leave it better off than it was before. This involves supplying missing tests and refactoring.

Speaking of which&#8230;

### 5. Refactoring examples.

The book has a ton of examples to support its theses, some of which are over 20 pages long and that&#8217;s a good thing. I always wanted to look and learn from examples of good code, but the book goes even further than that: it shows you step-by-step, how a messy, over-complicated, real-world code is transformed into a beautiful manageable module. It even includes some examples of open-source libraries&#8217; refactoring! I found the cognitive process and reasoning concerning all the examples extremely informative and I think it could be the sole reason to read this book.

### 6. Don&#8217;t use switch statements.

The authors argue that introducing switch statements is a hint that polymorphism should be used. It may seem obscure at first sight, but if you think about it, it kind of makes sense, because switch implies different types of handlers and different types that do the same thing in various ways is exactly polymorphism. Clever, huh?

<div class="wp-block-columns">
  <div class="wp-block-column">
    <pre class="brush: java; gutter: false; title: ; notranslate" title="">
void handle_document(Document document)
{
   switch(document.getType())
   {
      case DocumentType.Id:
         handle_id(document);
         break;
      case DocumentType.Passport:
         handle_passport(document);
         break;
       //...
}
</pre>
    
    <p>
      Each usage of <code>Document</code> class is burdened with document&#8217;s type checking.
    </p>
  </div>
  
  <div class="wp-block-column">
    <pre class="brush: java; gutter: false; title: ; notranslate" title="">
public interface DocumentHandler 
{ 
    void handle(Document document); 
}
//...
void handle_document(Document document)
{
    DocumentHandler handler = getDocumentHandler(document.getType());
    handler.handle(document);
}
</pre>
    
    <p>
      Specialized handler for each class takes all worries off <code>handle_document()</code> function. Such designs enables easy addition of new document types (adding new <code>DocumentHandler</code> implementation instead of modifying every usage of <code>Document</code> class).
    </p>
  </div>
</div>

### 7. Encapsulating boundaries of the system.

How to elegantly include an extern library? It is quite a tricky task for a newbie programmer. I know, because I had to deal with exactly that problem at the very beginning of my career as a software developer. &#8216;Clean Code&#8217; addresses that issue as well: define an interface specifying the operation you want the outer system to perform, namely, use the Adapter or Decorator pattern. It is a simple but profound answer, because it implies that you can create an interface not even knowing which library to pick. It also enables efficient testing through test doubles implementing that interface. It reduces the coupling considerably and makes it easy to replace the library with the newer version or a completely different dependency.<figure class="wp-block-image size-large">

<img src="https://thewolfsound.com/wp-content/uploads/2020/01/Boundaries-1024x358.png" alt="" class="wp-image-354" srcset="https://thewolfsound.com/wp-content/uploads/2020/01/Boundaries-1024x358.png 1024w, https://thewolfsound.com/wp-content/uploads/2020/01/Boundaries-300x105.png 300w, https://thewolfsound.com/wp-content/uploads/2020/01/Boundaries-768x269.png 768w, https://thewolfsound.com/wp-content/uploads/2020/01/Boundaries-1536x537.png 1536w, https://thewolfsound.com/wp-content/uploads/2020/01/Boundaries-2048x717.png 2048w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Example of abstracting out the details of how an audio file will be decoded. This boundary of the system is well-protected against change.</figcaption></figure> 

### 8. Early stop and early start in multithreaded code.

Because of the thread dependencies (like in the producer-consumer problem) programmer of a multithreaded code should ensure that all the threads are started and stopped properly regardless of the configuration. You may have experienced random exceptions thrown when exiting your program. I know I did. This is caused by the non-deterministic completion of particular threads. Such quasi-random situations should be heavily tested to eliminate possible source of unexpected bugs in production code and especially in releases.

### 9. Separation of code from its execution.

Dealing with and reasoning about multithreaded code is difficult. One needs to take a lot of factors into account and the result should always be deterministic. It is especially important in systems that are running continuously and cannot be easily stopped and rerun. The idea offered in the &#8216;Clean Code&#8217; is to separate the logic of the program from its execution policy. After all, business logic does not depend on how many threads or even computers it is run on, it does not change. We can think of the problem in terms of the Single Responsibility Principle: there should be classes that are responsible for program&#8217;s logic, e.g. HTTP request handling, and classes that determine how will this logic be executed, e.g. thread runners. Such separation also enables configurability what in turn provides the opportunity to test for correctness in the single thread scenario, what can be particularly helpful when answering the question: &#8216;does business logic not work or is it the multithreaded code&#8217;? It also helps to make the modules more readable: you don&#8217;t have to muddle through locks and executors when trying to understand core program logic.

### 10. Abstraction levels of functions.

It never occurred to me that functions should not only do 1 thing, but also 1 thing on a single abstraction level. It can be best explained through examples: Imagine a function or method handling a HTTP request. Should it deal with the format of the message? Should it deal with the correct&nbsp; placement of separators? Should it manipulate the response string? Probably not. Delegating these lower-level tasks makes the code much more readable, much less error-prone and most probably helps you adhere to the Don&#8217;t Repeat Yourself principle.

<div class="wp-block-columns">
  <div class="wp-block-column">
    <figure class="wp-block-image size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2020/01/AbstractionLevelsBefore-1.png" alt="" class="wp-image-369" width="350" height="187" srcset="https://thewolfsound.com/wp-content/uploads/2020/01/AbstractionLevelsBefore-1.png 361w, https://thewolfsound.com/wp-content/uploads/2020/01/AbstractionLevelsBefore-1-300x161.png 300w" sizes="(max-width: 350px) 100vw, 350px" /></figure> 
    
    <p>
      <code>processBlock()</code> operates on two different level of abstraction: first muddling through particular samples, then calling a higher level function.
    </p>
  </div>
  
  <div class="wp-block-column">
    <figure class="wp-block-image size-large is-resized"><img src="https://thewolfsound.com/wp-content/uploads/2020/01/AbstractionLevelsAfter.png" alt="" class="wp-image-366" width="349" height="96" srcset="https://thewolfsound.com/wp-content/uploads/2020/01/AbstractionLevelsAfter.png 324w, https://thewolfsound.com/wp-content/uploads/2020/01/AbstractionLevelsAfter-300x82.png 300w" sizes="(max-width: 349px) 100vw, 349px" /></figure> 
    
    <p>
      This function operates on a single level of abstraction. Notice the removal of now redundant comments.
    </p>
  </div>
</div>

## Part 2: The value of testing

<blockquote class="wp-block-quote">
  <p>
    Software testing is the art of writing code that ensures us that some other code works.
  </p>
  
  <cite>WolfSound Vocabulary</cite>
</blockquote>

Why would You need that? Let me ask you another question: how do you know that your code works? That&#8217;s something I asked myself when I started &#8220;serious&#8221; programming. Read the code? How many times? Is three enough?

Unfortunately, the audio code is pretty difficult to test, that is why&#8230; some resign from doing so! But today we look at &#8220;Clean Code&#8221; from Robert C. Martin to list out the reasons, why it&#8217;s important to write tests.

Above we&#8217;ve talked about what I&#8217;ve learned from &#8220;Clean Code&#8221; in terms of code design. In this section, I want to share with you my eye-opening experience with the book when it comes to tests and want to encourage you to set out with me on the path of testing.

Let&#8217;s dive into it: 

## Why are tests necessary?

### 1. Testing ensures that your system works.

It may sound straightforward, but just tell me: how many times did you launch the code, you were &#8220;quite certain&#8221; is correct only to see that something went wrong? If something doesn&#8217;t work, your tests are able to tell you where and what, sometimes with laser precision.

### 2. Testing enables refactoring.

According to the Boy Scout rule introduced in the previous part of the article, regular refactoring is a good practice. After all, we are in the agile-iterative work discipline. When you want to improve the code, with each change you need to be sure, that you don&#8217;t break it. Otherwise after hours of work you end up with a clean, disfunctional system. If there are no tests for the code you are refactoring, then repair someone&#8217;s mistake and write them in the first place.

### 3. Testing enables feature introduction.

You want to implement new features to the system. How would you know that they work properly? How would you know you didn&#8217;t break anything when introducing them? Remember, write tests firsts, then new code.

### 4. Tests show the usage of your code to the users.

If someone wants to use the classes you&#8217;ve written they may look at the class interface, but they are more likely to look at the previous usages. That is why the &#8220;Examples&#8221; section of each software library is so valuable. What if there aren&#8217;t any usages? It means there are no tests as well. Having a quick peek at the tests can make you understand the class&#8217;s purpose instantly. That makes their usage much easier.

### 5. Tests document your code.

That is a little bit related to the previous one. Why write what your method takes as parameters and what it returns if you can show it in actual code that&#8217;s not just some comments ignored by the compiler? As Napoleon Hill put it: &#8220;Tell the world what you intend to do but first show it&#8221;.

### 6. Tests show you where the bugs are.

Most often not every line of code is covered with tests. That is to be expected. However, the more tests you have, the more likely you are to catch errors, even the ones present outside your classes! Test failures following certain patterns may reveal not only where the bug is but also unexpected behaviours of the system. That, however, means that testing should be extensive, so keep this in mind when writing test code.

### 7. Using TDD makes your system testable by producing better interfaces.

If you need to interact with your code from the very beginning, you have a concrete proof of how the class you are writing will be used. Having it in code is everything, having it in head is nothing. Tests force you to write clean interfaces. Otherwise you may experience what I have with my poorly developed code: it&#8217;s hard to test, so let&#8217;s not test it. This is not the way of a good programmer. Had I written the tests beforehand the system would be testable from the very beginning.

### 8. Writing tests is a sign that you care.

As Linus Torvalds once said, “Talk is cheap. Show me the code.” I am not the person to judge other programmers&#8217; code, since I make tons of mistakes myself, but even the single fact, that someone has taken time to write test code, would mean, that that person cares. And people who care, change the world. Or at least the system they are working on.

**One final note**: many of my friends, colleagues and fellow programmers observe that software testing is an area almost completely skipped on during Computer Science programmes. The projects developed during various courses should only &#8220;work&#8221;, but whether the tests are there or not is irrelevant. Don&#8217;t learn from that and don&#8217;t follow that way of thinking. ALWAYS test.

That&#8217;s about it! What do you think I missed? Do you have your own design methodologies, varying from what has been presented here? Are you convinced to testing or would you rather employ a different methodology? If yes, which one? Tell me in the comments below.

I hope you have benefited from reading this article. If you want to read the book, click on its cover below:<figure class="wp-block-embed-amazon-kindle wp-block-embed is-type-rich is-provider-amazon">

<div class="wp-block-embed__wrapper">
  <div class="post-embed">
  </div>
</div><figcaption>Click on the image to view on Amazon.com</figcaption></figure> 

And remember: 

<blockquote class="wp-block-quote">
  <p>
    Always leave the code cleaner than you found it.
  </p>
</blockquote>

#### References

[1] R. C. Martin et. al., Clean Code: A Handbook of Agile Craftsmanship (Prentice Hall 2009)