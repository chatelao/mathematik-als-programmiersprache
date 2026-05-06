# Goal
Schreibe ein Buch über Mathematik als ultimatives Werkzeug für Softwarespezifikationen.

# HOWTO
- Use readthedocs.org to produce the documentation
- Use reStructuredText to document everything not markdown
- For every decision evaluate three options and archiv the discarded ones in a compressed way
  in an appendix of the documentation.

# Testing Locally & with Github Action Workflow
- Maintain a CI/CD pipeline that runs on every commit and every push.
- Use `test/install.sh` to install testing-specific dependencies.
- Verify the syntax and rendering on every task and ever steps.
- Add caching to the Github action workflows to speed up builds.

# ROADMAP rules
- Split big tasks into multiple and/or subtasks if not  modest, feasible and reasonable in one go.
- Add an intermediate usecase, architecture or design tasks if direct implementation is risky.
- Mark Tasks are  as completed with a timestamp and the corresponding issue id when closed.
