from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Number, Operator, Token

__all__ = ['MymintStyle']

class MymintStyle(Style):
    # Optional: Set a background color
    background_color = "#000000"

    styles = {
        # Comments
        Comment:                "#DEEF55",          # General comments
        Comment.Single:         "#F8BC65",          # Single line (#)
        Comment.Multiline:      "#F8BC65",          # Multiline

        # Keywords
        Keyword:                "#99C0DB",          # General keywords (def, class, import)
        Keyword:                "#99C0DB",          # General keywords (def, class, import)
        Keyword.Constant:       "#AD9191",          # Constants (True, False, None)
        Keyword.Type:           "#B1B1F6",          # Types (int, str, list)

        # Names (Variables, Functions, Classes)
        Name:                   "#DDDDDD",          # General names
        Name.Function:          "#7798CA",          # Function definitions
        Name.Class:             "#87A1C7",          # Class definitions
        Name.Constant:          "#C39E84",          # User-defined constants

        # Strings and Numbers
        String:                 "#F5EEE4",          # Strings
        Number:                 "#F5EBDE",          # Numbers

        # Operators
        Operator:               "#EEDDDD",          # Operators (+, -, =)
        Operator.Word:          "#EEDDAA",          # Logical operators (and, or, not)
    }
