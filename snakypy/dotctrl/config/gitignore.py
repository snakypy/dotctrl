from snakypy.dotctrl import __info__

content = f"""# {__info__['name']}: Ignored by default.

__pycache__/
*.lock
*.log
*.egg
*.so
.cache
"""
