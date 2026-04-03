"""Flask web server exposing a calculator UI and JSON API."""

import logging
import os
from pathlib import Path

from flask import Flask, Response, jsonify, request, send_from_directory

from calculator_app.calculator import add, divide, multiply, subtract

logger = logging.getLogger(__name__)

_STATIC_DIR = Path(__file__).parent / "static"

app = Flask(__name__, static_folder=str(_STATIC_DIR))


@app.get("/")
def index() -> Response:
    """Serve the calculator single-page application.

    Returns:
        The index.html file from the static directory.
    """
    return send_from_directory(str(_STATIC_DIR), "index.html")


@app.post("/calculate")
def calculate() -> tuple[Response, int]:
    """Evaluate a simple two-operand arithmetic expression.

    Expects a JSON body of the form::

        {"expression": "<number> <op> <number>"}

    where ``<op>`` is one of ``+``, ``-``, ``*``, ``/``.

    Returns:
        A JSON response containing ``{"result": <value>}`` on success or
        ``{"error": "<message>"}`` on failure, together with the appropriate
        HTTP status code (200 or 400).
    """
    payload = request.get_json(silent=True)
    if payload is None or "expression" not in payload:
        logger.warning("Received calculate request with missing or invalid JSON body")
        return jsonify({"error": "Request body must be JSON with an 'expression' key"}), 400

    expression: str = str(payload["expression"]).strip()
    logger.info("Evaluating expression: %r", expression)

    try:
        result = _evaluate(expression)
    except ZeroDivisionError:
        logger.warning("Division by zero in expression: %r", expression)
        return jsonify({"error": "Division by zero"}), 400
    except ValueError as exc:
        logger.warning("Invalid expression %r: %s", expression, exc)
        return jsonify({"error": str(exc)}), 400

    logger.info("Expression %r evaluated to %r", expression, result)
    return jsonify({"result": result}), 200


def _evaluate(expression: str) -> float:
    """Parse and evaluate a two-operand arithmetic expression string.

    Supported operators: ``+``, ``-``, ``*``, ``/``.

    Args:
        expression: A string of the form ``"<number> <op> <number>"``.

    Returns:
        The numeric result of the operation.

    Raises:
        ValueError: If the expression cannot be parsed or the operator is unknown.
        ZeroDivisionError: If a division by zero is attempted.
    """
    _OPS = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    for op_symbol, op_func in _OPS.items():
        # Split on the operator, being careful with leading minus signs.
        # We look for the operator surrounded by digits/whitespace.
        parts = expression.split(op_symbol)
        if len(parts) == 2:
            left_str, right_str = parts[0].strip(), parts[1].strip()
            try:
                left = float(left_str)
                right = float(right_str)
            except ValueError:
                continue
            return op_func(left, right)

    raise ValueError(f"Could not parse expression: {expression!r}")


def main() -> None:
    """Entry point for the calculator-web console script.

    Reads optional ``HOST`` and ``PORT`` environment variables (defaulting to
    ``127.0.0.1`` and ``5000`` respectively) and starts the Flask development
    server.
    """
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", "5000"))
    logger.info("Starting calculator web server on %s:%d", host, port)
    app.run(host=host, port=port)


if __name__ == "__main__":
    main()
