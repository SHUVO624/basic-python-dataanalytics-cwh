import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Calculator | Fast & Accurate Calculations")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""
        self.display_var = tk.StringVar(value="0")

        self.create_display()
        self.create_buttons()
        self.setup_keyboard()

    def create_display(self):
        """Create the calculator display."""
        display = tk.Entry(
            self.root,
            textvariable=self.display_var,
            font=("Arial", 32),
            justify="right",
            bd=0,
            relief="flat",
            state="readonly",
            readonlybackground="white"
        )

        display.pack(
            fill="both",
            padx=15,
            pady=(20, 10),
            ipady=20
        )

    def create_buttons(self):
        """Create calculator buttons."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        buttons = [
            ("C", 0, 0, 1, self.clear),
            ("⌫", 0, 1, 1, self.backspace),
            ("%", 0, 2, 1, self.percent),
            ("÷", 0, 3, 1, lambda: self.add_operator("/")),

            ("7", 1, 0, 1, lambda: self.add_number("7")),
            ("8", 1, 1, 1, lambda: self.add_number("8")),
            ("9", 1, 2, 1, lambda: self.add_number("9")),
            ("×", 1, 3, 1, lambda: self.add_operator("*")),

            ("4", 2, 0, 1, lambda: self.add_number("4")),
            ("5", 2, 1, 1, lambda: self.add_number("5")),
            ("6", 2, 2, 1, lambda: self.add_number("6")),
            ("−", 2, 3, 1, lambda: self.add_operator("-")),

            ("1", 3, 0, 1, lambda: self.add_number("1")),
            ("2", 3, 1, 1, lambda: self.add_number("2")),
            ("3", 3, 2, 1, lambda: self.add_number("3")),
            ("+", 3, 3, 1, lambda: self.add_operator("+")),

            ("±", 4, 0, 1, self.toggle_sign),
            ("0", 4, 1, 1, lambda: self.add_number("0")),
            (".", 4, 2, 1, self.add_decimal),
            ("=", 4, 3, 1, self.calculate),
        ]

        for text, row, column, colspan, command in buttons:
            button = tk.Button(
                button_frame,
                text=text,
                command=command,
                font=("Arial", 20),
                bd=0,
                relief="flat",
                cursor="hand2",
                padx=10,
                pady=15
            )

            button.grid(
                row=row,
                column=column,
                columnspan=colspan,
                sticky="nsew",
                padx=3,
                pady=3
            )

        # Make rows and columns expand evenly.
        for row in range(5):
            button_frame.rowconfigure(row, weight=1)

        for column in range(4):
            button_frame.columnconfigure(column, weight=1)

    def update_display(self):
        """Update the calculator display."""
        if self.expression:
            self.display_var.set(self.expression)
        else:
            self.display_var.set("0")

    def add_number(self, number):
        """Add a number to the expression."""
        if self.expression == "Error":
            self.expression = ""

        self.expression += number
        self.update_display()

    def add_operator(self, operator):
        """Add an arithmetic operator."""
        if self.expression == "Error":
            self.expression = ""

        if not self.expression:
            # Allow a negative number at the beginning.
            if operator == "-":
                self.expression = "-"
                self.update_display()
            return

        # Prevent two operators from being entered consecutively.
        if self.expression[-1] in "+-*/":
            self.expression = self.expression[:-1]

        self.expression += operator
        self.update_display()

    def add_decimal(self):
        """Add a decimal point to the current number."""
        if self.expression == "Error":
            self.expression = ""

        # Find the current number after the most recent operator.
        current_number = self.expression

        for operator in "+-*/":
            if operator in current_number:
                current_number = current_number.split(operator)[-1]

        # Don't allow multiple decimal points in one number.
        if "." not in current_number:
            if not current_number:
                self.expression += "0"

            self.expression += "."

        self.update_display()

    def clear(self):
        """Clear the calculator."""
        self.expression = ""
        self.update_display()

    def backspace(self):
        """Remove the last character."""
        if self.expression == "Error":
            self.expression = ""
        else:
            self.expression = self.expression[:-1]

        self.update_display()

    def toggle_sign(self):
        """Change the sign of the current number."""
        if not self.expression or self.expression == "Error":
            return

        # Find the last number in the expression.
        operators = "+-*/"
        last_operator_index = -1

        for i, char in enumerate(self.expression):
            if char in operators:
                # A minus at the beginning of a number is a sign,
                # not an arithmetic operator.
                if char == "-" and (
                    i == 0 or self.expression[i - 1] in operators
                ):
                    continue

                last_operator_index = i

        number_start = last_operator_index + 1

        # Handle a number that already has a negative sign.
        if (
            number_start < len(self.expression)
            and self.expression[number_start] == "-"
        ):
            self.expression = (
                self.expression[:number_start]
                + self.expression[number_start + 1:]
            )
        else:
            self.expression = (
                self.expression[:number_start]
                + "-"
                + self.expression[number_start:]
            )

        self.update_display()

    def percent(self):
        """Convert the current number to a percentage."""
        if not self.expression or self.expression == "Error":
            return

        try:
            # Find the start of the last number.
            start = len(self.expression) - 1

            while start >= 0 and (
                self.expression[start].isdigit()
                or self.expression[start] == "."
            ):
                start -= 1

            start += 1

            number = self.expression[start:]

            if number:
                percentage = float(number) / 100

                if percentage.is_integer():
                    result = str(int(percentage))
                else:
                    result = str(percentage)

                self.expression = self.expression[:start] + result

            self.update_display()

        except (ValueError, ZeroDivisionError):
            self.show_error()

    def calculate(self):
        """Evaluate the expression."""
        if not self.expression:
            return

        try:
            expression = self.expression

            # Don't calculate an incomplete expression.
            if expression[-1] in "+-*/":
                expression = expression[:-1]

            if not expression:
                return

            # Evaluate only arithmetic expressions created by our buttons.
            # No arbitrary user input is passed to eval().
            allowed_characters = "0123456789.+-*/ "

            if any(char not in allowed_characters for char in expression):
                raise ValueError

            result = eval(expression, {"__builtins__": None}, {})

            if isinstance(result, float):
                if result.is_integer():
                    result = int(result)
                else:
                    result = round(result, 10)

            self.expression = str(result)
            self.update_display()

        except (ZeroDivisionError, ValueError, TypeError, SyntaxError):
            self.show_error()

    def show_error(self):
        """Display an error message."""
        self.expression = "Error"
        self.display_var.set("Error")

    def setup_keyboard(self):
        """Enable keyboard input."""
        self.root.bind("<Key>", self.handle_keyboard)

    def handle_keyboard(self, event):
        """Handle keyboard presses."""
        key = event.keysym
        char = event.char

        if char.isdigit():
            self.add_number(char)

        elif char in "+-*/":
            self.add_operator(char)

        elif char == ".":
            self.add_decimal()

        elif char == "%":
            self.percent()

        elif key in ("Return", "KP_Enter"):
            self.calculate()

        elif key == "BackSpace":
            self.backspace()

        elif key in ("Escape", "Delete"):
            self.clear()


def main():
    root = tk.Tk()
    Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()