"""Runs a script to check that all validations are correct."""
import platform


suppOS = ["Windows", "Linux"]


def checkOS(os):
    """Check that OS is Supported."""
    os = platform.system()
    if os not in suppOS:
        msg1 = "Your operating system ({}) is not supported in this build. "
        msg2 = "Compatible operating system(s): {}"
        x = ", ".join(suppOS)

        raise SystemExit(msg1.format(os) + msg2.format(x))


checkOS(platform.system())
