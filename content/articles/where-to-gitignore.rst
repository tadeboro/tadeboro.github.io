Where to gitignore
==================

:date: 2022-08-07
:tags: git, gitignore


It is Thursday. You are fixing a bug in a project you usually do not work on.
Just before you commit your changes, you notice some temporary files your
editor left behind in the :code:`git status` output. So you add them to the
.gitignore file and commit those changes. You send your changes into review and
eagerly wait for someone to say *And thank you for taking care of that missing
gitignore entry.*

But to your surprise, the feedback you receive looks something like this:

   There are a few things I do not want to know. And what editor/IDE you use to
   edit files is one such thing. So please remove your editor-specific ignore
   entries from the project's .gitignore file and place them into your personal
   ignore file. Thank you!

And if your reaction is *My personal ignore file?*, you should read on.


There is more than one ignore file?
-----------------------------------

Yep. And git's built-in help will tell you the location of those files in its
synopsis::

   $ git help ignore
   ...
   SYNOPSIS
          $XDG_CONFIG_HOME/git/ignore, $GIT_DIR/info/exclude, .gitignore
   ...

If you read the manual's description section you will also get some information
about what to put into each of those files. The mathematician in me also likes
to think about those files using the following Venn diagram::

   <--------------- developer-specific --------------->
   .------------------------+-------------------------+--------------.
   |  ~/.config/git/ignore  |  $GIT_DIR/info/exclude  |  .gitignore  |
   '------------------------+-------------------------+--------------'
                            <----------- project-specific ----------->

I tend to call the ~/.config/git/ignore filea **personal ignore file**, and
.gitignore file(s) **project ignores**. I have no special name for
$GIT_DIR/info/exclude file since you can safely ignore it the in the vast
majority of cases. I have been using git for more than ten years now and I used
that ignore file location once.

During day-to-day activities, it is quite easy to determine where a particular
ignore entry should go. The rule of thumb I use is:

   If ignored entry pops into existence while I follow the build/test/release
   instructions, it should live in the repository's .gitignore file. Otherwise,
   it should be part of my ~/.config/git/ignore file.

If you follow my rule, you will most likely set up your personal ignore file
once (when you set up your computer) and only work with project ignore files
from then on.


Examples maybe?
---------------

If you need some inspiration, I would suggest you visit the `github/gitignore`_
repository. You should use ignore samples in the root of that repository as a
source of inspiration for your project-specific ignore entries. For personal
ignore entries, use files in the Global_ directory.


.. _github/gitignore: https://github.com/github/gitignore
.. _Global: https://github.com/github/gitignore/tree/main/Global


But distributed configuration is hard!
--------------------------------------

If you can keep your code sane, you should be able to track your ignores in two
locations ;) But if you ever get too confused by your setup, git has your back.
The :code:`git check-ignore -v` command will tell you the source of the ignore
entry::

   $ git check-ignore -v output/index.html content/articles/.*.swp
   .gitignore:1:output     output/index.html
   ~/.config/git/ignore:4:[._]*.sw[a-p] content/articles/.art.rst.swp


Cheers!
