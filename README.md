# MindFuck
Mindfuck is a minimalist, esoteric programming language that extends Brainfuck with additional functionalities like arithmetic operations and comparisons. This interpreter processes .mf files, executing their commands using a virtual memory tape.

**Features**

Basic arithmetic (+, -, *, /)

Memory navigation (<, >)

User input ($)

Output printing (:)

Comparisons (L, G)

Loop handling ((, ))

>Increment memory value(+)

>Decrement memory value(-)

>multiply previous memory value and current memory value(*)

>Divide previous memory value by current memory value(/)

>move memory pointer left(<)

>move memory pointer right(>)

>Take user input(Single character)($)

>Print the ASCII value of the current memory value(:)

>Compare previous memory value with current (Less than)(L)

>Compare previous memory value with current (Greater than)(G)

>Start loop (execute if current memory value is not equal to 0)('(')

>End loop(')')


**Using**
After cloning the repository

```

git clone https://github.com/ani-2008/MindFuck.git

cd MindFuck

```

To run a Mindfuck script (example.mf):

```

python mindfuck.py example.mf

```

**Contributions**
Pull requests are welcome! Feel free to improve this interpreter or expand Mindfuck’s capabilities.
Soon, I will build a compiler for this
