"""Runs a script to check that the user's OS is supported."""
import platform


suppOS = ["Windows"]


def checkOS(os):
    """Check that OS is Supported."""
    if os not in suppOS:
        msg1 = "Your operating system ({}) is not supported in this build. "
        msg2 = "Compatible operating system(s): {}"
        x = ", ".join(suppOS)
        raise SystemExit(msg1.format(os) + msg2.format(x))


checkOS(platform.system())
