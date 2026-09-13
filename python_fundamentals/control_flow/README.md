# Control flow 
# Python - More Control Flow Tools & Functions

## 1. Control Flow Statements
* **`if` Statements:** Evaluates conditional logic. Uses `elif` (else if) to handle multiple branching conditions and an optional `else` block for fallbacks.
* **`for` Loops:** Iterates directly over items in any sequence (lists, strings, dictionaries) in order. Always iterate over a copy (`collection.copy()`) if modifying the underlying collection inside the loop.
* **`range()` Function:** Generates arithmetic progressions (e.g., `range(start, stop, step)`). It returns an memory-efficient **iterable** object rather than constructing the full list in memory.
* **`break` & `continue`:** 
  * `break` exits the innermost enclosing loop.
  * `continue` skips the remainder of the current iteration and jumps to the next step.
* **`else` Clauses on Loops:** Executes **only if** the loop completes all iterations without encountering a `break` statement.
* **`pass` Statement:** A syntax placeholder that performs no action. Often used for empty classes, functions, or stubbed loops (or replaced by `...`).
* **`match` Statements:** Pattern matching mechanism (`match ... case`). Supports literal comparison, variable binding, sequence/mapping unpacking, class attribute extraction, and guard conditions (`if`).

## 2. Defining Functions
* **Syntax:** Declared using `def function_name(param):`. Functions without an explicit `return` statement automatically return `None`.
* **Docstrings:** The first string literal inside a function body serves as documentation (`function.__doc__`), summarizing its operation.

## 3. Function Parameters & Argument Handling
* **Default Arguments:** Values assigned in parameter definitions. *Warning:* Default values are evaluated once at definition; avoid using mutable default objects like lists or dictionaries (use `None` instead).
* **Positional vs. Keyword Arguments:** Arguments can be passed by position or by explicit name (`kwarg=value`). Positional arguments must always precede keyword arguments in function calls.
* **Arbitrary Arguments (`*args` and `**kwargs`):**
  * `*args`: Collects remaining positional arguments into a **tuple**.
  * `**kwargs`: Collects remaining keyword arguments into a **dictionary**.
* **Special Parameter Boundaries:**
  * `/` (Slash): All preceding parameters are **positional-only**.
  * `*` (Asterisk): All following parameters are **keyword-only**.
* **Argument Unpacking:** Pass elements of a list/tuple as positional arguments using `*`, or key-value pairs from a dictionary using `**`.

## 4. Lambda Expressions
* Small anonymous functions defined in a single line using `lambda args: expression`. Commonly used as short inline callback functions (e.g., sorting keys).
