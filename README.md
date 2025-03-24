# Inception: The Dream Layers

In the world of **shared dreaming**, only a select few have mastered the art of navigating the
subconscious. Among them are **Cobb**, **Arthur**, **Ariadne**, and **Eames**—experts in forging
dreamscapes, extracting secrets, and manipulating layers of reality. These four operatives
will be the ones embarking on journeys into the dream world, where every step deeper blurs
the line between dreams and reality.

Within each dream, participants can either go **deeper** into another dream layer or attempt
to wake up by receiving a **kick**. However, if a participant is left alone in a dream without a
**dreamer**, they get trapped in **Limbo** forever (trapped).

You are given a series of events describing how dreamers and participants navigate through
different dream layers. Your task is to determine whether a given individual is:

- **In Reality** (if they have woken up completely)
- **Still Dreaming** (if they are still in a dream layer)
- **Lost in Limbo** (if they were abandoned in a dream without a dreamer)

## Rules of Shared Dreaming:
1. **Entering a Dream:**
  - A person can dream alone or start a shared dream with more participants.
  - If a person is already dreaming, they can only start a deeper dream with people already in the same layer; otherwise, the input is **Invalid**.
  - If a person already lost in Limbo tries to dream alone or starts a shared dream, the input is **Invalid**.
2. **Receiving a Kick:**
  - A person can receive a kick to wake up from their **current** dream.
  - If the dreamer receives a kick while some others remain in the dream, those left behind are **lost in Limbo**.
  - If a person who is already in reality or lost in Limbo receives a kick, the input is **Invalid**.

## Input Format:
- **First line**: An integer **N** representing the number of events.
- **Next N lines**: Each line describes an event in one of the following formats:
  - `X started dreaming`
  - `X started a shared dream with Y"`
  - `X started a shared dream with Y, Z`
  - `X got a kick`
  - `X, Y got a kick`
  - `X, Y, Z got a kick`
- **Last line**: The name of the person whose status needs to be determined.

## Output Format:
- If the person is in reality: `X is in Reality.`
- If the person is still dreaming: `X is Dreaming...`
- If the person is lost in Limbo: `X got lost in Limbo.`
- If an invalid condition occurs: `Invalid Input.`

### Example 1:
#### Input:
```
3
Cobb started a shared dream with Arthur, Ariadne
Arthur started a shared dream with Cobb
Ariadne got a kick
Ariadne
```
#### Output:
`Ariadne is in Reality.`

### Example 2:
#### Input:
```
2
Cobb started a shared dream with Arthur, Ariadne
Arthur started a shared dream with Ariadne
Ariadne
```
#### Output:
`Ariadne is Dreaming...`
