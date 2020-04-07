from dotctrl.config import package

content = f"""# {package.info['name']}: Ignored by default.

__pycache__/
*.lock
*.log
*.egg
*.so
.cache
"""
