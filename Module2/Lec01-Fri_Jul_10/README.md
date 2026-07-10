CS335 - Friday, July 10 - Lecture 1 - Module 2

# Topics:
* [Today's Spiritual Thought](#todays-spiritual-thought)
* [Get To Know Your Professor](#get-to-know-your-professor)
* [Get To Know Each Other](#get-to-know-each-other)
* [Submitting Today's Participation Artifact](#submitting-todays-participation-artifact)
* [Code Lab Challenge 0 - Static or Dynamic](#code-lab-challenge-0---static-or-dynamic)
* [Code Lab Challenge 1 - Undo Button Stack](#code-lab-challenge-1---undo-button-stack)
* [Code Lab Challenge 2 - Locker Number Hashing](#code-lab-challenge-2---locker-number-hashing)
* [Code Lab Challenge 3 - Campus Map Neighbor Finder](#code-lab-challenge-3---campus-map-neighbor-finder)


------------------------------------------------------------
# Action Items

0.  Prayer
0.  Spiritual Thought
0.  Introductions
0.  Stand-Up Meeting
0.  Code Challenge
0.  Break
0.  Code Challenge
0.  Wrap Up & Parting Thoughts


# Today's Spiritual Thought

When we understand God's plan as a path back to Him, commandments, covenants, and hard experiences start to look less like interruptions and more like part of our growth. How would our choices change today if we measured them by where they are leading us eternally, not just by what feels easiest right now?


## Scripture

> Therefore God gave unto them commandments, after having made known unto them the plan of redemption, that they should not do evil, the penalty thereof being a second death, which was an everlasting death as to things pertaining unto righteousness; for on such the plan of redemption could have no power, for the works of justice could not be destroyed, according to the supreme goodness of God.
> 
> -- Alma 12:32



## Quote

> Understanding this plan of happiness provides us with an eternal perspective and helps us to truly value the commandments, the ordinances, the covenants, and the trials and tribulations.
> 
> -- Rafael E. Pino, ["The Eternal Perspective of the Gospel"](https://www.churchofjesuschrist.org/study/general-conference/2015/04/the-eternal-perspective-of-the-gospel)


# Get To Know Your Professor

Hi, I'm Brother Erik Falor, your professor for this course.

I was fascinated by computers from a young age, but it wasn't until I was in eighth grade that my family got our first computer. In High School I considered myself to be "good with computers," but I didn't begin programming until I was 21. I did not fit in with my peers who could truly call themselves "computer nerds": I am bad at math and I don't particularly enjoy *Star Trek*, *Dungeons and Dragons*, or *Magic: The Gathering*.

I started college as a Communications major but shifted to Computer Science after serving in the Taiwan Taichung mission. My late start meant that I had to play catch-up with classmates who had been programming from a very young age. This is how I learned I wasn't as good at computers as I thought. I remember being intimidated by my classmates who had programmers for parents, went to programming summer camps, made their own video games, and generally understood the jargon words my professor spoke. It felt so humiliating to be shown up by kids who were 2 or 3 years younger than me!

I stuck with the program and earned my Bachelor's degree. I went on to spend 13 years as a software engineer at Spillman Technologies, Inc. (now Motorola Solutions) and Automated Products Group. Midway through my career I began studying for my Master's Degree part-time at USU, graduating in fall 2016. I first taught as an adjunct there in spring 2017 and have been a teacher ever since.

When I was a software engineer I spent my days:

*   _Reading_ horrible documentation
*   _Writing_ documentation that was, hopefully, an improvement
*   _Maintaining_ software that was first written **way** before my time.  Some of the oldest code I encountered was first written when I was still in elementary school in the 90's.
    *   _Testing_ my code
    *   _Finding_ and fixing bugs
    *   _Monitoring_ our customers' systems
    *   _Porting_ programs between platforms
    *   _Reviewing_ code written by my team
*   _Building_ large-scale software systems (millions of lines of code)
*   _Designing_ new software
    *   _Writing_ brand-new code in Perl, C, C++, Java/C#, XSLT, and Shell with tools such as Vim, VisualStudio, Eclipse, and IAR Embedded Workbench

The lessons I learned from my own Algorithms & Data Structures course informed my programming decisions on a near daily basis.  This course was one of the most impactful courses I took, and I am excited to guide you on your journey through it!


# Get To Know Each Other

Take 45 seconds to introduce yourself

0.  Name
0.  Where you are from
0.  Why you are taking this class
0.  Your favorite programming language
0.  One interesting non-CS fact about you (talent, hobby, etc.)


# Submitting Today's Participation Artifact

*Today's in-class activity prepares you for this week's homework without asking you to work on the homework directly.*

Create a new GitHub repository for your work today.  I will open a Canvas discussion after the lecture.  **Reply to that discussion and include the link to your GitHub repository, along with any artifacts you created during the activity.**  Your reply in Canvas is how I will record attendance for the day.

Create the repository under the `Ensign-College` GitHub organization. If you do not create it under that organization, make sure the repository is set to **public** so I can clone it to verify your work and participation.

This activity is graded for *honest effort and participation*, not for perfect correctness. Focus on making a thoughtful attempt, documenting your choices, and showing the work you completed during class.


# Code Lab Challenge 0 - Static or Dynamic?

In this challenge you will practice choosing a data structure based on problem requirements.

Our goal today is not to find the one "best" data structure. The goal is to read the problem, identify the constraints, and explain why a static or dynamic structure is the better fit.


## Activity Requirements

0.  Create the file `challenge0.md` in your GitHub repo.
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

Answer each of these questions in your `challenge0.md`:

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

Answer these debrief questions in your `challenge0.md`:

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


# Code Lab Challenge 1 - Undo Button Stack

In this challenge you will build a small program that simulates an **undo button**.

Many programs keep track of recent user actions so the most recent action can be undone first. This behavior is called **LIFO**: Last In, First Out.

You will use a stack to store actions and remove them in reverse order.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 4.*

### Program Requirements

0. Create the file `challenge1.md` in your GitHub repo.
0. Create an `UndoStack` class.
0. Store user actions in a stack.
0. Add new actions with a method named `do_action`.
0. Undo the most recent action with a method named `undo_action`.
0. If the user tries to undo when there are no actions, return a helpful message.
0. Demonstrate that the most recent action is always undone first.
0. Do not use decorators or advanced Python features.

<details>
<summary><h3>undo_stack.py</h3></summary>

```python
# undo_stack.py

class UndoStack:
    def __init__(self):
        # TODO: Create an empty list to store actions
        pass

    def do_action(self, action):
        """
        Add a new action to the undo history.
        Example action: "typed hello"
        """
        # TODO: Add the action to the stack
        pass

    def undo_action(self):
        """
        Remove and return the most recent action.
        If there are no actions, return "Nothing to undo."
        """
        # TODO: Check whether the stack is empty

        # TODO: Remove and return the most recent action
        pass

    def show_history(self):
        """
        Print all actions currently stored in the undo history.
        """
        # TODO: Print the current action history
        pass


# Demo code
history = UndoStack()

history.do_action("typed hello")
history.do_action("made text bold")
history.do_action("changed font size")

history.show_history()

print(history.undo_action())
print(history.undo_action())

history.show_history()
```

</details>

[Download undo_stack.py](./undo_stack.py)

### Phase 0 - Design It

Answer each of these questions in your `challenge1.md`

0. What does the undo button need to remember?
1. When a new action happens, where should it go?
2. When the user clicks undo, which action should be removed first?
3. Why is a stack a better fit than a queue for this problem?
4. What should happen if the user clicks undo but there is nothing left to undo?

### Phase 1 - Pseudocode It

Using the answers above as your guide, write pseudocode as comments in your program.

Your pseudocode should explain how each method works:

0. `__init__`
1. `do_action`
2. `undo_action`
3. `show_history`

Start in plain English. Then revise the comments until they are close to real Python code.

### Phase 2 - Build It

When your pseudocode is clear, replace each comment with working Python code.

Your finished program should be able to:

0. Create an undo history.
1. Add at least three actions.
2. Show the current history.
3. Undo the most recent action.
4. Undo another action.
5. Show the updated history.
6. Correctly handle an undo attempt when the history is empty.

### Phase 3 - Test It

Run the program with several examples.

Make sure that:

0. The first undo removes the most recent action.
1. The second undo removes the action before that.
2. Actions are not removed in the same order they were added.
3. The program does not crash when there is nothing left to undo.
4. The output clearly shows LIFO behavior.

### Phase 4 - Reflect On It

Answer these debrief questions in your `challenge1.md`:

* Why does an undo button use stack behavior?
* What does LIFO mean in this program?
* What would go wrong if this program used FIFO behavior instead?
* Which method represents `push`?
* Which method represents `pop`?
* What part of this challenge felt easiest?
* What part of this challenge felt least obvious?


### Phase 5 - Stretch Challenges

Did you finish early? Was this still too easy for you? Try one or more of these:

0. Add a maximum history size. If the stack is full, do not allow more actions.
1. Add a `clear_history` method that removes all stored actions.
2. Add a `peek` method that shows the next action that would be undone without removing it.
3. Store each action as a dictionary with fields like `"description"` and `"timestamp"`.
4. Add a simple menu that lets the user choose whether to add an action, undo, show history, or quit.
5. Add a redo stack. When an action is undone, move it to the redo stack.


### Submission Reminder

Commit both files to your GitHub repository:

0. `undo_stack.py`
1. `challenge1.md`

Your `challenge1.md` file should include your reflection answers.

This challenge is graded for honest effort and participation, not perfect correctness. Focus on making a thoughtful attempt and showing your work.


# Code Lab Challenge 2 - Locker Number Hashing

In this challenge you will build a small program that assigns students to locker rows using a simple **hash function**.

A hash function takes a key, such as a student name, and converts it into a number. That number can be used as an index or bucket number.

Real hash tables use more sophisticated logic, but the basic idea is the same: use a repeatable rule to decide where a key belongs.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 5.*

### Program Requirements

0. Create a file named `challenge2.md` in your repository.
1. Create a Python file named `locker_hashing.py`.
2. Write a function named `locker_hash`.
3. The function should accept two parameters:
   0. `student_name`
   0. `number_of_rows`
4. The function should return a locker row number.
5. The same student name should always produce the same row number.
6. Different student names may sometimes produce the same row number. This is called a **collision**.
7. Demonstrate your function with at least five student names.
8. Do not use decorators or advanced Python features.

<details>
<summary><h3>locker_hashing.py</h3></summary>

```python
# locker_hashing.py

def locker_hash(student_name, number_of_rows):
    """
    Convert a student name into a locker row number.

    Example:
    locker_hash("Mia", 5) should return a number from 0 to 4.
    """
    # TODO: Start with a total of 0

    # TODO: Loop through each character in student_name

    # TODO: Convert each character to a number using ord()

    # TODO: Add that number to the total

    # TODO: Use modulo to keep the result inside the number of rows

    # TODO: Return the row number
    pass


def assign_students(student_names, number_of_rows):
    """
    Print each student name and the locker row assigned by locker_hash.
    """
    # TODO: Loop through the list of names

    # TODO: Print each name with its assigned locker row
    pass


# Demo data
students = [
    "Ava",
    "Liam",
    "Noah",
    "Mia",
    "Zoe",
]

assign_students(students, 5)
```

</details>

[Download locker_hashing.py](./locker_hashing.py)

### Phase 0 - Set Up Your Files

In your GitHub repository, create two files:

0. `locker_hashing.py`
1. `challenge2.md`

You will write your code in `locker_hashing.py`.

You will write your explanations, observations, and reflection answers in `challenge2.md`.

### Phase 1 - Predict It

Before writing the full code, open `challenge2.md` and answer these questions:

0. What kind of input does the hash function receive?
1. What kind of output should the hash function produce?
2. Why should the same name always produce the same locker row?
3. What might cause two different names to be assigned to the same row?
4. Is a collision always an error? Why or why not?

### Phase 2 - Build the Hash Function

In `locker_hashing.py`, complete the `locker_hash` function.

Use this basic algorithm:

0. Start with `total = 0`.
1. Loop through each character in the student name.
2. Use `ord(character)` to convert the character into a number.
3. Add that number to `total`.
4. Use `% number_of_rows` to convert the total into a valid locker row.
5. Return the row number.

For example, if there are 5 locker rows, the function should only return one of these values:

```python
0, 1, 2, 3, 4
```

### Phase 3 - Assign Students to Locker Rows

Complete the `assign_students` function.

The function should:

0. Accept a list of student names.
1. Accept the number of locker rows.
2. Loop through the list of student names.
3. Call `locker_hash` for each name.
4. Print each student name and assigned row.

Example output format:

```text
Ava -> row 0
Liam -> row 4
Noah -> row 1
Mia -> row 4
Zoe -> row 2
```

### Phase 4 - Test for Collisions

Add at least five more names to the `students` list.

Run your program several times.

Then open `challenge2.md` and answer:

0. Which names were assigned to the same row?
1. What row had the most students assigned to it?
2. Did the same name always get the same row when you ran the program again?
3. What changed when you increased the number of locker rows?
4. What changed when you decreased the number of locker rows?

### Phase 5 - Reflect On the Data Structure

In `challenge2.md`, answer these reflection questions:

0. What does the student name represent in this challenge: a key, a value, or an index?
1. What does the locker row number represent?
2. Why do we use modulo in the hash function?
3. Why are collisions more likely when there are fewer locker rows?
4. How is this similar to choosing a bucket in a hash table?
5. What would need to happen if each row could only hold one student?

### Phase 6 - Stretch Challenges

Did you finish early? Was this still too easy for you? Try one or more of these:

0. Store the results in a dictionary where each row maps to a list of student names.
1. Print all students grouped by locker row.
2. Count how many collisions happened.
3. Let the user type a name and print the assigned row.
4. Try a different hash rule, such as multiplying each character value by its position in the name.
5. Compare two hash functions and decide which one spreads names more evenly.
6. Add a function named `find_row` that returns the row for one student name.
7. Add a short paragraph to `challenge2.md` explaining whether your hash function distributes students evenly.

### Submission Reminder

Commit both files to your GitHub repository:

0. `locker_hashing.py`
1. `challenge2.md`

Your `challenge2.md` file should include your predictions, collision observations, and reflection answers.

This challenge is graded for honest effort and participation, not perfect correctness. Focus on making a thoughtful attempt and showing your work.


# Code Lab Challenge 3 - Campus Map Neighbor Finder

In this challenge you will build a small program that represents a campus map as a **graph**.

A graph is a data structure made of nodes and connections. In this challenge, each campus location is a node. Each walking path between locations is an edge.

You will use a dictionary of lists to represent the map. This is called an **adjacency list**.

*Note: Students with deeper programming experience can try the extra stretch challenges in Phase 6.*

### Program Requirements

0. Create a file named `challenge3.md` in your repository.
1. Create a Python file named `campus_map.py`.
2. Represent the campus map with a dictionary.
3. Each key in the dictionary should be a campus location.
4. Each value should be a list of nearby locations that can be reached directly.
5. Write a function named `show_neighbors`.
6. The function should accept two parameters:
   0. `campus_map`
   0. `location`
7. The function should print the direct neighbors of the requested location.
8. If the location is not in the map, print a helpful message.
9. Do not use decorators or advanced Python features.

<details>
<summary><h3>campus_map.py</h3></summary>

```python
# campus_map.py

campus_map = {
    "Library": ["Student Center", "Science Building"],
    "Student Center": ["Library", "Gym", "Cafeteria"],
    "Science Building": ["Library", "Engineering Lab"],
    "Gym": ["Student Center"],
    "Cafeteria": ["Student Center"],
    "Engineering Lab": ["Science Building"],
}


def show_neighbors(campus_map, location):
    """
    Print all locations directly connected to the given location.
    """
    # TODO: Check whether location is in campus_map

    # TODO: If not found, print a helpful message

    # TODO: If found, print the location name

    # TODO: Loop through the location's neighbors and print each one
    pass


# Demo calls
show_neighbors(campus_map, "Library")
show_neighbors(campus_map, "Gym")
show_neighbors(campus_map, "Parking Lot")
```

</details>

[Download campus_map.py](./campus_map.py)

### Phase 0 - Set Up Your Files

In your GitHub repository, create two files:

0. `campus_map.py`
1. `challenge3.md`

You will write your code in `campus_map.py`.

You will write your explanations, observations, and reflection answers in `challenge3.md`.

### Phase 1 - Understand the Map

Before writing code, open `challenge3.md` and answer these questions:

0. What are the nodes in this campus map?
1. What are the edges in this campus map?
2. What does each dictionary key represent?
3. What does each dictionary value represent?
4. Why is a graph a better fit than a plain list for this problem?

### Phase 2 - Read the Adjacency List

Look at the starter `campus_map` dictionary.

In `challenge3.md`, answer:

0. Which locations can be reached directly from `"Library"`?
1. Which locations can be reached directly from `"Student Center"`?
2. Which locations can be reached directly from `"Gym"`?
3. Is `"Library"` directly connected to `"Gym"`?
4. Is `"Library"` indirectly connected to `"Gym"` through another location?

### Phase 3 - Build the Neighbor Finder

In `campus_map.py`, complete the `show_neighbors` function.

Your function should:

0. Accept a map dictionary.
1. Accept a location name.
2. Check whether the location exists in the map.
3. If the location does not exist, print a helpful message.
4. If the location exists, print each directly connected neighbor.

Example output format:

```text
Neighbors of Library:
- Student Center
- Science Building
```

For a missing location, the output might look like this:

```text
Parking Lot is not in the campus map.
```

### Phase 4 - Add to the Map

Add at least two new campus locations to the dictionary.

You may use real campus locations or invented ones.

Examples:

```python
"Bookstore": ["Student Center", "Cafeteria"]
"Admin Office": ["Library"]
```

After adding new locations, update any existing locations that should also connect back to them.

For example, if `"Bookstore"` connects to `"Student Center"`, then `"Student Center"` should probably also list `"Bookstore"` as a neighbor.

This makes the connection work in both directions.

### Phase 5 - Test Your Program

Run your program with at least five different locations.

Test cases should include:

0. A location with several neighbors.
1. A location with one neighbor.
2. A location you added.
3. A location that does not exist.
4. A location that is indirectly connected to another location but not directly connected.

In `challenge3.md`, record at least three test calls you tried and what happened.

### Phase 6 - Reflect On the Data Structure

In `challenge3.md`, answer these reflection questions:

0. Why is this campus map an example of a graph?
1. What would be harder if this map were stored as one plain list of location names?
2. Why does a dictionary of lists work well for this problem?
3. What does it mean for two locations to be directly connected?
4. What does it mean for two locations to be indirectly connected?
5. How is this similar to a real map or navigation app?
6. What would need to change if walking paths had distances or travel times?

### Phase 7 - Stretch Challenges

Did you finish early? Was this still too easy for you? Try one or more of these:

0. Write a function named `are_neighbors` that returns `True` if two locations are directly connected.
1. Write a function named `add_location` that adds a new location to the map.
2. Write a function named `add_path` that connects two locations in both directions.
3. Print every location in the map with its list of neighbors.
4. Count how many direct paths exist in the map.
5. Let the user type a location and print its neighbors.
6. Write a function named `has_location` that checks whether a location exists.
7. Add walking times to each path by changing each neighbor list into a list of tuples, such as `("Library", 4)`.

### Submission Reminder

Commit both files to your GitHub repository:

0. `campus_map.py`
1. `challenge3.md`

Your `challenge3.md` file should include your answers, observations, test notes, and reflection responses.

This challenge is graded for honest effort and participation, not perfect correctness. Focus on making a thoughtful attempt and showing your work.


