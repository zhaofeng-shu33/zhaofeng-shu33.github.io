# Does overleaf support git?

Overleaf is a popular online collaborative platform for typesetting papers in LaTeX.
In 2018, sharelatex joined overleaf and overleaf platform staged into its v2 version.
Sharelatex is fully open source, and overleaf based on its v2 version on the code base
of sharelatex. But there are also some old codes of overleaf, called writelatex in the past.
These old codes contained some features which sharelatex does not have, for example,
basic integration with git. Some netizens did not think much of this integration feature,
since it only supports basic git operations and could not solve conflict well enough.
But in my view, a typesetting project is different to a software counterpart. Authors
did not need to handle complex branching situations.

The preprocessor of overleaf v2 is close source software. A part called "git-overleaf-bridge"
was open source but it lacked the necessary "snapshot api" to make it useful. I evaluated
the engineering work needed to change the old api (not open source) to new api (sharelatex)
was not so much. The difficulty lies at my unfamiliarity with the programming language (Java).