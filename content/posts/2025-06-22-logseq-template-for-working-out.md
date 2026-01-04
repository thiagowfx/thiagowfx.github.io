---
title: "Logseq template for working out"
date: 2025-06-22T02:19:09+02:00
tags:
  - bestof
  - pkm
  - serenity
---

Lately I've been tracking my gym sessions in [Logseq](https://logseq.com/).

This workflow has been in place for at least three months, therefore it's stable
enough by now. Here's the rough idea.

First, create a `[[Templates]]` page.

How to remember whether it's `Templates` or `Template`? Simple: add an
`alias::template` attribute to the page. It should be the first bullet point.
Now there's no need to remember: any of them will do.

Then add a `[[Gym 💪]]` bullet point[^1] with `alias::gym`. In it, add a
`template::gym` attribute. Within it, add the template content. This is the part
where you should adapt it to your own desires and goals, but I'll share mine:

```
- Location
	- [[mygym]] (mylocation1 | mylocation2)
- Defaults
	- 3-4x 8-12
- Warm-up
	- XX min what
- Upper
	- Exercise: 25 -> 30
- Lower
	-
- Cooldown
	- XX min what
- Protein recovery
	- XX g (what)
- Body weight
	- XX kg (gym | home)
```

A brief explanation:

- location: links to the page of each gym, where I can add details such as its
  Wi-Fi password, how much drinks cost there, etc.
- defaults: the baseline for the session – how many sets, how many repetitions
  in each?
- warm-up: what did I do, for how many minutes?
- upper: a bucket to group upper-body exercises: arms, chest, abs, etc.
- lower: a bucket to group lower-body exercises: legs, calves, glutes, etc.
- cooldown: what did I do, for how many minutes?
- protein recovery: in grams, what did I drink or eat?
- body weight: in kilos, and where did I measure it?[^2]

This template has served me well. The most important part is the one that
contains the exercises (upper and lower).

Now, let's say I am going to the gym today.

First, I open the journal page (`[[2025-06-22]]`).
Then I type in `/template gym`. This inserts the template above.

Now I click `[[Gym 💪]]` to open up the gym page.

The gym page contains a detailed explanation of my current goals and workflows.
In particular, it has an exercises reference section that looks like this (the
numbers are made up):

```
* # Exercises
* Upper
  * Biceps: 10 -> 12
  * Triceps: 18 -> 20
  * Butterfly normal: 20 -> 25
  * Butterfly reverse: 20 -> 25
  [...]
* Lower
  * Hip addiction: 17 -> 20
  * Hip abduction: 15 -> 20
```

Each entry tracks the latest weight and the one before it, which makes the
progression explicit (and doubles-down as a motivation factor!).

Now, because this is an advanced PKM, the backlink we inserted earlier with the
template shows up under "linked references" at the bottom. And this is the magic
that makes Logseq useful for this kind of tracking: all gym entries are
accessible at a glance, connected to the main `[[Gym 💪]]` page.

During the workout, I use the appropriate weight from the gym page as an input
to the corresponding daily note entry, and slowly increase it in-between sets.

For example, let's say that for biceps the reference entry is `Biceps: 10 ->
12`. Then, for today's workout, I will add an entry like `Biceps: 12 -> 13 ->
14`, starting with `12`, the latest reference value.

Repeat for each exercise.

At the end of the workout, I update the reference entries with the progress of
the day. For example, the updated entry for biceps becomes `* Biceps: 12 -> 14`.

I never liked to go to the gym, but now I am starting to enjoy it, because I
feel this approach brings many self-motivating benefits:

- there's a detailed record of every single workout that I do, down to the day
  and the exercise / weight in each set. These entries are psychologically
  powerful, they motivate me more than smartwatches and/or gym / workouts apps
- the progression ensures I am consistent and pick up where I left off in the
  previous session. There's no need to guess any longer which weight to use, I
  know exactly which one to use, and whether it was difficult or easy last time
  (as I also track this information in the reference).
- reduced risk of injury as I am increasing the weights slowly, and being
  mindful of the ones that incur a lot of stress and/or strain on my muscles
- ability to track goals and be realistic about them, and even estimate when
  I'll be able to reach them, based on historical progression.

I tried to use gym apps before, but they were never effective. They are often
complicated and bloated. The advantage of keeping the format plain and flexible
in the PKM is that it can suit all my needs. In fact, I could even bring pen and
paper to the gym instead of my smartphone if needed, as there's absolutely no
need for internet access when updating these entries, and no lock-in whatsoever.

There's nothing revolutionary in my approach. Its core is merely: (i)
(annotated!) consistency and (ii) ability to shape the system to the format that
suits/fits my needs.

Consistency is very important. Before adopting this system, I would always guess
which weight to use for each exercise. But there are too many of them, and as
such it's quite difficult to keep track of them all in my head.

The format flexibility is also important. The key is to shape a system to your
needs, not the other way around. With smartphone and smartwatch apps, I always
felt that I had to adapt myself to the input format the app expects, which is
painful from an UX perspective.

And now it is time to work out again 💪

[^1]: Yes, including the emoji. Life is short to skip having fun.

[^2]: There are tiny differences, therefore I like to note down whether I used
    the scale from the gym or the one at home.
