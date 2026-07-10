CS335 - Friday, July 10 - Lecture 1 - Module 2

# Topics:
* [Submitting Today's Participation Artifact](#submitting-todays-participation-artifact)
* [Code Lab Challenge 0 - Static or Dynamc](#code-lab-challenge-0---static-or-dynamc)


------------------------------------------------------------
# Submitting Today's Participation Artifact

*Today's in-class activity prepares you for this week's homework without asking you to work on the homework directly.*

Create a new GitHub repository for your work today.  I will open a Canvas discussion after the lecture.  **Reply to that discussion and include the link to your GitHub repository, along with any artifacts you created during the activity.**  Your reply in Canvas is how I will record attendance for the day.

Create the repository under the `Ensign-College` GitHub organization. If you do not create it under that organization, make sure the repository is set to **public** so I can clone it to verify your work and participation.

This activity is graded for *honest effort and participation*, not for perfect correctness. Focus on making a thoughtful attempt, documenting your choices, and showing the work you completed during class.


# Code Lab Challenge 0 - Static or Dynamc?

In this challenge you will practice choosing a data structure based on problem requirements.

Our goal today is not to find the one "best" data structure. The goal is to read the problem, identify the constraints, and explain why a static or dynamic structure is the better fit.


## Activity Requirements

0.  Classify several real-world scenarios as better suited for a static structure or a dynamic structure.
0.  Justify each choice using the problem's constraints.
0.  Compare the trade-offs of fixed-capacity storage and growable storage.
0.  Implement one small structure-based solution after choosing the structure first.
0.  Explain what operation matters most: direct access, insertion, deletion, fixed memory, or changing size.


### Key Terms

*   **Static structure**: A structure with a fixed capacity or fixed set of slots.
*   **Dynamic structure**: A structure that can grow or shrink as data is added or removed.
*   **Constraint**: A requirement or limitation that affects your design choice.
*   **Trade-off**: A benefit you gain while accepting a cost somewhere else.


### Phase 0 - Sort the Scenarios

Work with a partner. For each scenario, decide whether a static structure or a dynamic structure is the better fit.

Answer each of these questions in today's Wooclap:

0.  Should this scenario use a static or dynamic structure?
1.  What detail in the problem made you choose that structure?
2.  What operation matters most in this scenario?
3.  What is one disadvantage of your choice?

Scenarios:

0.  An airplane has exactly 180 seats. Each seat may be empty or assigned to one passenger.
0.  A help desk receives an unpredictable number of support tickets throughout the day.
0.  A vending machine has 12 fixed slots for snack types.
0.  A multiplayer game stores the players who are currently connected.
0.  A classroom has 30 numbered desks.
0.  A live chat system stores incoming messages until moderators review them.


### Phase 1 - Match the Constraint

For each scenario from Phase 0, choose the most important constraint from the list below.

Constraint choices:

*   Fixed maximum size
*   Unpredictable number of items
*   Need direct access by position
*   Frequent insertions and removals
*   Memory ceiling must be enforced
*   Empty slots are acceptable
*   Wasted unused space is a problem
*   Order of arrival matters

For each scenario, write one sentence using this pattern:

```text
I would use a __________ structure because __________.
The trade-off is __________.
```

Example:

```text
I would use a static structure because an airplane has a fixed number of seats.
The trade-off is that empty seats still take up storage space.
```


### Phase 2 - Design Before Coding

Choose one of the two mini-problems below. Do not start coding immediately. First, write your design choice.

Mini-problem A: Parking Lot

A parking lot has exactly 10 spaces. Each space is either empty or contains one license plate number.

Required operations:

*   Park a car in the first available space.
*   Remove a car by license plate number.
*   Display all 10 spaces.
*   Report when the lot is full.

Mini-problem B: Help Desk Queue

A help desk receives tickets throughout the day. The number of tickets is not known ahead of time.

Required operations:

*   Add a new ticket.
*   Resolve the oldest unresolved ticket.
*   Display the remaining tickets.
*   Report when there are no tickets to resolve.

Before coding, answer:

0.  Which mini-problem did you choose?
0.  Should it use a static or dynamic structure?
0.  Why does that structure fit the problem?
0.  What operation will happen most often?
0.  What is one weakness of your chosen structure?


### Phase 3 - Pseudocode It

Write pseudocode as comments before writing Python code.

Your pseudocode should describe the main operations for your chosen mini-problem.

For Mini-problem A, your pseudocode should include:

*   How to create the 10 parking spaces
*   How to find an empty space
*   How to remove a matching license plate
*   How to display the current spaces

For Mini-problem B, your pseudocode should include:

*   How to create the ticket collection
*   How to add a new ticket
*   How to resolve the oldest ticket
*   How to display the remaining tickets


### Phase 4 - Build It

When your pseudocode is basically line-for-line equivalent to real Python code, rewrite each comment as code.

Keep the implementation simple. You may use Python lists for this challenge.

For Mini-problem A, a good starting point is:

```python
spaces = [None] * 10
```

For Mini-problem B, a good starting point is:

```python
tickets = []
```

Your program should demonstrate at least three operations. For example:

*   Add or park two items.
*   Remove or resolve one item.
*   Display the final state.


### Phase 5 - Test It

Run your program with enough examples to check the important behavior.

For Mini-problem A, test that:

*   A car can be parked in an empty space.
*   A car can be removed by license plate number.
*   The program handles a license plate that is not found.
*   The program reports when the lot is full.

For Mini-problem B, test that:

*   Tickets are added successfully.
*   The oldest ticket is resolved first.
*   The program handles an empty ticket collection.
*   The remaining tickets display correctly.


### Phase 6 - Reflect On It

Answer these debrief questions in today's Wooclap:

*   What constraint mattered most in your design choice?
*   Did your chosen structure make any operation easier?
*   Did your chosen structure make any operation harder?
*   Would your choice still work if the problem became 10 times larger?
*   What would make you switch from a static structure to a dynamic structure, or from a dynamic structure to a static structure?


### Phase 7 - Stretch Challenges

Did you finish early? Here are more features to implement:

*   For the parking lot, allow the user to request a specific space number.
*   For the parking lot, count how many spaces are still empty.
*   For the help desk queue, store each ticket as a dictionary with `name`, `issue`, and `priority`.
*   For the help desk queue, add a function that searches for all tickets from one person.
*   Compare your implementation to the structure you would choose if memory were strictly limited.


